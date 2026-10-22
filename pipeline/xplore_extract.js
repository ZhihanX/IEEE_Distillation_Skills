// Read-only extractor for one IEEE Xplore full-text page (ieeexplore.ieee.org/document/<id>).
// Evaluate it as one expression in the page (browser console or an agent's JS tool, which must
// support top-level await). It waits up to 10 s for the full text to render, then returns JSON:
// structure counts, the intro and conclusion in full, condensed other sections, figure/table
// captions, theorem-type statements, and phrase/method counts with the first matching sentence
// (<= 30 words). Nothing is stored or sent anywhere.
await (async () => {
  for (let k = 0; k < 40 && !document.querySelector('#article div.section'); k++) await new Promise(r => setTimeout(r, 250));
  const A = document.querySelector('#article');
  const q = (s, r = document) => r.querySelector(s);
  const W = s => (s.match(/\S+/g) || []).length;
  const clip = (s, n) => { const w = s.split(' '); return w.length > n ? w.slice(0, n).join(' ') + ' …' : s; };
  const T = el => {
    const c = el.cloneNode(true);
    c.querySelectorAll('inline-formula').forEach(f => {
      const s = f.querySelector('script[type^="math/tex"]');
      let t = (s ? s.textContent : f.textContent).replace(/\s+/g, ' ').trim();
      f.replaceWith(' $' + (t.length > 40 ? t.slice(0, 40) + '…' : t) + '$ ');
    });
    c.querySelectorAll('disp-formula').forEach(f => f.replaceWith(' [EQ] '));
    c.querySelectorAll('.figure, .algorithm, .MathJax_Preview, script').forEach(f => f.remove());
    return c.textContent.replace(/\s+/g, ' ').replace(/\s([,.;:)])/g, '$1').trim();
  };
  const SENT = s => s
    .replace(/\b(i\.e|e\.g|w\.r\.t|i\.i\.d|w\.p)\./g, m => m.replace(/\./g, '․'))
    .replace(/\b(Fig|Figs|Eq|Eqs|Sec|Secs|Ref|Refs|Thm|No|vs|resp|cf|al|etc|approx|Prop|Lem|Cor|Def|Alg|Tab|Ch|Dr|Prof|St)\./g, '$1․')
    .split(/(?<=[.!?])\s+(?=[A-Z\[("“$])/).map(x => x.replace(/․/g, '.').trim()).filter(Boolean);
  const title = (q('h1.document-title') || {}).innerText || document.title;
  const absEl = q('.abstract-text');
  // Long abstracts are cut off with "Show More" in the page; og:description holds the full text.
  const ogd = (q('meta[property="og:description"]') || {}).content || '';
  const abstract = absEl && !/Show More/.test(absEl.innerText) ? T(absEl).replace(/^Abstract:\s*/, '') : ogd.replace(/\s+/g, ' ').trim();
  if (!A) return { noFullText: true, url: location.href, title, abstract };
  const hdr = s => { const h = q(':scope > .header h2, :scope > h2, :scope > h3, :scope > h4, :scope > .header h3', s); return h ? h.innerText.replace(/\s+/g, ' ').trim() : ''; };
  const KIND = [['appendix', /^(appendix|appendices|proof of|supplementary)/i], ['intro', /introduction/i],
    ['related', /related|prior work|literature|background|state of the art/i],
    ['conclusion', /conclu|final remarks|summary and|concluding/i],
    ['results', /simulation|numerical|experiment|evaluation|results|measurement|case stud/i],
    ['model', /system model|problem formulation|signal model|channel model|preliminar|network model/i]];
  const secs = [...A.querySelectorAll('div.section')];
  const isStmt = el => !!q(':scope > .statement', el);
  const subOf = p => { let x = p.closest('div.section_2, div.section_3'); while (x && isStmt(x)) x = x.parentElement.closest('div.section_2, div.section_3'); return x; };
  const body = [];
  let wordsAll = 0;
  const out = secs.map((s, i) => {
    const t = hdr(s);
    let kind = (KIND.find(([, rx]) => rx.test(t)) || ['other'])[0];
    if (i === 0 && kind === 'other') kind = 'intro';
    if (/^app/i.test(s.id)) kind = 'appendix';
    const allP = [...s.querySelectorAll('p')].filter(p => !p.closest('li, .figure, .algorithm, .footnote'));
    const ps = allP.filter(p => !p.closest('div.section_2, div.section_3') || !isStmt(p.closest('div.section_2, div.section_3')))
      .map(p => { const sub = subOf(p); return { sub: sub ? hdr(sub) : '', t: T(p) }; })
      .filter(p => p.t);
    ps.forEach(p => body.push(p.t));
    const words = allP.reduce((a, p) => a + W(T(p)), 0);
    wordsAll += words;
    const subs = [...s.querySelectorAll('div.section_2, div.section_3')].filter(x => !isStmt(x))
      .map(x => (x.classList.contains('section_3') ? '  ' : '') + hdr(x));
    const nFig = [...s.querySelectorAll('div.figure')].filter(f => !f.classList.contains('table')).length;
    if (kind === 'other' && nFig >= 2 && /simulat|numerical|experiment|evaluat/i.test(ps.slice(0, 2).map(p => p.t).join(' '))) kind = 'results';
    let text;
    if (kind === 'intro' || kind === 'conclusion') text = ps.map(p => (p.sub ? `[${p.sub}] ` : '') + p.t);
    else if (kind === 'appendix') text = ps.slice(0, 1).map(p => clip(SENT(p.t)[0] || '', 30));
    else if (kind === 'related') text = ps.map(p => clip(SENT(p.t)[0] || '', 40));
    else if (kind === 'results') text = ps.map((p, j) => (p.sub ? `[${p.sub}] ` : '') + (j === 0 ? clip(p.t, 150) : clip(SENT(p.t).slice(0, 2).join(' '), 60)));
    else text = ps.map((p, j) => (p.sub ? `[${p.sub}] ` : '') + (j === 0 ? clip(p.t, 120) : clip(SENT(p.t)[0] || '', 35)));
    return { i: i + 1, title: t, kind, words, paras: ps.length, subs, text };
  });
  const kindOf = el => { const s = el.closest('div.section'); const o = s ? out[secs.indexOf(s)] : null; return o ? o.kind : '?'; };
  const figs = [...A.querySelectorAll('div.figure')].map(f => {
    const cap = q('.figcaption', f); const img = q('img', f);
    const c = cap ? T(cap) : (img ? img.alt.replace(/\s+/g, ' ').trim() : '');
    return { id: f.id, table: f.classList.contains('table'), alg: /^Algorithm\s*\d/i.test(c), sec: kindOf(f), cap: c };
  }).filter(f => f.id || f.cap);
  const st = {}; const stmts = [];
  A.querySelectorAll('.statement').forEach(s => {
    const type = (s.innerText.trim().match(/^[A-Za-z]+/) || ['other'])[0].toLowerCase();
    const app = kindOf(s) === 'appendix';
    st[type] = st[type] || { n: 0, inAppendix: 0 }; st[type].n++; if (app) st[type].inAppendix++;
    const txt = [...s.parentElement.children].filter(c => c.tagName === 'P').map(T).join(' ');
    if (!/proof/.test(type)) stmts.push(`[${s.innerText.trim()}${app ? ' appendix' : ''}] ` + clip(txt, 45));
  });
  const lists = [...A.querySelectorAll('ul, ol')].filter(l => !l.closest('.figure, .algorithm, li') && l.closest('div.section'))
    .map(l => ({ sec: kindOf(l), tag: l.tagName, items: [...l.children].map(li => clip(T(li), kindOf(l) === 'intro' ? 90 : 40)) }));
  const notation = body.find(p => /^Notations?\b/i.test(p));
  const full = [abstract, ...body].join(' ');
  const sents = [abstract, ...body].flatMap(SENT);
  const P = {
    toTheBest: /to the best of (our|the authors['’]?) knowledge|to our best knowledge/i, inThisPaper: /\bin this (paper|work|article)\b/i,
    contribList: /contributions? of (this|the|our) (paper|work|article)|our (main |major |key )?contributions|summarized as follows|contributions are/i,
    roadmap: /(rest|remainder|organization) of (this|the) (paper|article|manuscript|work)|(paper|article|manuscript) is (organized|structured) as follows|^Organization:/i,
    however: /^However,/, transition: /^(Moreover|Furthermore|In addition|Besides|Additionally),/,
    resultsShow: /\b(simulation|numerical|experimental) results (show|demonstrate|reveal|verify|validate|confirm|indicate|illustrate)/i,
    motivatedBy: /\b(motivated|inspired) by\b/i, toAddress: /\bto (tackle|address|overcome|circumvent|handle|solve) (this|these|the|such)\b/i,
    gapWord: /\b(however|nevertheless|unfortunately), (the |most |these |existing |such |prior |previous )?(existing |prior |previous )?(works?|studies|approaches|methods|schemes|literature|results|designs)/i,
    nonconvex: /\bnon-?convex/i, npHard: /\bNP-hard/i, closedForm: /\bclosed-form/i, outperform: /\boutperform/i,
    intensifier: /\b(significantly|substantially|remarkably|dramatically|considerably)\b/i,
    worthNoting: /\bit is (worth|interesting|important) (noting|to note|mentioning|pointing out|emphasizing)|it is worth\b/i,
    observe: /\bit (can|could) be (observed|seen|found)|\bwe (can )?(observe|see) (that|from)|it is (observed|seen) (that|from)/i,
    thisIsBecause: /\bthis is because\b/i, asExpected: /\bas expected\b/i, insight: /\binsights?\b/i, tradeoff: /\btrade-?offs?\b/i,
    figVerb: /\bFigs?\. ?\d+(\([a-z]\))? (shows|illustrates|plots|depicts|compares|presents|demonstrates|investigates|studies|evaluates)/i,
    promising: /\bpromising\b/i, gen: /\b(6G|5G|B5G|beyond 5G|next[- ]generation)\b/i, contrast: /^(Unlike|In contrast|Different from|As opposed to|Compared with|Compared to)\b/,
    firstTime: /\bfor the first time\b|\bthe first (work|paper|study|attempt)\b/i, novel: /\bnovel\b/i, weProposeFirst: /\bwe propose\b/i,
    wlog: /without loss of generality/i, code: /github\.com|source code|code (is|will be) (publicly )?available/i,
    prototype: /\bprototype|testbed|field (trial|test)|measurement campaign|experimental (setup|platform)/i,
  };
  const M = {
    AO: /alternating optimization|\bAO\b/, SCA: /successive convex approximation|\bSCA\b/, SDR: /semidefinite relaxation|\bSDR\b/,
    BCD: /block coordinate descent|\bBCD\b/, MM: /majorization[- ]minimization|minorization[- ]maximization/i, FP: /fractional programming|quadratic transform|Dinkelbach/i,
    lagrange: /Lagrang/i, KKT: /\bKKT\b|Karush/, ADMM: /\bADMM\b|alternating direction method/i, penalty: /penalty/i, manifold: /manifold/i,
    WMMSE: /WMMSE|weighted minimum mean/i, bisection: /bisection/i, convexOpt: /\bCVX\b|interior[- ]point|convex optimization problem/i,
    BnB: /branch[- ]and[- ]bound/i, DRL: /reinforcement learning/i, DNN: /neural network/i, gameTheory: /game[- ]theor|Stackelberg|Nash equilibrium/i,
    stochGeom: /stochastic geometry|Poisson point process/i, lyapunov: /Lyapunov/i, randomMatrix: /random matrix|deterministic equivalent/i,
    CRB: /Cram[eé]r[- ]Rao|\bCRB\b/, monteCarlo: /Monte[- ]Carlo/i, compressedSensing: /compressed sensing|compressive sensing|sparse recovery|\bOMP\b/i,
    convergence: /converge/i, complexity: /complexity/i,
  };
  const phr = {}, ex = {};
  for (const [k, rx] of Object.entries(P)) { const hits = sents.filter(s => rx.test(s)); phr[k] = hits.length; if (hits.length) ex[k] = clip(hits[0], 30); }
  const meth = {};
  for (const [k, rx] of Object.entries(M)) { const n = sents.filter(s => rx.test(s)).length; if (n) meth[k] = n; }
  // Domain terms for semantic communication / JSCC papers (datasets, metrics, baselines, channels, models).
  const D = {
    CIFAR: /CIFAR/, Kodak: /Kodak/, CLIC: /\bCLIC/, ImageNet: /ImageNet/, DIV2K: /DIV2K/, OpenImages: /Open ?Images/i,
    CelebA: /CelebA/, FFHQ: /FFHQ/, COCO: /\bCOCO\b/, Cityscapes: /Cityscapes/, MNIST: /MNIST/, UCF101: /UCF-?101/,
    Kinetics: /Kinetics/, Vimeo: /Vimeo/, Europarl: /Europarl/, LibriSpeech: /LibriSpeech/, Edinburgh: /Edinburgh/, TIMIT: /TIMIT/,
    PSNR: /PSNR/, SSIM: /(?<!MS-)\bSSIM\b/, MSSSIM: /MS-SSIM/, LPIPS: /LPIPS/, FID: /\bFID\b/, BLEU: /BLEU/,
    sentSim: /sentence similarity|BERT/i, PESQ: /PESQ/, WER: /\bWER\b|word error rate|character error rate/i,
    accuracy: /accuracy/i, mIoU: /mIoU/,
    BPG: /\bBPG\b/, JPEG: /JPEG(?! ?2000)/, JPEG2000: /JPEG ?2000/, videoCodec: /H\.26[45]|HEVC|VVC/, LDPC: /LDPC/,
    polar: /polar code/i, turbo: /turbo code/i, Huffman: /Huffman/, capacityBound: /capacity-achieving|ideal channel cod|Shannon capacity/i,
    DeepJSCC: /Deep ?JSCC|ADJSCC|deep joint source-channel/i, DeepSC: /DeepSC/,
    AWGN: /AWGN/, Rayleigh: /Rayleigh/, Rician: /Rician/, MIMO: /MIMO/, OFDM: /OFDM/, feedback: /feedback/i,
    CNN: /convolutional|\bCNN/i, transformer: /[Tt]ransformer/, Swin: /Swin/, VAE: /variational auto-?encoder|\bVAE\b/i,
    VQ: /vector quantiz|\bVQ\b|codebook/i, GAN: /\bGAN\b|generative adversarial/i, diffusion: /diffusion model|denoising diffusion|DDPM|DDIM/i,
    LLM: /large language model|\bLLMs?\b|GPT|foundation model/i, attention: /attention/i,
    CBR: /bandwidth (compression )?ratio|\bCBR\b/i, SNRmismatch: /mismatch/i, quantization: /quantiz/i, QAM: /QAM|PSK/,
    IB: /information bottleneck/i, knowledgeBase: /knowledge base|knowledge graph/i, ratedist: /rate-distortion|rate distortion/i,
    perception: /perception|perceptual/i, complexityCost: /number of parameters|FLOPs|MACs|inference time|running time|latency/i,
    hardware: /prototype|testbed|USRP|software-defined radio|SDR platform|over-the-air experiment/i,
  };
  const dom = {};
  for (const [k, rx] of Object.entries(D)) { const n = sents.filter(s => rx.test(s)).length; if (n) dom[k] = n; }
  // Sentences that name limitations or open problems: seeds for new ideas.
  const OPEN = /future (work|research|direction|stud)|for future|left (as|for)|remains? (an )?open|open (problem|question|issue|challenge)|beyond the scope|limitation|not (yet )?(been )?(considered|addressed|investigated|studied)|we leave|worth (further )?(investigat|explor|stud)|next step|\bwe (will|plan to|intend to) (also )?(explore|investigate|study|consider|extend|look)/i;
  const openSents = [...new Set(sents.filter(s => OPEN.test(s)))].slice(0, 14).map(s => clip(s, 40));
  const top = out.filter(s => s.kind !== 'appendix');
  return {
    url: location.href, title, title_words: W(title), abstract_words: W(abstract), abstract_sents: SENT(abstract),
    stats: {
      words_total: wordsAll, n_sections: top.length, n_appendix: out.length - top.length,
      n_subsections: [...A.querySelectorAll('div.section_2')].filter(x => !isStmt(x)).length, n_figures: figs.filter(f => !f.table && !f.alg).length,
      n_tables: figs.filter(f => f.table).length, n_display_eq: A.querySelectorAll('disp-formula').length,
      n_algorithms: A.querySelectorAll('.algorithm').length + figs.filter(f => f.alg).length, statements: st,
      mean_sentence_words: Math.round(sents.reduce((a, s) => a + W(s), 0) / Math.max(1, sents.length) * 10) / 10,
      we_per_1k: Math.round(1000 * (full.match(/\bwe\b/gi) || []).length / Math.max(1, W(full)) * 10) / 10,
    },
    outline: out.map(s => `${s.i}. ${s.title} [${s.kind}, ${s.words}w, ${s.paras}p]` + (s.subs.length ? ' :: ' + s.subs.join(' | ') : '')),
    sections: out.map(({ i, title, kind, text }) => ({ i, title, kind, text })),
    figures: figs.map(f => `${f.id}${f.table ? ' (table)' : ''} @${f.sec}: ${clip(f.cap, 60)}`),
    statements: stmts, lists, notation: notation ? clip(notation, 80) : null,
    phrases: phr, examples: ex, methods: meth, domain: dom, open: openSents,
  };
})()
