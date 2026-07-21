# MarkItDown

> [!TIP]
> MarkItDown is a Python package and command-line utility for converting various files to Markdown (e.g., for indexing, text analysis, etc). 
>
> For more information, and full documentation, see the project [README.md](https://github.com/sakoho81/markitdown) on GitHub.

> [!IMPORTANT]
> MarkItDown performs I/O with the privileges of the current process. Like open() or requests.get(), it will access resources that the process itself can access. Sanitize your inputs in untrusted environments, and call the narrowest `convert_*` function needed for your use case (e.g., `convert_stream()`, or `convert_local()`). See the [Security Considerations](https://github.com/sakoho81/markitdown#security-considerations) section of the documentation for more information.

## Installation

From PyPI:

```bash
pip install markitdown[all]
```

Or install as a global tool with uv:

```bash
uv tool install './packages/markitdown[all]'
```

From source:

```bash
git clone git@github.com:sakoho81/markitdown.git
cd markitdown
uv sync --all-packages
```

## Usage

### Command-Line

```bash
markitdown path-to-file.pdf > document.md
```

Or from within the repo:

```bash
uv run markitdown path-to-file.pdf -o document.md
```

### Python API

```python
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("test.xlsx")
print(result.text_content)
```

### More Information

For more information, and full documentation, see the project [README.md](https://github.com/sakoho81/markitdown) on GitHub.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must follow
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
