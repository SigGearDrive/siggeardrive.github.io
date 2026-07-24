#!/usr/bin/env python3
"""Validate the built MkDocs site uses only the project GitHub Pages URL."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from xml.etree import ElementTree

SITE_DIR = Path("site")
EXPECTED_BASE = "https://siggeardrive.github.io/SigGear-product-docs/"
HOST_BASE = "https://siggeardrive.github.io/"
URL_PATTERN = re.compile(r"https://siggeardrive\.github\.io/[^\s\"'<>)]*")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def check_required_files() -> None:
    required = [
        SITE_DIR / "index.html",
        SITE_DIR / "sitemap.xml",
        SITE_DIR / "Applications/6-42mm-planetary-gear-reducer/index.html",
        SITE_DIR / "Applications/micro-robotics-gear-motor/index.html",
    ]
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        fail("Missing required generated files: " + ", ".join(missing))


def check_home_canonical() -> None:
    html = (SITE_DIR / "index.html").read_text(encoding="utf-8")
    expected = f'<link rel="canonical" href="{EXPECTED_BASE}">'
    if expected not in html:
        fail(f"Homepage canonical is not exactly {EXPECTED_BASE}")


def check_sitemap() -> None:
    sitemap_path = SITE_DIR / "sitemap.xml"
    root = ElementTree.parse(sitemap_path).getroot()
    namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locations = [node.text or "" for node in root.findall("sm:url/sm:loc", namespace)]
    if not locations:
        fail("Sitemap contains no URL locations")
    invalid = [url for url in locations if not url.startswith(EXPECTED_BASE)]
    if invalid:
        fail("Sitemap contains URLs outside the project path: " + ", ".join(invalid[:10]))


def check_all_generated_urls() -> None:
    invalid: list[tuple[str, str]] = []
    for path in SITE_DIR.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".html", ".xml", ".txt", ".js", ".json"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for url in URL_PATTERN.findall(text):
            if url.startswith(HOST_BASE) and not url.startswith(EXPECTED_BASE):
                invalid.append((str(path), url))
    if invalid:
        details = "; ".join(f"{path}: {url}" for path, url in invalid[:10])
        fail("Generated site contains root-domain URLs outside /SigGear-product-docs/: " + details)


def main() -> None:
    if not SITE_DIR.is_dir():
        fail("Build directory 'site' does not exist")
    check_required_files()
    check_home_canonical()
    check_sitemap()
    check_all_generated_urls()
    print("Site URL validation passed.")


if __name__ == "__main__":
    main()
