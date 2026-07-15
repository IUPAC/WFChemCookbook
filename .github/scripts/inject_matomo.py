"""Inject the Matomo analytics snippet into every built HTML page.

The MyST book-theme has no option for custom scripts, so the snippet in
book/static/js/matomo.html is inserted before </head> after `myst build --html`.
Safe to run twice: pages already containing the snippet are skipped.

Usage: python inject_matomo.py <html_dir> [snippet_file]
"""

import sys
from pathlib import Path

MARKER = "<!-- Matomo -->"


def main():
    html_dir = Path(sys.argv[1])
    snippet_file = (
        Path(sys.argv[2])
        if len(sys.argv) > 2
        else Path(__file__).parents[2] / "book" / "static" / "js" / "matomo.html"
    )
    snippet = snippet_file.read_text(encoding="utf-8")
    injected = 0
    for page in sorted(html_dir.rglob("*.html")):
        html = page.read_text(encoding="utf-8")
        if MARKER in html or "</head>" not in html:
            continue
        page.write_text(html.replace("</head>", snippet + "</head>", 1), encoding="utf-8")
        injected += 1
    print(f"Injected Matomo snippet into {injected} pages under {html_dir}")


if __name__ == "__main__":
    main()
