"""Title-keyword landscape of the semantic-communication candidate pool.

Tags each of the candidates in corpus/semcom/candidates.csv (Crossref, >= 10 cites, 2018-2025,
TWC/JSAC/TCOM/TCCN/TSP/JSAIT) with modality / paradigm / system / technique labels using
regular expressions on the TITLE ONLY (Crossref returned no abstracts), and writes

  corpus/semcom/landscape.csv  one row per paper with its tags
  corpus/semcom/landscape.md   tag counts, a modality x topic occupancy table, per-year counts and the
                               list of titles under every tag (for the novelty check in the
                               semantic-comm-ideas skill)

Title tags miss papers whose titles do not name the topic, so an empty cell means
"no title in this pool mentions it", not "nobody has done it". The skill always pairs this
index with a live literature search.

Usage: python3 pipeline/landscape_semcom.py
"""
import csv
import os
import re
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "corpus", "semcom", "candidates.csv")
OUT_CSV = os.path.join(ROOT, "corpus", "semcom", "landscape.csv")
OUT_MD = os.path.join(ROOT, "corpus", "semcom", "landscape.md")
OUT_SKILL = os.path.join(ROOT, "skills", "semantic-comm-ideas", "references", "landscape.md")

MODALITY = {
    "image": r"\bimages?\b|visual|vision|picture",
    "video": r"\bvideo",
    "text": r"\btext|sentence|language(?! model)",
    "speech/audio": r"speech|audio|voice",
    "point-cloud/3D": r"point cloud|3d|holograph|mesh",
    "multimodal": r"multi-?modal|cross-modal",
    "feature/inference": r"edge inference|feature|co-inference|split",
}
TOPIC = {
    "JSCC": r"source[- ]channel|\bjscc\b|deepjscc",
    "digital/modulation": r"digital|quantiz|constellation|modulation|codebook|discrete|bit-?level|binary|vector quantiz",
    "generative/LLM": r"generative|diffusion|\bgan\b|adversarial network|large language|\bllm|foundation model|gpt|aigc",
    "task/goal-oriented": r"task[- ]oriented|goal[- ]oriented|task[- ]aware|edge inference|classification|retrieval|detection|inference",
    "knowledge": r"knowledge",
    "theory/limits": r"rate[- ]distortion|information[- ]theor|bottleneck|capacity|fundamental|limit|entropy|bound",
    "MIMO": r"mimo|multi-antenna|multiple-input",
    "OFDM": r"ofdm",
    "multi-user/MA": r"multi-?user|multiple access|\bnoma\b|rate[- ]splitting|rsma|broadcast|multi-?device|downlink|uplink",
    "relay/cooperative": r"relay|cooperative",
    "feedback/HARQ": r"feedback|harq|retransmission|arq",
    "RIS": r"reconfigurable intelligent|\bris\b|intelligent reflecting|\birs\b",
    "UAV/vehicular/satellite": r"uav|vehicul|satellite|aerial|v2x",
    "sensing/ISAC": r"sensing|isac|radar",
    "resource allocation": r"resource|allocation|power control|scheduling|bandwidth allocation|energy|optimization",
    "security/privacy": r"secur|privacy|adversarial|eavesdrop|covert|attack|robust",
    "federated/distributed learning": r"federated|distributed learning|split learning",
    "adaptive": r"adaptive|adaptation|agile|variable[- ]length|rate[- ]adaptive|snr[- ]adaptive",
    "reinforcement learning": r"reinforcement|\bdrl\b",
    "transformer/attention": r"transformer|swin|attention",
}


def tags_for(title, table):
    t = title.lower()
    return [k for k, rx in table.items() if re.search(rx, t)]


def main():
    rows = list(csv.DictReader(open(SRC, encoding="utf-8")))
    out = []
    for r in rows:
        m = tags_for(r["title"], MODALITY)
        tp = tags_for(r["title"], TOPIC)
        out.append({**{k: r[k] for k in ["journal", "doi", "title", "year", "cites", "cites_per_year", "is_survey"]},
                    "modality": ";".join(m), "topics": ";".join(tp)})
    with open(OUT_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys()))
        w.writeheader()
        w.writerows(out)

    n = len(out)
    mc, tc = Counter(), Counter()
    occ = defaultdict(Counter)
    by_tag = defaultdict(list)
    years = Counter()
    year_tag = defaultdict(Counter)
    for r in out:
        ms = r["modality"].split(";") if r["modality"] else ["(none in title)"]
        ts = r["topics"].split(";") if r["topics"] else ["(none in title)"]
        years[r["year"]] += 1
        for m in ms:
            mc[m] += 1
            by_tag["modality:" + m].append(r)
            for t in ts:
                occ[m][t] += 1
        for t in ts:
            tc[t] += 1
            by_tag["topic:" + t].append(r)
            year_tag[t][r["year"]] += 1

    L = ["# 语义通信候选论文标题索引（landscape）\n",
         f"自动生成（`python3 pipeline/landscape_semcom.py`）。来源 `corpus/semcom/candidates.csv`：{n} 篇，"
         "TWC / JSAC / TCOM / TCCN / TSP / JSAIT，2018–2025，Crossref 引用 ≥ 10，标题匹配语义通信 / JSCC / 任务导向等关键词。",
         "标签只看标题（Crossref 没有摘要），空格表示\"这个池子里没有标题提到\"，不等于\"没人做过\"；"
         "查新时必须再做实时检索（arXiv、IEEE Xplore、Google Scholar）。\n",
         "## 1. 年份分布\n", ", ".join(f"{y}: {k}" for y, k in sorted(years.items())), "",
         "## 2. 标签计数\n",
         "- 模态：" + ", ".join(f"{k} {v}/{n}" for k, v in mc.most_common()),
         "- 主题：" + ", ".join(f"{k} {v}/{n}" for k, v in tc.most_common()), "",
         "## 3. 模态 × 主题占位表（篇数）\n"]
    topics = [t for t, _ in tc.most_common()]
    mods = [m for m, _ in mc.most_common()]
    L.append("| 模态 \\ 主题 | " + " | ".join(topics) + " |")
    L.append("|---|" + "---|" * len(topics))
    for m in mods:
        L.append(f"| {m} | " + " | ".join(str(occ[m][t]) if occ[m][t] else "·" for t in topics) + " |")
    L.append("")
    L.append("## 4. 主题按年份（标题计数）\n")
    ys = sorted(years)
    L.append("| 主题 | " + " | ".join(ys) + " |")
    L.append("|---|" + "---|" * len(ys))
    for t in topics:
        L.append(f"| {t} | " + " | ".join(str(year_tag[t][y]) if year_tag[t][y] else "·" for y in ys) + " |")
    L.append("")
    L.append("## 5. 各标签下的标题（按年均引用降序）\n")
    for key in ["topic:" + t for t in topics] + ["modality:" + m for m in mods]:
        L.append(f"### {key}（{len(by_tag[key])}）")
        for r in sorted(by_tag[key], key=lambda r: -float(r["cites_per_year"])):
            other = r["topics"].replace(";", ", ")
            L.append(f"- {r['title']} — {r['journal']} {r['year']}, {r['doi'].split('/', 1)[1]}, cpy {r['cites_per_year']}"
                     + (f" [{r['modality'].replace(';', ', ')} | {other}]" if r['modality'] or other else ""))
        L.append("")
    open(OUT_MD, "w", encoding="utf-8").write("\n".join(L) + "\n")

    # compact copy for the skill: sections 1-4 plus the top titles under each topic tag
    head = L[:L.index("## 5. 各标签下的标题（按年均引用降序）\n")]
    S = ["# 选题地图：234 篇候选论文的标题标签\n",
         "由 `pipeline/landscape_semcom.py` 生成；完整版（每个标签下的全部标题）在 `corpus/semcom/landscape.md`。",
         "用途：生成 idea 时找\"空格\"和\"少格\"，检查 idea 时找最接近的已有工作。",
         "**局限**：只看标题（Crossref 无摘要）；候选池限于 6 本期刊、2018–2025、引用 ≥ 10，"
         "会议论文、arXiv 预印本和被引不足的新论文都不在内。空格只说明\"这个池子里没有标题提到\"，"
         "查新必须再做实时检索。\n"]
    S += head[3:]
    S.append("## 5. 各主题年均引用最高的标题（每类前 6 篇）\n")
    for t_ in topics:
        if t_.startswith("("):
            continue
        rs = sorted(by_tag["topic:" + t_], key=lambda r: -float(r["cites_per_year"]))[:6]
        S.append(f"### {t_}（共 {len(by_tag['topic:' + t_])} 篇）")
        for r in rs:
            S.append(f"- {r['title']} — {r['journal']} {r['year']}, {r['doi'].split('/', 1)[1]}")
        S.append("")
    os.makedirs(os.path.dirname(OUT_SKILL), exist_ok=True)
    open(OUT_SKILL, "w", encoding="utf-8").write("\n".join(S) + "\n")
    print(f"{n} titles -> {OUT_CSV}, {OUT_MD}")
    print("modality:", mc.most_common())
    print("topics:", tc.most_common())


if __name__ == "__main__":
    main()
