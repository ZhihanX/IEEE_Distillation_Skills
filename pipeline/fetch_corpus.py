#!/usr/bin/env python3
"""Build the candidate corpus from Crossref.

For each target journal, list journal articles published in [--from-year,
--to-year], sorted by Crossref citation count, and keep those with at least
--min-cites citations. Crossref only counts citations from Crossref-registered
references, so its numbers run lower than Google Scholar's: a threshold of 50
here is stricter than 50 on Scholar.

Output: CSV with one row per paper, including citations per year and a
survey/tutorial flag (surveys are distilled separately from research articles).
"""
import argparse
import csv
import json
import re
import sys
import time
import urllib.parse
import urllib.request

JOURNALS = {
    "TWC": ("IEEE Transactions on Wireless Communications", "1536-1276"),
    "JSAC": ("IEEE Journal on Selected Areas in Communications", "0733-8716"),
    "TCOM": ("IEEE Transactions on Communications", "0090-6778"),
}

SURVEY_RE = re.compile(
    r"\b(survey|tutorial|overview|review|primer|roadmap|vision|perspective|"
    r"what will|road to|road ahead|a look at|state of the art|state-of-the-art|state of research|"
    r"how it works|research directions|future directions|opportunities|lessons learned|fundamentals)\b",
    re.I,
)
# Front matter and editorials that Crossref types as journal-article.
SKIP_RE = re.compile(
    r"^(guest editorial|editorial|introduction to the special|corrections? to|"
    r"erratum|comments? on|reply to|ieee .* information|table of contents|"
    r"special issue|call for papers)",
    re.I,
)


def get(url, retries=5):
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "ieee-distillation-skills/0.1"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except Exception as e:  # noqa: BLE001 - network retries
            wait = 2 ** (attempt + 1)
            print(f"  retry {attempt + 1} after {e!r}; sleeping {wait}s", file=sys.stderr)
            time.sleep(wait)
    raise RuntimeError(f"failed: {url}")


def pub_date(item):
    for key in ("published-print", "issued", "published", "published-online"):
        parts = (item.get(key) or {}).get("date-parts") or [[None]]
        if parts[0] and parts[0][0]:
            y = parts[0][0]
            m = parts[0][1] if len(parts[0]) > 1 else 6
            return y, m
    return None, None


def fetch_journal(code, issn, y0, y1, min_cites, now):
    name = JOURNALS[code][0]
    rows, cursor = [], "*"
    flt = f"type:journal-article,from-pub-date:{y0}-01-01,until-pub-date:{y1}-12-31"
    while True:
        q = urllib.parse.urlencode({
            "filter": flt,
            "sort": "is-referenced-by-count",
            "order": "desc",
            "rows": 500,
            "cursor": cursor,
            "select": "DOI,title,is-referenced-by-count,published-print,published-online,issued,published,author,page,volume,issue,subject",
        })
        data = get(f"https://api.crossref.org/journals/{issn}/works?{q}")["message"]
        items = data.get("items", [])
        if not items:
            break
        stop = False
        for it in items:
            cites = it.get("is-referenced-by-count", 0)
            if cites < min_cites:
                stop = True
                break
            title = " ".join((it.get("title") or [""])[0].split())
            if not title or SKIP_RE.search(title):
                continue
            y, m = pub_date(it)
            if y is None:
                continue
            age = max(1.0, now - (y + (m - 0.5) / 12))
            authors = it.get("author") or []
            rows.append({
                "journal": code,
                "doi": it["DOI"].lower(),
                "title": title,
                "year": y,
                "month": m,
                "cites": cites,
                "cites_per_year": round(cites / age, 1),
                "is_survey": int(bool(SURVEY_RE.search(title))),
                "n_authors": len(authors),
                "first_author": (authors[0].get("family", "") if authors else ""),
                "journal_name": name,
            })
        print(f"  {code}: {len(rows)} kept so far", file=sys.stderr)
        if stop:
            break
        cursor = data.get("next-cursor")
        if not cursor:
            break
        time.sleep(1)
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--journals", default="TWC,JSAC,TCOM")
    ap.add_argument("--from-year", type=int, default=2016)
    ap.add_argument("--to-year", type=int, default=2025)
    ap.add_argument("--min-cites", type=int, default=50)
    ap.add_argument("--now", type=float, default=2026.8, help="fractional year used for citation age")
    ap.add_argument("--out", default="corpus/candidates.csv")
    args = ap.parse_args()

    all_rows = []
    for code in args.journals.split(","):
        code = code.strip().upper()
        print(f"fetching {code}", file=sys.stderr)
        all_rows += fetch_journal(code, JOURNALS[code][1], args.from_year, args.to_year,
                                  args.min_cites, args.now)
    seen, uniq = set(), []
    for r in all_rows:
        if r["doi"] not in seen:
            seen.add(r["doi"])
            uniq.append(r)
    uniq.sort(key=lambda r: (r["journal"], -r["cites_per_year"]))
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(uniq[0].keys()))
        w.writeheader()
        w.writerows(uniq)
    print(f"wrote {len(uniq)} rows to {args.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
