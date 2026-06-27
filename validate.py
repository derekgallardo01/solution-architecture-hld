"""Placeholder linter for the HLD + diagram templates.

    python validate.py                    # check every .md under examples/
    python validate.py path/to/my-hld.md  # check one file (use this on your drafts)

Flags angle-bracket placeholders like `<project name>`, `<connector>` that you
forgot to fill in. Exit code 0 if clean, 1 if any remain — suitable for a
pre-share gate so half-finished HLDs don't reach a client.
"""

from __future__ import annotations

import glob
import re
import sys

PLACEHOLDER = re.compile(r"<[^<>\n]{1,80}>")

# Tags that look like placeholders but aren't (HTML / Mermaid / Markdown).
ALLOW = {
    "<br>", "<br/>", "<br />", "<details>", "</details>",
    "<summary>", "</summary>", "<html>", "</html>",
}


def lint(path: str) -> list[tuple[int, str]]:
    out: list[tuple[int, str]] = []
    with open(path, encoding="utf-8") as fh:
        in_fence = False
        for ln, line in enumerate(fh, 1):
            stripped = line.lstrip()
            if stripped.startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue  # Don't flag tokens inside fenced code (mermaid uses them).
            for m in PLACEHOLDER.finditer(line):
                text = m.group(0)
                if text.lower() in ALLOW:
                    continue
                if text.startswith("<!--"):
                    continue
                if text.startswith("<https://") or text.startswith("<http://"):
                    continue
                out.append((ln, text))
    return out


def main(argv: list[str]) -> int:
    files = argv if argv else sorted(glob.glob("examples/*.md"))
    if not files:
        print("No files to check (no examples/*.md and no path provided).")
        return 0

    total = 0
    for path in files:
        try:
            issues = lint(path)
        except FileNotFoundError:
            print(f"SKIP {path}: not found")
            continue
        if issues:
            print(f"\n{path}: {len(issues)} unfilled placeholder(s)")
            for ln, text in issues[:15]:
                print(f"  line {ln}: {text}")
            if len(issues) > 15:
                print(f"  ... and {len(issues) - 15} more")
            total += len(issues)
        else:
            print(f"OK   {path}")

    print(f"\n{total} placeholder(s) total.")
    return 0 if total == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
