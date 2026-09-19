# Obsidian Markdown 表格渲染实现调研（1.13.7 取证附录）

> ### ⚠️ 文首勘误（交叉复核后追加）
>
> **1. 版本提示（已更新）**：本报告的取证对象是 `%APPDATA%\obsidian\obsidian-1.13.7.asar`，
> 撰写时它被记为"已下载未安装"的更新包；**现已安装生效** —— `C:\Program Files\Obsidian` 下的
> `Obsidian.exe` 与 `resources\obsidian.asar` 均已是 **1.13.7**（24.59 MB / 358 文件，2026-09-18 复核）。
> 因此本报告的取证数据（offset、模块号、源码片段）**正是当前运行版本的数据**，
> 与主报告 `Obsidian-MD表格渲染机制.md` 的 1.12.4 数据互为双版本对照
> （两版表格机制已逐项验证一致，见主报告 §13.8）。
>
> ⚠️ **"更新包"这个说法本身也已修正**：`obsidian.log` 记录
> `Loaded updated app C:\Users\zghyu\AppData\Roaming\obsidian\obsidian-1.13.7.asar` —— Obsidian
> 的自动更新流程是「下载 asar 到 userData → 下次启动直接加载它」，所以 `%APPDATA%` 下这个 asar
> **就是被实际加载的那一个**，不是可删的缓存。
>
> **4. 技术栈背景见配套文档**：整个 Obsidian 的运行时版本（Electron 43.3.0 / Chromium 150 /
> Node 24.18.1）、源码语言（TypeScript）、md 渲染链各层实现语言与第三方库清单，见
> **`Obsidian-技术栈与实现语言调研.md`**。
>
> **2. 一处核心结论已被证伪**：本报告关于"**光标进入表格会退回源码**"的判定是**错的**。
> 报告依据 ViewPlugin 中存在 `b = OA(选区相交) || FA(搜索命中)` 这一判断；但逐字复核后确认，
> `b()` **只服务于公式/代码块等元素**，表格分支用的是 `if (!FA(...))`，**不含任何选区判断**。
> 因此真实行为是：**光标/选区进入表格不会退回源码**，而是保持渲染态、直接编辑单元格；
> 只有在**表格范围内搜索命中**时才退回源码（以便显示搜索高亮）。
>
> 误判原因：`J` 函数内 `var b = Y > 0 && ...` 局部**遮蔽**了外层同名的 `b` 函数，
> 顺着"看到 `b` 就以为走了选区逻辑"的直觉读，会得到完全相反的行为结论。
> **教训：判定行为必须定位到该元素真正的调用点，而不是只找到判断函数本身。**
>
> **3. 权威版本**：结论与逐字对照代码以同目录 **`Obsidian-MD表格渲染机制.md`** 为准
> （§5.6 表格 vs 公式的行为对照、§13.1 本条勘误的完整说明）。
> **本文件保留全部一手取证数据与生态调研，作为那份报告的详细取证附录。**

> **取证环境（本报告的第一手证据来源）**
> 本机安装的 **Obsidian 1.13.7（Windows 桌面版）**，其应用包 `C:\Users\zghyu\AppData\Roaming\obsidian\obsidian-1.13.7.asar` 可直接解包，内含 `app.js`（3,876,459 B，混淆但未加密）、`app.css`（637,090 B）、`lib/codemirror/*`。本报告中标 **[反编译]** 的结论全部来自对这两个文件的逐字节检索，并给出偏移量（offset）以便复核。**[官方文档]** = Obsidian 官方帮助/开发者文档；**[上游源码]** = CodeMirror/lezer/unified 生态源码；**[社区]** = 第三方文档/插件/论坛；**[推断]** = 由证据推出的合理结论；**[未验证]** = 无权威依据。
>
> 解包方法（可复现）：asar 头 16 B + JSON 目录（本包 JSON 大小 93,472）→ 数据区起点 `16 + 93472 = 93488`，文件偏移 = 93488 + 目录中的 `offset`。

---

## 概览（TL;DR）

| 问题 | 结论 |
|---|---|
| 解析器是什么 | **不是 markdown-it，也不是现代 remark/micromark。** 是 **remark-parse v8/v9 时代的 tokenizer 架构**（`blockTokenizers` / `inlineTokenizers` + `mdast`）自打成 bundle，配 `mdast-util-to-hast` + `hast-util-to-html`。**[反编译]** |
| 两模式是否同一解析器 | **渲染器同源，词法层不同**：Reading View 与 LP 表格 widget 都调用同一对函数 `WT()`（md→mdast）与 `GT()`（mdast→hast→HTML 字符串）+ `RF()`（DOMPurify→DOM）；但 LP 的**编辑器语法树**（判断哪些行是表格）来自 CM6 上的 **StreamLanguage 包装的 CM5「hypermd」模式**，与 mdast 无关。**[反编译]** |
| LP 表格实现 | ViewPlugin 产出 `Decoration.replace({widget, block:true, side:1, inclusiveStart})` 覆盖整段表格行范围；widget 是自定义 `WidgetType`。**[反编译]** |
| 光标进入如何退回源码 | ⚠️ **本条已在交叉复核中修正，详见文首勘误**：不使用 `atomicRanges` 这一点正确，但"选区相交即不产出 replace 装饰"**只适用于公式/代码块，不适用于表格**。表格的 ViewPlugin 分支只检查搜索命中，光标/选区进入时**保持渲染态**。**[反编译 + 交叉复核]** |
| 渲染出的 HTML | `<table>` + `<thead><tr><th align="…">` + `<tbody><tr><td align="…">`，由 `mdast-util-to-hast` 的 table handler 生成（原文见 §3.1）。**[反编译]** |
| LP 表格容器类名 | `div.cm-embed-block.cm-table-widget.markdown-rendered` > `div.table-wrapper` > `table.table-editor`。**[反编译]** |
| Reading View 是否有滚动容器 | **没有额外 wrapper div**：靠一个内置 post-processor 在「表格是父节点唯一子元素」时给**父元素**设 `style.overflowX="auto"`。**[反编译]** |
| 类名 `markdown-table-*` | **不存在**（`app.css`/`app.js` 中 0 命中）。相关类名是 `markdown-rendered` / `cm-table-widget` / `table-wrapper` / `table-editor` / `table-cell-wrapper` / `HyperMD-table-row`。**[反编译]** |

---

## 1. 渲染管线

### 1.1 解析器身份：remark-parse 时代的 unified 栈（不是 markdown-it / 不是 lezer）

**反编译证据 A：bundle 中存在 remark-parse 的表格 block tokenizer**（`app.js` 内 webpack 模块 `7793`，偏移 ≈ 203,700–204,200；常量行在 204,120 附近）：

```js
// remark-parse v8/v9 风格：this.options.gfm / blockTokenizers / tokenizeInline
e.exports=function(e,t,n){
  var r,a,g,y,b,w,k,C,E,M,S,x,T,D,A,P,I,L,O,F,R,N;
  if(!this.options.gfm)return;
  r=0,A=0,w=t.length+1,k=[];                       // 收集含 '|' 的连续行
  for(;r<w;){ if(O=t.indexOf(o,r) /* \n */, F=t.indexOf(u,r+1) /* | */, ...){ if(A<p)return; break }
    if(P=t.slice(r,O),0===A)N=P[0]!==u;            // 首行是否以 | 开头
    else if(N&&P[0]===u||!N&&P[0]!==u)break;       // 各行「首管道」必须一致
    k.push(P),A++,r=O+1 }
  y=k.join(o), a=k.splice(1,1)[0]||[];             // a = 第 2 行 = 分隔行
  ... // 逐字符解析分隔行得到对齐数组 S（见 §4.1）
  L=e(y).reset({type:"table",align:S,children:I}); // mdast table 节点，带 align 数组
  for(;++D<A;){ ... e(y)({type:"tableCell",padding:t,children:this.tokenizeInline(r,o)},b) }
  return L}
;
var r="\t",o="\n",a=" ",s="-",l=":",c="\\",u="|",h=1,p=2,d="left",f="center",v="right";
```

要点：
- 表格 = **≥2 行**（`p=2`：表头行 + 分隔行），后续行只要仍含 `|` 就继续归入表格。
- 单元格内容走 **`this.tokenizeInline(...)`**（即完整行内解析器）。
- 每个 `tableCell` 节点被额外塞入一个**非标准字段 `padding:{start,end}`**（`m(y)` 计算首尾空白），LP 靠它把 DOM 单元格映射回源码切片。
- **tab / 全角空白等细节**：`m()` 只跳过 `\t` 与空格。

**反编译证据 B：bundle 中存在 `mdast-util-to-hast`**（模块 `7194` 的 `handle()`、模块 `2258` 的 table handler、模块 `7583` 的 footnote footer、模块 `7497` 的 `mdast-util-definitions`、`mdurl`(8131)、`property-information`/aria(8055)、`unist-util-remove-position`(8124)、`hast-util-to-html` 的可选标签省略表（19,000–20,300 与 37,400 附近）。`app.js` 中 **`markdown-it` / `markdownit` / `micromark` / `@lezer/markdown` 全部 0 命中**。

**反编译证据 C：Obsidian 自己的管线装配**（偏移 ≈ 1,349,300–1,352,100）：

```js
var VT = IE;                                  // remark-parse 的 Parser 类
VT.globalOptions = { breaks:!0, commonmark:!0 };   // ← 全局共享的解析选项
var HT = new LE, zT = new LE, qT = {};        // HT: mdast transformers; zT: hast transformers; qT: 自定义 hast handlers

function WT(e){                               // Markdown 源文本 → mdast
  var t = iM()(e),                            // 预处理（BOM/换行归一）
      n = new VT(String(t), t);
  n.setOptions(VT.globalOptions);
  for (var i = n.parse(), r = 0, o = HT.transformers; r < o.length; r++) o[r](i, e);
  return i }

function GT(e,t){                             // mdast → HTML 字符串
  (t = t || {}).allowDangerousHtml = !0, t.handlers = qT;
  for (var n = OT(e,t) /* mdast-util-to-hast */, i = 0, r = zT.transformers; i < r.length; i++) r[i](n,"");
  return JE()(n, { allowDangerousHtml:!0 })   // hast-util-to-html
}
```

同区域内还有 Obsidian 的自定义扩展（都以 `identifier + 回退 tokenizer` 方式注册：`OE(parser,"ilink","link",fn,locator)`、`FE(parser,"comment","fencedCode",…)`）：
- `mark`：`==高亮==` → `type:"mark"` + `data.hName:"mark"`
- `ilink`：`[[...]]` → `data.hName:"a", hProperties:{className:"internal-link", href, dataHref, ["data-tooltip-position"]:"top"}`
- `iembed`：`![[...]]` → `data.hName:"span", hProperties:{className:"internal-embed", src, alt}`
- `tag`：`#标签`；`comment`：`%%注释%%`（`qT.comment = function(){ return null }`，即彻底不输出）
- 图片尺寸语法 `![alt|100x200]` → `data.hProperties.width/height`（函数 `NT`）
- `KT(ast)` 从根节点提取 YAML frontmatter；`updateStrictLineBreaks()` 直接改 `VT.globalOptions.breaks = !strictLineBreaks` 后整体重渲染 —— **说明 Reading View 与 LP 共用同一个全局解析配置对象**。

**反编译证据 D：消毒与注入**（偏移 ≈ 1,723,500）：

```js
var FF = { /* …ALLOWED_* … */ RETURN_DOM_FRAGMENT:!0, FORBID_TAGS:["style"],
           ADD_TAGS:["iframe"],
           ADD_ATTR:["frameborder","allowfullscreen","allow","sandbox","data-tooltip-position"] };
function RF(e){ return document.importNode(LF.sanitize(e, FF), !0) }   // LF = DOMPurify
```

**Reading View 完整链路 [反编译]**：

```
文件文本
 → WT()   : remark-parse(+gfm) → mdast
 → HT.transformers (mdast 变换，含 plugin/主题注册项)
 → GT()   : mdast-util-to-hast(handlers=qT) → hast → hast-util-to-html → HTML 字符串
 → RF()   : DOMPurify.sanitize({RETURN_DOM_FRAGMENT, FORBID_TAGS:["style"], …}) → document.importNode
 → 追加到 previewEl = div.markdown-preview-view.markdown-rendered
          （其内 div.markdown-preview-sizer.markdown-preview-section；外层 div.markdown-reading-view）
 → MarkdownPreviewRenderer.postProcess(app, ctx)  ← 内置 + 插件/主题的 post-processor
 → resolveLinks / 内嵌笔记异步加载（W1.load）
```

（容器类名证据：`app.js` 1,964,569 / 1,964,592；`markdown-reading-view` 2,004,822。公开 API `MarkdownRenderer.render(app, markdown, el, sourcePath, component)` 内部就是 `WT → GT → RF` + postProcess，见 `app.js` 2,004,0xx 一带及 [obsidian.d.ts](https://github.com/obsidianmd/obsidian-api/blob/master/obsidian.d.ts)。）

### 1.2 Live Preview 的解析器是**另一套**：CM6 + StreamLanguage 包装的 CM5「hypermd」模式

**反编译证据 E**（偏移 ≈ 2,107,000–2,121,000）：bundle 内含一个 **CodeMirror 5 模式**，其 `token(stream,state)` 使用 CM5 的 `StringStream` API（`peek/match/eatSpace/eol/start/pos`），并且结尾有：

```js
… o }), "hypermd"), nU.defineMIME("text/x-hypermd","hypermd");
```

其中出现的行级/词级 token 名是 **HyperMD 体系**的：`line-HyperMD-table-row`、`line-HyperMD-table-<0|1|2>`、`hmd-table-sep`、`hmd-table-sep-<n>`、`hmd-table-column-<align>`、`line-HyperMD-quote-*`、`hmd-codeblock`、`hmd-internal-link`、`formatting-link-start/end`、`hmd-html-begin/end`、`line-HyperMD-callout` 等；其中还有表格对齐识别：

```js
if(!K){ hU.test(t.string) ? K=Qj.SIMPLE : dU.test(t.string) && (K=Qj.NORMAL);
  … var te=t.lookAhead(1);           // 下一行 = 分隔行
  ee=te.split("|");
  for(...){ var ie=ee[ne];
    if(vU.test(ie)) ie="right"; else if(mU.test(ie)) ie="left";
    else if(gU.test(ie)) ie="center"; else { if(!yU.test(ie)){K=Qj.NONE;break} ie="default" } }
  K && (o.hmdTable=K, o.hmdTableColumns=ee, …) }
if(K){ …
  0==oe && (b+=" line-HyperMD-table-"+K+" line-HyperMD-table-row line-HyperMD-table-row-"+ie+" line-parse-next"),
  K===Qj.NORMAL && (…) ? b+=" hmd-table-sep hmd-table-sep-dummy"
                        : o.hmdTableCol<re && (b+=" hmd-table-sep hmd-table-sep-"+oe, o.hmdTableCol+=1) }
```

同一模块内还内联了 `@codemirror/language` 的 `Language`/`StreamLanguage` 实现（`StreamLanguage.define(spec)` 形态：`{name, token, blankLine, startState, copyState, indent, languageData, tokenTable, mergeTokens}`，偏移 ≈ 2,140,800–2,145,000）。**[推断，高置信]**：Obsidian 把这份 CM5 hypermd 模式用 StreamLanguage 适配进 CM6，作为编辑器的 markdown 语言；token 类名通过 Obsidian **打过补丁的** `@codemirror/language` 暴露的 `tokenClassNodeProp` / `lineClassNodeProp` 挂在语法树节点上。

> **[社区]** obsidian-typings 明确写道 `lineClassNodeProp`："The `@lezer/common#NodeProp` that holds the CSS class of corresponding line-mode token. **This only exists and can only be used in Obsidian.**" —— 即 Obsidian 对 `@codemirror/language` 做了非上游扩展（同一导出表里还有非上游的 `ignoreSpellcheckToken`，见 `app.js` 245,300–252,600 的导出映射）。
> 来源：<https://obsidian-typings.github.io/obsidian-typings/catalyst/api/@codemirror__language/augmentations/vars/lineClassNodeProp/>

对照：**[上游源码]** `@lezer/markdown` 的表格节点名是 `Table` / `TableHeader` / `TableRow` / `TableCell` / `TableDelimiter`，但 **Obsidian 的 bundle 里对 `TableDelimiter`、`"Table"`、`ATXHeading1`、`Hyperlink`、`InlineCode` 等 lezer-markdown 标识符的检索全部 0 命中** —— 这是「Obsidian 不用 lezer-markdown」的决定性证据。

### 1.3 Reading View vs Live Preview 差异总表

| 维度 | Reading View（预览） | Live Preview（实时预览/编辑） |
|---|---|---|
| 宿主 | 静态 DOM：`.markdown-reading-view > .markdown-preview-view.markdown-rendered > .markdown-preview-sizer` | CodeMirror 6 `EditorView`（`.markdown-source-view.mod-cm6`） |
| 行级词法 | 无（不参与） | CM6 语法树 = StreamLanguage(CM5 hypermd 模式)，行类 `HyperMD-table-row` |
| 表格识别 | remark-parse table tokenizer（mdast） | 颜色 token 判定「表格行」范围 → 触发 widget；widget 内**再**用 remark-parse 解析同一段源码 |
| 表格渲染 | `GT()` + `RF()` | widget 内**同一个** `GT()` + `RF()`（`RF(GT(a))`，`app.js` ≈2,033,150） |
| 折叠/源码切换 | 不适用（永远渲染） | 选区/搜索命中 → 撤销 replace 装饰 → 显示源码 |
| post-processor | 有（`MarkdownPreviewRenderer.postProcess`） | 有（每个单元格 `contentEl` 上也跑一次，`app.js` ≈2,043,9xx） |
| 插件 API 可见性 | `MarkdownRenderer.render` / `registerMarkdownPostProcessor` | 同左（`editorLivePreviewField` 用于判定当前是否 LP） |

**[官方文档]** 模式语义见 <https://obsidian.md/help/edit-and-read>；`editorLivePreviewField`（`StateField<boolean>`，`app.js` 2,516,102 定义 `xJ = CJ(!1)`）与 `registerMarkdownPostProcessor` 见 <https://docs.obsidian.md/Reference/TypeScript+API/editorLivePreviewField>、<https://docs.obsidian.md/Reference/TypeScript+API/Plugin/registerMarkdownPostProcessor>。

---

## 2. Live Preview 表格机制

### 2.1 装饰器：ViewPlugin + 块级 replace

**[反编译]**（`app.js` ≈ 2,987,000–2,996,500，单个大函数 `W3(app, view)`）：

```js
var d=h.state, f=Du(d),                       // f = syntaxTree(state)
    v=d.doc,
    m=t.hasFocus? d.selection.ranges : [],     // 编辑器失焦时视为「无选区」
    g=d.field(nO), y=tO.get("obsidian-search-match-highlight"),
    b=function(e,t){ return LL(m,e,t) || OL(g,y,e,t) },   // 选区相交 或 搜索命中相交
    w=function(e,t,n){ return e.block && n===v.length && (e.inclusiveEnd=!1), nn.replace(e).range(t,n) };
…
  var ie=i.prop(Sp);                          // Sp = lineClassNodeProp
  if(ie){
    var oe=ie.split(" "), re=new Set(oe);
    … re.has("HyperMD-table-row") && (Z(r), r-X>1 && J(r), -1===Y && (Y=r), X=a);   // 累积连续表格行 [Y,X)
  }
…
var J=function(t){
  if(-1!==Y && X<t){
    for(var o=v.slice(Y,X), s=(X!==f.length-1||f.length===v.length), c=null, …;
        …){ if(s? d.receiveUpdate(h,o) : d.receiveIncompleteUpdate(h,o)){ c=d; x.remove(d); break } }
    if(!OL(g,y,Y,X)){                                  // 搜索命中则也显示源码
      c || (c = new nj(n,e,o,s));                      // c = 表格 widget（nj 类）
      var b = Y>0 && Y>fO(h.newDoc)+1;
      C.push(w({ widget:c, side:1, block:!0, inclusiveStart:b }, Y, X));   // ← Decoration.replace(block:true)
      rd.isAndroidApp && X!==v.length && C.push(B3.range(X+1));
    }
    c && (c.setPos(Y,X), c.receiveSelection(h), a.push(c)), Y=-1, X=-1;
  }};
…
nn.set(C,!0)                                  // Decoration.set(ranges, true)  ← 排序后的 DecorationSet
```

要点：
- **是 `Decoration.replace` + `WidgetType`，块级（`block:true`）**，覆盖范围 = 第一行表格行的行首 ~ 最后一行表格行的行尾（`Y..X`），并带 `side:1`、`inclusiveStart`；文档末尾时把 `inclusiveEnd` 置 false（CM6 对块装饰的边界要求）。
- **`block:true` 意味着它会切断行结构**（CM6 要求 block replace 的范围两端在行边界），这正是「表格会撑满整块、并把源码行折叠掉」的原因。
- `Decoration.set(C, true)` 对应 `Decoration.set(ranges, sorted=true)`（CM6 的排序变体，见 [codemirror 参考](https://codemirror.net/docs/ref/#view.Decoration%5Ereplace)）。
- **没有使用 `atomicRanges`**：全文检索 `atomicRanges` 只命中 CM6 库自身的折叠/删除命令实现（`@codemirror/language` 的 fold 与 `@codemirror/view` 的 `s.expandSelection` 等），**没有任何表格相关的 `atomicRanges` 注册**。光标进出表格是靠「重算装饰 + 选区相交判断」实现的，不是原子范围。
- 光标/选区在表格内时 widget 消失 → 直接看到并使用原生文本编辑；点击 widget 空白区域由 widget 自己处理（`containerEl` 上绑 click → `placeCursorAround("after")`；`onpointerdown` 对 `e.target===containerEl` 直接 `preventDefault` 防止误进源码态）。

### 2.2 Widget 本体：`nj` 类（`app.js` ≈ 2,018,900–2,037,600）

```js
o.containerEl = createDiv({ cls:"cm-embed-block cm-table-widget markdown-rendered",
                            onpointerdown:function(e){ e.target===e.currentTarget && e.preventDefault() } });
o.containerEl.addEventListener("click", function(e){ e.target===a && o.placeCursorAround("after") });
```

`toDOM()` 返回该 `containerEl`；若文档尚未完整解析（`isDocComplete === false`）则：

```js
n.onNodeInserted(function(){ e.isDocComplete||e.tableEl||(n.addClass("is-loading"),
  n.style.height="".concat(1.1*i.containerEl.clientHeight,"px")) }, !0)
```

**`render()` 的完整流程（原文节选，`app.js` ≈ 2,033,000–2,035,000）**：

```js
t.prototype.render=function(){
  var e=this,t=this,n=t.doc,i=t.containerEl,r=t.rows;
  this.clear();
  var o, a=WT(n.toString());                       // ← 同一套 remark-parse
  if(NE(a,"table",function(e){ return o=e, NE.EXIT }), o){       // NE = unist-util-visit
    var s=this.alignments=o.align;                 // mdast table.align
    if(s?.length){
      var l=this.colWidths=s.map(function(){ return 5 }), c=RF(GT(a));   // ← 同一套 mdast-util-to-hast + hast-util-to-html + DOMPurify
      if(c?.firstChild.instanceOf(HTMLTableElement)){
        var u=c.firstChild; u.addClass("table-editor"), u.tabIndex=-1;
        var h=[]; h.push.apply(h,Array.from(u.tHead.rows));               // ← thead 必须存在
        for(var p=0,d=Array.from(u.tBodies);p<d.length;p++) h.push.apply(h,Array.from(d[p].rows));
        var v=s.length,m=v,g=!1;
        NE(o,"tableRow",function(t){
          var i=[],o=r.length,a=h[o],c=!0;
          NE(t,"tableCell",function(t){
            var r=t.position,u=t.padding,h=r.start,p=r.end,d=i.length,f=a.cells[d],
                m=n.sliceString(h.offset+u.start, p.offset-u.end);         // ← 用 ast position + padding 反查源码切片
            f||(g=!0,f=a.insertCell(d)),
            !c || m && /^\s*:?\s*-+\s*:?\s*$/.test(m) || (c=!1);          // ← 判断「分隔行缺失」→ isMalformed
            var y=new ej(e,o,d,m,u.start,u.end);
            y.init(f,h.offset,p.offset), i.push(y), e.postProcess(y);     // ← 单元格也跑 post-processor
            0===o && e.createDragHandle(y,"col"), 0===d && e.createDragHandle(y,"row");
            …
            l[d]=Math.max(l[d],m.length+2) });                            // ← 列宽 = 内容长度+2
          c? g=!0 : r.push(i) });
        … // 补齐 DOM 中缺失的行/列（insertRow/insertCell），并处理「末尾多余管道行」
      }}}
  // 组装 DOM
  i.createDiv("table-wrapper", function(t){
    t.append(u),                                                          // <table class="table-editor">
    t.createDiv("table-row-btn", function(t){ Ag(t,"lucide-plus"), … t.addEventListener("click",function(){ return e.insertRow(e.rows.length,0) }) }),
    t.createDiv("table-col-btn", function(t){ Ag(t,"lucide-plus"), … t.addEventListener("click",function(){ return e.insertColumn(0,e.alignments.length,null) }) }) }),
  i.removeClass("is-loading"), i.removeAttribute("style"),
  this.isMalformed=g, this.tableEl=u;
  … // 恢复跨单元格选择
}
```

由此可确认的 LP 结构：

```
div.cm-embed-block.cm-table-widget.markdown-rendered        ← widget 根（同时带 markdown-rendered，复用阅读视图 CSS）
├─ div.table-wrapper
│  ├─ table.table-editor[tabindex=-1]                       ← 由 GT()+RF() 生成，含 thead/tbody
│  │  ├─ thead > tr > th[align]
│  │  └─ tbody > tr > td[align]
│  │     └─ div.table-cell-wrapper                          ← ej.init() 包裹原单元格子节点（空则插入 <br>）
│  ├─ div.table-row-btn   (lucide-plus, 追加行)              ← 首行单元格内还有 div.table-col-drag-handle
│  └─ div.table-col-btn   (lucide-plus, 追加列)
└─ (拖动中临时) div.table-drag-target.mod-col|mod-row
```

### 2.3 单元格模型 `ej` 与「源文本自动对齐重排」

`app.js` ≈ 2,011,000–2,018,000：

```js
function ej(table,row,col,text,padStart,padEnd){ … this.text=text; this.padStart=…; this.padEnd=…; this.start/end … }
e.prototype.init=function(el,start,end){
  this.el=el; this.start=start; this.end=end; this.setTextDir();
  var r=Array.from(el.childNodes), o=this.contentEl=el.createDiv("table-cell-wrapper");
  o.append.apply(o,r), 0===r.length && o.createEl("br");   // 空单元格塞 <br> 撑高
  … // 四击选中整表、contextmenu、dragenter/leave、pointerdown 拖选
}
e.prototype.updateWidth=function(e){                        // 依据对齐把空格分配到左右
  var o=e-this.text.length, a=this.table.alignments[this.col];
  "right"===a ? s=o-1 : "center"===a ? (s=Math.floor(o/2), l=Math.ceil(o/2)) : l=o-1;
  this.padStart=s, this.padEnd=l }
e.prototype.getAbsoluteOffsets=function(){                  // 源码绝对偏移（供 CM6 事务/选区使用）
  var e=this.table.start, {start:n,end:i}=this;
  return { start:e+n, end:e+i, textStart:e+n+this.padStart, textEnd:e+i-this.padEnd } }
```

**关键行为：Obsidian 会在你打字时改写源 markdown 来保持表格「整齐」**——`updateCell()` 重新计算该列 `colWidths = max(全列最长文本+2, 5)`，然后为**整列所有单元格**生成 `{from,to,insert}` 变更（左侧补齐 `padStart`、右侧 `padEnd`），并对第 2 行（分隔行）重新生成：

```js
t.prototype.makeAlignmentRow=function(e,t){
  … case"left":   r+="| :"+"-".repeat(a-3)+" ";   break;
    case"center": r+="| :"+"-".repeat(a-4)+": ";  break;
    case"right":  r+="| "+"-".repeat(a-3)+": ";   break;
    default:      r+="| "+"-".repeat(a-2)+" " }
  return r+="|" }
```

整表回写（每次结构变化都走这一个事务）：

```js
t.prototype.dispatchTable=function(e,t,n){
  … var l=this.rebuildTable();        // 把 rows/alignments/colWidths 序列化回 markdown 文本
  if(l.length && e!==undefined && t!==undefined){ … }
  a.dispatch({ selection:s, changes:[{ from:r, to:o, insert:l }], scrollIntoView:!1 }) }
```

注意 `getTableString()` 中的对齐填充同样左右分配空格，且**列宽以 `text.length`（UTF-16 码元数）计**，不区分全角/半角 → **中文表格在源码态会视觉错位**（[推断/高置信]，见 §6 坑 ⑥）。

**双向同步**：文档变化时 widget 通过 `reconcileChanges(state, tr)`（用 `tr.changes.iterChanges` 只接受落在自己范围内的变更）+ `receiveUpdate` / `receiveIncompleteUpdate` 做增量重建；对 undo/redo 有专门分支（`e.isUserEvent("undo")||e.isUserEvent("redo")`）。

**单元格内嵌编辑器**：`editor.editTableCell(this, cell)` 会为被点中的单元格创建一个内嵌 CM6 `EditorView`（`tableCell.cm`），`tableCell` 是编辑器对象上的一个字段（`o.setReadonly(...)` / `o.cm.hasFocus` / `o.table === this`）；跨单元格拖选时 `updateCellReadonly` 会**把内嵌编辑器设为只读**，取消选区后再恢复。选区映射用 `pe.single/range`、`BL(sel,-offset)`、`VL(sel,from,to)`。

**上下文菜单/操作**（i18n key 均为 `bd.table.*`）：插入/删除/移动/复制 行与列、`setAlignment(cols,"start"|"center"|"end")`（RTL 感知：`"rtl"===getComputedStyle(this.tableEl).direction` 时 start/end 互换，最终写成 `left|center|right` 并 `el.setAttr("align", s)`）、清空选区、删除选区、`sortByColumn`、复制/剪切/粘贴（走 Electron `remote.getCurrentWebContents()`）。

### 2.4 与 Reading View 的共享点（重要）

1. 表格 HTML 由**同一个** `GT()` 产生（`RF(GT(a))`）；
2. 单元格内容会跑**同一套** `MarkdownPreviewRenderer.postProcess`（`$W.postProcess(app, {docId, sourcePath, promises, addChild, getSectionInfo, replace, containerEl, el: cellContentEl, displayMode:false})`）——所以 `registerMarkdownPostProcessor` 的插件在 LP 表格单元格里同样生效（**注意 `el` 是单元格的 `.table-cell-wrapper`，不是整个表格**）；
3. `resolveLinks`（`GW(app, el, path)`）在两边都要跑一次以解析 `[[链接]]`；
4. 共用 `VT.globalOptions`（`breaks` 等）。

---

## 3. DOM 与 CSS

### 3.1 Reading View 的表格 DOM（有原文可验）

**[反编译]** `mdast-util-to-hast` 的 table handler（webpack 模块 `2258`，`app.js` ≈ 29,440）**逐字**如下：

```js
e.exports=function(e,t){                       // e = state, t = mdast table 节点
  var n,a,s,l,c,u=t.children,h=u.length,p=t.align||[],d=p.length,f=[];
  for(;h--;){
    for(a=u[h].children, l = 0===h ? "th" : "td", n=d||a.length, s=[]; n--;)
      c=a[n], s[n]=e(c,l,{align:p[n]}, c?o(e,c):[]);      // ← 每个单元格带 {align: left|center|right|null}
    f[h]=e(u[h],"tr",r(s,!0)) }
  return e(t,"table", r([ e(f[0].position,"thead", r([f[0]],!0)) ]
    .concat(f[1] ? e({start:i.start(f[1]),end:i.end(f[f.length-1])},"tbody", r(f.slice(1),!0)) : []), !0)) };
```

（`e(tag,props,children)` = `mdast-util-to-hast` 的 `u()` 辅助；`r()` = `wrap(children,true)`，会在行/单元格之间插入 `"\n"` 文本节点 —— 所以 Obsidian 渲染出的表格 HTML 带换行缩进，是「多行、含空白的源 HTML」。）

因此 Reading View 输出的 HTML 形状为：

```html
<table>
<thead>
<tr>
<th align="left">…</th>
<th align="center">…</th>
<th align="right">…</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">…</td>
…
</tr>
</tbody>
</table>
```

- 无对齐（`null`）时该属性被 `hast-util-to-html` 省略（无 `align` 属性）。
- 首个数据行**只**进 `<thead>`，其余进 `<tbody>`（`tbody` 仅在存在第 2 行数据时才创建）。
- **没有 `<div class="table-wrapper">`、没有 `<colgroup>`、没有 `style="text-align"`**（`table-wrapper` 在 `app.js` 中仅出现 1 次，即 LP 的 `createDiv("table-wrapper")`；`align="` 字面量在 `app.js` 中 0 命中，说明对齐只通过 DOM 属性/属性对象传递）。

### 3.2 超宽表格的横向滚动（内置 post-processor）

**[反编译]** `app.js` ≈ 1,994,505（`AW.registerPostProcessor` = `MarkdownPreviewRenderer.registerPostProcessor`）：

```js
AW.registerPostProcessor(function(e,t){
  for(var n=0,i=e.findAll("table"); n<i.length; n++){
    var r=i[n], o=r.parentNode;
    if(o && o.instanceOf(HTMLElement) && r===o.firstChild && r===o.lastChild){
      o.style.overflowX="auto";                                  // ← 表格是父节点唯一子元素时，父节点成为滚动容器
      for(var a=r.findAll("th, td"), s=0,l=a.length; s<l; s++){
        var c=a[s], u=ag(c);                                     // ag = 文本方向探测
        c.dir=u, 0===s && (o.dir=u) } } } });
```

即 Reading View 的横向滚动**依赖父元素 `overflow-x:auto` 的内联样式**（hast 输出表格时其父就是容器元素，通常就是 `.markdown-preview-sizer` 里的那个节点），不是专门的 wrapper。LP 侧则由 CSS 承担（下一节）。

### 3.3 LP 表格 CSS（`app.css` 摘录，偏移 115,174–126,600）

```css
.markdown-source-view.mod-cm6 .cm-html-embed,
.markdown-source-view.mod-cm6 .cm-callout,
.markdown-source-view.mod-cm6 .cm-table-widget { white-space: normal; overflow-wrap: normal; word-break: normal; }

.markdown-source-view.mod-cm6 .cm-table-widget {
  --table-drag-handle-size: var(--size-4-4);
  padding: var(--table-drag-handle-size);
  margin: 0 calc(-1 * var(--size-4-4)) !important;
  overflow-x: auto;                    /* ← LP 的横向滚动容器 */
  overflow-y: hidden; }
.is-mobile .markdown-source-view.mod-cm6 .cm-table-widget { --table-drag-handle-size: var(--size-4-6); }
.markdown-source-view.mod-cm6 .cm-table-widget.is-loading { padding: 0; margin: 0 !important; }
.markdown-source-view.mod-cm6 .cm-table-widget .table-wrapper { position: relative; width: fit-content; }
.markdown-source-view.mod-cm6 .cm-table-widget tr { height: 1px; }
.markdown-source-view.mod-cm6 .cm-table-widget th,
.markdown-source-view.mod-cm6 .cm-table-widget td { height: inherit; min-width: … }

/* 状态类：.has-selection / .is-selected / .is-dragging / .has-focus（移动端） */
.markdown-source-view.mod-cm6 .cm-table-widget.has-selection .cm-selectionLayer,
.markdown-source-view.mod-cm6 .cm-table-widget.has-selection .cm-cursorLayer { display: none; }
.markdown-source-view.mod-cm6 .cm-table-widget.is-selected table::after { /* 选区蒙层 */ background-color: var(--table-selection); … }

/* 拖动句柄 / 加号按钮 */
.markdown-source-view.mod-cm6 .cm-table-widget .table-row-drag-handle,
.markdown-source-view.mod-cm6 .cm-table-widget .table-col-drag-handle { position:absolute; cursor:grab; opacity:0; touch-action:none; … }
.markdown-source-view.mod-cm6 .cm-table-widget .table-row-btn,
.markdown-source-view.mod-cm6 .cm-table-widget .table-col-btn { position:absolute; height:var(--table-drag-handle-size); width:var(--table-drag-handle-size); … }
.markdown-source-view.mod-cm6 .cm-table-widget .table-cell-wrapper { height:100%; padding: var(--size-2-2) var(--size-4-2); }
```

### 3.4 Reading View 表格 CSS（`app.css` 206,600–209,600）

```css
/* Tables */
.markdown-rendered table { margin-block-start: var(--p-spacing); margin-block-end: var(--p-spacing); word-break: normal; }
.cm-html-embed table, .markdown-rendered table { border-collapse: collapse; line-height: var(--table-line-height); }
.cm-html-embed td, .markdown-rendered td, .cm-html-embed th, .markdown-rendered th {
  padding: var(--size-2-2) var(--size-4-2);
  border: var(--table-border-width) solid var(--table-border-color);
  max-width: var(--table-column-max-width);
  min-width: var(--table-column-min-width);
  vertical-align: var(--table-cell-vertical-alignment); }
.cm-html-embed td, .markdown-rendered td { font-size: var(--table-text-size); color: var(--table-text-color); }
.cm-html-embed th, .markdown-rendered th { font-size: var(--table-header-size); font-weight: var(--table-header-weight);
  color: var(--table-header-color); font-family: var(--table-header-font); line-height: var(--line-height-tight); }
.cm-html-embed th, .markdown-rendered th, .cm-html-embed td, .markdown-rendered td { text-align: start; }
.markdown-rendered th[align="left"],  .markdown-rendered td[align="left"]  { text-align: start; }   /* 注意是逻辑值 start/end */
.markdown-rendered th[align="center"],.markdown-rendered td[align="center"]{ text-align: center; }
.markdown-rendered th[align="right"], .markdown-rendered td[align="right"] { text-align: end; }
.markdown-rendered thead > tr > th, .markdown-rendered tbody > tr > td {
  white-space: var(--table-white-space); text-overflow: ellipsis; overflow: hidden; }   /* 宽内容裁剪 */
.markdown-rendered thead > tr > th > .markdown-embed,
.markdown-rendered tbody > tr > td > .markdown-embed { white-space: normal; }          /* 但嵌入笔记可换行 */
.markdown-rendered tbody tr { background-color: var(--table-background); }
.markdown-rendered tbody tr:nth-child(odd) { background-color: var(--table-row-alt-background); }
.markdown-rendered tbody tr > td:nth-child(2n+2) { background-color: var(--table-column-alt-background); }
@media (hover:hover){ .markdown-rendered tbody tr:hover { background-color: var(--table-row-background-hover); } }
```

### 3.5 类名清单（表格相关，全部经 `app.css`/`app.js` 检索确认）

| 类名 | 出现位置 | 说明 |
|---|---|---|
| `markdown-rendered` | RV 容器、LP widget 根、嵌入、代码块 widget、canvas 卡片、社区插件 README… | 「已被渲染的 markdown」通用标记；表格样式都挂在它下面 |
| `markdown-preview-view` / `markdown-preview-sizer` / `markdown-preview-section` / `markdown-reading-view` | RV 容器层级 | — |
| `markdown-source-view mod-cm6` | LP 容器 | CM6 源视图 |
| `cm-embed-block` | LP widget 基类（表格/代码块/HTML 嵌入共用） | — |
| `cm-table-widget` | LP 表格 widget 根 | **只在 `app.js` 出现 1 次**（即 widget 构造处） |
| `is-loading` / `has-selection` / `is-selected` / `is-dragging` / `has-focus` | LP widget 状态 | — |
| `table-wrapper` | LP（`createDiv("table-wrapper")`） | RV **没有** |
| `table-editor` | LP 内层 `<table>`（`u.addClass("table-editor")`） | `app.css` 中无对应规则（仅作语义标记） |
| `table-cell-wrapper` | LP 每个 `th/td` 内的 div | RV 无 |
| `table-row-drag-handle` / `table-col-drag-handle` / `table-row-btn` / `table-col-btn` / `table-drag-target.mod-row|mod-col` | LP 交互件 | — |
| `cm-html-embed` (+`cm-embed-block`) | 源码里的原始 HTML 块（`createEl("div"/"span","cm-html-embed")` + `appendChild(RF(html))`） | 其内表格共用 `.cm-html-embed table` 样式 |
| `HyperMD-table-row` / `HyperMD-table-row-0` / `HyperMD-table-row-1` / `hmd-table-sep` / `hmd-table-column-<align>` | 语法树 token 类 + 旧版 CM5 编辑器 CSS | 见 §1.2、§5 |
| `markdown-table-*` | **不存在**（0 命中） | — |

### 3.6 表格 CSS 变量

**[官方文档]** 官方列出了 36 个表格变量（`--table-background`、`--table-border-width`、`--table-header-font`、`--table-column-max-width`、`--table-selection*`、`--table-drag-handle-*`、`--table-add-button-*` 等），与本机主题文档一致：<https://docs.obsidian.md/Reference/CSS+variables/Editor/Table>（本地 `docs\Obsidian-Dev-Docs\en\Reference\CSS variables\Editor\Table.md`）。
**[反编译]** `app.css` 中另有文档未列出的：`--table-drag-handle-size`（LP，默认 `--size-4-4`）、`--table-selection-blend-mode`、`--table-row-last-border-width`、`--table-column-first/last-border-width`。
**[反编译]** 变量定义集中在 `app.css` 87,379–89,241。

---

## 4. 特性处理细节

### 4.1 列对齐 `:---:` / `:--:` / `--:`

- **mdast 层**：remark-parse 的 tokenizer 只解析**第二行（分隔行）**得到 `align[]`（`app.js` ≈204,900 原文见 §1.1）：

```js
if((E=a.charAt(r))===u /* | */){ … if(!1===g){ if(!1===R) return } else S.push(g), g=!1; R=!1 }
else if(E===s /* - */) M=!0, g=g||null;
else if(E===l /* : */) g = g===d ? f : (M && null===g ? v : d);   // d="left" f="center" v="right"
else if(!i(E)) return;                                            // i = 数字判断
r++; }
!1!==g && S.push(g);
if(S.length<h) return;                                            // h=1：至少 1 列
```
  语义：`---` → `null`；`:--` → `left`；`:-:` → `center`；`--:` → `right`（无冒号 → null，不写 `align` 属性）。
- **hast/DOM 层**：`{align: p[n]}` → `align="left|center|right"`（§3.1）。
- **CSS 层**：`[align="left"] → text-align: start`、`right → end`（逻辑值，自动适配 RTL）。
- **LP 层**：`setAlignment(cols, "start"|"center"|"end")` 会先读 `getComputedStyle(tableEl).direction`，RTL 时把 start/end 对调成 `left/right`，再 `el.setAttr("align", s)` 并**重写整表源文本**（`makeAlignmentRow`）。
- **Obsidian 官方示例**（内置 sandbox 库的 `Formatting/Table.md`）：用 `:----------------|-------------:` 表达左右对齐。

### 4.2 单元格内联格式（粗体/链接/行内代码/高亮/内联公式/wiki 链接）

- tokenizer 内 `children: this.tokenizeInline(r, o)` → **单元格内走完整行内解析**，因此 `**bold**`、`` `code` ``、`[text](url)`、`==highlight==`、`$x$`、`[[wikilink]]`、`#tag`、`%%comment%%` 全部生效（`mark`/`ilink`/`iembed`/`tag` 是 Obsidian 自加的 tokenizer，§1.1）。
- 分隔行本身不会被渲染成数据行（`type:"table"` 的 children 只来自第 1、3、4… 行；第 2 行仅贡献 `align`）。
- 表格内 wiki 链接的 `|` 必须转义（§4.3）。

### 4.3 转义管道符 `\|`

- **remark 实现**（`app.js` ≈204,080 原文）：

```js
else C&&(x+=C,C=""), x+=E, E===c && r!==w-2 && (x+=P.charAt(r+1), r++);   // c="\\"
```
  即遇到 `\` 时把 `\` 与下一个字符一起并入当前单元格原文（不当作分隔符），随后交由**行内解析器**把 `\|` 解析为文本 `|`。
- **Obsidian 官方说明**（内置 sandbox 库 `Formatting/Table.md` 原文）：
  > "If you put links in tables, they will work, but if you use Piped Links, the pipe must be escaped with a `\` to prevent it being read as a table element."
  示例：`[[Format your notes\|Formatting]]`。
- **[上游对照]** lezer-markdown 的 `parseRow()` 用 `esc = !esc && next == 92` 处理反斜杠转义，规则一致（见 §5.1）。
- 反向（HTML→Markdown）时 Obsidian 用 Turndown 规则重新转义（`app.js` ≈1,694,9xx）：

```js
MO.addRule("tableCell",{ filter:["th","td"], replacement:function(e,t){
  return (0===Array.prototype.indexOf.call(t.parentNode.childNodes,t)?"|":"")
       + function(e){ return e=e.trim().replace(/\|+/g,"\\|").replace(/\n\r?/g,"<br>"), e+"|" }(e)
       + PO(t,"   |") } });
var TO={ left:":--", right:"--:", center:":-:" };     // ← Obsidian 自己生成分隔行时用的 3 字符写法
```

### 4.4 单元格内换行

- 表格行是**单行**，tokenizer 以 `\n` 切行，因此单元格内不可能有真实换行；
- 唯一途径是写内联 HTML `<br>`（走 `html` inline tokenizer → hast `raw`/`element` → `<br>`，且 `allowDangerousHtml:true` 会保留）；
- 佐证：Obsidian 自己的 HTML→Markdown 转换把单元格里的 `\n` 反向写成 `<br>`（上一节 Turndown 规则）。
- **[未验证]** LP 单元格内嵌编辑器是否允许输入软换行（源码层面找不到载体；`placeCursorInCell(...,"last-line")` 的存在只能说明代码做了多行防御）。

### 4.5 表格内嵌入图片 / wiki 链接

- `![[img.png]]` → mdast `iembed` 节点（`data.hName:"span", hProperties:{className:"internal-embed", src, alt}`）→ Reading View 渲染出 `span.internal-embed`，随后由 `MarkdownPreviewRenderer.postProcess` 里的内嵌加载逻辑**异步**加载：

```js
var v=r.findAll(".internal-embed:not(.is-loaded)");
… var w=W1.load({ app:e, linktext:b, sourcePath:n, containerEl:y, displayMode:o, showInline:!0, depth:f });
```
  LP 侧同一逻辑（widget 的 `postProcess` 用单元格 `contentEl` 作为 `containerEl`）。
- 图片尺寸语法 `![[img|100x200]]` 或 `![alt|100x200](url)` → `NT()` 写入 `data.hProperties.width/height`，最终成为 `<img width height>`。
- CSS 特例：`.markdown-rendered thead>tr>th>.markdown-embed { white-space: normal }` —— 嵌入（`![[note]]`）在单元格内允许换行（与普通文本单元格的 `ellipsis` 不同）。

### 4.6 超宽表格

- **Reading View**：内置 post-processor 给「唯一子元素」的父节点设 `overflowX:auto`（§3.2）；单元格 `max-width: var(--table-column-max-width)` + `text-overflow: ellipsis; overflow: hidden` → 内容过长时**省略号 + 裁剪**，表格整体横向滚动而不是无限撑宽。
- **Live Preview**：`.cm-table-widget { overflow-x: auto; overflow-y: hidden; padding: var(--table-drag-handle-size); margin: 0 calc(-1*var(--size-4-4)) !important }`（负 margin 抵消 padding，让表格贴边），另有 `.table-wrapper{position:relative;width:fit-content}` 作为拖动句柄定位参照。
- **[社区]** 论坛存在「表格宽度 / readable line width」相关讨论，例如 <https://forum.obsidian.md/t/max-table-width-without-rll-readable-line-width-minimal-theme/95127>（标题即结论，未逐篇核对正文）。

### 4.7 其它可复刻的实现细节

- **列数不一致的处理**：remark 只要求分隔行至少有 1 列（`S.length<h`, `h=1`），**不强制表头与分隔行列数相等**；行与行之间只要求「首管道一致性」（`N&&P[0]===u||!N&&P[0]!==u → break`）。LP 渲染时对超出的单元格 `insertCell()` 补齐、对缺失的补 `insertRow()/insertCell()`，并把这种不一致标记为 `isMalformed`（`g=true`）。**[上游对照]** lezer-markdown 反而要求 `firstCount == parseRow(delimiterLine)`（列数必须一致）。→ **两套实现对「脏表格」的容忍度不同。**
- **表格终止条件**：遇到不含 `|` 的行即结束（remark 实现），所以表格后必须空行或非管道行；**[社区]** 论坛有「表格上方空行」相关讨论 <https://forum.obsidian.md/t/hiding-the-blank-line-above-tables/63465>。
- **分隔行缺失**：LP 会 go through `!c || /^\s*:?\s*-+\s*:?\s*$/.test(m) || (c=!1)` 判定；`isMalformed` 时点选单元格会走 `dispatchTable()`（整表重写）而不是 DOM 内嵌编辑器。
- **空表格行**：LP 末尾若出现 `/^\|[^\|]*$/`（只有 `|`）或「分隔行式」的行，会**额外插入一行空行**（`u.insertRow(y)`），这是「表格末尾自动多一个空行」的来源。
- **HTML 消毒**：`FORBID_TAGS:["style"]` → 表格里写 `<style>` 会被 DOMPurify 删除；`ADD_TAGS:["iframe"]`、`ADD_ATTR` 含 `data-tooltip-position`。

---

## 5. 生态与第三方方案

### 5.1 CodeMirror 6 / lezer 官方生态

- **`@lezer/markdown`** 提供 GFM 表格**解析**（不含渲染）。**[上游源码]** 节点：`Table`(block)、`TableHeader`(style heading)、`TableRow`、`TableCell`(style content)、`TableDelimiter`(style processingInstruction)；表格判定：第二行必须匹配 `const delimiterLine = /^\|?(\s*:?-+:?\s*\|)+(\s*:?-+:?\s*)?$/` 且首行列数等于分隔行列数；单元格切分 `parseRow()` 处理 `\` 转义、跳过首尾 ASCII 空格/Tab。源码：<https://github.com/lezer-parser/markdown/blob/main/src/extension.ts>
- **`@codemirror/lang-markdown`**：`commonmarkLanguage`（严格 CommonMark，**无表格**）；`markdownLanguage` = commonmark + `GFM`（Table/TaskList/Strikethrough/Autolink）+ Subscript/Superscript/Emoji，并为 `Table` 注册 `foldNodeProp`（可折叠整表）。源码：<https://github.com/codemirror/lang-markdown/blob/main/src/markdown.ts>
- **CM6 官方没有「表格渲染 / 表格编辑器」扩展**：要实现 Obsidian 那种效果必须自己写 `WidgetType` + `Decoration.replace({block:true, widget})` + 选区判断（参考 <https://codemirror.net/docs/ref/#view.WidgetType>、<https://codemirror.net/docs/ref/#view.Decoration%5Ereplace>、[codemirror/dev#1529](https://github.com/codemirror/dev/issues/1529) 关于替换长文本的讨论）。
- **Obsidian 官方给插件开发者的装饰器文档**（内容基本是 CM6 文档的提炼，**没有**给出表格/atomicRanges 的实现范例）：<https://docs.obsidian.md/Plugins/Editor/Decorations>

### 5.2 第三方表格实现（可直接借用的参考）

| 项目 | 技术路线 | 与 Obsidian 的异同 |
|---|---|---|
| [HyperMD](https://github.com/laobubu/HyperMD)（laobubu，CM5） | 自研 CM5 模式 + fold/overlay widget；表格用行级 token（`HyperMD-table-row`、`hmd-table-column-*`）+ 键位（Tab/Enter 单元格跳转、Enter 建表） | **Obsidian LP 的 token 体系与它同源**：Obsidian bundle 内的 CM5 模式注册 `CodeMirror.defineMIME("text/x-hypermd","hypermd")`，且 obsidian 主题 CSS 里仍有 `.HyperMD-table-row`、`.hmd-table-column-left/center/right` 一类规则。区别：Obsidian 在 CM6 上重做了 widget（真实 `<table>` 可点击编辑），HyperMD 是 CM5 文本层美化 + 键位 |
| [Advanced Tables](https://github.com/tgrosinger/advanced-tables-obsidian) | Obsidian 插件；**格式化/重排源码文本**（对齐管道、Tab 跳格、排序），不替换成 HTML widget | 与 Obsidian **内建**表格编辑的「源码重排」部分思路相同（Obsidian 内建也做列宽重排），但它不渲染 `<table>` |
| [ckant/codemirror-markdown-tables](https://github.com/ckant/codemirror-markdown-tables) | CM6 扩展，把 markdown 表格变成**可交互组件** | 与 Obsidian LP 路线最接近的公开实现（WidgetType + 编辑写回），可作为复刻参考 |
| [@markwhen/codemirror-tables](https://www.npmjs.com/package/@markwhen/codemirror-tables) | CM6 表格编辑扩展 | 同上，另一条实现 |
| [obsidian-typings](https://github.com/obsidian-typings/obsidian-typings) | 社区维护的 Obsidian 内部 API 类型（含 `@codemirror/language` 的 Obsidian 私有扩展） | 逆向分析类权威参考；`lineClassNodeProp` 页面明确标注「only in Obsidian」 |

### 5.3 已知的逆向分析/结论来源

- **本报告的反编译结论**（最直接）：asar 解包 + 偏移取证（§开头）。
- **obsidian-typings**（社区）：证实 Obsidian 对 `@codemirror/language` 有非上游扩展（`lineClassNodeProp` / `tokenClassNodeProp` / `ignoreSpellcheckToken`）。
- **Obsidian 官方文档**：`editorLivePreviewField`、`registerMarkdownPostProcessor`、`sanitizeHTMLToDom`、CSS variables（Table）等公开面。
- **未找到**：官方对「使用 remark / mdast-util-to-hast」的公开说明；也没有找到专门针对「Obsidian 表格渲染」的成篇逆向文章（论坛/博客多为 CSS 片段与行为讨论）。
- **[未验证]** 搜索结果中出现的 HITCON 2023 议题《What You See IS NOT What You Get: Pwning Electron-based Markdown Note-taking Apps》可能涉及 Electron markdown 应用（含 Obsidian）的解析差异，但本报告未获取/核对其正文，故不作为依据。

---

## 6. 对复刻者的实操建议与坑

### 6.1 最小可靠路径（不用 CodeMirror，只要 md 表格 → HTML）

**推荐 A（生态一致）**：直接复刻 Obsidian 的栈，行为最容易对齐：

```
markdown → remark-parse(+gfm) → mdast → mdast-util-to-hast → hast → hast-util-to-html → HTML
```
即 `remark-parse`（或现代 `remark`/`micromark` 的 GFM 扩展）+ `mdast-util-to-hast` + `hast-util-to-html`；若在 Obsidian 插件里，直接用 `MarkdownRenderer.render(app, md, el, sourcePath, component)`，或 `sanitizeHTMLToDom(html)`——后者正是 Obsidian 公开导出的那个 `RF`。

**推荐 B（零依赖、最小算法）**，按 Obsidian/GFM 行为逐条实现：

1. 找到第一行含未转义 `|` 的行 → 候选表头；
2. 下一行必须匹配分隔行：`^\|?(\s*:?-+:?\s*\|)+(\s*:?-+:?\s*)?$`（Obsidian 版本更宽松：逐字符扫描，遇 `:`/`-` 累积 `left/center/right`，允许 `|` 分隔；至少 1 列）；
3. 解析分隔行 → `align[i] ∈ {null,left,center,right}`；
4. 收集后续行：只要仍含 `|` 就继续（GFM 更宽松：也可用「列数一致」终止）；
5. 每行按**未转义** `|` 切分：扫描时维护 `esc` 标志（`\` 转义下一字符），切掉首尾空管道与单元格首尾空白（记录 `padStart/padEnd` 以便将来回写源码）；
6. 每个单元格内容交给**你的行内渲染器**（同一套 inline parser，保证 `**b**`、`` `c` ``、`[t](u)`、`==mark==`、`[[wiki]]` 与正文一致）；
7. 输出 `<table><thead><tr><th align=…>…</th></tr></thead><tbody><tr><td align=…>…</td></tr></tbody></table>`，`align` 只在对齐非 null 时输出；
8. 包一层滚动容器或给父元素 `overflow-x:auto` + `max-width` + `ellipsis`（照抄 §3.4 的 CSS 变量思路）。

### 6.2 坑清单（按踩坑概率排序）

| # | 坑 | 说明/对策 |
|---|---|---|
| ① | **单元格数不一致** | 表头 3 列、分隔行 2 列、某行 4 列都真实存在。Obsidian 的 remark 实现**不校验列数一致**（只在 LP 里标记 `isMalformed` 并补齐 DOM），而 lezer-markdown **要求一致**。复刻时必须先决定策略（补齐/截断/放弃该表），否则会出现越界或错列 |
| ② | **转义 `\|`** | 切分前必须做 `\` 逃逸扫描；不要用简单的 `line.split("|")`。`[[a\|b]]` 是 Obsidian 场景下的高频写法（官方 sandbox 明说） |
| ③ | **行内代码/公式里的管道** | `` `a|b` ``、`$x|y$` 里的 `|` 在 GFM/Obsidian 里**仍需转义**才不分割（Obsidian 与 lezer 的实现都是纯字符级扫描，不看行内上下文）。若要更「聪明」，需要先扫描反引号/`$` 配对——但那会与 Obsidian 行为不一致 |
| ④ | **首尾管道与空白** | 首行有无 `|` 必须全表一致（Obsidian 实现会因此判定「不是表格」）；单元格内容要 `trim`，但**必须记住原始 padding**，否则源码态与渲染态互相覆盖时会抖动 |
| ⑤ | **空单元格 / 空表头** | 空单元格在 LP 里被塞 `<br>` 撑高；空表头行为在社区有专门 issue（[forum #111814](https://forum.obsidian.md/t/empty-table-headers-are-rendered-as-regular-empty-rows/111814)，标题即现象，正文未核对） |
| ⑥ | **中文/全角宽度与列宽重排** | Obsidian 的列宽按 `text.length`（UTF-16 码元）算，**不按显示宽度**；中英混排时源码态对齐会视觉错位（[推断/高置信]，来自 `l[d]=Math.max(l[d], m.length+2)` 与 `getTextWithPadding` 只补空格）。若你自己做「自动对齐源码」，建议按 East-Asian Width 计算显示宽度，但要注意与 Obsidian 输出不完全一致 |
| ⑦ | **宽表格** | 两个方案都可行：给表格套 `.table-wrapper{overflow-x:auto}`（LP 路线），或给「唯一子元素」的父节点设 `overflow-x:auto`（RV 路线）。别忘了配合 `max-width/ellipsis`，否则要么撑爆布局要么静默截断 |
| ⑧ | **表格前后需空行** | 表格紧跟段落时不会识别为表格；渲染后若给表格加 `margin-block-start` 之类的间距，视觉上会像多了空行 |
| ⑨ | **HTML 消毒** | 如果复刻 Obsidian，注意 `<style>` 会被丢掉、`<iframe>` 被放行（`FORBID_TAGS:["style"], ADD_TAGS:["iframe"]`）；自己实现时不要盲目照抄这条白名单 |
| ⑩ | **往返转换（HTML→MD）** | 需要时照抄 Turndown 规则：管道转义 `\|`、换行转 `<br>`、对齐标记用 `:--` / `--:` / `:-:`、`colspan` 用重复 `|` 补齐 |

### 6.3 若用 CodeMirror 6 复刻（骨架）

```
1) 语言层：用 @lezer/markdown + GFM（markdownLanguage）拿到 Table/TableHeader/TableRow/TableCell 节点——
   注意这与 Obsidian 不同（Obsidian 用 StreamLanguage+CM5 hypermd），但对外表现可对齐；
2) 装饰层：ViewPlugin，遍历 visibleRanges 内的 Table 节点 →
   if (!selectionIntersects(from,to)) deco.push(Decoration.replace({widget, block:true, side:1}).range(from,to))
   （要处理文档末尾的 inclusiveEnd、block:true 的边界必须在行首/行尾）；
3) WidgetType：toDOM() 返回 div.cm-embed-block.cm-table-widget.markdown-rendered，
   eq() 比较源码字符串避免重复渲染，ignoreEvent() 按需放行点击；
4) 交互：点击单元格 → 在单元格内挂一个内嵌 EditorView（只有单元格文本），
   输入后把变更 map 回主文档的绝对偏移（参考 ej.getAbsoluteOffsets 的思路：start/end + padStart/padEnd）；
5) 结构操作（增删行列/对齐/排序）统一走「重建整表文本 → 单个 dispatch({changes:[{from,to,insert}]})」，
   并用 annotation 标记该事务来自 widget，避免回环重渲染（Obsidian 用 tj.of(!0) 这类 annotation）；
6) 不要指望 atomicRanges：Obsidian 的做法是「选区相交就把 widget 撤掉」，
   若你想保留「光标跳过整块」的手感，可额外注册 EditorView.atomicRanges，但那与 Obsidian 行为不同。
```

---

## 7. 存疑与未验证项

1. **HyperMD 与 Obsidian 的关系**：证据是「同一批 token 名 + `text/x-hypermd` MIME + CSS 中的 `.HyperMD-*`/`.hmd-*`」，据此判断 Obsidian 的 CM5 markdown 模式源自 HyperMD（fork 或衍生）。**未找到 Obsidian 官方或作者本人的确认**，标 **[推断/高置信]**。
2. **`nO` 字段身份**：LP 装饰器中 `g=d.field(nO)` 与 `OL(g,y,e,t)` 参与「搜索命中则不折叠」判断，未能确定其字段定义处（疑似搜索高亮相关 StateField）。**[未验证]**
3. **行内代码 span 内的 `|`**：实现层面是纯字符级扫描，但**未实测** Obsidian 真实行为（是否在 `` ` `` 内也强制要求转义）。**[未验证]**
4. **中文字符宽度对齐**：由代码推断 LP 源码重排会按码元数错位，**未真机实测截图验证**。**[推断]**
5. **列表内的表格**：社区有长期 issue（[forum #60605 "Live Preview: Support Tables in list items"](https://forum.obsidian.md/t/live-preview-support-tables-in-list-items/60605)，仅见标题），本报告未验证当前 1.13.7 的具体行为。**[未验证]**
6. **`mdast-util-to-hast` / `hast-util-to-html` 的确切版本号**：只能由代码特征（`hName/hProperties/hChildren` patch、`allowDangerousHtml` 弃用警告、footnote footer 形状）判断为 remark 12/13 时代（v10/v11 量级），**未能读到 package.json 版本**（asar 内 `package.json` 仅 260 B，为主进程信息）。**[推断]**
7. **表格相关的内置 post-processor 是否还有其它**：只逐字确认了 overflowX/dir 这一个；`app.js` 中 `AW.registerPostProcessor` 还有多个调用（callout、标题方向等），未逐一核对是否涉及表格。**[部分验证]**
8. **Catalyst 版本（1.14.x）差异**：本机为 1.13.7；obsidian-typings 同时列出 Catalyst 1.14.2，未核对其表格实现是否有变动。**[未验证]**
9. **移动端**：CSS 有 `.is-mobile` 分支与 `rd.isAndroidApp/isIosApp` 特殊逻辑（触摸拖选、滚动选择），未展开分析。**[未验证]**

---

## 8. 参考来源

**第一手（本机反编译，Obsidian 1.13.7 / Windows）**
- 应用包：`C:\Users\zghyu\AppData\Roaming\obsidian\obsidian-1.13.7.asar`（`app.js` 3,876,459 B；`app.css` 637,090 B；`lib/codemirror/*`）
- 内置 sandbox 库中 Obsidian 自带的表格说明：asar 内 `sandbox/Formatting/Table.md`（镜像：<https://raw.githubusercontent.com/cxplonka/obsidian-sandbox-mkdocs/main/docs/Formatting/Table.md>）

**官方文档 / 官方仓库**
- 视图与编辑模式（Reading view / Live Preview / Source mode）：<https://obsidian.md/help/edit-and-read>
- 开发者文档 · Decorations（Widget/Replace/ViewPlugin/StateField）：<https://docs.obsidian.md/Plugins/Editor/Decorations>（源码：<https://github.com/obsidianmd/obsidian-developer-docs/blob/main/en/Plugins/Editor/Decorations.md>）
- CSS 变量 · Table（36 个表格变量）：<https://docs.obsidian.md/Reference/CSS+variables/Editor/Table>
- `editorLivePreviewField`：<https://docs.obsidian.md/Reference/TypeScript+API/editorLivePreviewField>
- `registerMarkdownPostProcessor`：<https://docs.obsidian.md/Reference/TypeScript+API/Plugin/registerMarkdownPostProcessor>
- `sanitizeHTMLToDom`：<https://docs.obsidian.md/Reference/TypeScript+API/sanitizeHTMLToDom>
- Obsidian API 类型定义（本地：`docs\Obsidian-API\obsidian.d.ts`）：<https://github.com/obsidianmd/obsidian-api>

**上游源码**
- `@lezer/markdown` GFM Table 扩展（节点名、`delimiterLine`、`parseRow` 转义）：<https://github.com/lezer-parser/markdown/blob/main/src/extension.ts>
- `@codemirror/lang-markdown`（`commonmarkLanguage` / `markdownLanguage` / Table fold）：<https://github.com/codemirror/lang-markdown/blob/main/src/markdown.ts>
- CodeMirror 6 参考：`Decoration.replace` / `WidgetType` / ViewPlugin — <https://codemirror.net/docs/ref/#view.Decoration%5Ereplace>、<https://codemirror.net/docs/ref/#view.WidgetType>
- `mdast-util-to-hast`：<https://github.com/syntax-tree/mdast-util-to-hast>；`hast-util-to-html`：<https://github.com/syntax-tree/hast-util-to-html>
- remark-parse：<https://github.com/remarkjs/remark/tree/main/packages/remark-parse>；Turndown：<https://github.com/mixmark-io/turndown>；DOMPurify：<https://github.com/cure53/DOMPurify>
- GFM 表格规范：<https://github.github.com/gfm/#tables-extension->

**社区 / 第三方**
- obsidian-typings · `lineClassNodeProp`（"only exists … in Obsidian"）：<https://obsidian-typings.github.io/obsidian-typings/catalyst/api/@codemirror__language/augmentations/vars/lineClassNodeProp/>；仓库：<https://github.com/obsidian-typings/obsidian-typings>
- HyperMD（CM5，`HyperMD-table-row` 等 token 体系来源）：<https://github.com/laobubu/HyperMD>
- Advanced Tables（Obsidian 插件，源码重排路线）：<https://github.com/tgrosinger/advanced-tables-obsidian>
- ckant/codemirror-markdown-tables（CM6 交互式表格组件）：<https://github.com/ckant/codemirror-markdown-tables>
- @markwhen/codemirror-tables：<https://www.npmjs.com/package/@markwhen/codemirror-tables>
- codemirror/dev#1529（替换长文本）：<https://github.com/codemirror/dev/issues/1529>
- 论坛（**仅搜索命中，未逐篇核对正文**，引用其标题所示现象）：
  - Live Preview: Support Tables in list items — <https://forum.obsidian.md/t/live-preview-support-tables-in-list-items/60605>
  - Empty table headers are rendered as regular empty rows — <https://forum.obsidian.md/t/empty-table-headers-are-rendered-as-regular-empty-rows/111814>
  - Writing a table entry longer than the line wrap width breaks the "end" keyboard button — <https://forum.obsidian.md/t/writing-a-table-entry-longer-than-the-line-wrap-width-breaks-the-end-keyboard-button/5518>
  - Hiding the blank line above tables — <https://forum.obsidian.md/t/hiding-the-blank-line-above-tables/63465>
  - Max table width without rll (readable line width) — <https://forum.obsidian.md/t/max-table-width-without-rll-readable-line-width-minimal-theme/95127>
  - What is the tech stack currently? — <https://forum.obsidian.md/t/what-is-the-tech-stack-currently/833>

---

### 附：取证脚本要点（可复现）

```powershell
# 1) 读取 asar 头 16B：jsonSize = UInt32LE(offset 12)，数据区起点 = 16 + jsonSize
# 2) 解析 JSON 目录得到每个 entry 的 {size, offset}；文件偏移 = 数据区起点 + offset
# 3) 用 Latin1/UTF8 解码 app.js 后做 IndexOf 检索 + 上下文切片
#    关键偏移（1.13.7）：
#    remark-parse 表格 tokenizer ≈ 203,700；mdast-util-to-hast 表格 handler ≈ 29,440
#    WT()/GT()/VT.globalOptions ≈ 1,349,300–1,352,100；RF()/DOMPurify 配置 ≈ 1,723,500
#    Reading View 容器 ≈ 1,964,569；表格 overflowX post-processor ≈ 1,994,505
#    LP widget 根类名 ≈ 2,019,368；render()/table-wrapper ≈ 2,033,000–2,035,000
#    LP 装饰器（HyperMD-table-row 分支）≈ 2,992,550
#    CM5 hypermd 模式 + defineMIME("text/x-hypermd") ≈ 2,107,000–2,121,000
```
