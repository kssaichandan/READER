# Local Book Reader

Local Book Reader is a browser-based reading app packed into a single HTML file.

It is designed for private, local reading with a polished interface, customizable typography, built-in notes and highlights, search, reading stats, and text-to-speech controls.

## Run

Use this single terminal command:

```powershell
Start-Process ".\textbook reader.html"
```

## What It Does

The app opens supported book files directly in the browser and lets you:

- read without a backend
- keep a local library in browser storage
- resume where you left off
- customize the reading surface
- search through the current book
- save bookmarks, highlights, and notes
- export saved highlights
- use text-to-speech controls

## Main Features

### Library

- Upload books from your device
- Keep a local shelf of opened books
- Reopen recent books from the library view
- Remove books you no longer want saved

### Reading Experience

- Clean reading layout
- Scroll-based reading flow
- Progress bar and current page display
- Adjustable reading width
- Optional two-column reading mode
- Focus mode for distraction-free reading

### Themes and Typography

- Preset reading themes
- Custom page background color
- Custom page text color
- Custom accent color
- Font family selector
- Font size control
- Line height control
- Letter spacing control
- Word spacing control
- Paragraph spacing control

Theme changes are applied to the reading surface so the surrounding UI stays stable.

### Search, Notes, and Highlights

- In-book text search
- Next and previous match navigation
- Text selection popup for quick actions
- Highlight selected text in multiple colors
- Attach notes to saved highlights
- Jump back to saved highlights

### Bookmarks and Progress

- Save the current reading position as a bookmark
- Return to saved bookmarks
- Automatically store resume position
- Track reading progress and daily reading activity

### TTS and Dictionary

- Built-in text-to-speech player
- Voice selection
- Rate control
- Sentence highlighting while speech is active
- Double-click word lookup with dictionary popup

## Supported File Types

- `TXT`
- `HTML`
- `HTM`
- `PDF`
- `EPUB`

## Keyboard Shortcuts

- `Ctrl + F` opens search
- `Ctrl + B` adds a bookmark
- `Ctrl + D` toggles dark/light behavior
- `Ctrl + +` increases font size
- `Ctrl + -` decreases font size
- `F11` or `Ctrl + Shift + F` toggles fullscreen
- `Page Up` and `Page Down` move between reading sections
- `Escape` closes overlays or exits focus mode
- `?` opens the shortcuts help panel

## Storage

The app stores reading data locally in the browser using:

- `localStorage`
- `sessionStorage`

This can include:

- library entries
- last opened position
- reading progress
- bookmarks
- highlights
- notes
- reading stats

## Tech Notes

- The entire app lives in `textbook reader.html`
- The interface, styles, and logic are all embedded in that file
- PDF and EPUB support depend on browser-side libraries loaded from CDNs
- Speech features depend on browser support for the Web Speech API

## Good Fit For

- personal reading
- local-first workflows
- offline-friendly reading after assets are loaded
- quick ebook viewing without a separate app install

## Limitations

- PDF and EPUB parsing depend on external browser libraries loading successfully
- Speech synthesis support varies by browser and operating system
- Very large books may hit browser storage limits
- Dictionary lookup depends on network access to the dictionary API

## File In This Repo

- `textbook reader.html` - the complete application
