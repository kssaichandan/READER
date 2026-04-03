import re

with open('update.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 6. Toggle Switch Styling
# Remove .toggle from the shared padding/min-height group
text = re.sub(r'\.btn,\s*\.select,\s*\.input,\s*\.range,\s*\.color,\s*\.toggle', '.btn, .select, .input, .range, .color', text)

toggle_styles = """
    .toggle { position: relative; width: 44px; height: 24px; display: inline-block; padding: 0; min-height: auto; border:none; cursor: pointer; }
    .toggle input { opacity: 0; width: 0; height: 0; position:absolute; }
    .toggle::before { content: ""; position: absolute; inset: 0; background: rgba(0,0,0,0.15); border-radius: 999px; transition: 0.2s; }
    .toggle::after { content: ""; position: absolute; left: 2px; top: 2px; width: 20px; height: 20px; background: #fff; border-radius: 50%; transition: 0.2s; box-shadow: 0 2px 5px rgba(0,0,0,0.15); }
    .toggle:has(input:checked)::before { background: var(--accent); }
    .toggle:has(input:checked)::after { transform: translateX(20px); }
"""
# Insert toggles style
text = re.sub(r'(\.btn\.icon-only.*?\}\n)', r'\1' + toggle_styles + '\n', text)

# 4. Bookmark handler
text = text.replace(
    '''"el.bookmarkBtn.addEventListener('click', addBookmark);\\n       el.settingsBtn?.addEventListener('click', () => openOverlay('settings'));"''',
    '''"el.bookmarkBtn.addEventListener('click', () => { renderBookmarks(); openOverlay('bookmarks'); });\\n       el.settingsBtn?.addEventListener('click', () => openOverlay('settings'));"'''
)

# 7. Custom Colors customAccent UI
text = text.replace(
    '''      <div class="row" style="padding-left:90px"><input class="color" id="bgColor" type="color" title="Background" style="flex:1"><input class="color" id="fgColor" type="color" title="Text" style="flex:1"></div>''',
    '''      <div class="row" style="padding-left:90px"><input class="color" id="bgColor" type="color" title="Background" style="flex:1"><input class="color" id="fgColor" type="color" title="Text" style="flex:1"><input class="color" id="accentColor" type="color" title="Accent" style="flex:1"></div>'''
)

# 7. Custom Colors - Logic replacing strings inside script_content replacements
text = text.replace(
    "const customBg=el.bgColor.value; const customFg=el.fgColor.value; document.documentElement.style.setProperty('--bg', customBg); document.documentElement.style.setProperty('--fg', customFg);",
    "const customBg=el.bgColor.value; const customFg=el.fgColor.value; state.settings.customAccent=el.accentColor.value; document.documentElement.style.setProperty('--bg', customBg); document.documentElement.style.setProperty('--fg', customFg); document.documentElement.style.setProperty('--accent', state.settings.customAccent);"
)
text = text.replace(
    "el.themeSelect.value='custom'; el.bgColor.value = getComputedStyle(document.documentElement).getPropertyValue('--bg').trim(); el.fgColor.value = getComputedStyle(document.documentElement).getPropertyValue('--fg').trim();",
    "el.themeSelect.value='custom'; el.bgColor.value = getComputedStyle(document.documentElement).getPropertyValue('--bg').trim(); el.fgColor.value = getComputedStyle(document.documentElement).getPropertyValue('--fg').trim(); el.accentColor.value = state.settings.customAccent || '#C8602A'; document.documentElement.style.setProperty('--accent', el.accentColor.value);"
)

# 8. closeDict missing settingsDrawer
text = text.replace(
    "[el.searchbar, el.popup, el.bookmarksDrawer, el.highlightsDrawer, el.statsDrawer].some(x => x.classList.contains('on'))",
    "[el.searchbar, el.popup, el.bookmarksDrawer, el.highlightsDrawer, el.statsDrawer, el.settingsDrawer].some(x => x.classList.contains('on'))"
)

# 9. Duplicate openFileBtn
# Searching for el.readerEmpty.querySelector('button')?.addEventListener...
text = re.sub(
    r"el\.readerEmpty\.querySelector\('button'\)\?\.addEventListener\('click',\s*\(\)\s*=>\s*el\.fileInput\.click\(\)\);\s*\\n",
    "",
    text
)
# Just in case it's different format
text = text.replace("el.readerEmpty.querySelector('button')?.addEventListener('click', () => el.fileInput.click());\n", "")
text = text.replace("el.readerEmpty.querySelector('button')?.addEventListener('click', () => el.fileInput.click());", "")

# 10. remove standalone populateVoices()
text = text.replace("populateVoices(); speechSynthesis.onvoiceschanged = populateVoices;", "speechSynthesis.onvoiceschanged = populateVoices;")
text = text.replace("populateVoices();\n      speechSynthesis.onvoiceschanged = populateVoices;", "speechSynthesis.onvoiceschanged = populateVoices;")

with open('update.py', 'w', encoding='utf-8') as f:
    f.write(text)
print("fix.py run successfully")
