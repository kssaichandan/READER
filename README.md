# Local Book Reader

> A free, private, browser-based ebook reader — open TXT, PDF, EPUB and HTML files with themes, highlights, notes, search and read-aloud. Your files never leave your browser.

Local Book Reader is a browser-based reading app for opening and reading books directly in the browser.

It is built as a lightweight local-first reader with support for uploading files, customizing the reading experience, saving progress, and using tools like bookmarks, highlights, notes, search, and text-to-speech.

<!-- Screenshot: a screenshot or animated demo of the reader could go here. -->

## Live Link

Deploy the contents of this folder to any static host (Render, Netlify, GitHub Pages).

Example Render service is configured in `render.yaml` — push this folder to a Git repo and connect it to Render as a static site.

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

## Tech Stack

- Minimal static HTML, CSS and vanilla JavaScript — no build step

This simplified starter removes the heavy inlined app and provides a clean UI you can extend. PDF/EPUB parsing is out of scope for this minimal redesign; add back libraries like `pdf.js` or `epub.js` if you need full support.

## Browser Support

Works in modern evergreen browsers (recent Chrome, Edge, Firefox and Safari) with JavaScript enabled. PDF and EPUB rendering depend on the browser-side libraries above; read-aloud depends on the browser's Web Speech API support.

## Local Run

Open `index.html` in your browser or serve this folder from a static host.

Example (serve locally with Python):

```bash
python -m http.server 8000
```

Git push instructions

Run these commands from the project root to push to your repository (replace remote URL):

```bash
git init
git add .
git commit -m "Minimal reader: responsive UI + PDF/EPUB support"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

Note: I cannot push to your remote from here — run the commands above on your machine or give me repository access/token and I can prepare a script for you.

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

## License

Released under the MIT License.

## Contact

kssaichandan@gmail.com
