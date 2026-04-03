import re

with open('textbook reader.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Keep fonts link from HTML
# 2. Extract <script> block intact
script_match = re.search(r'<script>(.*?)</script>', text, re.DOTALL)
script_content = script_match.group(1) if script_match else ""

# 3. New <style> block
new_style = """

    :root {
      --bg: #FAFAF7;
      --fg: #1C1C1E;
      --page-bg: #FEFCF8;
      --muted: #6B6B6B;
      --panel: rgba(255,255,255,0.82);
      --accent: #C8602A;
      --accent2: #E8936A;
      --border: rgba(0,0,0,0.07);
      --shadow: 0 4px 24px rgba(0,0,0,0.08);
      --radius: 18px;
      --font-size: 18px;
      --line-height: 1.7;
      --letter-spacing: 0px;
      --word-spacing: 0px;
      --paragraph-spacing: 18px;
      --reading-width: 720px;
      --reader-font: 'Crimson Pro', serif;
      --texture-opacity: .07;
    }
    * { box-sizing: border-box; }
    html, body { height: 100%; }
    body { 
        margin: 0; background: var(--bg); color: var(--fg); 
        font-family: 'DM Sans', sans-serif; transition: background .3s, color .3s; overflow-x: hidden; 
    }
    
    /* Vignette and texture */
    body::before, body::after { content: ""; position: fixed; inset: 0; pointer-events: none; }
    body::before { background: radial-gradient(circle at 50% 20%, rgba(255,255,255,.22), transparent 40%), radial-gradient(circle at 50% 85%, rgba(0,0,0,.06), transparent 55%); z-index: -2; }
    body::after { background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cg fill='%23000' fill-opacity='.08'%3E%3Ccircle cx='10' cy='20' r='.7'/%3E%3Ccircle cx='34' cy='46' r='.6'/%3E%3Ccircle cx='58' cy='18' r='.8'/%3E%3Ccircle cx='86' cy='62' r='.7'/%3E%3C/g%3E%3C/svg%3E"); background-size: 220px 220px; opacity: var(--texture-opacity); z-index: -1; }

    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-thumb { background: var(--accent2); border-radius: 999px; }
    ::-webkit-scrollbar-track { background: transparent; }

    .topbar { position: fixed; inset: 0 0 auto 0; height: 4px; background: rgba(255,255,255,.1); z-index: 80; }
    #progressBar { height: 100%; width: 0; background: var(--accent); transition: width .12s linear; }
    .view { min-height: calc(100vh - 4px); padding: 24px 14px 60px; }
    .hidden { display: none !important; }

    .card, .drawer, .modal, .popup, .searchbar, .toast, .dict {
      backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); background: var(--panel); border: 1px solid var(--border); box-shadow: var(--shadow);
    }

    .landing { max-width: 1200px; margin: 0 auto; }
    
    .hero { display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 18px; margin-bottom: 20px; }
    .hero-card { 
        background: linear-gradient(135deg, #FDF6F0 0%, #F5EBE0 50%, #EDD9C5 100%);
        border-radius: var(--radius); padding: 40px; position:relative; overflow:hidden;
    }
    .hero-card h1 { margin: 0 0 16px; font-family: 'Playfair Display', serif; font-size: clamp(2.5rem, 5vw, 3.5rem); font-style: italic; line-height: 1.1; }
    .hero-card p { margin: 0; color: var(--muted); line-height: 1.65; max-width:480px;}

    .hero-icon { position:absolute; right:-20px; bottom:-20px; opacity:0.8;}

    .chips { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 24px; }
    .chip { padding: 8px 16px; border-radius: 999px; background: rgba(255,255,255,.5); border: 1px solid rgba(0,0,0,0.05); font-weight: 700; font-size: .9rem; }

    .uploadbox { display: flex; flex-direction: column; gap: 12px; justify-content: space-between; border-radius:var(--radius); padding:20px; }
    .drop { min-height: 200px; border: 2px dashed var(--border); border-radius: var(--radius); display: grid; place-items: center; text-align: center; padding: 18px; transition: .2s; }
    .drop:hover, .drop.hover { border-color: var(--accent); transform: translateY(-2px); border-style:dashed;}
    .drop i { font-size: 2.2rem; color: var(--accent); transition:transform 0.2s;}
    .drop:hover i { transform:translateY(-5px); }

    .btn, .select, .input, .range, .color { font-family: inherit; border-radius: 12px; border: 1px solid var(--border); min-height: 42px; padding:0 14px;}
    .toggle { position: relative; width: 44px; height: 24px; background: rgba(0,0,0,0.1); border-radius: 12px; cursor: pointer; display: inline-block; transition: .2s; margin-top: 8px;}
    .toggle input { opacity: 0; width: 0; height: 0; position:absolute;}
    .toggle::after { content: ''; position: absolute; top: 2px; left: 2px; width: 20px; height: 20px; background: #fff; border-radius: 50%; transition: transform .2s; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
    .toggle:has(input:checked) { background: var(--accent); }
    .toggle:has(input:checked)::after { transform: translateX(20px); }
    .btn { background: var(--accent); color: #fff; padding: 10px 16px; cursor: pointer; font-weight: 600; display: inline-flex; align-items: center; justify-content: center; gap: 8px; transition:0.15s; border-color:transparent;}
    .btn:hover { filter:brightness(1.1); transform:translateY(-1px);}
    .btn.secondary { background: rgba(255,255,255,.6); color: var(--fg); border-color:var(--border);}
    .btn.icon-only { width:42px; padding:0; justify-content:center;}

    .toggle { position: relative; width: 44px; height: 24px; display: inline-block; padding: 0; min-height: auto; border:none; cursor: pointer; }
    .toggle input { opacity: 0; width: 0; height: 0; position:absolute; }
    .toggle::before { content: ""; position: absolute; inset: 0; background: rgba(0,0,0,0.15); border-radius: 999px; transition: 0.2s; }
    .toggle::after { content: ""; position: absolute; left: 2px; top: 2px; width: 20px; height: 20px; background: #fff; border-radius: 50%; transition: 0.2s; box-shadow: 0 2px 5px rgba(0,0,0,0.15); }
    .toggle:has(input:checked)::before { background: var(--accent); }
    .toggle:has(input:checked)::after { transform: translateX(20px); }


    .row { display: flex; flex-wrap: wrap; gap: 10px; align-items: center; }
    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 20px; }
    
    .library { margin-top: 40px; }
    .librarycard { border-radius: 18px; overflow: hidden; background: var(--panel); border: 1px solid var(--border); box-shadow: var(--shadow); display: flex; height: 180px; position:relative;}
    .cover-spine { width:4px; height:100%; position:absolute; left:0;top:0; bottom:0;}
    .card-letter { position:absolute; left:20px; top:20px; opacity:0.08; font-family:'Playfair Display', serif; font-size:3rem; font-weight:900;}
    .body { padding: 24px; padding-left:32px; display: flex; flex-direction: column; gap: 10px; flex: 1; align-items: flex-start; text-align: left; }
    .body h3 { margin: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; font-size: 1.15rem; max-width: 100%; font-family:'Playfair Display', serif; font-weight:700;}
    .meta { color: var(--muted); font-size: .85rem; display: flex; flex-wrap: wrap; gap: 8px; justify-content: flex-start; }
    .bar { height: 6px; background: rgba(0,0,0,.08); border-radius: 999px; overflow: hidden; width:100%;}
    .bar span { display: block; height: 100%; background: var(--accent); }
    .actions { display: flex; gap: 8px; margin-top: auto; flex-wrap: wrap; justify-content: flex-start; width: 100%; }

    .reader { max-width: 1600px; margin: 0 auto; display:flex; flex-direction:column;}
    
    /* Header Toolbar */
    .toolbar { position: sticky; top: 0; z-index: 50; border-radius: 0 0 24px 24px; padding: 0 24px; display: flex; height:64px; align-items: center; justify-content:space-between; margin-bottom: 24px; backdrop-filter: blur(20px); background:rgba(255,255,255,0.7); border-bottom:1px solid var(--border); box-shadow:0 4px 12px rgba(0,0,0,0.03);}
    .toolbar-left { display:flex; align-items:center; gap:16px; flex:1;}
    .toolbar-center { display:flex; align-items:center; gap:16px; justify-content:center; flex:1; font-family:'Playfair Display', serif; font-size:1.1rem; font-weight:700; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;}
    .page-info { font-family:'DM Sans', sans-serif; font-size:0.85rem; font-weight:600; color:var(--muted); font-variant-numeric:tabular-nums;}
    .toolbar-right { display:flex; align-items:center; justify-content:flex-end; gap:8px; flex:1;}
    .toolbar-right button { transition:transform 0.15s; }
    .toolbar-right button:hover { transform:scale(1.12); }

    .exportwrap { position: relative; }
    .exportmenu { position: absolute; top: calc(100% + 8px); right: 0; min-width: 220px; padding: 8px; border-radius: 16px; background: var(--panel); border: 1px solid var(--border); box-shadow: var(--shadow); display: none; z-index: 100; }
    .exportmenu.on { display: grid; gap: 6px; }
    .exportmenu button { justify-content: flex-start; background: transparent; color: var(--fg); width: 100%; padding: 10px 12px; }

    .readercontent { max-width: min(var(--reading-width), calc(100vw - 24px)); margin: 0 auto; padding: 16px 0 70px; display: flex; flex-direction: column; gap: 32px; }
    .readercontent.columns2 .pageinner { column-count: 2; column-gap: 2rem; column-fill: auto; }
    
    .page { position: relative; border-radius: 0; background: var(--page-bg); border-top: 1px solid color-mix(in srgb, var(--accent) 15%, transparent); box-shadow: 0 1px 3px rgba(0,0,0,0.04), 0 8px 32px rgba(0,0,0,0.06), 0 24px 64px rgba(0,0,0,0.04); min-height: 440px; animation: pageIn 0.6s ease forwards; opacity:0; }
    .page:nth-child(1){animation-delay:0.0s} .page:nth-child(2){animation-delay:0.1s} .page:nth-child(3){animation-delay:0.2s} .page:nth-child(4){animation-delay:0.3s} .page:nth-child(n+5){animation-delay:0.4s}
    @keyframes pageIn { from { opacity:0; transform:translateY(24px) } to { opacity:1; transform:translateY(0) } }

    .pageinner { position: relative; padding: 48px 56px 64px; font-family: var(--reader-font); font-size: var(--font-size); line-height: var(--line-height); letter-spacing: var(--letter-spacing); word-spacing: var(--word-spacing); color: var(--fg); transition: background .3s, color .3s; }
    .pageinner p { margin: 0 0 var(--paragraph-spacing); }
    .footer { position: absolute; left: 50%; bottom: 20px; transform: translateX(-50%); color: var(--muted); font-size: .85rem; font-variant: small-caps; }
    .footer::before, .footer::after { content: "—"; margin:0 8px;}

    mark.search { background: #FFB347; color: #111; border-radius: 3px; padding: 0 2px; }
    mark.user { border-radius: 3px; padding: 0 2px; color: inherit; }
    .tts { background: color-mix(in srgb, var(--accent) 24%, transparent); box-shadow: inset 0 -2px 0 color-mix(in srgb, var(--accent) 45%, transparent); }
    
    .readerempty { max-width: 760px; margin: 70px auto; padding: 34px; border-radius: 24px; border: 1px solid var(--border); background: var(--panel); box-shadow: var(--shadow); text-align: center; }
    .readerempty i { font-size: 3rem; color: var(--accent); }

    .backdrop, .modback { position: fixed; inset: 0; background: rgba(0,0,0,.15); backdrop-filter:blur(3px); opacity: 0; pointer-events: none; transition: .2s; z-index: 84; }
    .backdrop.on, .modback.on { opacity: 1; pointer-events: auto; }
    
    /* Drawers */
    .drawer { position: fixed; top: 12px; right: 12px; bottom: 12px; width: min(380px, calc(100vw - 24px)); transform: translateX(110%); transition: transform 0.4s cubic-bezier(0.32, 0, 0.67, 0); z-index: 90; border-radius: 22px; overflow: hidden; display: flex; flex-direction: column; background:rgba(255,255,255,0.85); backdrop-filter:blur(24px);}
    .drawer.on { transform: translateX(0); transition: transform 0.4s cubic-bezier(0.33, 1, 0.68, 1);}
    .drawer header, .modal header { padding: 16px 20px; border-bottom: 1px solid var(--border); display: flex; align-items: center; justify-content: space-between; gap: 8px; position:relative;}
    .drawer header::before { content:''; position:absolute; top:0;left:0;right:0; height:2px; background:linear-gradient(90deg, var(--accent), var(--accent2));}
    .drawer header h3 { margin:0; font-size:1.1rem; display:flex; align-items:center; gap:8px;}
    .drawercontent, .modalcontent { padding: 0; overflow: auto; flex: 1; }
    .drawercontent-inner { padding: 20px; display:flex; flex-direction:column; gap:20px;}

    .item { display: flex; justify-content: space-between; gap: 10px; padding: 16px 20px; border-bottom: 1px solid rgba(0,0,0,.04); transition:background 0.2s;}
    .item:hover { background:rgba(0,0,0,0.02); border-left:3px solid var(--accent); padding-left:17px;}
    .item strong { display: block; margin-bottom: 4px; font-weight:600;}
    .item small { color: var(--muted); }
    .item .ops { display: flex; gap: 8px; }

    .statgrid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px; margin-bottom:20px;}
    .stat { padding: 16px; border-radius: 16px; background: rgba(255,255,255,.62); border: 1px solid var(--border); text-align:center;}
    .stat .label { font-size: .75rem; color: var(--muted); margin-bottom: 6px; text-transform:uppercase; letter-spacing:1px; font-weight:600;}
    .stat .value { font-size: 1.6rem; font-weight: 700; font-family:'Playfair Display', serif; color:var(--accent);}

    .reading-ring-container { display:flex; justify-content:center; align-items:center; margin:20px 0;}
    .reading-ring { position:relative; width:120px; height:120px;}
    .reading-ring svg { transform:rotate(-90deg); width:100%; height:100%;}
    .reading-ring circle { fill:none; stroke-width:8; stroke:rgba(0,0,0,0.05); }
    .reading-ring circle.progress { stroke:var(--accent); stroke-dasharray:314; stroke-dashoffset:314; transition:stroke-dashoffset 1s ease;}
    .reading-ring .center { position:absolute; inset:0; display:flex; align-items:center; justify-content:center; font-family:'Playfair Display',serif; font-size:1.8rem; font-weight:700; color:var(--fg);}

    .modal { position: fixed; inset: 50% auto auto 50%; transform: translate(-50%, -50%) scale(.96); opacity: 0; pointer-events: none; transition: .2s; z-index: 92; width: min(720px, calc(100vw - 24px)); border-radius: 22px; overflow: hidden; background:rgba(255,255,255,0.9); backdrop-filter:blur(24px);}
    .modal.on { opacity: 1; pointer-events: auto; transform: translate(-50%, -50%) scale(1); }
    .helpgrid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px; }
    .key { display: flex; justify-content: space-between; gap: 10px; align-items: center; padding: 12px 14px; border-radius: 14px; background: rgba(255,255,255,.6); border: 1px solid var(--border); }
    kbd { font-family: 'JetBrains Mono', monospace; background: rgba(0,0,0,.08); border-radius: 8px; padding: 3px 7px; font-size: .84rem; }

    /* Searchbar spotlight style */
    .searchbar { position: fixed; left: 50%; top: 40px; transform: translateX(-50%) translateY(-20px); opacity: 0; pointer-events: none; z-index: 94; width: min(600px, calc(100vw - 18px)); border-radius: 99px; padding: 12px 24px; display: flex; gap: 12px; align-items: center; flex-wrap: wrap; transition: .2s; }
    .searchbar.on { opacity: 1; pointer-events: auto; transform: translateX(-50%) translateY(0); }
    .searchbar .input { flex: 1; min-width: 170px; border:none; background:transparent; font-size:1.1rem; outline:none;}
    .searchcount { color: var(--muted); font-weight: 600; margin-left: auto; font-size:0.9rem; background:rgba(0,0,0,0.05); padding:4px 10px; border-radius:99px;}

    /* Popups */
    .popup { position: absolute; z-index: 96; border-radius: 99px; display: none; padding:8px 16px; flex-direction:row; align-items:center; gap:12px; box-shadow:var(--shadow);}
    .popup::after { content:''; position:absolute; bottom:-6px; left:50%; transform:translateX(-50%); border-style:solid; border-width:6px 6px 0; border-color:var(--panel) transparent transparent;}
    .popup.on { display: flex; }
    
    .colors { display: flex; gap: 8px; }
    .colors button { width: 28px; height: 28px; border: 0; border-radius: 50%; cursor: pointer; box-shadow: inset 0 0 0 1px rgba(0,0,0,.1); transition:transform 0.1s;}
    .colors button:hover { transform:scale(1.2);}
    .popup-divider { width:1px; height:24px; background:var(--border);}

    .row2 { display: flex; gap: 8px; flex-wrap: wrap; }
    .row2 input { flex: 1; min-width: 130px; border: 1px solid var(--border); border-radius: 12px; padding: 10px; background: rgba(255,255,255,.65); color: var(--fg); outline:none;}
    
    .dict { position: absolute; z-index: 96; border-radius: 16px; display: none; padding: 20px; width: min(360px, calc(100vw - 20px)); border-left:3px solid var(--accent); background:#fff;}
    .dict.on { display:flex; flex-direction:column; gap:12px; }
    #dictWord { font-family:'Playfair Display', serif; font-size:1.6rem; font-style:italic;}
    #dictPhonetic { color:var(--muted); font-size:0.9rem; font-family:'DM Sans';}
    #dictBody { font-family:'Crimson Pro', serif; font-size:1.1rem; line-height:1.5; color:var(--fg);}

    .toastwrap { position: fixed; left: 50%; bottom: 24px; transform: translateX(-50%); z-index: 120; display: grid; gap: 10px; pointer-events: none; }
    .toast { min-width: 240px; padding: 14px 20px; background: rgba(28,28,28,.92); color: #fff; border-radius: 16px; border-left:3px solid var(--accent); animation: toast 2.8s cubic-bezier(0.2,0.8,0.2,1) forwards; box-shadow:var(--shadow);}
    @keyframes toast { 0% { opacity: 0; transform: translateY(20px) } 12% { opacity: 1; transform: translateY(0) } 84% { opacity: 1; transform: translateY(0) } 100% { opacity: 0; transform: translateY(14px) } }
    
    .loading { position: fixed; inset: 0; display: grid; place-items: center; background: rgba(255,255,255,.8); backdrop-filter:blur(5px); z-index: 110; opacity: 0; pointer-events: none; transition: .2s; }
    .loading.on { opacity: 1; pointer-events: auto; }
    .spin { width: 50px; height: 50px; border-radius: 50%; border: 4px solid rgba(0,0,0,.05); border-top-color: var(--accent); animation: spin 1s linear infinite; margin: 0 auto 16px; }
    @keyframes spin { to { transform: rotate(360deg) } }

    .focusbtn { position: fixed; top: 14px; left: 50%; transform: translateX(-50%); z-index: 101; opacity: 0; pointer-events: none; transition: .2s; }
    body.focus .focusbtn { opacity: 1; pointer-events: auto; }
    body.focus .toolbar, body.focus .drawer, body.focus .modal, body.focus .backdrop, body.focus .searchbar, body.focus .popup, body.focus .dict, body.focus .tts-player { display: none !important; }
    body.focus .page { background: transparent; border-color: transparent; box-shadow: none; }
    
    /* Settings specific */
    .slider-group { display: flex; flex-direction: column; gap: 6px; }
    .slider-group label { display: flex; justify-content: space-between; gap: 8px; font-size: .85rem; color: var(--muted); font-weight:600; text-transform:uppercase; letter-spacing:0.5px;}
    .val { min-width: 38px; text-align: right; }
    
    /* TTS Mini Player */
    .tts-player { position:fixed; bottom:24px; left:50%; transform:translateX(-50%) translateY(100px); z-index:90; background:var(--panel); border:1px solid var(--border); box-shadow:var(--shadow); border-radius:99px; padding:12px 20px; display:flex; align-items:center; gap:16px; opacity:0; transition:0.3s; pointer-events:none;}
    .tts-player.on { transform:translateX(-50%) translateY(0); opacity:1; pointer-events:auto;}

    @media (max-width: 1100px) { .hero { grid-template-columns: 1fr; } .helpgrid, .statgrid { grid-template-columns: 1fr; } }
    @media (max-width: 768px) { 
        .toolbar { padding: 10px; } .title { max-width: 180px; } .pageinner { padding: 32px 24px 46px; } .view { padding-inline: 10px; } 
        .drawer { right: 0; left: 0; bottom: 0; top: auto; width: 100vw; max-height:85vh; border-radius:24px 24px 0 0; transform:translateY(100%); } 
        .drawer.on { transform:translateY(0);}
        .searchbar { top: 12px; } 
        .tts-player { width:calc(100vw - 32px); bottom:16px; border-radius:24px;}
        :root { --font-size: 16px; }
    }
    @font-face{font-family:'OpenDyslexic';src:url('https://cdn.jsdelivr.net/npm/@fontsource/opendyslexic/files/opendyslexic-latin-400-normal.woff2') format('woff2');font-display:swap}

  """

# HTML structure to replace body contents up to the scripts
new_html_content = '''<div class="topbar"><div id="progressBar"></div><div class="bar-shimmer"></div></div>
  <div class="loading" id="loading"><div><div class="spin"></div><div id="loadingText" style="font-weight:700;text-align:center;font-size:1.1rem">Parsing book...</div></div></div>
  <div class="backdrop" id="backdrop"></div>
  <div class="modback" id="modback"></div>
  
  <div class="searchbar" id="searchbar">
    <i class="fa-solid fa-magnifying-glass" style="color:var(--muted)"></i>
    <input class="input" id="searchInput" placeholder="Search this book..." style="flex:1">
    <span class="searchcount" id="searchCount">0 of 0</span>
    <button class="btn secondary icon-only" id="prevMatch"><i class="fa-solid fa-angle-up"></i></button>
    <button class="btn secondary icon-only" id="nextMatch"><i class="fa-solid fa-angle-down"></i></button>
    <button class="btn secondary icon-only" id="closeSearch" style="border-radius:50%"><i class="fa-solid fa-xmark"></i></button>
  </div>
  
  <div class="popup" id="popup">
    <div class="colors">
      <button data-color="#FFD700" style="background:#FFD700"></button>
      <button data-color="#90EE90" style="background:#90EE90"></button>
      <button data-color="#FFB6C1" style="background:#FFB6C1"></button>
      <button data-color="#ADD8E6" style="background:#ADD8E6"></button>
    </div>
    <div class="popup-divider"></div>
    <div class="row2">
      <button class="btn secondary icon-only" id="addNote" style="border-radius:50%;width:32px;height:32px"><i class="fa-regular fa-note-sticky"></i></button>
      <button class="btn secondary icon-only" id="copySel" style="border-radius:50%;width:32px;height:32px"><i class="fa-regular fa-copy"></i></button>
    </div>
  </div>
  <div class="popup hidden" id="noteRow" style="padding:12px;flex-direction:column;align-items:stretch;top:calc(100% + 10px);">
    <input id="noteText" placeholder="Write a note..." class="input" style="margin-bottom:8px">
    <button class="btn" id="saveNote">Save</button>
  </div>

  <div class="dict" id="dict">
    <div class="row" style="justify-content:space-between;margin-bottom:8px">
      <div><div id="dictWord"></div><div id="dictPhonetic"></div></div>
      <div>
        <button class="btn secondary icon-only" id="dictSpeak"><i class="fa-solid fa-volume-high"></i></button>
        <button class="btn secondary icon-only" id="closeDictBtn"><i class="fa-solid fa-xmark"></i></button>
      </div>
    </div>
    <div id="dictBody"></div>
  </div>
  
  <div class="toastwrap" id="toastwrap"></div>
  <button class="btn secondary focusbtn" id="focusExit"><i class="fa-solid fa-compress"></i> Esc to exit</button>

  <section id="landingView" class="view landing">
    <div class="hero">
      <div class="hero-card card">
        <div style="position:relative;z-index:2">
          <h1>Read locally,<br>beautifully.</h1>
          <p>Upload a TXT, PDF, EPUB, or HTML file and get a local-only reader with themes, notes, bookmarks, search, stats, and read-aloud.</p>
          <div class="chips">
            <span class="chip"><i class="fa-solid fa-folder-open"></i> Single file</span>
            <span class="chip"><i class="fa-solid fa-bookmark"></i> Local marks</span>
            <span class="chip"><i class="fa-solid fa-highlighter"></i> Highlights</span>
            <span class="chip"><i class="fa-solid fa-volume-high"></i> Speed reading</span>
          </div>
        </div>
        <svg class="hero-icon" width="280" height="280" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="1" stroke-linecap="round" stroke-linejoin="round">
            <path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"/>
        </svg>
      </div>
      <div class="card uploadbox">
        <div class="drop" id="drop">
          <div>
            <i class="fa-solid fa-cloud-arrow-up"></i>
            <h3 style="margin:12px 0 4px;font-family:'DM Sans', sans-serif;">Drop a book here</h3>
            <div style="color:var(--muted);font-size:.92rem">TXT, PDF, EPUB, HTML</div>
          </div>
          <div class="row" style="margin-top:16px;">
            <label class="btn" for="fileInput"><i class="fa-solid fa-upload"></i> Browse Files</label>
            <button class="btn secondary" id="demoBtn"><i class="fa-solid fa-book"></i> Demo</button>
          </div>
        </div>
        <input id="fileInput" type="file" accept=".txt,.pdf,.epub,.html,.htm" hidden>
      </div>
    </div>
    <div class="library">
      <div class="row" style="justify-content:space-between;margin-bottom:16px">
        <div><h2 style="margin:0 0 4px;font-size:1.6rem;font-family:'Playfair Display'">Your Library</h2></div>
        <button class="btn secondary" id="clearLib"><i class="fa-solid fa-trash"></i> Clear All</button>
      </div>
      <div class="grid" id="libraryGrid"></div>
    </div>
  </section>

  <section id="readerView" class="view reader hidden">
    <div class="toolbar" id="toolbar">
      <div class="toolbar-left">
        <button class="btn secondary icon-only" id="toLibrary" title="Back to Library"><i class="fa-solid fa-arrow-left"></i></button>
      </div>
      <div class="toolbar-center" id="bookTitle">No book open</div>
      <div class="toolbar-right">
        <span class="page-info" id="pageInfo">0 / 0</span>
        <button class="btn secondary icon-only" id="searchBtn" title="Search"><i class="fa-solid fa-magnifying-glass"></i></button>
        <button class="btn secondary icon-only" id="bookmarkBtn" title="Bookmark"><i class="fa-solid fa-bookmark"></i></button>
        <button class="btn secondary icon-only" id="highlightsBtn" title="Highlights"><i class="fa-solid fa-highlighter"></i></button>
        <button class="btn secondary icon-only" id="statsBtn" title="Stats"><i class="fa-solid fa-chart-column"></i></button>
        <button class="btn secondary icon-only" id="ttsBtn" title="Read Aloud"><i class="fa-solid fa-volume-high"></i></button>
        <div class="exportwrap">
          <button class="btn secondary icon-only" id="exportBtn" title="Export"><i class="fa-solid fa-file-export"></i></button>
          <div class="exportmenu" id="exportMenu">
            <button id="exportNotesBtn"><i class="fa-solid fa-file-lines"></i> Export Highlights</button>
            <button id="printBtn"><i class="fa-solid fa-print"></i> Print Book</button>
          </div>
        </div>
        <button class="btn secondary icon-only" id="settingsBtn" title="Settings"><i class="fa-solid fa-gear"></i></button>
      </div>
    </div>
    
    <div class="readercontent" id="readerContent"></div>
    <div class="readerempty hidden" id="readerEmpty">
      <i class="fa-solid fa-book-open"></i>
      <h2 style="margin:16px 0 6px;font-family:'Playfair Display'">Open a book to begin</h2>
      <p style="margin:0;color:var(--muted)">Go back to the library and upload a file.</p>
      <button class="btn" id="openFileBtn" style="margin-top:18px"><i class="fa-solid fa-upload"></i> Choose a file</button>
    </div>
  </section>

  <!-- Drawers -->
  <aside class="drawer" id="settingsDrawer"><header><h3><i class="fa-solid fa-gear"></i> Settings</h3><button class="btn secondary icon-only closeDrawer"><i class="fa-solid fa-xmark"></i></button></header><div class="drawercontent"><div class="drawercontent-inner">
      <div class="row"><span class="small" style="font-weight:600;text-transform:uppercase;color:var(--muted);width:80px">Theme</span><select class="select" id="themeSelect" style="flex:1"><option value="paper">Paper White</option><option value="sepia">Sepia</option><option value="night">Night Dark</option><option value="amoled">AMOLED Black</option><option value="ocean">Ocean Blue</option><option value="custom">Custom</option></select></div>
      <div class="row" style="padding-left:90px"><input class="color" id="bgColor" type="color" title="Background" style="flex:1"><input class="color" id="fgColor" type="color" title="Text" style="flex:1"><input class="color" id="accentColor" type="color" title="Accent" style="flex:1"></div>
      <div class="row"><span class="small" style="font-weight:600;text-transform:uppercase;color:var(--muted);width:80px">Font</span><select class="select" id="fontSelect" style="flex:1"></select></div>
      <hr style="border:0;border-top:1px solid var(--border);margin:10px 0">
      <div class="slider-group"><label>Font Size <span id="fontSizeVal" class="val">18px</span></label><input class="range" id="fontSize" type="range" min="12" max="32" step="1" value="18"></div>
      <div class="slider-group"><label>Line Spacing <span id="lineHeightVal" class="val">1.7</span></label><input class="range" id="lineHeight" type="range" min="1.2" max="2.5" step="0.05" value="1.7"></div>
      <div class="slider-group"><label>Letter Spacing <span id="letterSpacingVal" class="val">0px</span></label><input class="range" id="letterSpacing" type="range" min="-1" max="5" step="0.1" value="0"></div>
      <div class="slider-group"><label>Word Spacing <span id="wordSpacingVal" class="val">0px</span></label><input class="range" id="wordSpacing" type="range" min="0" max="10" step="0.1" value="0"></div>
      <div class="slider-group"><label>Paragraph Spacing <span id="paraSpacingVal" class="val">18px</span></label><input class="range" id="paraSpacing" type="range" min="0" max="40" step="1" value="18"></div>
      <div class="slider-group"><label>Reading Width <span id="readingWidthVal" class="val">680px</span></label><input class="range" id="readingWidth" type="range" min="400" max="1200" step="10" value="680"></div>
      <hr style="border:0;border-top:1px solid var(--border);margin:10px 0">
      <div class="row" style="justify-content:space-between"><label style="font-weight:600;text-transform:uppercase;color:var(--muted);font-size:.85rem">Two Columns</label><label class="toggle"><input type="checkbox" id="columnsToggle"></label></div>
      <div class="row" style="justify-content:space-between"><label style="font-weight:600;text-transform:uppercase;color:var(--muted);font-size:.85rem">Focus Mode</label><label class="toggle"><input type="checkbox" id="focusToggle"></label></div>
      <div class="row" style="justify-content:space-between;align-items:center"><label style="font-weight:600;text-transform:uppercase;color:var(--muted);font-size:.85rem">Jump to Page</label><input class="input jump" id="jumpPage" type="number" min="1" placeholder="#" style="width:80px"></div>
      <div class="row" style="margin-top:10px"><button class="btn secondary" id="nightModeBtn" style="flex:1"><i class="fa-solid fa-moon"></i> Sub Toggle Night</button><button class="btn secondary" id="helpBtn" style="flex:1"><i class="fa-regular fa-circle-question"></i> Shortcuts</button></div>
  </div></div></aside>

  <aside class="drawer" id="bookmarksDrawer"><header><h3><i class="fa-solid fa-bookmark"></i> Bookmarks</h3><button class="btn secondary icon-only closeDrawer"><i class="fa-solid fa-xmark"></i></button></header><div class="drawercontent" id="bookmarksList"></div></aside>
  <aside class="drawer" id="highlightsDrawer"><header><h3><i class="fa-solid fa-highlighter"></i> Highlights</h3><button class="btn secondary icon-only closeDrawer"><i class="fa-solid fa-xmark"></i></button></header><div class="drawercontent" id="highlightsList"></div></aside>
  <aside class="drawer" id="statsDrawer"><header><h3><i class="fa-solid fa-chart-column"></i> Reading Stats</h3><button class="btn secondary icon-only closeDrawer"><i class="fa-solid fa-xmark"></i></button></header><div class="drawercontent"><div class="drawercontent-inner">
        <div class="reading-ring-container">
            <div class="reading-ring">
                <svg><circle cx="60" cy="60" r="50"></circle><circle class="progress" cx="60" cy="60" r="50" id="progressRing"></circle></svg>
                <div class="center" id="progressText">0%</div>
            </div>
        </div>
        <div class="statgrid" id="statsGrid"></div>
        <div style="color:var(--muted);font-size:.92rem;line-height:1.5;text-align:center">🔥 Streak: <span id="streakFlame">0</span> days</div>
  </div></div></aside>
  
  <div class="modal" id="helpModal"><header><h3><i class="fa-regular fa-circle-question"></i> Keyboard Shortcuts</h3><button class="btn secondary icon-only" id="helpClose"><i class="fa-solid fa-xmark"></i></button></header><div class="modalcontent" style="padding:20px"><div class="helpgrid" id="helpGrid"></div></div></div>

  <div class="tts-player" id="ttsPlayer">
    <button class="btn icon-only" id="ttsPlay"><i class="fa-solid fa-play"></i></button>
    <button class="btn secondary icon-only" id="ttsStop"><i class="fa-solid fa-stop"></i></button>
    <select class="select" id="voiceSelect" style="max-width:180px"></select>
    <input class="range" id="ttsRate" type="range" min="0.5" max="2" step="0.1" value="1" style="width:100px">
  </div>
'''

# 4. Integrate with Script (fixing el lookups)
# e.g., missing ID like settingsBtn
script_content = script_content.replace(
    'const el = {',
    "const el = { settingsBtn:$('#settingsBtn'), settingsDrawer:$('#settingsDrawer'), ttsPlayer:$('#ttsPlayer'), progressRing:$('#progressRing'), progressText:$('#progressText'), streakFlame:$('#streakFlame'), "
)
script_content = script_content.replace(
    "const map = { bookmarks:el.bookmarksDrawer, highlights:el.highlightsDrawer, stats:el.statsDrawer, help:el.helpModal };",
    "const map = { bookmarks:el.bookmarksDrawer, highlights:el.highlightsDrawer, stats:el.statsDrawer, help:el.helpModal, settings:el.settingsDrawer };"
)
script_content = script_content.replace(
    "[el.bookmarksDrawer,el.highlightsDrawer,el.statsDrawer,el.helpModal]",
    "[el.bookmarksDrawer,el.highlightsDrawer,el.statsDrawer,el.settingsDrawer,el.helpModal]"
)
script_content = script_content.replace(
    "el.ttsBtn.addEventListener('click', startTTS);",
    "el.ttsBtn.addEventListener('click', () => { el.ttsPlayer.classList.add('on'); startTTS(); });"
)
script_content = script_content.replace(
    "function stopSpeech(){ speechSynthesis.cancel(); state.tts.utterance = null; clearTTS(); el.ttsPlay.innerHTML = '<i class=\"fa-solid fa-play\"></i>'; }",
    "function stopSpeech(){ speechSynthesis.cancel(); state.tts.utterance = null; clearTTS(); el.ttsPlay.innerHTML = '<i class=\"fa-solid fa-play\"></i>'; el.ttsPlayer.classList.remove('on');}"
)
script_content = script_content.replace(
    "el.settingsBtn?.addEventListener('click', () => { openOverlay('settings'); });",
    ""
)
# Add settings icon bind
script_content = script_content.replace(
    "el.bookmarkBtn.addEventListener('click', addBookmark);",
    "el.bookmarkBtn.addEventListener('click', addBookmark);\n      el.settingsBtn?.addEventListener('click', () => openOverlay('settings'));"
)

# Fix empty dictionary pronunciation
script_content = script_content.replace(
    "el.closeDict.addEventListener('click', closeDict);",
    "el.closeDictBtn = document.getElementById('closeDictBtn');\n    el.dictSpeak = document.getElementById('dictSpeak');\n    if(el.closeDictBtn) el.closeDictBtn.addEventListener('click', closeDict);\n    if(el.dictSpeak) el.dictSpeak.addEventListener('click', () => { const w=el.dictWord.innerText; if(w) speechSynthesis.speak(new SpeechSynthesisUtterance(w)); });\n"
)
# Update Library grid missing drawing elements (first letter)
script_content = script_content.replace(
    '<div class="cover" style="--c1:${c.c1};--c2:${c.c2}"><div class="letter">${escapeHtml((book.title || book.filename || \'?\').trim().charAt(0).toUpperCase())}</div><div style="font-size:.85rem;font-weight:800">${escapeHtml(book.type || \'\')}</div></div>',
    '<div class="cover-spine" style="background:linear-gradient(180deg, ${c.c1}, ${c.c2})"></div><div class="card-letter">${escapeHtml((book.title || book.filename || \'?\').trim().charAt(0).toUpperCase())}</div>'
)

# Library card update string
script_content = script_content.replace(
    '<article class="librarycard">',
    '<article class="librarycard">'
)

# Hook up progress ring
script_content = script_content.replace(
    "function renderStats(){",
    "function renderStats(){\n      const p = Math.round(clamp(state.activeBook?.progress||0,0,100)); if(el.progressText) el.progressText.textContent=p+'%'; if(el.progressRing) el.progressRing.style.strokeDashoffset = 314 - (314 * p / 100);\n      if(el.streakFlame) el.streakFlame.textContent = state.stats.streak || 0;"
)
script_content = script_content.replace(
    "if(!state.library.length){ el.libraryGrid.innerHTML = `<div class=\"readerempty\" style=\"grid-column:1/-1;margin:0\"><i class=\"fa-solid fa-book-open\"></i><h2 style=\"margin:10px 0 6px\">No books yet</h2><p style=\"margin:0;color:var(--muted)\">Upload your first file to create a local shelf.</p></div>`; return; }",
    "if(!state.library.length){ el.libraryGrid.innerHTML = `<div class=\"readerempty\" style=\"grid-column:1/-1;margin:0\"><svg width=\"120\" height=\"120\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"var(--accent)\" stroke-width=\"1\"><path d=\"M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20\"></path></svg><h2 style=\"margin:16px 0 6px;font-family:'Playfair Display'\">Your shelf awaits</h2><p style=\"margin:0;color:var(--muted)\">Upload your first file to create a local shelf.</p></div>`; return; }"
)

# Put it all together
new_full_html = re.sub(r'<style>.*?</style>', lambda m: f'<style>\n{new_style}\n  </style>', text, flags=re.DOTALL)
new_full_html = re.sub(r'<body>.*?<script>', lambda m: f'<body>\n{new_html_content}\n  <script>', new_full_html, flags=re.DOTALL)
new_full_html = re.sub(r'<script>.*?</script>', lambda m: f'<script>{script_content}</script>', new_full_html, flags=re.DOTALL)

with open('textbook reader.html', 'w', encoding='utf-8') as f:
    f.write(new_full_html)
print("Updated successfully")

