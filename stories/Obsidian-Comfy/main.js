'use strict';

/**
 * Comfy 数据表 — Obsidian 插件
 *
 * 功能:
 *   1. 第一列是 ID 的 md 表格: TEXT 类型列超长内容在渲染层用省略号截断(源码不变)
 *   2. 所有列与内容严格单行展示, 超出时横向滚动
 *   3. 完整分页: 每页数量选择 / 首页 / 上一页 / 页码 / 下一页 / 尾页 / 跳转
 *   4. 表格上方搜索过滤
 *   5. ID 列点击切换增序 / 降序
 *   6. 在表格内输入 @ 自动弹窗浏览 ComfyUI output 目录(仅普通文件 + 「数字-」编号目录),
 *      选中文件后确定, 自动插入 @{目录名/文件名} 或 @{文件名}
 */

const obsidian = require('obsidian');
const fs = require('fs');
const path = require('path');

const { Plugin, PluginSettingTab, Setting, Modal, Notice, MarkdownRenderChild } = obsidian;

// ─── 常量 ────────────────────────────────────────────────────────────────

/** 图片扩展名 → 弹窗里显示静态缩略图 */
const IMAGE_EXT = new Set(['png', 'jpg', 'jpeg', 'webp', 'gif', 'bmp', 'avif', 'svg']);

/** 视频扩展名 → 弹窗里用 <video> 显示首帧 */
const VIDEO_EXT = new Set(['mp4', 'webm', 'mov', 'mkv', 'm4v', 'avi']);

/** 音频扩展名 → 弹窗里用音频图标 + 可播放 */
const AUDIO_EXT = new Set(['mp3', 'wav', 'flac', 'ogg', 'm4a', 'aac', 'opus']);

/** 编号目录判据: 数字开头后接连字符, 例如 0040-文生视频 */
const NUMBERED_DIR_RE = /^\d+-/;

/** 默认设置 */
const DEFAULT_SETTINGS = {
  /** ComfyUI output 目录绝对路径; 留空则用 vault 同级的 media/七纹刻印 猜测 */
  outputDir: 'D:\\Comfy\\media\\七纹刻印',
  /** 表格增强总开关 */
  enableTable: true,
  /** @ 弹窗总开关 */
  enableAtSuggest: true,
  /** 每页数量可选项 */
  pageSizes: [20, 50, 100, 200],
  /** 默认每页数量; 0 表示全部 */
  defaultPageSize: 20,
  /** TEXT 列最大宽度(px), 超出用省略号 */
  textColMaxWidth: 420,
  /** 其它列最大宽度(px) */
  otherColMaxWidth: 720,
  /** 缩略图取图方式: app(app://local 协议) | base64(读文件转 data URL) */
  thumbMode: 'app',
  /** 弹窗缩略图尺寸 */
  thumbWidth: 72,
  /** 记住用户手动选的每页数量 */
  lastPageSize: 20,
};

// ─── 通用小工具 ──────────────────────────────────────────────────────────

/**
 * 去掉表头里的类型标注, 只留列名。
 *
 * @param {string} header 表头原文, 例如 `主-正词(TEXT)`
 * @returns {string} 列名, 例如 `主-正词`
 */
function stripType(header) {
  return String(header || '').replace(/\([^()]*\)\s*$/, '').trim();
}

/**
 * 取出表头括号里的类型名。
 *
 * @param {string} header 表头原文, 例如 `主-正词(TEXT)`
 * @returns {string} 大写类型名; 没有标注时返回空串
 */
function colType(header) {
  const m = /\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)\s*$/.exec(String(header || ''));
  return m ? m[1].toUpperCase() : '';
}

/**
 * 提取 ID 的排序键: 取开头的数字段。
 *
 * @param {string} text 单元格文本, 例如 `00011-插入项`
 * @returns {number} 数值键; 无数字时排到最后
 */
function idKey(text) {
  const m = /^\s*(\d+)/.exec(String(text || ''));
  return m ? Number.parseInt(m[1], 10) : Number.MAX_SAFE_INTEGER;
}

/**
 * 取小写扩展名(不含点)。
 *
 * @param {string} name 文件名
 * @returns {string} 小写扩展名; 无扩展名时为空串
 */
function extOf(name) {
  const i = String(name).lastIndexOf('.');
  return i < 0 ? '' : String(name).slice(i + 1).toLowerCase();
}

/**
 * 去掉扩展名。
 *
 * @param {string} name 文件名
 * @returns {string} 不含扩展名的名字
 */
function stemOf(name) {
  const i = String(name).lastIndexOf('.');
  return i <= 0 ? String(name) : String(name).slice(0, i);
}

/**
 * 判断文件属于图片 / 视频 / 音频 / 其它。
 *
 * @param {string} name 文件名
 * @returns {'image'|'video'|'audio'|'other'} 类别
 */
function kindOf(name) {
  const e = extOf(name);
  if (IMAGE_EXT.has(e)) return 'image';
  if (VIDEO_EXT.has(e)) return 'video';
  if (AUDIO_EXT.has(e)) return 'audio';
  return 'other';
}

/**
 * 人类可读的文件大小。
 *
 * @param {number} n 字节数
 * @returns {string} 例如 `1.3 MB`
 */
function fmtSize(n) {
  if (!Number.isFinite(n)) return '';
  const u = ['B', 'KB', 'MB', 'GB'];
  let v = n;
  let i = 0;
  while (v >= 1024 && i < u.length - 1) {
    v /= 1024;
    i += 1;
  }
  return `${i === 0 ? v : v.toFixed(1)} ${u[i]}`;
}

// ─── @ 文件浏览弹窗 ──────────────────────────────────────────────────────

class ComfyFileModal extends Modal {
  /**
   * @param {import('obsidian').App} app Obsidian app
   * @param {object} opts 选项
   * @param {string} opts.root 根目录绝对路径
   * @param {string} opts.thumbMode `app` 或 `base64`
   * @param {number} opts.thumbWidth 缩略图宽度
   * @param {(text: string) => void} opts.onPick 确定回调, 收到 `@{...}`
   */
  constructor(app, opts) {
    super(app);
    this.root = opts.root;
    this.thumbMode = opts.thumbMode;
    this.thumbWidth = opts.thumbWidth;
    this.onPick = opts.onPick;

    /** 当前所在子目录名; 空串表示根目录 */
    this.sub = '';
    /** 当前高亮的条目 */
    this.picked = null;
    /** 过滤词 */
    this.filter = '';
  }

  /**
   * 打开时构建界面。
   *
   * @returns {void}
   */
  onOpen() {
    this.modalEl.addClass('oc-modal');
    this.titleEl.setText('插入 output 资源引用');
    this.render();
  }

  /**
   * 关闭时清空。
   *
   * @returns {void}
   */
  onClose() {
    this.contentEl.empty();
  }

  /**
   * 列出当前目录下的条目: 编号子目录 + 普通文件, 均跳过点开头的项。
   *
   * @returns {Array<object>} 条目数组
   */
  listEntries() {
    const dir = this.sub ? path.join(this.root, this.sub) : this.root;
    let raw = [];
    try {
      raw = fs.readdirSync(dir, { withFileTypes: true });
    } catch {
      return [];
    }

    const dirs = [];
    const files = [];
    for (const e of raw) {
      if (e.name.startsWith('.')) continue;
      const full = path.join(dir, e.name);
      if (e.isDirectory()) {
        // 只显示「数字-」编号目录(与 ComfyUI 插件侧判据一致)
        if (!this.sub && NUMBERED_DIR_RE.test(e.name)) dirs.push({ name: e.name, isDir: true });
        continue;
      }
      if (!e.isFile()) continue;
      let size = 0;
      try {
        size = fs.statSync(full).size;
      } catch {
        size = 0;
      }
      files.push({ name: e.name, isDir: false, size });
    }

    dirs.sort((a, b) => a.name.localeCompare(b.name, 'zh'));
    files.sort((a, b) => a.name.localeCompare(b.name, 'zh'));
    return dirs.concat(files);
  }

  /**
   * 过滤条目。
   *
   * @param {Array<object>} entries 全部条目
   * @returns {Array<object>} 命中的条目
   */
  filtered(entries) {
    const q = this.filter.trim().toLowerCase();
    if (!q) return entries;
    return entries.filter((x) => x.name.toLowerCase().includes(q));
  }

  /**
   * 生成 file:// 或 app:// 可用的资源地址。
   *
   * @param {string} abs 绝对路径
   * @returns {string} URL
   */
  resourceUrl(abs) {
    const norm = abs.replace(/\\/g, '/');
    if (this.thumbMode === 'base64') {
      try {
        const buf = fs.readFileSync(abs);
        const ext = extOf(abs);
        const mime = ext === 'png' ? 'image/png'
          : ext === 'webp' ? 'image/webp'
            : ext === 'gif' ? 'image/gif'
              : ext === 'svg' ? 'image/svg+xml'
                : 'image/jpeg';
        return `data:${mime};base64,${buf.toString('base64')}`;
      } catch {
        return '';
      }
    }
    return `app://local/${encodeURI(norm)}`;
  }

  /**
   * 渲染整个弹窗内容(重建 DOM)。
   *
   * @returns {void}
   */
  render() {
    const { contentEl } = this;
    contentEl.empty();

    // 面包屑
    const crumbs = contentEl.createDiv({ cls: 'oc-crumbs' });
    crumbs.createSpan({ text: 'output' });
    if (this.sub) {
      crumbs.createSpan({ text: ' / ' });
      crumbs.createSpan({ text: this.sub });
      const back = crumbs.createEl('a', { text: '  ← 返回根目录' });
      back.onclick = () => {
        this.sub = '';
        this.picked = null;
        this.filter = '';
        this.render();
      };
    }

    // 过滤框
    const filterInput = contentEl.createEl('input', { cls: 'oc-filter', type: 'text' });
    filterInput.placeholder = '过滤文件名…';
    filterInput.value = this.filter;
    filterInput.oninput = () => {
      this.filter = filterInput.value;
      this.renderList();
    };
    window.setTimeout(() => filterInput.focus(), 0);

    // 列表容器
    this.listEl = contentEl.createDiv({ cls: 'oc-list' });
    this.renderList();

    // 结果预览
    this.resultEl = contentEl.createDiv({ cls: 'oc-result' });
    this.updateResult();

    // 按钮行
    const btns = contentEl.createDiv({ cls: 'modal-button-container' });
    const ok = btns.createEl('button', { text: '确定', cls: 'mod-cta' });
    ok.onclick = () => this.confirm();
    const cancel = btns.createEl('button', { text: '取消' });
    cancel.onclick = () => this.close();

    contentEl.createDiv({
      cls: 'oc-hint',
      text: '只列出普通文件与「数字-」编号目录; 目录内选中文件后可再返回上一级。',
    });
  }

  /**
   * 渲染列表区域。
   *
   * @returns {void}
   */
  renderList() {
    if (!this.listEl) return;
    this.listEl.empty();

    if (!this.root) {
      this.listEl.createDiv({ cls: 'oc-empty', text: '未配置 output 目录, 请到插件设置里填写。' });
      return;
    }

    const entries = this.filtered(this.listEntries());
    if (entries.length === 0) {
      this.listEl.createDiv({ cls: 'oc-empty', text: '没有匹配的条目。' });
      return;
    }

    for (const e of entries) {
      const row = this.listEl.createDiv({ cls: 'oc-row' });
      if (this.picked && this.picked.name === e.name && this.picked.isDir === e.isDir) {
        row.addClass('is-selected');
      }

      this.buildThumb(row, e);

      const meta = row.createDiv({ cls: 'oc-meta' });
      meta.createDiv({ cls: 'oc-name', text: e.name });
      if (e.isDir) {
        meta.createDiv({ cls: 'oc-sub', text: '目录 · 点击进入' });
      } else {
        const k = kindOf(e.name);
        const label = k === 'image' ? '图片' : k === 'video' ? '视频' : k === 'audio' ? '音频' : '文件';
        meta.createDiv({ cls: 'oc-sub', text: `${label} · ${fmtSize(e.size)}` });
      }

      if (e.isDir) {
        row.createSpan({ cls: 'oc-kind', text: 'DIR' });
      } else {
        row.createSpan({ cls: 'oc-kind', text: extOf(e.name).toUpperCase() || 'FILE' });
      }

      row.onclick = () => {
        if (e.isDir) {
          this.sub = e.name;
          this.picked = null;
          this.filter = '';
          this.render();
          return;
        }
        this.picked = e;
        this.renderList();
        this.updateResult();
      };

      // 双击直接确定
      row.ondblclick = () => {
        if (e.isDir) return;
        this.picked = e;
        this.confirm();
      };
    }
  }

  /**
   * 构建左侧缩略图: 图片走 <img>, 视频走 <video>, 音频与其它走图标。
   *
   * @param {HTMLElement} row 行元素
   * @param {object} e 条目
   * @returns {void}
   */
  buildThumb(row, e) {
    const box = row.createDiv({ cls: 'oc-thumb' });
    box.style.width = `${this.thumbWidth}px`;

    if (e.isDir) {
      box.createSpan({ cls: 'oc-icon', text: '📁' });
      return;
    }

    const abs = path.join(this.sub ? path.join(this.root, this.sub) : this.root, e.name);
    const k = kindOf(e.name);

    if (k === 'image') {
      const url = this.resourceUrl(abs);
      if (!url) {
        box.createSpan({ cls: 'oc-icon', text: '🖼' });
        return;
      }
      const img = box.createEl('img');
      img.src = url;
      img.loading = 'lazy';
      img.onerror = () => {
        box.empty();
        box.createSpan({ cls: 'oc-icon', text: '🖼' });
      };
      return;
    }

    if (k === 'video') {
      const v = box.createEl('video');
      v.src = `app://local/${encodeURI(abs.replace(/\\/g, '/'))}`;
      v.muted = true;
      v.preload = 'metadata';
      v.ondblclick = (ev) => ev.stopPropagation();
      v.onerror = () => {
        box.empty();
        box.createSpan({ cls: 'oc-icon', text: '🎬' });
      };
      return;
    }

    if (k === 'audio') {
      box.createSpan({ cls: 'oc-icon', text: '🎵' });
      return;
    }

    box.createSpan({ cls: 'oc-icon', text: '📄' });
  }

  /**
   * 计算当前选中项对应的引用文本。
   *
   * @returns {string} 例如 `@{0040-文生视频/video}`; 未选中时为空串
   */
  currentRef() {
    if (!this.picked) return '';
    const stem = stemOf(this.picked.name);
    return this.sub ? `@{${this.sub}/${stem}}` : `@{${stem}}`;
  }

  /**
   * 刷新底部的结果预览。
   *
   * @returns {void}
   */
  updateResult() {
    if (!this.resultEl) return;
    const ref = this.currentRef();
    this.resultEl.setText(ref ? `将插入: ${ref}` : '请选择一个文件');
  }

  /**
   * 确定: 回调插入文本并关闭。
   *
   * @returns {void}
   */
  confirm() {
    const ref = this.currentRef();
    if (!ref) {
      new Notice('请先选择一个文件');
      return;
    }
    this.onPick(ref);
    this.close();
  }
}

// ─── 表格增强 ────────────────────────────────────────────────────────────

class ComfyTableChild extends MarkdownRenderChild {
  /**
   * @param {HTMLElement} containerEl 表格所在容器
   * @param {HTMLElement} table 原始 table 元素
   * @param {object} plugin 插件实例
   */
  constructor(containerEl, table, plugin) {
    super(containerEl);
    this.table = table;
    this.plugin = plugin;

    /** 表头列名(已去类型标注) */
    this.headers = [];
    /** 各列类型(大写) */
    this.types = [];
    /** tbody 行快照 */
    this.rows = [];

    this.query = '';
    this.sortDir = 'asc';
    this.page = 1;
    this.pageSize = plugin.settings.lastPageSize || plugin.settings.defaultPageSize;
  }

  /**
   * 挂载: 解析表格 → 重排 DOM → 绑定交互。
   *
   * @returns {void}
   */
  onload() {
    const headRow = this.table.querySelector('thead tr') || this.table.querySelector('tr');
    if (!headRow) return;

    this.headers = Array.from(headRow.children).map((th) => stripType(th.textContent || ''));
    this.types = Array.from(headRow.children).map((th) => colType(th.textContent || ''));
    if (this.headers.length < 2) return;

    // 第一列必须是 ID 才接管
    if (this.headers[0].toLowerCase() !== 'id') return;

    const body = this.table.querySelector('tbody') || this.table;
    this.rows = Array.from(body.querySelectorAll('tr')).filter((tr) => tr !== headRow);
    if (this.rows.length === 0) return;

    this.applyCellClasses(headRow);
    this.buildShell(headRow);
    this.apply();
  }

  /**
   * 给表头与单元格打类名: ID 列可排序, TEXT 列走省略号截断。
   *
   * @param {HTMLElement} headRow 表头行
   * @returns {void}
   */
  applyCellClasses(headRow) {
    Array.from(headRow.children).forEach((th, i) => {
      if (i === 0) th.addClass('oc-th-id');
    });
    for (const tr of this.rows) {
      Array.from(tr.children).forEach((td, i) => {
        if (i === 0) {
          td.addClass('oc-td-id');
          return;
        }
        const isText = this.types[i] === 'TEXT';
        td.addClass(isText ? 'oc-cell-text' : 'oc-cell-other');
        this.wrapClip(td, isText);
      });
    }
  }

  /**
   * 在单元格内容外包一层裁剪容器。
   *
   * td 自身的 max-width 在 table-layout:auto 下不生效, 只有包一层块级元素
   * 才能让 max-width + text-overflow:ellipsis 可靠截断。
   *
   * @param {HTMLElement} td 单元格
   * @param {boolean} isText 是否为 TEXT 类型列
   * @returns {void}
   */
  wrapClip(td, isText) {
    // 空单元格不必包装
    if (!td.firstChild) return;
    const box = document.createElement('div');
    box.addClass('oc-clip');
    box.addClass(isText ? 'oc-clip-text' : 'oc-clip-other');
    while (td.firstChild) box.appendChild(td.firstChild);
    td.appendChild(box);
  }

  /**
   * 用 工具条 + 滚动容器 + 分页条 三层结构包住原表格。
   *
   * @param {HTMLElement} headRow 表头行
   * @returns {void}
   */
  buildShell(headRow) {
    const block = document.createElement('div');
    block.addClass('oc-table-block');

    const toolbar = document.createElement('div');
    toolbar.addClass('oc-toolbar');

    // 工具栏: 搜索框 + 排序按钮 + 计数
    const search = document.createElement('input');
    search.addClass('oc-search');
    search.type = 'text';
    search.placeholder = '搜索(ID 或任意字段)…';
    search.value = this.query;
    search.oninput = () => {
      this.query = search.value;
      this.page = 1;
      this.apply();
    };
    toolbar.appendChild(search);

    const sortBtn = document.createElement('button');
    sortBtn.addClass('oc-sort-btn');
    sortBtn.onclick = () => this.toggleSort();
    toolbar.appendChild(sortBtn);
    this.sortBtn = sortBtn;

    this.countEl = document.createElement('span');
    this.countEl.addClass('oc-count');
    toolbar.appendChild(this.countEl);

    const scroll = document.createElement('div');
    scroll.addClass('oc-table-scroll');

    const pager = document.createElement('div');
    pager.addClass('oc-pager');
    this.pagerEl = pager;

    const table = this.table;
    table.parentElement.insertBefore(block, table);
    scroll.appendChild(table);
    block.appendChild(toolbar);
    block.appendChild(scroll);
    block.appendChild(pager);

    // ID 列点击排序: 用事件委托, 避免 Obsidian 重建表格后句柄失效
    scroll.addEventListener('click', (ev) => {
      const t = ev.target;
      if (!(t instanceof Element)) return;
      if (!t.closest('th.oc-th-id')) return;
      this.toggleSort();
    });

    sortBtn.addEventListener('click', () => this.toggleSort());

    // 支持横向滚动: 阻止滚轮冒泡到画布
    scroll.addEventListener('wheel', (ev) => {
      if (ev.deltaX !== 0) ev.stopPropagation();
    }, { passive: true });
  }

  /**
   * 切换 ID 列的升降序。
   *
   * @returns {void}
   */
  toggleSort() {
    this.sortDir = this.sortDir === 'asc' ? 'desc' : 'asc';
    this.page = 1;
    this.apply();
  }

  /**
   * 按当前查询 / 排序 / 分页重算可见行并刷新 UI。
   *
   * @returns {void}
   */
  apply() {
    const q = this.query.trim().toLowerCase();

    // 1) 过滤
    let visible = this.rows.filter((tr) => {
      if (!q) return true;
      return (tr.textContent || '').toLowerCase().includes(q);
    });

    // 2) 排序(仅按 ID 列数字键)
    visible = visible.slice().sort((a, b) => {
      const ka = idKey(a.children[0] ? a.children[0].textContent : '');
      const kb = idKey(b.children[0] ? b.children[0].textContent : '');
      return this.sortDir === 'asc' ? ka - kb : kb - ka;
    });

    // 3) 重排 DOM 顺序: 可见行按排序结果排前, 被过滤掉的行排在后面(它们 display:none)
    const body = this.rows[0].parentElement;
    for (const tr of visible) body.appendChild(tr);
    for (const tr of this.rows) {
      if (!visible.includes(tr)) body.appendChild(tr);
    }

    // 4) 分页切片
    const size = this.pageSize > 0 ? this.pageSize : visible.length || 1;
    const total = visible.length;
    const pages = Math.max(1, Math.ceil(total / size));
    if (this.page > pages) this.page = pages;
    if (this.page < 1) this.page = 1;
    const start = (this.page - 1) * size;
    const slice = visible.slice(start, start + size);

    // 5) 显隐
    const shown = new Set(slice);
    for (const tr of this.rows) {
      tr.style.display = shown.has(tr) ? '' : 'none';
    }

    // 6) 刷新计数与排序标记
    if (this.countEl) {
      const mark = this.sortDir === 'asc' ? '↑' : '↓';
      this.countEl.setText(`${total} / ${this.rows.length} 行 · ID ${mark}`);
    }
    if (this.sortBtn) {
      this.sortBtn.setText(this.sortDir === 'asc' ? 'ID ↑' : 'ID ↓');
      this.sortBtn.setAttr('title', '点击切换 ID 增序 / 降序');
    }

    this.renderPager(pages, total);
  }

  /**
   * 渲染分页条: 每页数量、首页、上一页、页码、下一页、尾页、跳转。
   *
   * @param {number} pages 总页数
   * @param {number} total 总行数(过滤后)
   * @returns {void}
   */
  renderPager(pages, total) {
    if (!this.pagerEl) return;
    this.pagerEl.empty();

    // 每页数量
    this.pagerEl.createSpan({ text: '每页' });
    const sel = this.pagerEl.createEl('select');
    const sizes = (this.plugin.settings.pageSizes || []).slice();
    sizes.push(0); // 0 = 全部
    for (const s of sizes) {
      const opt = sel.createEl('option', { text: s === 0 ? '全部' : String(s) });
      opt.value = String(s);
      if (s === this.pageSize) opt.selected = true;
    }
    sel.onchange = () => {
      this.pageSize = Number.parseInt(sel.value, 10) || 0;
      this.page = 1;
      this.plugin.settings.lastPageSize = this.pageSize;
      this.plugin.saveSettings();
      this.apply();
    };
    this.pagerEl.createSpan({ text: '条' });

    // 导航按钮
    const mk = (label, target, disabled) => {
      const b = this.pagerEl.createEl('button', { text: label });
      b.disabled = Boolean(disabled);
      b.onclick = () => {
        this.page = target;
        this.apply();
      };
      return b;
    };
    mk('首页', 1, this.page <= 1);
    mk('上一页', this.page - 1, this.page <= 1);

    // 页码(最多 7 个, 两端加省略)
    const nums = pageWindow(this.page, pages, 7);
    for (const n of nums) {
      if (n === '…') {
        this.pagerEl.createSpan({ cls: 'oc-ellipsis', text: '…' });
        continue;
      }
      const b = this.pagerEl.createEl('button', { text: String(n) });
      if (n === this.page) b.addClass('oc-page-active');
      b.onclick = () => {
        this.page = n;
        this.apply();
      };
    }

    mk('下一页', this.page + 1, this.page >= pages);
    mk('尾页', pages, this.page >= pages);

    // 跳转
    this.pagerEl.createSpan({ text: '跳至' });
    const jump = this.pagerEl.createEl('input', { cls: 'oc-jump', type: 'text' });
    jump.value = String(this.page);
    jump.onkeydown = (ev) => {
      if (ev.key !== 'Enter') return;
      const n = Number.parseInt(jump.value, 10);
      if (!Number.isFinite(n)) return;
      this.page = Math.min(Math.max(n, 1), pages);
      this.apply();
    };
    this.pagerEl.createSpan({ text: `/${pages} 页 · 共 ${total} 行` });
  }
}

/**
 * 计算要显示的页码窗口。
 *
 * @param {number} page 当前页
 * @param {number} pages 总页数
 * @param {number} width 最多显示几个
 * @returns {Array<number|'…'>} 页码与省略号序列
 */
function pageWindow(page, pages, width) {
  if (pages <= width) return Array.from({ length: pages }, (_, i) => i + 1);
  const half = Math.floor(width / 2);
  let start = Math.max(1, page - half);
  let end = start + width - 1;
  if (end > pages) {
    end = pages;
    start = end - width + 1;
  }
  const out = [];
  if (start > 1) {
    out.push(1);
    if (start > 2) out.push('…');
  }
  for (let i = start; i <= end; i += 1) out.push(i);
  if (end < pages) {
    if (end < pages - 1) out.push('…');
    out.push(pages);
  }
  return out;
}

// ─── 设置页 ──────────────────────────────────────────────────────────────

class ComfySettingTab extends PluginSettingTab {
  /**
   * @param {import('obsidian').App} app Obsidian app
   * @param {object} plugin 插件实例
   */
  constructor(app, plugin) {
    super(app, plugin);
    this.plugin = plugin;
  }

  /**
   * 渲染设置界面。
   *
   * @returns {void}
   */
  display() {
    const { containerEl } = this;
    containerEl.empty();

    new Setting(containerEl)
      .setName('output 目录')
      .setDesc('ComfyUI 的 output 目录绝对路径, @ 弹窗浏览的就是这里。')
      .addText((t) => t
        .setValue(this.plugin.settings.outputDir)
        .onChange(async (v) => {
          this.plugin.settings.outputDir = v.trim();
          await this.plugin.saveSettings();
        }));

    new Setting(containerEl)
      .setName('启用表格增强')
      .setDesc('对第一列是 ID 的 md 表格启用单行渲染、分页、搜索与排序。')
      .addToggle((t) => t
        .setValue(this.plugin.settings.enableTable)
        .onChange(async (v) => {
          this.plugin.settings.enableTable = v;
          await this.plugin.saveSettings();
        }));

    new Setting(containerEl)
      .setName('启用 @ 弹窗')
      .setDesc('在编辑器里输入 @ 时弹出 output 目录浏览器。')
      .addToggle((t) => t
        .setValue(this.plugin.settings.enableAtSuggest)
        .onChange(async (v) => {
          this.plugin.settings.enableAtSuggest = v;
          await this.plugin.saveSettings();
        }));

    new Setting(containerEl)
      .setName('每页数量可选项')
      .setDesc('逗号分隔, 例如 20,50,100,200')
      .addText((t) => t
        .setValue((this.plugin.settings.pageSizes || []).join(','))
        .onChange(async (v) => {
          const arr = v.split(',')
            .map((s) => Number.parseInt(s.trim(), 10))
            .filter((n) => Number.isFinite(n) && n > 0);
          if (arr.length === 0) return;
          this.plugin.settings.pageSizes = arr;
          await this.plugin.saveSettings();
        }));

    new Setting(containerEl)
      .setName('默认每页数量')
      .setDesc('0 表示全部')
      .addText((t) => t
        .setValue(String(this.plugin.settings.defaultPageSize))
        .onChange(async (v) => {
          const n = Number.parseInt(v, 10);
          if (!Number.isFinite(n) || n < 0) return;
          this.plugin.settings.defaultPageSize = n;
          await this.plugin.saveSettings();
        }));

    new Setting(containerEl)
      .setName('TEXT 列最大宽度')
      .setDesc('像素; 超出即用省略号截断(只影响渲染, 不改源码)')
      .addText((t) => t
        .setValue(String(this.plugin.settings.textColMaxWidth))
        .onChange(async (v) => {
          const n = Number.parseInt(v, 10);
          if (!Number.isFinite(n) || n < 60) return;
          this.plugin.settings.textColMaxWidth = n;
          await this.plugin.saveSettings();
          this.applyCssVars();
        }));

    new Setting(containerEl)
      .setName('其它列最大宽度')
      .setDesc('像素; 非 TEXT 列的上限')
      .addText((t) => t
        .setValue(String(this.plugin.settings.otherColMaxWidth))
        .onChange(async (v) => {
          const n = Number.parseInt(v, 10);
          if (!Number.isFinite(n) || n < 60) return;
          this.plugin.settings.otherColMaxWidth = n;
          await this.plugin.saveSettings();
          this.applyCssVars();
        }));

    new Setting(containerEl)
      .setName('缩略图取图方式')
      .setDesc('app = app://local 协议(推荐); base64 = 读文件转 data URL(兼容性最好但占内存)')
      .addDropdown((d) => d
        .addOption('app', 'app 协议')
        .addOption('base64', 'base64 内联')
        .setValue(this.plugin.settings.thumbMode)
        .onChange(async (v) => {
          this.plugin.settings.thumbMode = v;
          await this.plugin.saveSettings();
        }));

    new Setting(containerEl)
      .setName('弹窗缩略图宽度')
      .setDesc('像素')
      .addText((t) => t
        .setValue(String(this.plugin.settings.thumbWidth))
        .onChange(async (v) => {
          const n = Number.parseInt(v, 10);
          if (!Number.isFinite(n) || n < 24) return;
          this.plugin.settings.thumbWidth = n;
          await this.plugin.saveSettings();
        }));
  }

  /**
   * 把宽度设置写进 CSS 变量。
   *
   * @returns {void}
   */
  applyCssVars() {
    const root = document.body;
    root.style.setProperty('--oc-text-max', `${this.plugin.settings.textColMaxWidth}px`);
    root.style.setProperty('--oc-other-max', `${this.plugin.settings.otherColMaxWidth}px`);
  }
}

// ─── 插件主体 ────────────────────────────────────────────────────────────

class ComfyPlugin extends Plugin {
  /**
   * 加载插件。
   *
   * @returns {Promise<void>} 完成
   */
  async onload() {
    await this.loadSettings();
    this.applyCssVars();

    // 1) 表格增强
    this.registerMarkdownPostProcessor((el, ctx) => {
      if (!this.settings.enableTable) return;
      const tables = el.querySelectorAll('table');
      for (const table of Array.from(tables)) {
        const headRow = table.querySelector('thead tr') || table.querySelector('tr');
        if (!headRow) continue;
        const first = stripType(headRow.children[0] ? headRow.children[0].textContent : '');
        if (first.toLowerCase() !== 'id') continue;
        if (table.hasClass('oc-done')) continue;
        table.addClass('oc-done');
        // 交给 ctx 托管, 阅读视图重渲染时会自动卸载
        ctx.addChild(new ComfyTableChild(el, table, this));
      }
    });

    // 2) @ 弹窗: 借 EditorSuggest.onTrigger 检测, 命中即开自定义 Modal
    this.registerEditorSuggest(new AtTriggerSuggest(this.app, this));

    // 3) 命令
    this.addCommand({
      id: 'open-file-browser',
      name: '打开 output 文件浏览器',
      editorCallback: (editor) => {
        this.openBrowser((ref) => {
          editor.replaceSelection(ref);
        });
      },
    });

    // 4) 设置页
    this.addSettingTab(new ComfySettingTab(this.app, this));
  }

  /**
   * 卸载插件。
   *
   * @returns {void}
   */
  onunload() {
    // 交由 Obsidian 处理已注册资源
  }

  /**
   * 打开文件浏览器弹窗。
   *
   * @param {(ref: string) => void} onPick 选中回调
   * @returns {void}
   */
  openBrowser(onPick) {
    new ComfyFileModal(this.app, {
      root: this.settings.outputDir,
      thumbMode: this.settings.thumbMode,
      thumbWidth: this.settings.thumbWidth,
      onPick,
    }).open();
  }

  /**
   * 读取设置。
   *
   * @returns {Promise<void>} 完成
   */
  async loadSettings() {
    this.settings = Object.assign({}, DEFAULT_SETTINGS, await this.loadData());
  }

  /**
   * 保存设置。
   *
   * @returns {Promise<void>} 完成
   */
  async saveSettings() {
    await this.saveData(this.settings);
  }

  /**
   * 应用 CSS 变量。
   *
   * @returns {void}
   */
  applyCssVars() {
    document.body.style.setProperty('--oc-text-max', `${this.settings.textColMaxWidth}px`);
    document.body.style.setProperty('--oc-other-max', `${this.settings.otherColMaxWidth}px`);
  }
}

// ─── @ 触发检测 ──────────────────────────────────────────────────────────

/**
 * 用 EditorSuggest 的触发钩子检测 `@`, 命中即打开文件浏览器并返回 null(不显示候选列表)。
 */
class AtTriggerSuggest extends obsidian.EditorSuggest {
  /**
   * @param {import('obsidian').App} app Obsidian app
   * @param {ComfyPlugin} plugin 插件实例
   */
  constructor(app, plugin) {
    super(app);
    this.plugin = plugin;
    /** 防止一次按键触发多个弹窗 */
    this._armed = true;
  }

  /**
   * 判断是否该触发。
   *
   * @param {import('obsidian').EditorPosition} cursor 光标
   * @param {import('obsidian').Editor} editor 编辑器
   * @returns {null} 始终返回 null: 弹窗由这里直接打开, 不用候选列表
   */
  onTrigger(cursor, editor) {
    if (!this.plugin.settings.enableAtSuggest) return null;

    const line = editor.getLine(cursor.line) || '';
    const before = line.slice(0, cursor.ch);

    // 只在刚敲下 @ 时触发: @ 前面不是 @ 或 {, 且 @ 后没有内容
    if (!before.endsWith('@')) return null;
    const prev = before.slice(0, -1);
    if (prev.endsWith('@') || prev.endsWith('{') || prev.endsWith('\\')) return null;

    if (!this._armed) return null;
    this._armed = false;
    window.setTimeout(() => {
      this._armed = true;
    }, 300);

    // 稍后打开, 避免与编辑器当前按键处理抢占
    window.setTimeout(() => {
      this.plugin.openBrowser((ref) => {
        editor.replaceRange(ref, { line: cursor.line, ch: cursor.ch - 1 }, cursor);
      });
    }, 0);

    return null;
  }

  /**
   * 未使用: onTrigger 始终返回 null。
   *
   * @returns {Array} 空数组
   */
  getSuggestions() {
    return [];
  }

  /**
   * 未使用。
   *
   * @returns {void}
   */
  renderSuggestion() {}

  /**
   * 未使用。
   *
   * @returns {void}
   */
  selectSuggestion() {}
}

module.exports = ComfyPlugin;
