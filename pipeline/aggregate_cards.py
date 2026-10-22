#!/usr/bin/env python3
"""Aggregate the YAML front matter of corpus/cards/*.md into frequency tables.

Research articles and overviews are counted separately. For every coded
field the report gives counts over research papers, then per journal and per
year band, so each rule in the skill can cite "k/n papers". List-valued fields
(solution, gap_type, ...) count papers that contain the value. Numeric fields
get median and interquartile range. Phrase counts report how many papers use a
phrase at least once.

Output: corpus/summary.md (human-readable) and corpus/summary.json.
"""
import argparse
import collections
import glob
import json
import os
import statistics
import sys

import yaml

GROUPS = ["journal", "band"]
JOURNALS = ["TWC", "JSAC", "TCOM"]
BANDS = ["2016-2018", "2019-2021", "2022-2025"]
NUMERIC_AUTO = ["words_total", "n_sections", "n_subsections", "n_figures", "n_tables", "n_display_eq",
                "n_algorithms", "n_appendix", "mean_sentence_words", "we_per_1k", "title_words",
                "abstract_words", "abstract_sentences"]
NUMERIC_CODE = ["intro_paragraphs", "contrib_n", "baselines_n", "conclusion_paragraphs"]
REQUIRED_CODE = [
    "title_pattern", "abstract_moves", "abstract_has_numbers", "abstract_anchor", "intro_paragraphs",
    "intro_moves", "related_work", "contrib_format", "contrib_n", "contrib_verbs", "contrib_quantified",
    "first_claim", "roadmap", "notation", "gap_type", "motivating_figure", "problem_class", "solution",
    "theory_role", "proofs_location", "complexity_analysis", "convergence_analysis", "sim_param_table",
    "baselines_n", "baseline_naming", "x_axes", "fig1_role", "caption_style", "prototype_or_measurement",
    "code_released", "conclusion_paragraphs", "conclusion_has_numbers", "conclusion_future_work",
]


def load(card_dir):
    cards, problems = [], []
    for path in sorted(glob.glob(os.path.join(card_dir, "*.md"))):
        text = open(path, encoding="utf-8").read()
        if not text.startswith("---"):
            problems.append(f"{path}: no front matter")
            continue
        meta = yaml.safe_load(text.split("---", 2)[1])
        meta["_path"] = os.path.basename(path)
        missing = [k for k in REQUIRED_CODE if k not in (meta.get("code") or {})]
        if missing:
            problems.append(f"{path}: missing code fields {missing}")
        cards.append(meta)
    return cards, problems


def iqr(xs):
    xs = sorted(xs)
    if len(xs) < 4:
        return f"{statistics.median(xs):g}" if xs else "-"
    q = statistics.quantiles(xs, n=4)
    return f"{statistics.median(xs):g} [{q[0]:g}–{q[2]:g}]"


def counter(cards, field, source="code"):
    c = collections.Counter()
    for m in cards:
        v = (m.get(source) or {}).get(field)
        if isinstance(v, list):
            for x in set(map(str, v)):
                c[x] += 1
        elif v is not None:
            c[str(v).lower() if isinstance(v, bool) else str(v)] += 1
    return c


def fmt_counter(c, n, top=12):
    return ", ".join(f"{k} {v}/{n}" for k, v in c.most_common(top))


def section(cards, title):
    n = len(cards)
    out = [f"## {title}（n = {n}）", ""]
    if not n:
        return out
    by = {g: {k: [m for m in cards if str(m.get(g)) == k] for k in (JOURNALS if g == "journal" else BANDS)}
          for g in GROUPS}
    out += ["### 数值（中位数 [四分位距]）", "", "| 字段 | 全部 | " + " | ".join(JOURNALS + BANDS) + " |",
            "|---|---|" + "---|" * (len(JOURNALS) + len(BANDS))]
    for src, fields in (("auto", NUMERIC_AUTO), ("code", NUMERIC_CODE)):
        for f in fields:
            vals = lambda cs: [m[src][f] for m in cs if isinstance((m.get(src) or {}).get(f), (int, float))]
            cells = [iqr(vals(cards))] + [iqr(vals(by["journal"][j])) for j in JOURNALS] + \
                    [iqr(vals(by["band"][b])) for b in BANDS]
            out.append(f"| {f} | " + " | ".join(cells) + " |")
    st = collections.Counter()
    for m in cards:
        for k, v in ((m.get("auto") or {}).get("statements") or {}).items():
            if isinstance(v, int) and v > 0 and k != "proof_in_appendix":
                st[k] += 1
    out += ["", f"含定理类陈述的论文数：{fmt_counter(st, n)}", "", "### 编码字段（含该值的论文数 / n）", ""]
    for f in REQUIRED_CODE:
        if f in NUMERIC_CODE:
            continue
        line = f"- **{f}**：{fmt_counter(counter(cards, f), n)}"
        per_j = "; ".join(f"{j}: {fmt_counter(counter(by['journal'][j], f), len(by['journal'][j]), 4)}"
                          for j in JOURNALS if by["journal"][j])
        per_b = "; ".join(f"{b}: {fmt_counter(counter(by['band'][b], f), len(by['band'][b]), 4)}"
                          for b in BANDS if by["band"][b])
        out += [line, f"  - 按期刊：{per_j}", f"  - 按年份段：{per_b}"]
    ph = collections.Counter()
    for m in cards:
        for k, v in ((m.get("auto") or {}).get("phrases") or {}).items():
            if isinstance(v, int) and v > 0:
                ph[k] += 1
    me = collections.Counter()
    for m in cards:
        for k, v in ((m.get("auto") or {}).get("methods") or {}).items():
            if isinstance(v, int) and v > 0:
                me[k] += 1
    out += ["", "### 短语（至少出现一次的论文数）", "", fmt_counter(ph, n, 40), "",
            "### 方法关键词（至少出现一次的论文数）", "", fmt_counter(me, n, 40), ""]
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--cards", default="corpus/cards")
    ap.add_argument("--out", default="corpus/summary")
    args = ap.parse_args()
    cards, problems = load(args.cards)
    for p in problems:
        print("WARN", p, file=sys.stderr)
    research = [m for m in cards if m.get("article_type") == "research"]
    overview = [m for m in cards if m.get("article_type") != "research"]
    lines = ["# 卡片汇总", "", f"卡片 {len(cards)} 张：研究论文 {len(research)}，综述 / 教程 {len(overview)}。",
             "由 `pipeline/aggregate_cards.py` 生成，不要手改。", ""]
    lines += section(research, "研究论文") + section(overview, "综述 / 教程 / 展望")
    open(args.out + ".md", "w", encoding="utf-8").write("\n".join(lines) + "\n")
    json.dump({"research": research, "overview": overview}, open(args.out + ".json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1, default=str)
    print(f"{len(cards)} cards -> {args.out}.md")


if __name__ == "__main__":
    main()
