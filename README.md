# Local Book Reader

Local-first ebook reader built as a single HTML file.

Open books in the browser, customize the reading surface, save highlights and notes locally, track progress, and use read-aloud controls without a backend.

## Run

```powershell
Start-Process ".\textbook reader.html"
```

## Included File

- `textbook reader.html` - the complete app

## Features

- Supports `TXT`, `HTML`, `PDF`, and `EPUB`
- Local library view
- Reader themes and typography controls
- Search with match navigation
- Bookmarks, highlights, and notes
- Reading stats and resume position
- Text-to-speech controls
- Dictionary popup
- Focus mode

## Storage

The app stores reading data in your browser using `localStorage` and `sessionStorage`.

## Notes

- The app runs fully on the client side
- Some features depend on browser support and CDN-loaded libraries
- PDF and EPUB support require the external parsing libraries to load successfully
