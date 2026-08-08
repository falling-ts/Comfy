# 分段执行机制 — ComfyUI 执行引擎 · 继续节点 lazy · 路由节点目标收集

日期:2026-08-08
关联插件:ComfyUI-FallingTS(`FallingTSContinue` / `FallingTSRoute` / `FallingTSSwitch`)
相关源码:`ComfyUI/execution.py`、`ComfyUI/comfy_execution/graph.py`、`ComfyUI/comfy_execution/caching.py`、`ComfyUI/main.py`、`ComfyUI/server.py`

本文整理三部分内容:

1. **ComfyUI 执行引擎核心驱动逻辑** —— 从点击 Run 到节点逐个执行,收集起点在哪、核心循环怎么驱动
2. **继续节点 lazy 机制对节点收集的影响** —— lazy 边如何切断上游收集,check_lazy_status 如何动态补拉
3. **路由节点(Route)的目标收集** —— 尤其假输出后续节点如何被收集进 partial 执行

---

## 一、ComfyUI 执行引擎:核心驱动逻辑

### 1.1 入口链路:Run 按钮 → /prompt → 队列

前端 Run 按钮(`Comfy.QueuePrompt` 命令)调 `app.queuePrompt(0, batchCount)`,内部(`settingStore`):

```
queuePrompt(e, t=1, n):
  d = !!n?.length                        # n=nodeIds, 非空=partial 执行
  graphToPrompt(this.rootGraph)          # 整张图 → prompt(全图序列化, 无"只提交某段"选项)
  V.queuePrompt(e, f, {partialExecutionTargets: n})   # → POST /prompt
```

后端 `server.py:1106-1131`:`/prompt` → `validate_prompt()` → `prompt_queue.put((number, prompt_id, prompt, extra_data, outputs_to_execute, sensitive))` 入队。

### 1.2 收集起点:validate_prompt 从"输出节点"开始

**执行从"输出节点"开始往回找,不是从画布顶部。** `execution.py:1128-1165`:

```python
outputs = set()
for x in prompt:                                    # 遍历所有节点
    if 该节点是 OUTPUT_NODE:
        if partial_execution_list is None or x in partial_execution_list:
            outputs.add(x)                          # ← 收集"执行目标"
```

- **全量 Run**:`partial_execution_targets=None` → 所有输出节点都是目标
- **继续(partial)**:只保留 targets 里的输出节点(非输出节点即使传了也被过滤,`execution.py:1163`)

`outputs` 就是 **`execute_outputs`** —— **收集节点的起点是"终端输出节点"**。

### 1.3 队列 → worker 取出

`main.py:359-372`:`prompt_worker` 死循环 `q.get()` → `e.execute(item[2], prompt_id, extra_data, item[4])`,item[4] 就是上面的 `outputs_to_execute`。

### 1.4 核心驱动:execute_async + ExecutionList 循环

**这就是"开始跑节点流程"的核心。** `execution.py:730-812`:

```python
async def execute_async(self, prompt, prompt_id, extra_data={}, execute_outputs=[]):
    dynamic_prompt = DynamicPrompt(prompt)                # 图对象
    for cache in self.caches.all:
        await cache.set_prompt(dynamic_prompt, ...)       # 算所有节点缓存键
    ...
    execution_list = ExecutionList(dynamic_prompt, self.caches.outputs, ...)  # 执行列表
    for node_id in list(execute_outputs):
        execution_list.add_node(node_id)                  # ★ 从目标开始, 向上收集

    while not execution_list.is_empty():                  # ★ 核心驱动循环
        node_id, error, ex = await execution_list.stage_node_execution()  # 选下一个就绪节点
        if error: break
        result, error, ex = await execute(self.server, dynamic_prompt,
                                          self.caches, node_id, ...)      # 真正跑这个节点
        if result == ExecutionResult.FAILURE:  break
        elif result == ExecutionResult.PENDING: execution_list.unstage_node_execution()
        else: execution_list.complete_node_execution()    # 出栈, 解锁下游
```

**驱动本质**:一个**拓扑排序队列** —— 谁"就绪"(所有输入依赖已完成)谁执行,执行完出栈、解锁下游,循环直到空。

### 1.5 add_node:如何"向上收集"节点

`graph.py:138-166`(TopologicalSort.add_node):

```python
def add_node(self, node_unique_id, include_lazy=False, subgraph_nodes=None):
    node_ids = [node_unique_id]                    # 从目标节点开始
    while len(node_ids) > 0:
        unique_id = node_ids.pop()
        ... 标记 pending ...
        for input_name in inputs:                  # 沿每条输入边向上游
            if is_link(value):
                is_lazy = input_info["lazy"]       # lazy 边不遍历(缓存无关)
                if (include_lazy or not is_lazy):
                    if not self.is_cached(from_node_id):   # 已缓存节点跳过
                        node_ids.append(from_node_id)      # 未缓存 → 继续向上加
                    links.append((from_node_id, from_socket, unique_id))
    for link in links:
        self.add_strong_link(*link)                # 建立依赖(blocking)关系
```

形成 `pendingNodes`(待执行集)+ `blockCount`(每个节点被几个上游阻塞)+ `blocking`(解锁关系)。

### 1.6 stage_node_execution:下一个跑谁

`graph.py:242-313`:`get_ready_nodes()` = `blockCount==0` 的节点;`ux_friendly_pick_node()` 优先挑输出节点、异步节点(体验优先)。

### 1.7 execute:真正跑一个节点

`execution.py:438-617`,核心 4 步:

```python
async def execute(server, dynprompt, caches, current_item, ...):
    cached = await caches.outputs.get(unique_id)          # 1. 查执行缓存
    if cached is not None:                                #    命中 → 发缓存 UI, 跳过(不重跑)
        _send_cached_ui(...); return SUCCESS

    input_data_all, missing_keys, v3_data = get_input_data(inputs, class_def, ...)  # 2. 解析输入
    #    链接输入 → execution_list.get_cache(上游) 取上游输出值
    #    常量输入 → widget 值; 缺失 → None

    if lazy_status_present:                               # 3. lazy 门控
        required_inputs = await obj.check_lazy_status(**inputs)
        if required_inputs 中有缺失输入:
            execution_list.make_input_strong_link(...)    # 拉上游进来
            return PENDING                                # 先暂停, 等上游跑完再调度

    output_data, output_ui, has_subgraph = await get_output_data(...)   # 4. 调节点函数
    #    _async_map_node_over_list → obj.FUNCTION(**inputs)
    cache_entry = CacheEntry(ui=..., outputs=output_data)
    execution_list.cache_update(unique_id, cache_entry)   # 通知下游: 我的输出好了
    await caches.outputs.set(unique_id, cache_entry)      # 写缓存
```

### 1.8 复杂节点(子图扩展)如何执行

`execution.py:351-414` `get_output_from_returns`:节点返回里若带 `'expand'`(子图),标记 `has_subgraph`。随后 `execution.py:579-613`:

```python
if has_subgraph:
    for node_id, node_info in new_graph.items():
        dynprompt.add_ephemeral_node(...)               # 动态生成的新节点加入图
    for node_id in new_output_ids:
        execution_list.add_node(node_id)                # 新子图的输出节点加入执行列表
    pending_subgraph_results[unique_id] = cached_outputs
    return PENDING                                      # 本节点"暂停", 先跑子图
```

节点执行过程中**动态长出子图**,子图跑完再回到本节点(通过 `pending_subgraph_results` 在下次调度时 `execution.py:469-490` 解析)。

### 1.9 一句话总结

> **`execute_async` 的 `while not execution_list.is_empty()` 循环** + **`ExecutionList`(拓扑排序队列)** 是核心:从 `validate_prompt` 定的**输出节点**开始,`add_node` 沿输入边**向上**收集未缓存节点、跳过 lazy 边,形成依赖图;循环里 `stage_node_execution` 挑 `blockCount==0` 的就绪节点 → `execute` 查缓存/解析输入/调 `FUNCTION` → 写缓存、`complete_node_execution` 解锁下游 → 直到空。

---

## 二、继续节点 lazy 机制对节点收集的影响

继续节点 `FallingTSContinue` 的 `any` 输入声明了 `"lazy": True` + 后端 `check_lazy_status`,对收集节点的影响是**结构性的**,分三个阶段:

### 2.1 收集阶段(add_node):lazy 边 = 硬边界,直接切断

`graph.py:159-163`:

```python
is_lazy = input_info is not None and "lazy" in input_info and input_info["lazy"]
if (include_lazy or not is_lazy):          # include_lazy=False(execute_async 没传)
    if not self.is_cached(from_node_id):
        node_ids.append(from_node_id)       # 沿这条边向上加节点
    links.append((from_node_id, from_socket, unique_id))
```

`any` 输入标了 `"lazy": True` → `include_lazy or not is_lazy` = `False` → **整个块被跳过**:

- ❌ 上游节点**不加入**收集队列
- ❌ 这条边**不建立**依赖关系(`blocking`/`blockCount`)

**结果:add_node 从 targets 向上回溯时,遇到继续节点就"到此为止",上游段整段不进执行列表。** 无论上游缓存有没有、种子变没变 —— lazy 是**缓存无关**的硬门(对比 `is_cached` 那行是软门,缓存失效就会继续往上走)。

### 2.2 就绪阶段:继续节点"先于上游"就绪

因为 lazy 边没建立 `blocking` 依赖,继续节点的 `blockCount==0` → 它**不依赖上游就能就绪**(`graph.py:182` `get_ready_nodes`)。所以调度顺序上,继续节点会**先于它的上游段**被 stage。

### 2.3 执行阶段:check_lazy_status 决定"要不要补拉上游"

`execution.py:507-520`:

```python
if lazy_status_present:
    required_inputs = await obj.check_lazy_status(**inputs)   # 返回 ["any"] 或 []
    required_inputs = [x for x in required_inputs if x 缺失]
    if len(required_inputs) > 0:
        for i in required_inputs:
            execution_list.make_input_strong_link(unique_id, i)   # 动态拉上游
        return (ExecutionResult.PENDING, None, None)              # 暂停, 等上游
```

`make_input_strong_link`(`graph.py:120-128`)这时才真正 `add_node` 上游 + 建 `blocking`,返回 **PENDING**。上游跑完、缓存写好后,继续节点才被重新调度,用 `get_input_data` 拿到上游值(`execution.py:180-188`,此时 `execution_list.get_cache(上游)` 有值了)。

### 2.4 三种情况对照

| 场景 | check_lazy_status | 收集时 | 执行时 | 结果 |
|------|------|------|------|------|
| 首次 Run(未放行) | 返回 `["any"]` | 上游不进列表 | 执行时 `make_input_strong_link` 补拉上游 → PENDING → 上游跑 → 重新调度 | 上游被拉进来执行,填缓存后阻塞 |
| 点「继续」(已放行) | 返回 `[]` | 上游不进列表 | 不拉,`any=None`(来自 `get_input_data` 的 missing 分支 `execution.py:181-183`) | 上游完全不跑,用节点缓存 |
| 没连线 | `any is MISSING` → 返回 `[]` | 无上游 | 不拉 | 阻塞 |

### 2.5 关键结论

1. **lazy 让继续节点成为"段边界"**:收集时上游段直接被切断,这就是「继续」不重跑开头、且不依赖全局缓存的根本原因。
2. **但 lazy 只切"这一条边"**:如果上游段通过**其它非 lazy 路径**(直连边)也连进执行列表,照样会被收集、被执行 —— 这就是 `ColorMatch→PreviewImage(19)` 直连边把段0拉回来的原因。lazy 门只管"经过继续节点的边"。
3. **收集时切断 ≠ 执行时不拉**:未放行的继续节点会在执行阶段用 `make_input_strong_link` 把上游补进来(所以 Run 能跑完整段)。lazy 是"按需拉取",不是"永远排除"。
4. **副作用**:lazy 边不建依赖 → 继续节点 `blockCount=0` 先就绪 → 每次它都可能先于上游被 stage 一次,再因 PENDING 等待。多一个 PENDING 往返,但正确。

> 一句话:**lazy 边让 add_node 在继续节点处停止向上收集、且不建立依赖(硬边界);是否真的执行上游,由 check_lazy_status 在节点执行时动态决定。**

---

## 三、路由节点(Route)的目标收集:假输出后续节点

### 3.1 两条收集线合并

```
继续按钮(proceed.js)          route.js 包装器
    │                              │
    ├─ collectOutputsAfter(#5401)  ├─ collectAllFalseBranchTargets(图)
    │  = {6005, 6009}(下一段输出)   │  = switch=false 的 route 假分支输出
    │                              │
    └──────► queueNodeIds 合并 ◄───┘   (Set 去重, route.js:155)
                     │
                     ▼
              app.queuePrompt(0,1,合并后) → /prompt partial_execution_targets
```

route.js 只在 **partial 提交(queueNodeIds 非空)**时介入,全量 Run 不掺和。

### 3.2 collectFalseBranchOutputs 逻辑

**只挑 `switch=false` 的 route**(`route.js:119-127`):

```js
function collectAllFalseBranchTargets(graph) {
  for (const n of graph._nodes) {
    if (!isRouteNode(n)) continue;
    if (getSwitchValue(n)) continue;   // switch=true 跳过 —— 真分支由继续节点覆盖
    for (const t of collectFalseBranchOutputs(n)) targets.add(t);
  }
}
```

**为什么不收真分支**:真分支是"下一个继续"的上游,继续节点的 `collectOutputsAfter(#5401)` 已经会通过执行回溯把它带上;只有假分支是末端死胡同,得在这里补。

**从假输出槽(slot0)向下 BFS**(`route.js:85-111`):

```js
function collectFalseBranchOutputs(routeNode) {
  const out = routeNode.outputs?.[0];           // output_false = slot 0
  ...
  queue 从 out.links 的 target_id 出发;
  while (queue) {
    n = getNodeById(nid);
    if (isContinueNode(n)) continue;            // ① 遇到继续节点: 停止, 不越过段边界
    if (isOutputNode(n)) targets.add(n.id);     // ② 只收"输出节点"(保存/预览/对比)
    // ③ 非输出节点继续往深处 BFS
  }
}
```

三个要点:
- **起点**:route 节点的 `output_false` 槽(第 0 个输出)
- **收集对象**:只收 `nodeData.output_node === true` 的节点(`SaveImageAdvanced`/`PreviewImage`/`ImageCompare` 等)—— 只有它们能作为 partial 执行目标(`validate_prompt` 也只认 OUTPUT_NODE)
- **边界**:BFS 遇到继续节点就停,不会越过段边界收到下一段的输出

### 3.3 中间节点怎么被带上

收集到的只是**末端输出节点**。假输出分支里那些非输出节点(比如中间的变换节点),**不用收集** —— 它们会在引擎回溯时作为"target 的上游祖先"自动进执行列表(`execution.py:779` add_node 向上走)。你只需要把"终点"钉成 target,中间的自动带出来。

### 3.4 合并交给引擎

```js
queueNodeIds = [...new Set([...queueNodeIds, ...routeTargets])];   // route.js:155
```

去重合并后,继续节点的 targets(下一段)+ route 假分支 targets(保存节点)一起成为 `partial_execution_targets` → 服务端 `validate_prompt` 保留这些输出节点 → `add_node` 从它们向上收集 → 假分支下游真的执行。

### 3.5 工作流举例

```
route(6006) switch=false
  output_false → SaveImage6007        ← collectFalseBranchOutputs 收集到 {6007}
  output_true  → 放大→...→PreviewImage33 → #5401   ← 不收(继续节点覆盖)

继续 #43:
  合并 targets = {6005,6009}(继续) ∪ {6007}(route假分支)
  → 6007 进执行列表 → 基图保存 ✓;放大分支被 switch 阻断;下个继续不缓存、停住
```

### 3.6 边界条件

`collectFalseBranchOutputs` **只收 `output_node=true` 的节点**。如果假输出后面接的是一个"非输出节点"、且它后面没有输出节点,那这条假分支不会有任何 target 被补 → 还是不跑。因为 ComfyUI 的 partial 执行目标**必须是输出节点**(`execution.py:1163` 只保留 OUTPUT_NODE)。

> 所以假输出分支的设计原则:**末端一定要放一个输出节点(保存/预览)**。这正是"保存本段并停止"的用法。如果假分支想接到某个中间节点再继续,那它其实不是"停止"语义,应该走真分支或换结构。

---

## 附:相关源码位置速查

| 位置 | 说明 |
|------|------|
| `ComfyUI/server.py:1106-1131` | /prompt 入口,validate_prompt + 入队 |
| `ComfyUI/execution.py:1128-1165` | validate_prompt: 从输出节点收集 targets |
| `ComfyUI/main.py:359-372` | prompt_worker 取出执行 |
| `ComfyUI/execution.py:730-812` | execute_async + ExecutionList 主循环 |
| `ComfyUI/execution.py:438-617` | execute: 单节点执行(缓存/输入/lazy/FUNCTION) |
| `ComfyUI/execution.py:343-414` | get_output_data / 子图扩展 |
| `ComfyUI/comfy_execution/graph.py:138-166` | add_node 向上收集 |
| `ComfyUI/comfy_execution/graph.py:242-313` | stage_node_execution 挑节点 |
| `ComfyUI/comfy_execution/caching.py:67-127` | 缓存键(IS_CHANGED 参与) |
| `ComfyUI-FallingTS/web/js/proceed.js` | 继续节点前端(包装 queuePrompt + 继续按钮) |
| `ComfyUI-FallingTS/web/js/route.js` | 路由节点前端(假输出分支补 targets) |
| `ComfyUI-FallingTS/proceed/nodes.py` | 继续节点后端(lazy + 节点缓存 + HTTP 路由) |
| `ComfyUI-FallingTS/route/nodes.py` | 路由节点后端(switch 路由 + ExecutionBlocker) |
