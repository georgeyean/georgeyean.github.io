#!/usr/bin/env python3
"""
Exports items from georgeyean's Zotero library into papers.json for
view.html to load statically (no live Zotero API calls per visitor). Re-run
this whenever the Zotero library changes:

    python3 scripts/export_zotero.py

The library is private, so this needs a Zotero API key (read access) to
authenticate. Put it in a file named `.zotero_api_key` next to this repo's
root (same directory as this script's parent) — that file is git-ignored
and must never be committed, since it grants read access to the whole
private library. Generate one at zotero.org -> Settings -> Security.

Scope: every top-level item in the whole personal library (items/top —
excludes child notes/attachments), including items without an abstract.
Each item is tagged with a "group" name used for the feed's Group dropdown:
its top-level ("first level") collection ancestor, EXCEPT when that
top-level ancestor is "Zotero Library" — that one folder is broad enough
that we instead use the collection one level below it (e.g. "Globalization",
"Trade Imbalance") so it isn't one giant undifferentiated group. Items
filed with no deeper nesting directly under "Zotero Library" (or in no
collection at all) fall back to "Zotero Library" / "My Library".

For items with no abstractNote in Zotero's metadata, this also tries to
recover a REAL abstract from the attached PDF's Zotero-indexed full text
(the /fulltext endpoint) — many PDFs have an actual "Abstract" section on
the page that was just never copied into the metadata field. This is only
ever a real excerpt of the paper's own text, never a generated summary:
Claude does not fabricate summaries of papers it hasn't read. Items with
no indexed full text, or no recognizable Abstract section within it,
simply keep abstract: "" and the page shows "No abstract available."
Recovered abstracts are flagged via a "source" field ("pdf" for text
extracted here, "web" for ones a separate web-search pass merged in via
merge_web_abstracts.py, "" for normal Zotero metadata) so the UI can (and
does) disclose that provenance rather than presenting them as Zotero
metadata.
"""

import json
import re
import time
import urllib.request
from pathlib import Path
from urllib.error import HTTPError, URLError

ZOTERO_USER_ID = "10447698"
API = f"https://api.zotero.org/users/{ZOTERO_USER_ID}"
OUT_PATH = Path(__file__).resolve().parent.parent / "papers.json"
API_KEY_PATH = Path(__file__).resolve().parent.parent / ".zotero_api_key"
PAGE_SIZE = 100
FULLTEXT_DELAY_SECONDS = 0.4  # be polite; Zotero throttles hard on repeated 404s


def load_api_key():
    if not API_KEY_PATH.exists():
        raise SystemExit(
            f"Missing {API_KEY_PATH.name} — the library is private now, so this "
            f"script needs a Zotero API key (read access) to authenticate. "
            f"Generate one at zotero.org -> Settings -> Security, and save it "
            f"(just the key, no quotes/newline needed) to {API_KEY_PATH}."
        )
    return API_KEY_PATH.read_text().strip()


API_KEY = load_api_key()
AUTH_HEADERS = {"Zotero-API-Key": API_KEY}
ABSTRACT_STOP = re.compile(
    r"\n\s*\n|\bkeywords?\b\s*[:.]|\bjel\b\s*(classification|codes|no)?\s*[:.]?|"
    r"\b1\.?\s+introduction\b|\bI\.\s+introduction\b",
    re.IGNORECASE,
)
ABSTRACT_HEADING = re.compile(r"\babstract\b\s*[:.\n]?\s*", re.IGNORECASE)


class RateLimited(Exception):
    def __init__(self, retry_after):
        self.retry_after = retry_after


def fetch_fulltext_abstract(item_key):
    """Best-effort recovery of a real abstract from Zotero's indexed PDF text.
    Returns "" if there's no indexed text or no recognizable Abstract section —
    never fabricates anything. Raises RateLimited on a 429 so the caller can
    stop immediately instead of digging the hole deeper."""
    time.sleep(FULLTEXT_DELAY_SECONDS)
    try:
        req = urllib.request.Request(f"{API}/items/{item_key}/fulltext", headers=AUTH_HEADERS)
        with urllib.request.urlopen(req, timeout=8) as r:
            content = json.load(r).get("content", "") or ""
    except HTTPError as e:
        if e.code == 429:
            raise RateLimited(int(e.headers.get("Retry-After", 300)))
        return ""
    except (URLError, TimeoutError, json.JSONDecodeError):
        return ""

    heading = ABSTRACT_HEADING.search(content)
    if not heading:
        return ""
    rest = content[heading.end():heading.end() + 4000]
    stop = ABSTRACT_STOP.search(rest)
    excerpt = rest[: stop.start() if stop else 2000]
    excerpt = re.sub(r"\s+", " ", excerpt).strip()
    return excerpt if len(excerpt) >= 100 else ""  # too short = probably a false match


def fetch_json(url):
    req = urllib.request.Request(url, headers=AUTH_HEADERS)
    with urllib.request.urlopen(req) as r:
        return json.load(r)


def fetch_all_pages(path):
    """GETs every page of a Zotero list endpoint (limit/start pagination)."""
    results = []
    start = 0
    while True:
        sep = "&" if "?" in path else "?"
        page = fetch_json(f"{API}{path}{sep}format=json&limit={PAGE_SIZE}&start={start}")
        results.extend(page)
        if len(page) < PAGE_SIZE:
            return results
        start += PAGE_SIZE


def pretty_folder_name(name):
    name = name.replace("_", " ")
    return re.sub(r"\b\w", lambda m: m.group(0).upper(), name)


def best_link(data, alt_href):
    # Always point at the item's own Zotero page (zotero.org/georgeyean/items/...),
    # not the public DOI/URL — the library is private, so this page (and the PDF
    # attachment on it) only actually opens for someone logged in as the owner.
    # Anyone else hits Zotero's own login wall, which is the whole point.
    return alt_href or (f"https://doi.org/{data['DOI']}" if data.get("DOI") else data.get("url", ""))


def build_group_map(collections):
    """Maps every collection key -> the group name a card filed there should use."""
    by_key = {c["data"]["key"]: c["data"] for c in collections}

    def ancestor_path(key):
        """[key, parent, grandparent, ..., top-level root]"""
        path, cur, seen = [key], key, {key}
        while True:
            parent = by_key[cur].get("parentCollection")
            if not parent or parent not in by_key or parent in seen:
                return path
            path.append(parent)
            seen.add(parent)
            cur = parent

    group_map = {}
    for key in by_key:
        path = ancestor_path(key)
        root_name = by_key[path[-1]]["name"].strip().lower()
        if root_name == "zotero library" and len(path) >= 2:
            group_key = path[-2]  # one level below "Zotero Library"
        else:
            group_key = path[-1]  # first-level ancestor, as normal
        group_map[key] = pretty_folder_name(by_key[group_key]["name"])

    return group_map


def load_cache():
    """Previous run's output, keyed by Zotero item key, so re-running doesn't
    re-fetch fulltext for items we already resolved (recovered or confirmed
    unrecoverable)."""
    if not OUT_PATH.exists():
        return {}
    try:
        existing = json.loads(OUT_PATH.read_text())
        return {p["key"]: p for p in existing if "key" in p}
    except (json.JSONDecodeError, KeyError):
        return {}


def main():
    collections = fetch_all_pages("/collections")
    group_map = build_group_map(collections)

    items = fetch_all_pages("/items/top")
    cache = load_cache()

    missing = [it for it in items if not (it["data"].get("abstractNote") or "").strip()]
    print(f"{len(missing)} of {len(items)} items have no abstract in Zotero; "
          f"checking each one's indexed PDF text for a real Abstract section "
          f"(skipping ones with no attachments at all, and ones already resolved by a previous run)...")

    papers = []
    recovered_count = 0
    checked_count = 0
    rate_limited = False

    for n, it in enumerate(items, 1):
        data = it["data"]
        key = it["key"]
        creator_summary = it.get("meta", {}).get("creatorSummary", "")
        year_match = re.search(r"\b(1[5-9]\d{2}|20\d{2})\b", data.get("date") or "")
        year = year_match.group(0) if year_match else ""
        subtitle = " · ".join(p for p in [creator_summary, year] if p)
        alt_href = it.get("links", {}).get("alternate", {}).get("href", "")
        journal = data.get("publicationTitle") or data.get("bookTitle") or data.get("proceedingsTitle") or ""

        item_collections = data.get("collections") or []
        group = group_map.get(item_collections[0], "My Library") if item_collections else "My Library"

        abstract = (data.get("abstractNote") or "").strip()
        source = ""

        if not abstract and not rate_limited:
            cached = cache.get(key)
            already_resolved = cached and (cached.get("source") in ("pdf", "web") or it.get("meta", {}).get("numChildren", 0) == 0)
            if already_resolved:
                # Already resolved last run (recovered by some method, or confirmed no attachment)
                abstract = cached.get("abstract", "")
                source = cached.get("source", "")
            elif it.get("meta", {}).get("numChildren", 0) > 0:
                checked_count += 1
                try:
                    abstract = fetch_fulltext_abstract(key)
                    source = "pdf" if abstract else ""
                except RateLimited as e:
                    rate_limited = True
                    print(f"\nRate-limited by Zotero after checking {checked_count} items "
                          f"({recovered_count} recovered). Retry-After: {e.retry_after}s "
                          f"(~{e.retry_after // 60} min). Stopping fulltext lookups for this run — "
                          f"everything else is still written out, and re-running later will only "
                          f"check items not yet resolved.")
                    abstract = cached.get("abstract", "") if cached else ""
                    source = cached.get("source", "") if cached else ""
            if source:
                recovered_count += 1
            if checked_count and checked_count % 50 == 0:
                print(f"  ...{checked_count} fulltext lookups made, {recovered_count} recovered so far")

        papers.append({
            "key": key,
            "title": data.get("title") or "Untitled",
            "subtitle": subtitle,
            "journal": journal,
            "abstract": abstract,
            "source": source,
            "link": best_link(data, alt_href),
            "group": group,
        })

    OUT_PATH.write_text(json.dumps(papers, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote {len(papers)} papers to {OUT_PATH}")
    print(f"Recovered {recovered_count} real abstracts from indexed PDF text "
          f"(out of {len(missing)} that had none in Zotero's metadata; "
          f"{checked_count} fulltext lookups actually made this run)")
    if rate_limited:
        print("Run again later to keep resolving the remaining items.")


if __name__ == "__main__":
    main()
