# AGENTS.md

## Project Overview

MarkItDown is a Python utility for converting various file formats to Markdown. It's designed for use with LLMs and text analysis pipelines. The repo is a monorepo managed with uv workspaces.

## Package Map

| Package | Purpose |
|---------|---------|
| `packages/markitdown` | Core library and CLI (`markitdown` command). Converts files to markdown. |
| `packages/markitdown-ocr` | Plugin that adds LLM Vision OCR to PDF, DOCX, PPTX, XLSX converters. |
| `packages/markitdown-mcp` | MCP server exposing markitdown as a tool for AI agents. CLI: `markitdown-mcp`. |
| `packages/markitdown-sample-plugin` | Reference implementation for building third-party plugins. |

## Setup

```bash
# Install uv if needed
uv sync --all-packages

# Run the CLI
uv run markitdown <file>
uv run markitdown-mcp --help
```

For global installation (available outside the repo):
```bash
uv tool install git+https://github.com/sakoho81/markitdown.git --directory packages/markitdown
```

## Supported File Formats

### Built-in Converters

| Format | Converter | Extensions |
|--------|-----------|------------|
| Plain Text | `PlainTextConverter` | `.txt`, `.md`, `.json`, `.jsonl` |
| HTML | `HtmlConverter` | `.html`, `.htm` |
| Word | `DocxConverter` | `.docx` |
| PowerPoint | `PptxConverter` | `.pptx` |
| Excel (modern) | `XlsxConverter` | `.xlsx` |
| Excel (legacy) | `XlsConverter` | `.xls` |
| PDF | `PdfConverter` | `.pdf` |
| Images | `ImageConverter` | `.jpg`, `.jpeg`, `.png` |
| Audio | `AudioConverter` | `.wav`, `.mp3`, `.m4a` |
| EPUB | `EpubConverter` | `.epub` |
| CSV | `CsvConverter` | `.csv` |
| Jupyter | `IpynbConverter` | `.ipynb` |
| ZIP | `ZipConverter` | `.zip` |
| Outlook | `OutlookMsgConverter` | `.msg` |
| YouTube | `YouTubeConverter` | URL-based |
| Wikipedia | `WikipediaConverter` | URL-based |
| Bing SERP | `BingSerpConverter` | URL-based |
| RSS/Atom | `RssConverter` | `.rss`, `.atom`, `.xml` |

### Azure Cloud Converters (opt-in, require Azure endpoints)

- `DocumentIntelligenceConverter`: `.docx`, `.pptx`, `.xlsx`, `.html`, `.pdf`, `.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`
- `ContentUnderstandingConverter`: Documents (`.pdf`, `.docx`, `.pptx`, `.xlsx`, `.html`, `.txt`, `.md`, `.rtf`, `.xml`), Email (`.eml`, `.msg`), Images (`.jpeg`, `.jpg`, `.png`, `.bmp`, `.tiff`, `.heif`), Video (`.mp4`, `.m4v`, `.mov`, `.avi`, `.mkv`, `.webm`, `.flv`, `.wmv`), Audio (`.wav`, `.mp3`, `.m4a`, `.flac`, `.ogg`, `.aac`, `.wma`)

## CLI Reference

```
markitdown [OPTIONS] [FILENAME]

Options:
  -o, --output FILE       Output file (default: stdout)
  -x, --extension EXT     Hint for file extension (when reading from stdin)
  -m, --mime-type TYPE    Hint for MIME type
  -c, --charset CHARSET   Hint for charset (e.g., UTF-8)
  -d, --use-docintel      Use Azure Document Intelligence (requires -e)
  -e, --endpoint URL      Document Intelligence endpoint
  --use-cu                Use Azure Content Understanding (requires --cu-endpoint)
  --cu-endpoint URL       Content Understanding endpoint
  --cu-analyzer ID        Content Understanding analyzer ID
  --cu-file-types LIST    Comma-separated file types for CU routing
  -p, --use-plugins       Enable third-party plugins
  --list-plugins          List installed plugins
  --keep-data-uris        Keep base64-encoded images in output
  -v, --version           Show version
```

If FILENAME is omitted, reads from stdin.

## Common Workflows

### Single file conversion
```bash
uv run markitdown document.pdf -o output.md
```

### Stdin piping
```bash
cat document.pdf | uv run markitdown -x .pdf
```

### Batch conversion
```bash
for f in *.pdf; do uv run markitdown "$f" -o "${f%.pdf}.md"; done
```

### With plugins and LLM
```bash
uv run markitdown --use-plugins document.pdf
# In Python:
# md = MarkItDown(enable_plugins=True, llm_client=client, llm_model="gpt-4o")
```

### List installed plugins
```bash
uv run markitdown --list-plugins
```

## Development

### Run tests
```bash
uv run pytest packages/markitdown/tests/
```

### Type checking
```bash
uv run mypy --ignore-missing-imports packages/markitdown/src/
```

### Pre-commit checks
```bash
pre-commit run --all-files
```

### Install optional dependencies
Optional dependencies are defined in `packages/markitdown/pyproject.toml` under `[project.optional-dependencies]`. Categories: `all`, `pptx`, `docx`, `xlsx`, `xls`, `pdf`, `outlook`, `audio-transcription`, `youtube-transcription`, `az-doc-intel`, `az-content-understanding`.

## OpenCode Skill

This repo includes an OpenCode skill at `.opencode/skills/markitdown/SKILL.md` that teaches OpenCode to use the markitdown CLI for file conversion. To install globally:

```bash
ln -s "$(pwd)/.opencode/skills/markitdown" ~/.config/opencode/skills/markitdown
```
