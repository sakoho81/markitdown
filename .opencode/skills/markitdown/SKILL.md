---
name: markitdown
description: >
  Convert documents (PDF, DOCX, PPTX, XLSX, images, audio, HTML, EPUB, ZIP,
  CSV, JSON, Outlook .msg, Jupyter notebooks, and more) to Markdown using
  the markitdown CLI. Use when the user asks to convert a file or batch of
  files to markdown, when you encounter an unsupported file format that you
  need to read, or when the user mentions document conversion, extraction,
  or text analysis from binary files.
---

# MarkItDown File Conversion

Use the globally installed `markitdown` CLI to convert files to Markdown.

## Availability Check

Before using markitdown, verify it is installed:

```bash
markitdown --version
```

If the command is not found, tell the user:

```
markitdown is not installed. Install it globally with:
  uv tool install git+https://github.com/sakoho81/markitdown.git --directory packages/markitdown
```

Do not proceed until the user confirms they have installed it.

## Supported Formats

markitdown can convert: PDF, DOCX, PPTX, XLSX, XLS, CSV, HTML, EPUB, Jupyter notebooks (.ipynb), images (JPEG, PNG), audio (WAV, MP3, M4A), ZIP archives, Outlook .msg files, plain text, JSON, XML, RSS/Atom feeds, YouTube URLs, Wikipedia pages, and Bing search results.

With optional Azure cloud backends: Document Intelligence and Content Understanding (adds video, email, HEIF, and higher-quality extraction).

## Single File Conversion

```bash
markitdown input.pdf -o output.md
```

If no `-o` flag, output goes to stdout. Use this when the user wants the markdown in a file:

```bash
markitdown input.docx -o input.md
```

To pipe to another command or capture output, omit `-o`:

```bash
markitdown input.pdf
```

## Reading Stdin

When piping content or the file extension would help disambiguate:

```bash
cat input.pdf | markitdown -x .pdf
```

Provide extension hints with `-x` (with or without leading dot), MIME type hints with `-m`, or charset hints with `-c`.

## Batch Conversion

For multiple files, use a shell loop:

```bash
for f in *.pdf; do markitdown "$f" -o "${f%.pdf}.md"; done
```

Or process all files in a directory:

```bash
for f in /path/to/dir/*.docx; do markitdown "$f" -o "${f%.docx}.md"; done
```

## When to Use This Skill

- User says "convert this PDF to markdown"
- User says "extract text from this PowerPoint"
- User says "I need to read this Excel file"
- You encounter a binary file (PDF, DOCX, XLSX, etc.) that you cannot read directly
- User asks to batch process documents
- User asks to analyze content of non-text files
- User mentions "markitdown" or "mark it down"

## Plugins and LLM-Assisted Conversion

To use plugins (e.g., markitdown-ocr for OCR):

```bash
markitdown --use-plugins document.pdf
```

List installed plugins:

```bash
markitdown --list-plugins
```

## Azure Cloud Backends

For higher-quality extraction via Azure:

```bash
# Document Intelligence
markitdown -d -e "<endpoint>" document.pdf

# Content Understanding
markitdown --use-cu --cu-endpoint "<endpoint>" document.pdf
```

## Keep Data URIs

By default, base64-encoded images (data URIs) are truncated. To preserve them:

```bash
markitdown --keep-data-uris document.html
```

## Output Options

- `-o <file>` — write to file
- Omit `-o` — write to stdout (for piping, redirection, or display)

Always prefer `-o` when the user wants the result saved to a specific file.
