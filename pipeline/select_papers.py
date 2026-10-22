#!/usr/bin/env python3
"""Pick the papers to distill into cards.

Per journal, research articles are ranked by citations per year inside each
publication-year band (2016-18 / 2019-21 / 2022-25) and taken round-robin
across bands, so a partial batch still covers every band. A paper is skipped
when its primary topic already fills --topic-cap of the journal's research
quota, so a hot topic (RIS) cannot dominate. Surveys, tutorials and overview
articles form their own stream.

Crossref's `is_survey` flag comes from a title regex that misses many invited
overviews (JSAC special issues) and catches research titles ending in
"A ... Perspective"; `overview_title()` below is the refined test. An arXiv
abstract, when one has been matched, can still overrule it (see
`overview_abstract()`), and the card's `article_type` is the final word.

Output: corpus/selected.csv in selection order.
"""
import argparse
import csv
import json
import math
import os
import re

BANDS = [(2016, 2018), (2019, 2021), (2022, 2025)]

# Ordered: the first matching topic is the primary one; all matches go to `tags`.
TOPICS = [
    ("RIS", r"reconfigurable intelligent surface|intelligent reflecting surface|\bRIS\b|\bIRS\b|"
            r"metasurface|\bSTARS?\b|holographic (reconfigurable )?surface|reflecting surface|-RIS\b|-IRS\b"),
    ("movable-fluid-antenna", r"movable[- ]antenna|fluid antenna|pinching|flexible[- ]antenna|\bFAS\b"),
    ("semantic", r"semantic|task-oriented|source-channel coding|\bJSCC\b|beyond transmitting bits"),
    ("federated-edge-learning", r"federated|edge learning|split learning|distributed learning|"
            r"over-the-air computation|edge ai\b|edge artificial intelligence|edge inference"),
    ("ISAC-sensing", r"sensing|radar|\bISAC\b|localization|target detection|direction-of-arrival"),
    ("UAV", r"\bUAVs?\b|unmanned aerial|aerial vehicle|drone|aerial-ground|low-altitude"),
    ("MEC-offloading", r"edge computing|offloading|\bMEC\b|fog|computation rate"),
    ("cell-free-massive-MIMO", r"cell-free|massive mimo|extremely large|\bXL-MIMO\b|large antenna array|holographic mimo"),
    ("near-field", r"near-field|beam focusing|beamfocusing"),
    ("NOMA-RSMA-access", r"\bNOMA\b|non-orthogonal|rate-splitting|\bRSMA\b|multiple access|massive access|random access"),
    ("SWIPT-WPT", r"wireless power|\bSWIPT\b|energy harvesting|wireless-powered|wireless powered|"
            r"information and power transfer|backscatter"),
    ("security", r"secure|secrecy|security|covert|eavesdrop|jamming|authentication|privacy"),
    ("satellite-NTN", r"satellite|\bLEO\b|space-air-ground|\bHAP\b|non-terrestrial|\bSAGIN"),
    ("mmWave-THz", r"millimeter|mmwave|terahertz|\bTHz\b|hybrid (analog|precoding|beamforming)"),
    ("waveform-modulation", r"\bOTFS\b|\bAFDM\b|affine frequency|\bOFDM|index modulation|modulation|"
            r"waveform|orthogonal time frequency"),
    ("learning-for-wireless", r"deep learning|neural|reinforcement learning|learning-based|\bDRL\b|"
            r"machine learning|generative|large language model|\bLLM"),
    ("vehicular", r"vehicular|\bV2X\b|vehicle"),
    ("URLLC-AoI", r"\bURLLC\b|ultra-reliable|low-latency|age of information"),
    ("channel-estimation", r"channel estimation|\bCSI\b|channel state"),
    ("caching-D2D", r"caching|cache|device-to-device|\bD2D\b"),
]
TOPICS = [(name, re.compile(rx, re.I)) for name, rx in TOPICS]

OVERVIEW_TITLE = re.compile(
    r"\b(survey|tutorial|overview|review|primer|roadmap|vision|"
    r"what will|road to|road ahead|a look at|state of the art|state-of-the-art|state of research|"
    r"how it works|research directions|future directions|opportunities|lessons learned|^fundamentals of [^:]*:|"
    r"recent progress|recent advances|future challenges|future trends|challenges ahead|design challenges|"
    r"past, present|enablers|key technologies|basics|myths|"
    r"toward dual-functional|for future mobile networks|evolution of|"
    r"prospective|next generation advanced|era of)\b",
    re.I,
)
# Research titles that the patterns above would otherwise catch.
NOT_OVERVIEW_TITLE = re.compile(r"long-term perspective|optimization perspective|many-agent perspective|"
                                r"computer vision", re.I)

OVERVIEW_ABSTRACT = re.compile(
    r"\b(this (article|paper|tutorial|survey) (provides|presents|offers|gives) (a |an )?"
    r"(comprehensive |brief |systematic |holistic )?(overview|survey|tutorial|review)|"
    r"we (provide|present|give|offer) (a |an )?(comprehensive |brief |systematic |holistic )?"
    r"(overview|survey|tutorial|review)|"
    r"in this (article|paper|survey|tutorial), we (survey|review|overview)|"
    r"this (survey|tutorial|overview|review))\b",
    re.I,
)


def topics(title):
    tags = [name for name, rx in TOPICS if rx.search(title)]
    return (tags[0] if tags else "other"), tags


def overview_title(title):
    return bool(OVERVIEW_TITLE.search(title)) and not NOT_OVERVIEW_TITLE.search(title)


def overview_abstract(abstract):
    return bool(abstract) and bool(OVERVIEW_ABSTRACT.search(abstract))


def band(year):
    for lo, hi in BANDS:
        if lo <= year <= hi:
            return f"{lo}-{hi}"
    return None


def load_abstracts(path):
    out = {}
    if path and os.path.exists(path):
        for line in open(path, encoding="utf-8"):
            rec = json.loads(line)
            if rec.get("arxiv_abstract"):
                out[rec["doi"]] = rec["arxiv_abstract"]
    return out


def select(rows, per_band, surveys_per_journal, topic_cap, abstracts):
    picked = []
    for j in sorted({r["journal"] for r in rows}):
        js = [r for r in rows if r["journal"] == j]
        for r in js:
            r["primary_topic"], tags = topics(r["title"])
            r["tags"] = ";".join(tags)
            r["band"] = band(int(r["year"]))
            r["kind"] = "overview" if (overview_title(r["title"]) or
                                       overview_abstract(abstracts.get(r["doi"]))) else "research"
        quota = per_band * len(BANDS)
        cap = max(1, math.floor(topic_cap * quota))
        by_cpy = lambda r: -float(r["cites_per_year"])
        streams = [sorted((r for r in js if r["kind"] == "research" and r["band"] == f"{lo}-{hi}"), key=by_cpy)
                   for lo, hi in BANDS]
        taken = [0] * len(BANDS)
        per_topic = {}
        pos = [0] * len(BANDS)
        out = []
        while any(t < per_band and p < len(s) for t, p, s in zip(taken, pos, streams)):
            for b, s in enumerate(streams):
                while taken[b] < per_band and pos[b] < len(s):
                    r = s[pos[b]]
                    pos[b] += 1
                    if per_topic.get(r["primary_topic"], 0) >= cap:
                        continue
                    per_topic[r["primary_topic"]] = per_topic.get(r["primary_topic"], 0) + 1
                    taken[b] += 1
                    r["rank_in_band"] = taken[b]
                    out.append(r)
                    break
        surveys = sorted((r for r in js if r["kind"] == "overview"), key=by_cpy)[:surveys_per_journal]
        for i, r in enumerate(surveys, 1):
            r["rank_in_band"] = i
        picked += out + surveys
    return picked


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--candidates", default="corpus/candidates.csv")
    ap.add_argument("--abstracts", default="corpus/arxiv_matches.jsonl",
                    help="arXiv match file; its abstracts refine the overview test")
    ap.add_argument("--per-band", type=int, default=8)
    ap.add_argument("--surveys-per-journal", type=int, default=3)
    ap.add_argument("--topic-cap", type=float, default=0.25)
    ap.add_argument("--exclude", default="", help="comma-separated DOIs to drop (e.g. no full text)")
    ap.add_argument("--out", default="corpus/selected.csv")
    args = ap.parse_args()

    rows = list(csv.DictReader(open(args.candidates, encoding="utf-8")))
    drop = {d.strip().lower() for d in args.exclude.split(",") if d.strip()}
    rows = [r for r in rows if r["doi"] not in drop]
    picked = select(rows, args.per_band, args.surveys_per_journal, args.topic_cap,
                    load_abstracts(args.abstracts))
    cols = ["journal", "kind", "band", "rank_in_band", "doi", "title", "year", "cites", "cites_per_year",
            "primary_topic", "tags", "first_author"]
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(picked)
    print(f"wrote {len(picked)} rows to {args.out}")


if __name__ == "__main__":
    main()
