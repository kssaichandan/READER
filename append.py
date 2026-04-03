with open("update.py", "r", encoding="utf-8") as f:
    lines = f.read().split("\n")

# Find the end of the script_content manipulation block, right before "# Put it all together"
insert_idx = -1
for i, l in enumerate(lines):
    if "# Put it all together" in l:
        insert_idx = i
        break

new_code = """
# 4. Bookmark handler
script_content = script_content.replace(
    "el.bookmarkBtn.addEventListener('click', addBookmark);",
    "el.bookmarkBtn.addEventListener('click', () => { renderBookmarks(); openOverlay('bookmarks'); });"
)

# 7. Custom Colors - Settings Accent Color Input
# We injected the third input previously in new_body block, but we must do it via update.py if there's a new_html_content block!
"""
lines.insert(insert_idx, new_code)

with open("update.py", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
