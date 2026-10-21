#!/usr/bin/env python3
"""Find arXiv preprints for the highest-priority candidates.

IEEE Xplore blocks scripted access, so full text comes from arXiv. Candidates
are visited in priority order (per journal and publication-year band, by
citations per year; surveys as their own stream), and each is matched by a
title phrase search, falling back to a keyword + first-author search. A match
needs a close title (difflib ratio >= 0.9), or a looser title (>= 0.7) plus the
first author's surname in the arXiv author list.

Results append to a JSONL file so the run can be interrupted and resumed.
arXiv asks for at most one API request every 3 seconds.
"""
import argparse
import csv
import difflib
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ATOM = "{http://www.w3.org/2005/Atom}"
BANDS = [(2016, 2018), (2019, 2021), (2022, 2025)]
STOP = set("a an the of for and in on with via to from by under over toward towards using based its is are".split())
_last = [0.0]


def norm(t):
    t = re.sub(r"\$[^$]*\$", " ", t.lower())
    t = re.sub(r"[^a-z0-9]+", " ", t)
    return " ".join(t.split())


def api(query, max_results=5):
    wait = 3.2 - (time.time() - _last[0])
    if wait > 0:
        time.sleep(wait)
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(
        {"search_query": query, "max_results": max_results})
    for attempt in range(6):
        _last[0] = time.time()
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "ieee-distillation-skills/0.1"})
            with urllib.request.urlopen(req, timeout=90) as r:
                root = ET.fromstring(r.read())
            out = []
            for e in root.findall(f"{ATOM}entry"):
                out.append({
                    "id": e.find(f"{ATOM}id").text.rsplit("/abs/", 1)[-1],
                    "title": " ".join(e.find(f"{ATOM}title").text.split()),
                    "authors": [a.find(f"{ATOM}name").text for a in e.findall(f"{ATOM}author")],
                    "summary": " ".join(e.find(f"{ATOM}summary").text.split()),
                })
            return out
        except Exception as ex:  # noqa: BLE001 - arXiv returns 503s under load
            backoff = 5 * (attempt + 1)
            print(f"  arXiv error {ex!r}; retry in {backoff}s", file=sys.stderr)
            time.sleep(backoff)
    return []


def best_match(row, entries):
    want = norm(row["title"])
    surname = norm(row["first_author"])
    best = None
    for e in entries:
        ratio = difflib.SequenceMatcher(None, want, norm(e["title"])).ratio()
        author_ok = bool(surname) and any(surname in norm(a) for a in e["authors"])
        if ratio >= 0.9 or (ratio >= 0.7 and author_ok):
            score = ratio + (0.05 if author_ok else 0)
            if not best or score > best[0]:
                best = (score, e, ratio, author_ok)
    return best


def find(row):
    phrase = re.sub(r"[^A-Za-z0-9\- ]+", " ", row["title"])
    phrase = " ".join(phrase.split())
    m = best_match(row, api(f'ti:"{phrase}"'))
    if m:
        return m
    words = [w for w in norm(row["title"]).split() if w not in STOP and len(w) > 2][:6]
    if not words:
        return None
    q = " AND ".join(f"ti:{w}" for w in words)
    if row["first_author"]:
        q += f' AND au:{norm(row["first_author"]).split()[-1]}'
    return best_match(row, api(q, max_results=10))


def priority(rows, per_band, surveys_per_journal):
    out = []
    for j in sorted({r["journal"] for r in rows}):
        js = [r for r in rows if r["journal"] == j]
        research = sorted((r for r in js if r["is_survey"] == "0"),
                          key=lambda r: -float(r["cites_per_year"]))
        streams = [[r for r in research if lo <= int(r["year"]) <= hi][:per_band] for lo, hi in BANDS]
        streams.append(sorted((r for r in js if r["is_survey"] == "1"),
                              key=lambda r: -float(r["cites_per_year"]))[:surveys_per_journal])
        # Interleave the streams so a partial run still covers every band.
        for i in range(max(map(len, streams))):
            out += [s[i] for s in streams if i < len(s)]
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--candidates", default="corpus/candidates.csv")
    ap.add_argument("--out", default="corpus/arxiv_matches.jsonl")
    ap.add_argument("--per-band", type=int, default=60)
    ap.add_argument("--surveys-per-journal", type=int, default=15)
    args = ap.parse_args()

    rows = list(csv.DictReader(open(args.candidates)))
    done = set()
    if os.path.exists(args.out):
        done = {json.loads(l)["doi"] for l in open(args.out)}
    todo = [r for r in priority(rows, args.per_band, args.surveys_per_journal) if r["doi"] not in done]
    print(f"{len(done)} already checked, {len(todo)} to go", file=sys.stderr)
    with open(args.out, "a") as f:
        for i, r in enumerate(todo, 1):
            m = find(r)
            rec = {"doi": r["doi"], "journal": r["journal"], "title": r["title"]}
            if m:
                _, e, ratio, author_ok = m
                rec.update(arxiv_id=re.sub(r"v\d+$", "", e["id"]), arxiv_title=e["title"],
                           title_ratio=round(ratio, 3), author_match=author_ok,
                           arxiv_abstract=e["summary"])
            else:
                rec["arxiv_id"] = None
            f.write(json.dumps(rec) + "\n")
            f.flush()
            hit = rec["arxiv_id"] or "-"
            print(f"[{i}/{len(todo)}] {r['journal']} {hit} {r['title'][:70]}", file=sys.stderr)


if __name__ == "__main__":
    main()
