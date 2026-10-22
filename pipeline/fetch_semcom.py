#!/usr/bin/env python3
"""Build the semantic-communication / JSCC candidate pool from Crossref.

Same approach as fetch_corpus.py (citation-sorted Crossref listing per journal),
but with a lower citation threshold, three more journals that host the
foundational deep-JSCC and semantic-communication papers (TCCN, TSP, JSAIT), and
a topic filter on the title or the abstract.

Outputs:
  corpus/semcom/candidates.csv  - metadata only (no abstracts), safe to commit
  data/semcom_abstracts.jsonl   - Crossref abstracts for local tagging only (gitignored)
"""
import argparse
import csv
import html
import json
import os
import re
import sys
import time
import urllib.parse

sys.path.insert(0, os.path.dirname(__file__))
from fetch_corpus import JOURNALS, SKIP_RE, SURVEY_RE, get, pub_date  # noqa: E402

JOURNALS = dict(JOURNALS)
JOURNALS.update({
    "TCCN": ("IEEE Transactions on Cognitive Communications and Networking", "2332-7731"),
    "TSP": ("IEEE Transactions on Signal Processing", "1053-587X"),
    "JSAIT": ("IEEE Journal on Selected Areas in Information Theory", "2641-8770"),
})

TITLE_RE = re.compile(
    r"semantic|source[- ]channel|\bJSCC\b|task[- ]oriented|goal[- ]oriented|edge inference|"
    r"(image|video|speech|text) (transmission|communication)",
    re.I,
)
ABSTRACT_RE = re.compile(
    r"semantic communication|semantic transmission|joint source[- ]channel coding|\bJSCC\b|"
    r"task[- ]oriented communication|goal[- ]oriented communication",
    re.I,
)
# Title hits that are about something else (vision-aided beam prediction, semantic segmentation, ...).
NEGATIVE_RE = re.compile(r"semantic segmentation|semantic web|ontology", re.I)


def clean_abstract(raw):
    text = re.sub(r"<[^>]+>", " ", raw or "")
    return " ".join(html.unescape(text).split())


def fetch(code, y0, y1, min_cites, now):
    name, issn = JOURNALS[code]
    rows, cursor = [], "*"
    flt = f"type:journal-article,from-pub-date:{y0}-01-01,until-pub-date:{y1}-12-31"
    while True:
        q = urllib.parse.urlencode({
            "filter": flt, "sort": "is-referenced-by-count", "order": "desc", "rows": 500, "cursor": cursor,
            "select": "DOI,title,is-referenced-by-count,published-print,published-online,issued,published,author,abstract",
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
            abstract = clean_abstract(it.get("abstract"))
            by_title = bool(TITLE_RE.search(title)) and not NEGATIVE_RE.search(title)
            by_abstract = bool(ABSTRACT_RE.search(abstract))
            if not (by_title or by_abstract):
                continue
            y, m = pub_date(it)
            if y is None:
                continue
            age = max(1.0, now - (y + (m - 0.5) / 12))
            authors = it.get("author") or []
            rows.append({
                "journal": code, "doi": it["DOI"].lower(), "title": title, "year": y, "month": m,
                "cites": cites, "cites_per_year": round(cites / age, 1),
                "is_survey": int(bool(SURVEY_RE.search(title))),
                "matched_by": "title" if by_title else "abstract",
                "first_author": authors[0].get("family", "") if authors else "",
                "_abstract": abstract,
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
    ap.add_argument("--journals", default="TWC,JSAC,TCOM,TCCN,TSP,JSAIT")
    ap.add_argument("--from-year", type=int, default=2018)
    ap.add_argument("--to-year", type=int, default=2025)
    ap.add_argument("--min-cites", type=int, default=10)
    ap.add_argument("--now", type=float, default=2026.8)
    ap.add_argument("--out", default="corpus/semcom/candidates.csv")
    ap.add_argument("--abstracts-out", default="data/semcom_abstracts.jsonl")
    args = ap.parse_args()

    rows, seen = [], set()
    for code in args.journals.split(","):
        code = code.strip().upper()
        print(f"fetching {code}", file=sys.stderr)
        for r in fetch(code, args.from_year, args.to_year, args.min_cites, args.now):
            if r["doi"] not in seen:
                seen.add(r["doi"])
                rows.append(r)
    rows.sort(key=lambda r: -r["cites_per_year"])

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    os.makedirs(os.path.dirname(args.abstracts_out), exist_ok=True)
    with open(args.abstracts_out, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps({"doi": r["doi"], "abstract": r["_abstract"]}, ensure_ascii=False) + "\n")
    fields = [k for k in rows[0] if not k.startswith("_")]
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {len(rows)} rows to {args.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
