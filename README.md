# Local Book Reader

A polished local-first ebook reader built as a single HTML file with embedded CSS and JavaScript.

It lets you open books directly in the browser, customize the reading experience, save highlights and notes locally, track progress, and use read-aloud controls without needing a backend.

## Highlights

- Local-only reading workflow for privacy-friendly use
- Supports `TXT`, `HTML`, `PDF`, and `EPUB`
- Beautiful reading UI with library view and reader view
- Theme switching with reader-surface color customization
- Typography controls for font, size, spacing, width, and columns
- Search with match navigation
- Bookmarks, highlights, and notes stored in browser storage
- Reading stats, progress tracking, and streaks
- Built-in text-to-speech controls
- Dictionary lookup popup for selected words
- Focus mode for distraction-free reading

## Project Structure

- `textbook reader.html`
  Main application file. Contains the full UI, styling, and client-side logic.
- `update.py`
  Helper script used during earlier automated editing/refactoring work.
- `fix.py`
  Helper patch script from prior iterations.
- `append.py`
  Small helper script used to append/modify earlier update logic.

## How It Works

This app runs entirely in the browser:

1. Open the HTML file in a modern browser.
2. Upload a supported book file or use the demo content.
3. Read locally with no backend or database required.
4. Settings, bookmarks, resume position, and highlights are saved in browser storage.

## Running the App

### Option 1: Open directly

Open `textbook reader.html` in your browser.

### Option 2: Serve locally

If your browser blocks any local-file integrations, serve the folder with a lightweight static server.

Examples:

```powershell
python -m http.server 8000
```

Then open:

```text
http://localhost:8000/textbook%20reader.html
```

## Supported Formats

- `TXT`
- `HTML` / `HTM`
- `PDF`
- `EPUB`

## Core Features

### 1. Library

- Upload books from your machine
- Keep a local reading shelf
- Resume recently opened items
- Remove books from the local shelf

### 2. Reading Experience

- Clean reading layout
- Adjustable reading width
- Single-column or two-column reading mode
- Scroll-based reading with live progress
- Focus mode for distraction reduction

### 3. Themes and Typography

- Preset reader themes
- Custom page background, text, and accent color
- Font family selector
- Font size control
- Line height, letter spacing, word spacing, and paragraph spacing controls

Important note:

Theme customization is applied to the reading surface so the outside app chrome stays visually stable.

### 4. Highlights, Notes, and Bookmarks

- Select text to create highlights
- Add notes to selected passages
- Save bookmarks for the current reading position
- Jump back to saved highlights and bookmarks
- Export highlights and notes as a text file

### 5. Search

- Search the current book
- Navigate between matches
- View live match count

### 6. TTS and Dictionary

- Read-aloud controls with voice and rate selection
- Playback mini-player
- Double-click word lookup with dictionary popup

## Keyboard Shortcuts

The app includes built-in keyboard shortcuts such as:

- `Ctrl + F` for search
- `Ctrl + B` for bookmark
- `Ctrl + D` for dark/light toggle
- `Ctrl + +` to increase font size
- `Ctrl + -` to decrease font size
- `F11` or `Ctrl + Shift + F` for fullscreen
- `Page Up` / `Page Down` for page navigation
- `Escape` to close overlays
- `?` to open the shortcuts panel

## Data Storage

The reader uses browser storage:

- `localStorage`
- `sessionStorage`

Saved data can include:

- library metadata
- current reading progress
- resume position
- bookmarks
- highlights
- notes
- reading stats

## External Dependencies

The app currently loads a few browser-side dependencies from CDNs:

- `pdf.js` for PDF parsing
- `JSZip`
- `epub.js` for EPUB parsing
- Google Fonts
- Font Awesome

Because of that:

- internet access may be needed the first time those assets load
- PDF/EPUB functionality depends on the external scripts loading successfully

## Recent Stability Work

The current version includes fixes for:

- runtime script errors
- popup visibility and positioning
- bookmark click behavior
- reader-only theme application
- safer mobile column handling
- more reliable highlight restore behavior
- cleaner local persistence handling
- more defensive TTS support checks

## Known Limitations

- Browser support for speech synthesis varies by platform
- Dictionary lookup depends on an external API call
- Very large books may exceed browser storage limits
- CDN failures can affect PDF, EPUB, fonts, or icons

## Publishing This Project

To publish this folder to GitHub:

```powershell
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/kssaichandan/READER.git
git branch -M main
git push -u origin main
```

## License

No license file is included yet. Add one if you want to make reuse terms explicit.
