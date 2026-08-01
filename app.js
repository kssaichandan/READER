// Minimal reader JS: handles file input, demo text and simple library UI.
const $ = s => document.querySelector(s);
const $$ = s => Array.from(document.querySelectorAll(s));
const library = [];
function el(id){return document.getElementById(id)}
function bytesToKb(n){return Math.max(1,Math.round(n/1024))+' KB'}

function escapeHtml(s){ return String(s||'').replace(/[&<>'"]/g, ch=>({ '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":"&#39;" }[ch])); }
function stripHtml(raw){ try{ const doc = new DOMParser().parseFromString(raw,'text/html'); return doc.body.innerHTML || ''; }catch{ return escapeHtml(raw); } }

function renderLibrary(){
  const list = el('libraryList');
  list.innerHTML = library.length ? library.map((b,i)=>`<div class="card"><div><strong>${escapeHtml(b.title)}</strong><div class="small">${escapeHtml(b.filename)} • ${b.size}</div></div><div><button class="btn" data-i="${i}">Open</button></div></div>`).join('') : '<div class="small">No books yet — drop or choose a file.</div>';
  list.querySelectorAll('button[data-i]').forEach(btn=>btn.addEventListener('click', e=>openBook(library[btn.dataset.i])));
}

function openBook(book){
  el('landing').classList.add('hidden');
  el('readerView').classList.remove('hidden');
  el('bookTitle').textContent = book.title;
  el('readerContent').innerHTML = `<div class="page"><h2>${escapeHtml(book.title)}</h2><div>${book.html}</div></div>`;
  window.scrollTo({top:0,behavior:'auto'});
}

async function parsePdfFile(file){
  if(typeof pdfjsLib === 'undefined') return null;
  const buf = await file.arrayBuffer();
  pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';
  const loadingTask = pdfjsLib.getDocument({ data: buf });
  const pdf = await loadingTask.promise;
  let html = '';
  for(let i=1;i<=pdf.numPages;i++){
    try{
      const p = await pdf.getPage(i);
      const content = await p.getTextContent();
      const text = (content.items || []).map(it=>it.str).join(' ');
      html += `<h3>Page ${i}</h3><p>${escapeHtml(text)}</p>`;
    }catch(e){ html += `<h3>Page ${i}</h3><p>(could not render page)</p>`; }
  }
  return { title: file.name.replace(/\.[^.]+$/,''), filename: file.name, size: bytesToKb(file.size), html };
}

async function parseEpubFile(file){
  if(typeof ePub === 'undefined') return null;
  const buf = await file.arrayBuffer();
  const book = ePub(buf);
  await book.ready;
  let html = '';
  try{
    const items = book.spine && book.spine.items ? book.spine.items : [];
    for(const item of items){
      try{
        const doc = await book.load(item.href);
        const content = typeof doc === 'string' ? doc : (doc && doc.documentElement ? doc.documentElement.outerHTML : '');
        html += stripHtml(content);
      }catch(e){ }
    }
  }catch(e){ html = '<p>(could not parse EPUB)</p>'; }
  return { title: file.name.replace(/\.[^.]+$/,''), filename: file.name, size: bytesToKb(file.size), html };
}

async function handleFiles(files){
  for(const f of files){
    const ext = (f.name.split('.').pop()||'').toLowerCase();
    try{
      let book = null;
      if(ext === 'pdf'){
        book = await parsePdfFile(f);
      } else if(ext === 'epub'){
        book = await parseEpubFile(f);
      } else if(ext === 'html' || ext === 'htm'){
        const txt = await f.text(); book = { title: f.name.replace(/\.[^.]+$/,''), filename: f.name, size: bytesToKb(f.size), html: stripHtml(txt) };
      } else if(ext === 'txt'){
        const txt = await f.text(); book = { title: f.name.replace(/\.[^.]+$/,''), filename: f.name, size: bytesToKb(f.size), html: `<p>${escapeHtml(txt).replace(/\n/g,'<br>')}</p>` };
      } else {
        const txt = await f.text(); book = { title: f.name.replace(/\.[^.]+$/,''), filename: f.name, size: bytesToKb(f.size), html: escapeHtml(txt).replace(/\n/g,'<br>') };
      }
      if(book) library.unshift(book);
    }catch(e){ console.error('file parse error', e); library.unshift({ title:f.name, filename:f.name, size:bytesToKb(f.size), html:`<p>(could not parse ${escapeHtml(f.name)})</p>` }); }
  }
  renderLibrary();
}

function makeDemo(){
  const content = `<p>This is a minimal demo book. Use the upload area to open your own files.</p><p>Enjoy the clean, minimal reader layout.</p>`;
  const obj = { title:'Demo Book', filename:'demo.txt', size:'small', html:content };
  library.unshift(obj); renderLibrary(); openBook(obj);
}

document.addEventListener('DOMContentLoaded', ()=>{
  el('fileInput').addEventListener('change', e=>handleFiles(e.target.files));
  el('dropZone').addEventListener('dragover', e=>{ e.preventDefault(); e.dataTransfer.dropEffect='copy'; el('dropZone').classList.add('hover'); });
  el('dropZone').addEventListener('dragleave', e=>{ el('dropZone').classList.remove('hover'); });
  el('dropZone').addEventListener('drop', e=>{ e.preventDefault(); el('dropZone').classList.remove('hover'); handleFiles(e.dataTransfer.files); });
  el('chooseBtn').addEventListener('click', ()=>el('fileInput').click());
  el('demoBtn').addEventListener('click', makeDemo);
  el('backBtn').addEventListener('click', ()=>{ el('landing').classList.remove('hidden'); el('readerView').classList.add('hidden'); });
  renderLibrary();
});
