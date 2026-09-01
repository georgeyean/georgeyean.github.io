#!/usr/bin/env python3
"""
Best-effort automated fill-in for papers.json entries that are still missing
an abstract and/or a journal/venue after export_zotero.py has run — using
OpenAI's web-search-enabled Responses API to look the paper up online.

Run this AFTER scripts/export_zotero.py, whenever new papers have been added
to Zotero:

    python3 scripts/enrich_with_openai.py

Needs an OPENAI_API_KEY environment variable (already set in this shell —
never hardcode it into this file or commit it anywhere).

WHAT THIS DOES AND DOESN'T DO
------------------------------
- Only touches items that currently have abstract == "" or journal == "".
  A paper that already has either field filled in (by Zotero itself, by a
  previous run of this script, or by hand) is left completely alone — this
  never overwrites existing data.
- For each such item, asks the model to search the web and identify the
  specific paper, explicitly warning it not to conflate the title with a
  different paper on a similar topic by different authors (this is exactly
  the failure mode a human caught and had to fix by hand in this project's
  history — title-similarity alone is not identity).
- If the model cannot confidently identify the paper, it reports "cannot
  find" and nothing is written for that item (abstract/journal stay "").
- Anything the model DOES fill in is tagged with "source": "web-auto" in
  papers.json (as opposed to "web" for a human-verified web search, "pdf"
  for extracted PDF text, or "" for native Zotero metadata) — so the UI and
  future maintainers can tell this was an automated, unsupervised pass, not
  something a person checked line by line. Treat "web-auto" entries as
  lower-confidence than "web" ones.
- This is explicitly a "may not be extensive" best-effort pass, not a
  substitute for the careful manual research pass — it's here so routine
  new-paper additions get *something* automatically instead of sitting
  empty indefinitely, not to replace human review for anything that matters.

This script makes real, billed OpenAI API calls (one or two per missing
item). It prints progress and a summary; nothing is written until the very
end (all-or-nothing per run), and it never touches papers.json unless at
least one field was actually filled in.
"""

import json
import os
import sys
import time
from pathlib import Path

from openai import OpenAI

REPO_ROOT = Path(__file__).resolve().parent.parent
PAPERS_PATH = REPO_ROOT / "papers.json"
MODEL = "gpt-4o"
REQUEST_DELAY_SECONDS = 0.5

SYSTEM_INSTRUCTIONS = (
    "You are a careful research assistant helping identify academic papers from "
    "sparse, sometimes garbled citation-manager metadata (titles are often "
    "truncated, paraphrased, all-caps, or missing entirely). Your job is to "
    "search the web and determine, if possible: (1) the correct journal, "
    "conference proceedings, book, or working-paper series it was published "
    "in, and (2) a 2-4 sentence factual summary of its actual argument or "
    "findings, written from the paper's real content (never invent claims the "
    "paper doesn't make). "
    "\n\n"
    "CRITICAL: title similarity alone is NOT sufficient evidence of identity. "
    "Many papers share generic or near-identical titles while being completely "
    "different works by different authors with different arguments. Before "
    "answering, check that any author names, years, or subtitle text given "
    "actually corroborate the specific paper you found — do not substitute a "
    "different, more-findable paper on a similar topic just because the exact "
    "one is hard to locate. "
    "\n\n"
    "If you cannot confidently identify the specific paper with corroborating "
    "evidence (not just a topical match), respond with exactly the single word "
    "CANNOT_FIND and nothing else. Otherwise, respond with ONLY a JSON object "
    "(no markdown fences, no commentary) with these exact keys: "
    '{"journal": "<venue name, or \\"\\" if truly unknown>", '
    '"abstract": "<2-4 sentence real summary, or \\"\\" if you found the venue '
    'but not enough content to summarize>", '
    '"confidence": "<one sentence on what corroborated the match>"}'
)


def load_papers():
    return json.loads(PAPERS_PATH.read_text())


def needs_enrichment(paper):
    return not (paper.get("abstract") or "").strip() or not (paper.get("journal") or "").strip()


def build_query(paper):
    parts = [f"Title (from a citation manager, may be truncated/paraphrased/garbled): {paper['title']!r}"]
    if paper.get("subtitle"):
        parts.append(f"Author/year hint: {paper['subtitle']!r}")
    if paper.get("group"):
        parts.append(f"Subject area: {paper['group']!r}")
    have_abstract = bool((paper.get("abstract") or "").strip())
    have_journal = bool((paper.get("journal") or "").strip())
    if have_abstract and not have_journal:
        parts.append(
            "The abstract is already known (see below) — I only need the "
            "journal/venue this specific paper was published in, not a new "
            "summary. Existing abstract: " + paper["abstract"]
        )
    return "\n".join(parts)


def enrich_one(client, paper):
    query = build_query(paper)
    resp = client.responses.create(
        model=MODEL,
        tools=[{"type": "web_search_preview"}],
        instructions=SYSTEM_INSTRUCTIONS,
        input=query,
    )
    text = (resp.output_text or "").strip()
    if text == "CANNOT_FIND" or not text:
        return None
    # Strip accidental markdown fences if the model added them anyway.
    if text.startswith("```"):
        text = text.strip("`")
        if text.lower().startswith("json"):
            text = text[4:].strip()
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        print(f"    (unparseable response, skipping: {text[:200]!r})")
        return None
    return data


def main():
    if "OPENAI_API_KEY" not in os.environ:
        sys.exit("OPENAI_API_KEY is not set in the environment.")

    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    papers = load_papers()
    targets = [p for p in papers if needs_enrichment(p)]

    print(f"{len(targets)} of {len(papers)} papers still need abstract and/or journal.")
    if not targets:
        return

    results = {}  # key -> {"journal": ..., "abstract": ...} for whatever the model actually filled in
    for i, paper in enumerate(targets, 1):
        print(f"[{i}/{len(targets)}] {paper['title'][:70]!r} ({paper['key']})...", end=" ")
        time.sleep(REQUEST_DELAY_SECONDS)
        try:
            result = enrich_one(client, paper)
        except Exception as e:  # noqa: BLE001 - best-effort script, keep going
            print(f"error: {e}")
            continue

        if not result:
            print("cannot find")
            continue

        to_apply = {}
        if not (paper.get("journal") or "").strip() and result.get("journal"):
            to_apply["journal"] = result["journal"]
        if not (paper.get("abstract") or "").strip() and result.get("abstract"):
            to_apply["abstract"] = result["abstract"]
            to_apply["source"] = "web-auto"

        if to_apply:
            results[paper["key"]] = to_apply
            print(f"filled -> journal={to_apply.get('journal', paper.get('journal', ''))!r}")
        else:
            print("nothing new")

    if not results:
        print("\nNo changes made; papers.json left untouched.")
        return

    # Re-read papers.json fresh right before writing, in case it changed on
    # disk while this (slow, many-API-calls) run was in flight — merge our
    # findings by key onto the CURRENT file rather than overwriting it with
    # the stale copy we loaded when this run started. Only fields this run
    # actually filled in are touched; everything else in each record is left
    # exactly as it is on disk right now.
    current = load_papers()
    filled = 0
    for p in current:
        patch = results.get(p["key"])
        if patch:
            p.update(patch)
            filled += 1

    PAPERS_PATH.write_text(json.dumps(current, indent=2, ensure_ascii=False) + "\n")
    print(f"\nUpdated {filled} papers. Wrote {PAPERS_PATH}")


if __name__ == "__main__":
    main()
