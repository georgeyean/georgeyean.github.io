#!/usr/bin/env python3
"""
Exports abstract-bearing items from georgeyean's public Zotero library into
papers.json for view.html to load statically (no live Zotero API calls per
visitor). Re-run this whenever the Zotero library changes:

    python3 scripts/export_zotero.py

Scope matches view.html's original design: every top-level ("first level")
collection, using only each collection's own top-level items (items/top —
excludes child notes/attachments and items filed only in sub-collections),
keeping items that have a non-empty abstract.
"""

import json
import re
import urllib.request
from pathlib import Path

ZOTERO_USER_ID = "10447698"
API = f"https://api.zotero.org/users/{ZOTERO_USER_ID}"
OUT_PATH = Path(__file__).resolve().parent.parent / "papers.json"


def fetch_json(url):
    with urllib.request.urlopen(url) as r:
        return json.load(r)


def pretty_folder_name(name):
    name = name.replace("_", " ")
    return re.sub(r"\b\w", lambda m: m.group(0).upper(), name)


def best_link(data, alt_href):
    if data.get("url"):
        return data["url"]
    if data.get("DOI"):
        return f"https://doi.org/{data['DOI']}"
    return alt_href or ""


def main():
    collections = fetch_json(f"{API}/collections/top?format=json&limit=100")

    papers = []
    for col in collections:
        key = col["data"]["key"]
        folder_name = pretty_folder_name(col["data"]["name"])
        items = fetch_json(f"{API}/collections/{key}/items/top?format=json&limit=100")

        for it in items:
            data = it["data"]
            abstract = (data.get("abstractNote") or "").strip()
            if not abstract:
                continue
            creator_summary = it.get("meta", {}).get("creatorSummary", "")
            year_match = re.search(r"\b(1[5-9]\d{2}|20\d{2})\b", data.get("date") or "")
            year = year_match.group(0) if year_match else ""
            subtitle = " · ".join(p for p in [creator_summary, year] if p)
            alt_href = it.get("links", {}).get("alternate", {}).get("href", "")
            papers.append({
                "title": data.get("title") or "Untitled",
                "subtitle": subtitle,
                "abstract": abstract,
                "link": best_link(data, alt_href),
                "kicker": folder_name,
            })

    OUT_PATH.write_text(json.dumps(papers, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote {len(papers)} papers to {OUT_PATH}")


if __name__ == "__main__":
    main()
