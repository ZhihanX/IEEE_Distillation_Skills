"""Aggregate the semantic-communication sub-corpus cards.

Reads every card with a `semcom:` block (corpus/semcom/cards/*.md plus the main
cards in corpus/cards/ that were extended in place) and writes
corpus/semcom/summary.md and corpus/semcom/summary.json:

  * k/n counts for every `semcom` field (research papers only; overviews are listed separately)
  * evaluation-completeness rates (SNR mismatch, complexity, digital compatibility, ...)
  * idea_delta frequencies, per category
  * the lineage graph: which cards cite which other cards as baseline / follow-up (from section 10)
  * the pooled open-problem list from section 10, split into author-stated and inferred items,
    grouped by theme
  * weakness themes from section 10 (keyword counts are lower bounds, written as ">=k/n")

Usage: python3 pipeline/aggregate_semcom.py
"""
import glob
import json
import os
import re
import statistics
from collections import Counter, defaultdict

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARD_DIRS = [os.path.join(ROOT, "corpus", "semcom", "cards"), os.path.join(ROOT, "corpus", "cards")]
OUT_MD = os.path.join(ROOT, "corpus", "semcom", "summary.md")
OUT_JSON = os.path.join(ROOT, "corpus", "semcom", "summary.json")

LIST_FIELDS = ["source", "task", "architecture", "channel", "adaptivity", "training", "metrics",
               "datasets", "baselines", "idea_delta"]
SCALAR_FIELDS = ["category", "paradigm", "theory"]
BOOL_FIELDS = ["snr_mismatch_test", "complexity_reported", "digital_compatible", "hardware_validation"]

# Normalise near-synonyms so counts are not split across spellings.
ALIAS = {
    "swin": "Swin", "MS-SSIM": "MS-SSIM", "sentence-similarity": "sentence-similarity",
    "OFDMA": "OFDM", "MISO": "MIMO", "noiseless-bits": "abstract", "erasure": "erasure-packet",
    "Fashion-MNIST": "Fashion-MNIST", "Tiny-ImageNet": "Tiny-ImageNet",
    "two-stage": "multi-stage", "two-phase": "multi-stage", "none-pretrained": "pretrained-frozen",
    "pretrained-generator": "pretrained-frozen", "IoU": "mIoU", "bits": "bit-rate",
}

DOI_RE = re.compile(r"\b(?:tccn|twc|jsac|tcomm|jsait|tsp)\.\d{4}\.\d{7}\b")

THEMES = [
    ("fading / MIMO / OFDM / real channels", r"衰落|MIMO|OFDM|多径|频率选择|fading|non-Gaussian|channels with memory|信道估计|CSI|time-varying channel|CFO|carrier frequency"),
    ("digital compatibility / modulation / channel coding", r"数字|调制|星座|量化|码本|信道编码|HARQ|AMC|不等错误保护|soft-output|demodulation|modulation|quantization|digital|constellation|三元组.*纠错|比特相关"),
    ("multi-user / multiple access / networking", r"多用户|多址|广播|多设备|RSMA|NOMA|RIS|ISAC|multi-user|multiple devices|S- and B-users|semantic and bit|decentralized|资源分配|调度|多传感器"),
    ("complexity / energy / latency / deployment", r"复杂度|时延|轻量|移动设备|采样步|加速|实时|能效|能耗|lighten|mobile devices|computation|energy|反馈开销"),
    ("hardware / over-the-air validation", r"硬件|SDR|原型|实测|software defined radio|practical channels|more practical"),
    ("generative / foundation models", r"生成|扩散|GAN|大模型|LLM|基础模型|personalized content|generative"),
    ("theory / limits / metrics", r"理论|率失真|界|信息论|度量|指标|可达性|逆定理|解析模型|metric|rate-distortion|theoretical|fidelity|distortion criteria|semantic information theory|performance limit|semantics involved"),
    ("security / privacy / robustness", r"隐私|安全|攻击|对抗|鲁棒|窃听|robust|privacy|attack"),
    ("new modality / task / dataset", r"视频|语音|音频|多模态|模态|数据集|任务|多说话人|多语言|副语言|高分辨率|ImageNet|datasets|downstream tasks|modalities|audio|video|types of sources|semantic concept|语义概念"),
    ("knowledge base / continual & online learning", r"知识库|知识图谱|持续学习|在线|漂移|数据分布|knowledge|minimum communication cost"),
    ("architecture / training improvements", r"架构|网络结构|architecture|training algorithm|coding capability|Transformer|loss functions|alternating minimization"),
    ("adaptivity (SNR / bandwidth / content)", r"自适应|可变|分层|SNR|带宽|adaptive|variable|feedback|hybrid solution|条件编码"),
]

WEAK_THEMES = [
    ("AWGN only / limited channel", r"只有 AWGN|只用 AWGN|只在 AWGN|单一信道|只有标量高斯|无物理信道|完美 CSI|理想信道估计"),
    ("no complexity / latency analysis", r"无复杂度|没有复杂度|未报告时延|无墙钟|未计入|复杂度.*未|无时延"),
    ("small images / few datasets", r"小图|小数据集|单一数据集|单数据集|只在.*上验证|窄分布|数据集多为|只有 Kodak|只有 Cityscapes"),
    ("analog only (not digital-compatible)", r"模拟传输|不兼容数字"),
    ("no hardware validation", r"无硬件|没有硬件|无 SDR"),
    ("weak / missing baselines", r"基准只有|基准不全|没有与.*比较|缺少.*基准|基准只是"),
    ("strong or unverified assumptions", r"假设.*偏强|白盒|近似假设|比特独立|假设比特|回归|拟合"),
    ("no future work stated", r"无未来工作"),
]


def load():
    cards = []
    seen = set()
    for d in CARD_DIRS:
        for path in sorted(glob.glob(os.path.join(d, "*.md"))):
            text = open(path, encoding="utf-8").read()
            if not text.startswith("---"):
                continue
            meta = yaml.safe_load(text.split("---", 2)[1])
            if not meta or "semcom" not in meta:
                continue
            if meta["doi"] in seen:
                continue
            seen.add(meta["doi"])
            meta["_path"] = os.path.relpath(path, ROOT).replace("\\", "/")
            meta["_body"] = text.split("---", 2)[2]
            cards.append(meta)
    return cards


def norm(v):
    v = str(v).strip()
    return ALIAS.get(v, v)


def section10(body):
    m = re.search(r"^## 10\..*?$(.*)", body, re.S | re.M)
    return m.group(1) if m else ""


def field_line(sec, name):
    m = re.search(r"^- \*\*" + name + r"\*\*[：:](.*)$", sec, re.M)
    return m.group(1).strip() if m else ""


def open_items(sec):
    m = re.search(r"^- \*\*开放问题\*\*.*?$(.*)", sec, re.S | re.M)
    if not m:
        return [], []
    author, inferred = [], []
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line.startswith("- "):
            if line.startswith("- **") or line.startswith("##"):
                break
            continue
        item = line[2:].strip()
        if item.startswith("推断"):
            inferred.append(item.split("：", 1)[-1].strip())
        else:
            author.append(item)
    return author, inferred


def kn(counter, n, top=None):
    items = counter.most_common(top)
    return ", ".join(f"{k} {v}/{n}" for k, v in items)


def main():
    cards = load()
    research = [c for c in cards if c.get("article_type", "research") == "research"]
    overview = [c for c in cards if c.get("article_type") != "research"]
    n = len(research)
    sfx = {c["doi"].split("/", 1)[1]: c for c in cards}

    counts = {f: Counter() for f in LIST_FIELDS + SCALAR_FIELDS}
    bools = {f: 0 for f in BOOL_FIELDS}
    by_cat = defaultdict(list)
    delta_by_cat = defaultdict(Counter)
    for c in research:
        s = c["semcom"]
        by_cat[s["category"]].append(c)
        for f in SCALAR_FIELDS:
            counts[f][norm(s.get(f, "unclear"))] += 1
        for f in LIST_FIELDS:
            vals = s.get(f) or []
            for v in {norm(x) for x in vals}:
                counts[f][v] += 1
                if f == "idea_delta":
                    delta_by_cat[s["category"]][v] += 1
        for f in BOOL_FIELDS:
            bools[f] += 1 if s.get(f) is True else 0

    # derived evaluation-completeness checks
    def has(c, field, vals):
        return any(norm(v) in vals for v in (c["semcom"].get(field) or []))
    fading = sum(has(c, "channel", {"Rayleigh", "Rician", "MIMO", "OFDM", "real-measured"}) for c in research)
    awgn_only = sum(set(map(norm, c["semcom"].get("channel") or [])) <= {"AWGN"} for c in research)
    sep_base = sum(has(c, "baselines", {"separate"}) for c in research)
    perceptual = sum(has(c, "metrics", {"LPIPS", "FID", "KID", "MS-SSIM", "CLIP"}) for c in research)
    hires = sum(has(c, "datasets", {"Kodak", "CLIC", "DIV2K", "ImageNet", "CelebA-HQ", "HEVC", "UVG", "Cityscapes"}) for c in research)
    img = [c for c in research if "image" in (c["semcom"].get("source") or []) or "video" in (c["semcom"].get("source") or [])]
    hires_img = sum(has(c, "datasets", {"Kodak", "CLIC", "DIV2K", "ImageNet", "CelebA-HQ", "HEVC", "UVG", "Cityscapes"}) for c in img)
    code_rel = sum(1 for c in research if (c.get("code") or {}).get("code_released") is True)

    # lineage graph from section 10
    edges, follow = [], []
    for c in cards:
        sec = section10(c["_body"])
        base = field_line(sec, "基线")
        me = c["doi"].split("/", 1)[1]
        for d in DOI_RE.findall(base):
            if d != me:
                edges.append((me, d))
        for d in DOI_RE.findall(sec.split("**基线**", 1)[-1] if "**基线**" in sec else sec):
            if d != me and d not in DOI_RE.findall(base):
                follow.append((me, d))
    indeg = Counter(d for _, d in edges)

    # open problems
    pooled = []
    for c in cards:
        a, i = open_items(section10(c["_body"]))
        me = c["doi"].split("/", 1)[1]
        for x in a:
            pooled.append({"doi": me, "kind": "author", "text": x})
        for x in i:
            for part in re.split(r"[；;]", x):
                part = part.strip().rstrip("。")
                if part:
                    pooled.append({"doi": me, "kind": "inferred", "text": part})
    theme_of = []
    for p in pooled:
        th = [name for name, rx in THEMES if re.search(rx, p["text"], re.I)]
        p["themes"] = th or ["other"]
        theme_of.extend(p["themes"])
    theme_counts = Counter()
    theme_cards = defaultdict(set)
    for p in pooled:
        for t in p["themes"]:
            theme_counts[t] += 1
            theme_cards[t].add(p["doi"])

    weak = Counter()
    weak_cards = defaultdict(list)
    for c in research:
        w = field_line(section10(c["_body"]), "弱点")
        me = c["doi"].split("/", 1)[1]
        for name, rx in WEAK_THEMES:
            if re.search(rx, w):
                weak[name] += 1
                weak_cards[name].append(me)

    cpy_cat = {k: statistics.median([c["cites_per_year"] for c in v]) for k, v in by_cat.items()}

    # ---------- write markdown ----------
    L = []
    L.append("# 语义通信 / JSCC 子语料汇总\n")
    L.append(f"自动生成（`python3 pipeline/aggregate_semcom.py`）。研究论文 n = {n}，综述 {len(overview)} 篇（单独列出，不计入频率）。")
    L.append("频率写成 k/n；列表字段一篇可计多个值。关键词主题计数（开放问题、弱点）是下界，引用时写成 \"≥k/n\"。\n")
    L.append("## 1. 类别与年均引用\n")
    L.append("| 类别 | 篇数 | 年均引用中位数 |\n|---|---|---|")
    for k in sorted(by_cat, key=lambda x: -len(by_cat[x])):
        L.append(f"| {k} | {len(by_cat[k])} | {cpy_cat[k]:g} |")
    L.append("")
    L.append("## 2. 字段频率（研究论文）\n")
    for f in SCALAR_FIELDS + LIST_FIELDS:
        top = 25 if f == "datasets" else None
        L.append(f"- **{f}**：{kn(counts[f], n, top)}")
    L.append("")
    L.append("## 3. 评测完整性\n")
    rows = [
        ("SNR 失配（训练 / 测试 SNR 不同）实验", bools["snr_mismatch_test"]),
        ("报告复杂度（参数量 / FLOPs / 运行时间）", bools["complexity_reported"]),
        ("输出可直接接入数字链路", bools["digital_compatible"]),
        ("硬件 / 空口验证", bools["hardware_validation"]),
        ("至少一种衰落 / MIMO / OFDM 信道", fading),
        ("信道只有 AWGN（不含无信道 / 抽象模型的论文）", awgn_only),
        ("基准含分离式方案（JPEG/BPG/H.26x + LDPC/容量界等）", sep_base),
        ("报告感知类指标（MS-SSIM / LPIPS / FID / KID / CLIP）", perceptual),
        ("开源代码", code_rel),
    ]
    for name, k in rows:
        L.append(f"- {name}：{k}/{n}")
    L.append(f"- 图像 / 视频论文中用到高分辨率数据集（Kodak / CLIC / DIV2K / ImageNet / CelebA-HQ / HEVC / UVG / Cityscapes）：{hires_img}/{len(img)}")
    L.append("")
    L.append("## 4. idea_delta（相对基线的增量类型）\n")
    L.append(f"- 全体：{kn(counts['idea_delta'], n)}")
    L.append("- 每篇的增量类型数：" + ", ".join(f"{k} 类 {v}/{n}" for k, v in sorted(Counter(len(c['semcom'].get('idea_delta') or []) for c in research).items())))
    for k in sorted(delta_by_cat):
        L.append(f"- {k}（{len(by_cat[k])} 篇）：{kn(delta_by_cat[k], len(by_cat[k]))}")
    L.append("")
    L.append("## 5. 继承关系（第 10 节\"基线\"行中引用的语料内论文）\n")
    L.append("被作为基线引用的次数：" + ", ".join(f"{d} ({sfx[d]['semcom'].get('category', '?') if d in sfx else '?'}) {k}" for d, k in indeg.most_common()))
    L.append("")
    L.append("| 论文 | 类别 | 年 | 基线（语料内） | 增量 |\n|---|---|---|---|---|")
    for c in sorted(research, key=lambda c: (c["year"], c["doi"])):
        me = c["doi"].split("/", 1)[1]
        bs = ", ".join(d for s_, d in edges if s_ == me) or "—"
        L.append(f"| {me} | {c['semcom']['category']} | {c['year']} | {bs} | {', '.join(c['semcom'].get('idea_delta') or [])} |")
    L.append("")
    L.append("## 6. 开放问题（第 10 节，按主题汇总）\n")
    na = sum(1 for p in pooled if p["kind"] == "author")
    ni = sum(1 for p in pooled if p["kind"] == "inferred")
    L.append(f"共 {na} 条作者原文、{ni} 条推断（来自 {len(cards)} 张卡片）。一条可属多个主题；括号内是涉及的卡片数。\n")
    for t, k in theme_counts.most_common():
        L.append(f"### {t}（{k} 条，{len(theme_cards[t])} 篇）")
        for p in pooled:
            if t in p["themes"]:
                tag = "原文" if p["kind"] == "author" else "推断"
                L.append(f"- [{tag}] {p['text']} — {p['doi']}")
        L.append("")
    L.append("## 7. 弱点主题（第 10 节\"弱点\"行，关键词下界）\n")
    for name, _ in WEAK_THEMES:
        L.append(f"- {name}：≥{weak[name]}/{n}（{', '.join(weak_cards[name])}）")
    L.append("")
    L.append("## 8. 写作字段（`code:` 块，研究论文）\n")
    CODE_FIELDS = ["gap_type", "first_claim", "contrib_format", "abstract_has_numbers", "theory_role", "problem_class",
                   "solution", "x_axes", "fig1_role", "complexity_analysis", "sim_param_table", "code_released",
                   "conclusion_future_work", "related_work", "roadmap"]
    code_counts = {}
    for f in CODE_FIELDS:
        cc = Counter()
        for c in research:
            v = (c.get("code") or {}).get(f)
            vals = v if isinstance(v, list) else [v]
            for x in {str(x) for x in vals}:
                cc[x] += 1
        code_counts[f] = dict(cc)
        L.append(f"- **{f}**：{kn(cc, n, 12)}")
    bl = [(c.get("code") or {}).get("baselines_n") for c in research]
    bl = [b for b in bl if isinstance(b, int)]
    L.append(f"- **baselines_n**：中位数 {statistics.median(bl):g}，范围 {min(bl)}–{max(bl)}")
    L.append("")
    L.append("## 9. 综述\n")
    for c in overview:
        L.append(f"- {c['doi'].split('/', 1)[1]} {c['title']}（{c['year']}，年均引用 {c['cites_per_year']}）")
    open(OUT_MD, "w", encoding="utf-8").write("\n".join(L) + "\n")

    out = {
        "n_research": n, "n_overview": len(overview),
        "fields": {f: dict(counts[f]) for f in counts},
        "bools": bools,
        "derived": {"fading": fading, "awgn_only": awgn_only, "separate_baseline": sep_base,
                    "perceptual_metric": perceptual, "hires_image_video": [hires_img, len(img)], "code_released": code_rel},
        "idea_delta_by_category": {k: dict(v) for k, v in delta_by_cat.items()},
        "lineage_edges": edges, "followup_mentions": follow,
        "open_problems": pooled,
        "weak_themes": {k: weak_cards[k] for k, _ in WEAK_THEMES},
        "median_cpy_by_category": cpy_cat,
        "code_fields": code_counts,
    }
    json.dump(out, open(OUT_JSON, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    write_skill_open_problems(pooled, cards, theme_counts, theme_cards, n)
    print(f"research {n}, overview {len(overview)}, open problems {na}+{ni}, edges {len(edges)} -> {OUT_MD}")


OUT_SKILL_OPEN = os.path.join(ROOT, "skills", "semantic-comm-ideas", "references", "open-problems.md")


def write_skill_open_problems(pooled, cards, theme_counts, theme_cards, n):
    """Skill reference: open problems grouped by theme, author quotes first, then inferred items."""
    year = {c["doi"].split("/", 1)[1]: c["year"] for c in cards}
    L = ["# 开放问题清单（按主题）\n",
         "由 `pipeline/aggregate_semcom.py` 从 39 张卡片第 10 节自动汇总（完整版见 `corpus/semcom/summary.md` 第 6 节）。",
         "- **[原文]**：作者在结论或正文里写的局限 / 未来工作（原句，≤ 30 词，后附 DOI 后缀）。",
         "- **[推断]**：蒸馏时从论文弱点推出、作者没写的问题，是假设，使用前必须查新。",
         "  写着\"后续 xxx\"的推断项表示语料里已有论文部分回应了它，不再是空白，除非换设定。",
         "- 一条可属多个主题；主题按条目数排序。括号内：条目数，涉及论文数。\n",
         "使用方法：生成 idea 时，先在与用户方向相关的主题下挑 2–3 条，再用 `landscape.md` 和实时检索确认没人做过；",
         "检查 idea 时，看它是否回应了某条 [原文] 问题——能回应原文问题的 idea 在引言里更容易立住。\n"]
    for t, k in theme_counts.most_common():
        if t == "other":
            continue
        L.append(f"## {t}（{k} 条，{len(theme_cards[t])} 篇）\n")
        seen = set()
        items = [p for p in pooled if t in p["themes"]]
        items.sort(key=lambda p: (p["kind"] != "author", -year.get(p["doi"], 0)))
        for p in items:
            key = p["text"][:40]
            if key in seen:
                continue
            seen.add(key)
            tag = "[原文]" if p["kind"] == "author" else "[推断]"
            L.append(f"- {tag} {p['text']}（{p['doi']}）")
        L.append("")
    others = [p for p in pooled if p["themes"] == ["other"]]
    if others:
        L.append("## 其他\n")
        for p in others:
            tag = "[原文]" if p["kind"] == "author" else "[推断]"
            L.append(f"- {tag} {p['text']}（{p['doi']}）")
        L.append("")
    os.makedirs(os.path.dirname(OUT_SKILL_OPEN), exist_ok=True)
    open(OUT_SKILL_OPEN, "w", encoding="utf-8").write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
