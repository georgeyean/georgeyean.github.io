#!/usr/bin/env python3
"""
Merges web-search-recovered abstracts into papers.json.

Usage:
    python3 scripts/merge_web_abstracts.py <results_dir>

<results_dir> should contain one or more JSON files, each an array of
{"key": "<zotero item key>", "abstract": "<verbatim text>", "source_url": "..."}
— the output format used by the web-search agents that look up real
published abstracts for items with nothing in Zotero (and no recoverable
PDF full text). Only fills in items that currently have an empty abstract
in papers.json; never overwrites an existing one.
"""

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PAPERS_PATH = REPO_ROOT / "papers.json"


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/merge_web_abstracts.py <results_dir>")
        sys.exit(1)

    results_dir = Path(sys.argv[1])
    result_files = sorted(results_dir.glob("*.json"))
    if not result_files:
        print(f"No .json files found in {results_dir}")
        sys.exit(1)

    found = {}
    for f in result_files:
        try:
            entries = json.loads(f.read_text())
        except json.JSONDecodeError:
            print(f"  skipping {f.name}: invalid JSON")
            continue
        for entry in entries:
            key = entry.get("key")
            abstract = (entry.get("abstract") or "").strip()
            if key and abstract:
                found[key] = {"abstract": abstract, "source_url": entry.get("source_url", "")}
        print(f"  {f.name}: {len(entries)} entries")

    print(f"Total unique items found across all result files: {len(found)}")

    papers = json.loads(PAPERS_PATH.read_text())
    merged = 0
    for p in papers:
        if not p.get("abstract") and p.get("key") in found:
            p["abstract"] = found[p["key"]]["abstract"]
            p["source"] = "web"
            merged += 1

    PAPERS_PATH.write_text(json.dumps(papers, indent=2, ensure_ascii=False) + "\n")
    print(f"Merged {merged} web-found abstracts into {PAPERS_PATH}")

    still_missing = sum(1 for p in papers if not p.get("abstract"))
    print(f"{still_missing} items still have no abstract after merge")


if __name__ == "__main__":
    main()
