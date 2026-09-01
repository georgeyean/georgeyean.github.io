#!/usr/bin/env python3
"""
For papers.json entries tagged "source": "web" — meaning their abstract was
synthesized from web-search snippets rather than lifted verbatim from the
paper itself — this tries to find and substitute the REAL, VERBATIM published
abstract, using OpenAI's web-search-enabled Responses API.

Run after scripts/export_zotero.py (and optionally after
scripts/enrich_with_openai.py):

    python3 scripts/fetch_real_abstracts.py

Needs OPENAI_API_KEY set in the environment.

WHY THIS EXISTS
----------------
A synthesized summary (however careful) is not the paper's own words. Many of
these entries are real, well-indexed journal articles/working papers whose
actual abstract is publicly available (publisher page, NBER, SSRN, etc.) —
there's no reason to keep a paraphrase once the real text can be found. This
script only ever REPLACES a synthesized abstract with the paper's own
published abstract; it never touches papers whose abstract already came from
Zotero natively (source == "") or from the PDF's own indexed text
(source == "pdf") — those are already the paper's real text.

Because the journal/author/year for these entries have already been
independently verified (that's how they got their "source": "web" abstract
and non-empty journal field in the first place), this script's job is
narrower and lower-risk than scripts/enrich_with_openai.py: it isn't trying
to identify WHICH paper this is, only to fetch that already-identified
paper's own abstract text. It's still told explicitly not to guess: if it
can't find the actual published abstract (as opposed to a summary of it), it
reports CANNOT_FIND and the existing synthesized text is left in place
rather than being replaced with another paraphrase.

Like enrich_with_openai.py, this reloads papers.json fresh right before
writing and merges its findings in by key, so it can never clobber edits
made elsewhere while it was running.
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
# NOTE: an earlier version of this script gated replacement on a raw
# character-overlap ratio between the old paraphrase and the new candidate
# abstract, on the theory that a wildly different-looking result might mean
# the model found a DIFFERENT paper's abstract. In practice this was a false
# signal: a real academic abstract is written in completely different prose
# than any paraphrase of it, even for a perfectly correct match, so nearly
# every correct replacement scored "low overlap" too (manually verified
# against a batch of 147 flagged candidates -- every single one was in fact
# the right paper, just phrased differently). The real defense against a
# wrong-paper match is the strict system prompt above (identity already
# verified, only fetch that exact paper's own text, say CANNOT_FIND rather
# than substitute a different paper) -- not a text-similarity heuristic.

SYSTEM_INSTRUCTIONS = (
    "You are helping replace paraphrased paper summaries with the paper's own "
    "real, verbatim published abstract. You will be given a paper's title, "
    "author(s), year, and publication venue — these have already been "
    "verified, so do not second-guess the paper's identity. Your only job is "
    "to search the web (publisher page, NBER, SSRN, JSTOR, Google Scholar, "
    "the authors' own site, etc.) and find that specific paper's own "
    "published abstract, exactly as written by the authors — not a "
    "paraphrase, not a review, not someone else's summary of it. "
    "\n\n"
    "If you find the actual abstract text, respond with ONLY that abstract "
    "text, copied as exactly as you can reproduce it (minor whitespace "
    "normalization is fine). Do not add commentary, quotation marks, or a "
    "citation. If you cannot find the paper's own real abstract text — only "
    "secondary summaries, or nothing at all — respond with exactly the "
    "single word CANNOT_FIND and nothing else. Do not fabricate or "
    "reconstruct an abstract from a summary; only ever return the paper's "
    "actual published abstract."
)


def load_papers():
    return json.loads(PAPERS_PATH.read_text())


def build_query(paper):
    parts = [f"Title: {paper['title']!r}"]
    if paper.get("subtitle"):
        parts.append(f"Author/year: {paper['subtitle']}")
    if paper.get("journal"):
        parts.append(f"Publication venue: {paper['journal']}")
    parts.append(f"Currently-recorded (paraphrased, to be replaced) summary: {paper.get('abstract', '')}")
    return "\n".join(parts)


def fetch_one(client, paper):
    resp = client.responses.create(
        model=MODEL,
        tools=[{"type": "web_search_preview"}],
        instructions=SYSTEM_INSTRUCTIONS,
        input=build_query(paper),
    )
    text = (resp.output_text or "").strip()
    if not text or text == "CANNOT_FIND":
        return None
    # Sanity guards against obviously-bad output.
    if len(text) < 80 or len(text) > 4000:
        return None
    return text


def main():
    if "OPENAI_API_KEY" not in os.environ:
        sys.exit("OPENAI_API_KEY is not set in the environment.")

    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    papers = load_papers()
    targets = [p for p in papers if p.get("source") == "web" and (p.get("abstract") or "").strip()]

    print(f"{len(targets)} papers have a synthesized ('web') abstract to try to replace with the real one.")
    if not targets:
        return

    results = {}  # key -> real abstract text
    for i, paper in enumerate(targets, 1):
        print(f"[{i}/{len(targets)}] {paper['title'][:70]!r} ({paper['key']})...", end=" ", flush=True)
        time.sleep(REQUEST_DELAY_SECONDS)
        try:
            real_abstract = fetch_one(client, paper)
        except Exception as e:  # noqa: BLE001 - best-effort script, keep going
            print(f"error: {e}")
            continue

        if not real_abstract:
            print("cannot find real abstract, keeping paraphrase")
            continue

        results[paper["key"]] = real_abstract
        print(f"found real abstract ({len(real_abstract)} chars)")

    if not results:
        print("\nNo replacements found; papers.json left untouched.")
        return

    current = load_papers()
    replaced = 0
    for p in current:
        if p["key"] in results:
            p["abstract"] = results[p["key"]]
            replaced += 1

    PAPERS_PATH.write_text(json.dumps(current, indent=2, ensure_ascii=False) + "\n")
    print(f"\nReplaced {replaced} synthesized abstracts with real published ones. Wrote {PAPERS_PATH}")


if __name__ == "__main__":
    main()
