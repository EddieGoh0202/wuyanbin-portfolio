/* Local portfolio interactions. All content remains explicitly sample data. */
(() => {
  if (new URLSearchParams(location.search).get('demo') !== '1') return;
  const dialog = document.createElement('dialog');
  dialog.id = 'portfolio-prototype-preview';
  dialog.style.cssText = 'width:min(840px,94vw);max-height:88vh;padding:28px;border:1px solid #dce1e9;border-radius:12px;color:#1b2638;background:#fff;overflow:auto';
  const heading = document.createElement('h2');
  const note = document.createElement('p');
  note.textContent = '样例资料预览 · 内容摘自本原型的展示数据，供体验产品流程。';
  note.style.cssText = 'font-size:13px;color:#64748b;line-height:1.7';
  const content = document.createElement('div');
  content.style.cssText = 'white-space:pre-wrap;font-size:14px;line-height:1.9;padding:18px;background:#f5f7fa;border-radius:8px;margin:18px 0';
  const close = document.createElement('button'); close.textContent = '关闭'; close.className = 'btn'; close.onclick = () => dialog.close();
  const download = document.createElement('button'); download.textContent = '下载当前示例'; download.className = 'btn primary'; download.style.marginLeft = '10px';
  dialog.append(heading, note, content, close, download); document.body.append(dialog);
  dialog.addEventListener('keydown', event => event.stopPropagation());
  dialog.addEventListener('click', event => { if (event.target === dialog) { const r = dialog.getBoundingClientRect(); if (event.clientX < r.left || event.clientX > r.right || event.clientY < r.top || event.clientY > r.bottom) dialog.close(); } });
  function save(title, text) {
    const url = URL.createObjectURL(new Blob([title, '\n\n样例数据 · 产品流程演示\n\n', text], { type: 'text/plain;charset=utf-8' }));
    const link = document.createElement('a'); link.href = url; link.download = title.replace(/[\\/:*?"<>|]/g, '-') + '-示例.txt';
    document.body.append(link); link.click(); link.remove(); setTimeout(() => URL.revokeObjectURL(url), 1000);
  }
  function context(button) {
    return button.closest('.result-card,.outcome-card,.knowledge-row,.business-modal-summary,.modal-body,.panel') || button.closest('.view') || button.parentElement;
  }
  function readContent(element) {
    const copy = element.cloneNode(true);
    copy.querySelectorAll('button,script,style,select,input').forEach(el => el.remove());
    copy.querySelectorAll('p,div,h1,h2,h3,tr,li').forEach(el => el.append('\n'));
    return copy.textContent.replace(/[ \t]+/g, ' ').replace(/\n\s*\n/g, '\n').trim();
  }
  document.addEventListener('click', event => {
    const button = event.target.closest('button'); if (!button || dialog.contains(button)) return;
    const action = button.getAttribute('onclick') || '';
    if (!/^showToast\(/.test(action)) return;
    const text = button.textContent.trim();
    if (!/下载|导出|查看内容|查看报告/.test(text)) return;
    event.preventDefault(); event.stopImmediatePropagation();
    const element = context(button);
    const title = element.querySelector('.result-title,.outcome-title,.panel-title,h1,h2,h3,.knowledge-name')?.textContent.trim() || '当前成果';
    const body = readContent(element);
    if (/下载|导出/.test(text)) { save(title, body); return; }
    heading.textContent = title; content.textContent = body;
    download.onclick = () => save(title, body);
    dialog.showModal();
  }, true);

  // These are metadata chips, not navigation controls.
  document.querySelectorAll('.search-result-row .global-search-platforms button:not([onclick])').forEach(button => {
    const label = document.createElement('span'); label.className = 'tag'; label.textContent = button.textContent; button.replaceWith(label);
  });

  const panel = document.querySelector('[data-account-profile-panel="clues"] .panel');
  if (panel) {
    const rows = [...panel.querySelectorAll('tbody tr')];
    const filters = [{ label:'全部', match:() => true }, { label:'自动关联', match:row => row.cells[3]?.textContent.includes('自动关联') }, { label:'待核事件', match:row => /待核|待确认/.test(row.cells[3]?.textContent || '') }];
    const empty = document.createElement('tr'); const cell = document.createElement('td'); cell.colSpan = 6; cell.textContent = '当前示例没有符合此条件的记录'; empty.append(cell); empty.hidden = true; panel.querySelector('tbody')?.append(empty);
    panel.querySelectorAll('.drill-segment button').forEach((button, i) => {
      const filter = filters[i]; if (!filter) return;
      button.textContent = `${filter.label} ${rows.filter(filter.match).length}`;
      button.onclick = () => {
        rows.forEach(row => { row.hidden = !filter.match(row); });
        empty.hidden = rows.some(row => !row.hidden);
        panel.querySelectorAll('.drill-segment button').forEach(item => { item.classList.toggle('active', item === button); item.setAttribute('aria-pressed', String(item === button)); });
      };
    });
  }
})();
