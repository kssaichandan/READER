# Local Book Reader

Local Book Reader is a browser-based reading app for opening and reading books directly in the browser.

It is built as a lightweight local-first reader with support for uploading files, customizing the reading experience, saving progress, and using tools like bookmarks, highlights, notes, search, and text-to-speech.

## Live Link

https://reader-dljp.onrender.com/textbook%20reader.html

## What This Is

This project is a clean ebook and document reader made for simple browser use.

You can upload supported files, read them in a polished interface, change the reading style, and keep your reading data saved in the browser.

It is useful for:

- reading books locally in the browser
- keeping bookmarks and notes
- searching inside uploaded content
- resuming from your last reading position
- using text-to-speech for read-aloud support

## How It Works

The app runs on the client side in the browser.

1. Open the reader.
2. Upload a supported file such as TXT, HTML, PDF, or EPUB.
3. The app parses the file in the browser and renders it into readable pages or sections.
4. Your reading state is saved in browser storage so bookmarks, highlights, notes, and progress can be restored later.

## Main Features

- local library view for opened books
- resume reading from the last saved position
- search with next and previous navigation
- bookmarks for quick return points
- highlights in multiple colors
- notes attached to highlights
- text-to-speech controls
- dictionary popup for selected words
- focus mode
- adjustable reading width
- font and spacing controls
- theme and custom color controls
- reading progress and reading stats

## Supported File Types

- `TXT`
- `HTML`
- `HTM`
- `PDF`
- `EPUB`

## Local Run Command

```powershell
Start-Process ".\index.html"
```

## Storage

The app uses browser storage to keep useful reading data such as:

- library items
- resume position
- bookmarks
- highlights
- notes
- reading progress
- reading stats

## Notes

- PDF and EPUB support depend on browser-side libraries loading correctly
- text-to-speech depends on browser support for the Web Speech API
- very large books may hit browser storage limits
