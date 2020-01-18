"""
Renders the examples into a single HTML output file.
"""
import os
import time
from typing import Dict, List
from jinja2 import Environment, FileSystemLoader
from mistune import escape, Markdown, Renderer
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
EXAMPLE_DIR = os.path.join(BASE_DIR, "examples")


class HighlightRenderer(Renderer):
    """
    Markdown renderer including syntax highlighting from pygments.
    """
    def block_code(self, code: str, lang: str = None):
        if not lang:
            return "\n<pre>%s</pre>\n" % escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = html.HtmlFormatter()
        return highlight(code, lexer, formatter)


def markdown_to_html(markdown_text: str) -> str:
    """
    Renders a string of markdown as HTML.
    """
    md2html = Markdown(renderer=HighlightRenderer())
    return md2html(markdown_text)


def examples_to_html(directory: str) -> List[Dict[str, str]]:
    """
    Renders all `.md` files in a directory, and corresponding
    `.before.py` and `.after.py` files as HTML.
    """
    # Find all examples and render them.
    examples = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for fname in filenames:
            # Only look for markdown files.
            if not fname.endswith(".md"):
                continue
            # Strip .md from end of filename and get basename.
            fpath = os.path.join(dirpath, fname)
            base_fname = fpath[:-3]
            # Get before/after and render those with syntax highlighting.
            before_py = f"{base_fname}.before.py"
            after_py = f"{base_fname}.after.py"
            # Skip if these files do not exist.
            if not (os.path.exists(before_py) and os.path.exists(after_py)):
                continue
            # Info
            example = {}
            example["slug"] = os.path.basename(base_fname)
            with open(fpath, encoding="utf8") as fopen:
                # Read first line as the title.
                title = fopen.readline().strip("# ")
                example["title"] = title
                # Rewind, then read and render entire file.
                fopen.seek(0)
                text = fopen.read()
                example["info"] = markdown_to_html(text)
            # Before
            with open(before_py, encoding="utf8") as fopen:
                text = fopen.read()
                # Convert to markdown and render.
                md_text = f"```python3\n{text}\n```"
                example["before"] = markdown_to_html(md_text)
            # After
            with open(after_py, encoding="utf8") as fopen:
                text = fopen.read()
                # Convert to markdown and render.
                md_text = f"```python3\n{text}\n```"
                example["after"] = markdown_to_html(md_text)
            # Add the example.
            examples.append(example)
    return examples


def render_template(template_name: str, context: dict = None) -> str:
    """
    Renders a Jinja HTML template.
    """
    # Set up jinja templates
    jenv = Environment(
        loader=FileSystemLoader(searchpath=TEMPLATE_DIR),
        lstrip_blocks=True,
        trim_blocks=True,
    )
    template = jenv.get_template(template_name)
    # Render the template.
    return template.render(context)


def main():
    """
    Generate the static site.
    """
    # Get examples
    examples = examples_to_html(EXAMPLE_DIR)
    # Render template.
    output = render_template(
        "index.html",
        {
            "date": time.strftime(r"%b. %d, %Y", time.localtime()),
            "examples": examples,
        }
    )
    # Write to file.
    outpath = os.path.join(BASE_DIR, "index.html")
    with open(outpath, encoding="utf8", mode="w") as index:
        index.write(output)


if __name__ == "__main__":
    main()
