const projectData={
  opinion:{kicker:'02 / TEST_02 · AI DRIVER',title:'舆情智能分析与监测 Agent',summary:'基于 React 与 Python 的 AI 主驾工程，用自然语言调度画像、监测方案、事件研判和报告工作区。',problem:'从一句业务需求走到可执行监测，需要连续处理用户画像、检索范围、关键词、研判专家和结果交付；传统页面切换让这条链路被切碎。',contribution:'围绕业务需求组织对话入口与协同工作区，将监测范围编辑、人工确认、事件研判和报告交付串成可追踪的任务流程。',solution:'前端使用 HomeV2、DriverShell 和统一状态模型承接对话；Python Supervisor 编排 16 个 Worker，覆盖画像、意图、风险、监测、事件与报告，并将结构化结果返回对应工作区。',result:'保留真实前端组件，提供监测方案编辑→确认→示例信息→事件研判→示例报告的可交互体验。展示版使用本地样例；真实采集、模型分析与业务写入依赖后端和授权配置。',links:[{label:'体验 test_02 AI 主驾',href:'portfolio-assets/test02/index.html'}]},
  lab:{kicker:'03 / MINI PROGRAM · PRODUCT',title:'实验室设备时空地理围栏管理',summary:'让共享实验室的预约、签到、超时释放和通知真正形成闭环。',problem:'设备使用依赖群聊和纸面登记，预约后不到场、资源冲突与值日遗漏频繁发生，管理员很难实时确认现场状态。',contribution:'梳理预约状态机与异常分支，设计 300 米地理围栏签到、防作弊校验、超时释放和群消息通知流程，并参与小程序界面与素材制作。',solution:'以“预约中—待签到—使用中—已释放”为核心状态，结合微信定位 API 校验到场距离；超时自动释放设备并触发提醒，减少人工追踪。',result:'设备利用率提升 42%，资源冲突下降 95%，值日遗漏降至 0%。',links:[{label:'查看演示视频',href:'portfolio-assets/lab-demo.mp4'}]},
  feedback:{kicker:'04 / WORKFLOW · OPERATIONS',title:'学生会问卷反馈 AI 自动化',summary:'把分散的问卷原话转成一份能推动行动的运营洞察报告。',problem:'问卷回收后，人工整理分类、统计共性问题和撰写总结耗时，反馈难以被快速转成优先级和执行建议。',contribution:'设计从数据清洗到分类、聚类、摘要、洞察和建议的工作流，编写提示词并用真实样本反复校验输出质量。',solution:'问卷输入 → AI 主题分类 → 高频问题聚类 → 代表性原话提炼 → 运营洞察 → 可执行建议，最终自动生成结构化报告。',result:'将 90+ 条反馈压缩成可阅读、可讨论、可分工的洞察材料，支持学生会快速定位体验问题。',links:[{label:'查看工作流图',href:'portfolio-assets/workflow.png'},{label:'打开洞察报告',href:'portfolio-assets/运营洞察报告.pdf'}]},
  writing:{kicker:'05 / CONTENT AGENT · RESEARCH',title:'公众号文章仿写 Agent',summary:'学习结构与论证方式，而不是复制句子，建立有边界的内容生产流程。',problem:'同类舆情文章数量多、结构复杂，单纯模仿措辞容易失去原文逻辑，也可能把未经核实的事实带进成稿。',contribution:'整理 63 篇语料并建立样本索引，抽取体裁、论证骨架与适用场景；设计“选样—学习—检索—写作—质量核查”流程。',solution:'先按类型标签与论证主线选样，再学习段落功能和节奏；写作后必须输出参考资料与事实核查，明确不确定信息与引用边界。',result:'形成一套可复用的内容分析与写作 Agent 工作流，适用于热点评论、声誉风险评析和方法论文章。',links:[{label:'查看样本索引',href:'公众号文章汇总的副本/样本索引.md'}]},
  mvp:{kicker:'01 / PRODUCT MVP · TRANSFORMATION',title:'产品转型：智能舆情系统 MVP',summary:'围绕“从工具到服务”的产品转型，把能力重新组织成持续交付的智能工作台。',problem:'传统 SaaS 的页面和功能很多，但用户仍要自己理解流程、配置任务和拼接结果；价值没有以业务结果的方式交付。',contribution:'参与转型方向、核心场景优先级、Agent 工作流和动态工作区设计；把监测、事件、风险和报告重新编排成一条任务链。',solution:'以自然语言入口承接任务，用 Supervisor Agent 编排多个 Worker，再将关键证据、判断过程与行动建议呈现在动态工作区。',result:'形成可演示的前端 MVP，支持日均汇聚约 100 条线索、聚合约 30 件事件，为后续智能服务化奠定产品骨架。',links:[{label:'打开产品原型',href:'智能服务版-双视角-Agent Teams的副本.html'}]}
};
Object.assign(projectData.feedback, {
  title: '学生反馈洞察工作流',
  summary: '沿用原工作流的词云、情绪图、问题报告与每周事件总结四条支路，整理为 17 个节点。',
  contribution: '',
  solution: '问卷读取与清洗后，并行生成词云、情绪图和问题报告；公众号材料独立提取校园事件并生成每周总结。四路结果从左向右汇入统一排版与结束节点。',
  result: '展示材料包含 90 条测试反馈、3 篇公众号材料、四分支工作流设计与一份图文示例报告。',
  links: [{ label: '查看工作流', media: 'workflow' }, { label: '阅读示例报告', media: 'report' }]
});
projectData.lab.links = [{ label: '播放演示视频', media: 'video' }];
projectData.writing.result = '以 63 篇参考语料建立结构学习流程，并展示两篇 Agent 生成成稿：公共服务议题评论与科技议题评论。每篇保留正文、写作说明、参考资料与质量核查记录，可直接阅读或下载原稿。';
projectData.writing.links = [
  { label: '阅读成稿 · 迪士尼盲杖争议', href: 'portfolio-assets/writing-results/disney-commentary.html' },
  { label: '阅读成稿 · AGI 叙事与安全', href: 'portfolio-assets/writing-results/ai-commentary.html' },
  { label: '浏览 63 篇参考样本', media: 'samples' }
];
projectData.opinion.links = [{ label: '体验 test_02 AI 主驾', href: 'portfolio-assets/test02/index.html' }];
projectData.mvp.links = [{ label: '打开产品演示原型', href: '智能服务版-双视角-Agent Teams的副本.html?demo=1' }];

const modal = document.querySelector('#project-modal');
const mediaDialog = document.querySelector('#media-dialog');
const mediaContent = document.querySelector('#media-content');
const mediaTools = document.querySelector('#media-tools');
let projectTrigger;
let projectKey;
const lockScroll = () => { document.body.style.overflow = modal.classList.contains('open') || mediaDialog.open ? 'hidden' : ''; };
const make = (tag, className, value) => { const el = document.createElement(tag); if (className) el.className = className; if (value) el.textContent = value; return el; };
const fileLink = (label, url, download = false) => { const link = make('a', 'media-download', label); link.href = url; if (download) link.download = ''; return link; };

const openModal = key => {
  const data = projectData[key]; if (!data) return;
  projectKey = key; projectTrigger = document.activeElement;
  for (const field of ['kicker', 'title', 'summary', 'problem', 'contribution', 'solution', 'result']) {
    const element = document.querySelector(`#modal-${field}`);
    element.textContent = data[field] || '';
    const block = element.closest('.modal-block');
    if (block) block.hidden = !data[field];
  }
  const actions = document.querySelector('#modal-actions'); actions.replaceChildren();
  data.links.forEach(link => {
    if (link.media) { const button = make('button', 'case-media-button', `${link.label} ↗`); button.type = 'button'; button.addEventListener('click', () => openMedia(link.media)); actions.append(button); }
    else actions.append(fileLink(`${link.label} ↗`, link.href));
  });
  modal.classList.add('open'); modal.setAttribute('aria-hidden', 'false');
  modal.querySelector('.modal-panel').scrollTop = 0;
  ['main', '.site-nav', '.site-footer'].forEach(s => { document.querySelector(s).inert = true; });
  lockScroll(); modal.querySelector('button[data-close]').focus();
};
const closeModal = () => {
  modal.classList.remove('open'); modal.setAttribute('aria-hidden', 'true');
  ['main', '.site-nav', '.site-footer'].forEach(s => { document.querySelector(s).inert = false; });
  lockScroll(); projectTrigger?.focus();
};

const mediaInfo = {
  resume: { title: '吴炎斌 · 个人简历', note: '原版简历 · 可直接阅读或下载 PDF', url: 'portfolio-assets/简历-吴炎斌.pdf' },
  contact: { title: '联系吴炎斌', note: '欢迎交流 AI 产品、Agent 与项目实践。' },
  samples: { title: '公众号文章样本库', note: '63 篇参考语料 · 可搜索并展开原文；语料用于结构研究，不代表本人原创。' },
  video: { title: '实验室智能管家 · 产品演示', note: '原始演示视频 · 约 1 分 41 秒 · 已转换为浏览器兼容的 H.264 格式', url: 'portfolio-assets/lab-demo-h264.mp4' },
  workflow: { title: '学生反馈洞察工作流', note: 'Coze 风格 · 17 个节点 · 4 条分析支路', url: 'portfolio-assets/workflow-v2.svg' },
  original: { title: '原版工作流 · 留档对照', note: '原始 Coze 工作流截图，保留与升级设计的对照。', url: 'portfolio-assets/workflow-v1.png' },
  report: { title: '工作流示例报告', note: '3 页示例报告 · 基于测试素材', url: 'portfolio-assets/运营洞察报告.pdf' }
};

async function openMedia(kind) {
  const info = mediaInfo[kind]; if (!info) return;
  document.querySelector('#media-title').textContent = info.title;
  document.querySelector('#media-note').textContent = info.note;
  mediaContent.replaceChildren(); mediaTools.replaceChildren(); mediaDialog.dataset.kind = kind;
  if (info.url) mediaTools.append(fileLink(kind === 'workflow' ? '下载高清 PNG' : ['report', 'resume'].includes(kind) ? '下载原版 PDF' : '下载文件', kind === 'workflow' ? 'portfolio-assets/workflow.png' : info.url, true));
  const notice = make('p', 'media-error', '材料加载失败，请使用上方下载按钮保存后查看。'); notice.hidden = true;
  if (kind === 'video') {
    const video = make('video', 'case-video'); video.controls = true; video.playsInline = true; video.preload = 'metadata'; video.src = info.url;
    video.setAttribute('aria-label', '实验室小程序演示视频');
    video.addEventListener('error', () => { notice.hidden = false; });
    const state = make('p', 'media-state', '正在读取视频…');
    video.addEventListener('loadedmetadata', () => { state.textContent = `视频已就绪 · ${Math.floor(video.duration / 60)} 分 ${Math.round(video.duration % 60)} 秒 · 点击播放`; });
    video.addEventListener('playing', () => { state.textContent = '正在播放'; });
    video.addEventListener('pause', () => { state.textContent = '已暂停'; });
    mediaContent.append(video, state);
  } else if (kind === 'contact') {
    const panel = make('div', 'contact-panel');
    const email = make('input', 'contact-email'); email.value = 'wyb18959209440@163.com'; email.readOnly = true; email.setAttribute('aria-label', '联系邮箱');
    const copy = make('button', 'zoom-button', '复制邮箱'); copy.type = 'button';
    const state = make('p', 'media-state', '也可以选中邮箱地址手动复制。'); state.setAttribute('role', 'status');
    copy.addEventListener('click', async () => {
      try { await navigator.clipboard.writeText(email.value); state.textContent = '邮箱已复制'; }
      catch {
        email.focus(); email.select();
        let copied = false;
        try { copied = document.execCommand('copy'); } catch { /* Keep the selected address available for manual copy. */ }
        state.textContent = copied ? '邮箱已复制' : '请按 Ctrl/Cmd+C 复制已选中的邮箱。';
      }
    });
    panel.append(email, copy, fileLink('使用邮件客户端撰写', `mailto:${email.value}`), state);
    mediaContent.append(panel);
  } else if (kind === 'samples') {
    showSamples();
  } else if (kind === 'report' || kind === 'resume') {
    const pages = make('div', 'report-pages');
    const count = kind === 'resume' ? 1 : 3;
    for (let n = 1; n <= count; n++) {
      const figure = make('figure', 'report-page'); const img = new Image();
      img.src = kind === 'resume' ? 'portfolio-assets/resume-page.png' : `portfolio-assets/report-pages/page-${n}.png`;
      img.alt = kind === 'resume' ? '吴炎斌个人简历' : `原版运营洞察报告第 ${n} 页，共 3 页`;
      img.addEventListener('error', () => { notice.hidden = false; });
      figure.append(make('figcaption', '', `第 ${n} / ${count} 页`), img); pages.append(figure);
    }
    mediaContent.append(pages);
  } else {
    const viewport = make('div', 'diagram-viewport'); viewport.tabIndex = 0; viewport.setAttribute('aria-label', '流程图区域，可滚动查看放大后的图像');
    const image = new Image(); image.src = info.url; image.alt = info.title; image.className = 'workflow-full'; image.draggable = false;
    image.addEventListener('error', () => { notice.hidden = false; }); viewport.append(image); mediaContent.append(viewport);
    let scale = 1;
    const label = make('span', 'zoom-label', '适应画布'); label.setAttribute('aria-live', 'polite');
    const applyZoom = () => { image.style.width = `${scale * 100}%`; label.textContent = scale === 1 ? '适应画布' : `${scale.toFixed(1)}×`; };
    [['−', '缩小流程图', () => { scale = Math.max(1, scale - .5); }], ['＋', '放大流程图', () => { scale = Math.min(5, scale + .5); }], ['适应', '适应画布', () => { scale = 1; }]].forEach(([text, title, change]) => {
      const button = make('button', 'zoom-button', text); button.type = 'button'; button.setAttribute('aria-label', title); button.addEventListener('click', () => { change(); applyZoom(); }); mediaTools.append(button);
    });
    mediaTools.append(label);
    if (kind === 'workflow') {
      mediaTools.append(fileLink('下载矢量 SVG', info.url, true));
      const details = make('details', 'node-specs'); details.append(make('summary', '', '查看 17 个节点的输入、输出与设计规则'));
      const nodeList = make('div', 'node-list'); details.append(nodeList); mediaContent.append(details);
      fetch('portfolio-assets/workflow-v2.json').then(r => { if (!r.ok) throw Error(); return r.json(); }).then(data => {
        data.nodes.forEach(n => { const row = make('article', 'node-spec'); row.append(make('h3', '', `${n.id} · ${n.title}`), make('p', '', n.description), make('small', '', `输入：${n.input} → 输出：${n.output}`)); nodeList.append(row); });
      }).catch(() => nodeList.append(make('p', '', '节点说明暂未加载，高清图仍可查看。')));
    }
  }
  mediaContent.append(notice); if (!mediaDialog.open) mediaDialog.showModal(); mediaContent.scrollTop = 0; lockScroll();
}
document.querySelector('[data-media-close]').addEventListener('click', () => mediaDialog.close());
mediaDialog.addEventListener('click', event => { if (event.target === mediaDialog) { const box = mediaDialog.getBoundingClientRect(); if (event.clientX < box.left || event.clientX > box.right || event.clientY < box.top || event.clientY > box.bottom) mediaDialog.close(); } });
mediaDialog.addEventListener('close', () => { const video = mediaContent.querySelector('video'); if (video) { video.pause(); video.removeAttribute('src'); video.load(); } lockScroll(); });
document.querySelectorAll('[data-open]').forEach(button => button.addEventListener('click', () => openModal(button.dataset.open)));
document.querySelectorAll('[data-close]').forEach(button => button.addEventListener('click', closeModal));
document.querySelectorAll('[data-media]').forEach(link => link.addEventListener('click', event => { event.preventDefault(); openMedia(link.dataset.media); }));
document.querySelectorAll('.project-card').forEach(card => {
  const trigger = card.querySelector('[data-open]');
  const link = make('button', 'project-hit-area'); link.type = 'button';
  link.setAttribute('aria-label', `查看${card.querySelector('h3').textContent}案例`);
  link.addEventListener('click', () => openModal(trigger.dataset.open));
  card.prepend(link);
});
document.addEventListener('keydown', event => {
  if (mediaDialog.open || !modal.classList.contains('open')) return;
  if (event.key === 'Escape') { closeModal(); return; }
  if (event.key === 'Tab') { const items = [...modal.querySelectorAll('button,a[href]')]; const first = items[0], last = items.at(-1); if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last.focus(); } else if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first.focus(); } }
});
function applyFilter(category) {
  document.querySelectorAll('.filter').forEach(button => { const selected = button.dataset.filter === category; button.classList.toggle('active', selected); button.setAttribute('aria-pressed', String(selected)); });
  document.querySelectorAll('.project-card').forEach(card => { const show = category === 'all' || card.dataset.category === category; card.style.display = show ? '' : 'none'; if (show) card.classList.add('in'); });
}
document.querySelectorAll('.filter').forEach(button => button.addEventListener('click', () => applyFilter(button.dataset.filter)));
document.querySelectorAll('[data-category-link]').forEach(link => link.addEventListener('click', () => applyFilter(link.dataset.categoryLink)));
document.querySelectorAll('a[href="#work"]:not([data-category-link])').forEach(link => link.addEventListener('click', () => applyFilter('all')));
applyFilter('all');
const observer=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');observer.unobserve(e.target)}}),{threshold:.12});document.querySelectorAll('.reveal').forEach(el=>observer.observe(el));

async function showSamples() {
  const container = make('section', 'sample-library');
  const label = make('label', 'sample-search-label', '搜索文章标题、主题或论证主线');
  const search = make('input', 'sample-search'); search.type = 'search'; search.placeholder = '例如：AI、平台治理、品牌声誉'; label.append(search);
  const count = make('p', 'sample-count', '正在加载样本…'); count.setAttribute('role', 'status');
  const list = make('div', 'sample-list'); container.append(label, count, list); mediaContent.append(container);
  try {
    const response = await fetch('portfolio-assets/writing-samples.json'); if (!response.ok) throw Error();
    const { samples } = await response.json();
    const render = () => {
      const query = search.value.trim().toLocaleLowerCase();
      const selected = samples.filter(item => [item.title, item.topic, item.tags, item.logic, item.section].join(' ').toLocaleLowerCase().includes(query));
      count.textContent = `${selected.length} / ${samples.length} 篇样本`; list.replaceChildren();
      if (!selected.length) list.append(make('p', 'sample-empty', '没有匹配的文章，试试其他关键词。'));
      selected.forEach(item => {
        const entry = make('details', 'sample-entry'); const title = make('summary', '', item.title);
        const body = make('div', 'sample-body');
        body.append(make('p', 'sample-meta', `${item.section} · ${item.genre} · 约 ${item.length} 字`), make('p', 'sample-logic', `论证主线：${item.logic}`), make('p', 'sample-meta', `适用场景：${item.useCase}`));
        const article = make('div', 'sample-article', item.content); body.append(article); entry.append(title, body); list.append(entry);
      });
    };
    search.addEventListener('input', render); render();
  } catch {
    count.textContent = '样本暂未加载成功，可下载原索引查看。';
    list.append(fileLink('下载原始索引', '公众号文章汇总的副本/样本索引.md', true));
  }
}

// Allow generated article pages to return directly to their project case.
const initialProject = new URLSearchParams(location.search).get('project');
if (initialProject && Object.hasOwn(projectData, initialProject)) openModal(initialProject);
