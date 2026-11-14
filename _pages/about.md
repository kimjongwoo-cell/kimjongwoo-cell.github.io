---
permalink: /
title: "I am Jongwoo Kim"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,600;8..60,700&display=swap">
<style>
  .page__content h2 { font-size: 1.15em; letter-spacing: 0.04em; text-transform: uppercase; color: #1f2937; border-bottom: none; padding-bottom: 0.3em; margin-top: 2.2em; position: relative; }
  .page__content h2::after { content: ""; display: block; width: 42px; height: 3px; margin-top: 0.45em; border-radius: 2px; background: linear-gradient(90deg, #1d4ed8, #7c3aed); }
  .home-section { margin-top: 1.6em; }
  .news-list { list-style: none; margin: 0.6em 0 0 0; padding-left: 1.1em; border-left: 2px solid #e5e7eb; }
  .news-list li { position: relative; display: flex; gap: 0.6em; margin-bottom: 0.7em; font-size: 0.92em; line-height: 1.5; }
  .news-list li::before { content: ""; position: absolute; left: -1.47em; top: 0.48em; width: 9px; height: 9px; border-radius: 50%; background: #fff; border: 2px solid #1d4ed8; }
  .news-date { flex: 0 0 5.4em; font-weight: 700; color: #1d4ed8; font-variant-numeric: tabular-nums; }
  .sel-pub { display: flex; gap: 18px; align-items: center; margin-bottom: 14px; padding: 12px; border: 1px solid #eef0f3; border-radius: 12px; background: #fff; box-shadow: 0 1px 2px rgba(15,23,42,0.04), 0 4px 14px rgba(15,23,42,0.05); transition: box-shadow .2s ease, transform .2s ease; }
  .sel-pub:hover { box-shadow: 0 2px 4px rgba(15,23,42,0.06), 0 10px 24px rgba(15,23,42,0.08); transform: translateY(-1px); }
  .sel-pub img { width: 190px; height: 116px; object-fit: contain; border-radius: 8px; background: #f8fafc; padding: 4px; flex-shrink: 0; }
  .sel-title { font-weight: 700; font-size: 0.93em; line-height: 1.38; margin-bottom: 3px; }
  .sel-title a, .sel-title a:visited { color: #111827; text-decoration: none; }
  .sel-title a:hover { color: #1d4ed8; }
  .sel-meta { font-size: 0.85em; color: #4b5563; }
  .sel-venue { font-size: 0.84em; font-style: italic; color: #6b7280; margin-top: 2px; }
  .venue-tag { display: inline-block; padding: 1px 8px; margin-right: 7px; border-radius: 999px; font-size: 0.74em; font-weight: 700; letter-spacing: 0.03em; color: #fff; background: #1d4ed8; font-style: normal; }
  .cv-row { display: flex; justify-content: space-between; gap: 12px; font-size: 0.92em; padding: 3px 0; }
  .cv-row span:last-child { color: #6b7280; white-space: nowrap; font-variant-numeric: tabular-nums; }
  .cv-sub { font-size: 0.84em; color: #6b7280; margin: 0 0 0.7em 0; }
  @media (max-width: 700px) { .sel-pub { flex-direction: column; align-items: flex-start; } .sel-pub img { width: 100%; height: 160px; } .cv-row { flex-direction: column; gap: 0; } }
  .page__content { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; }
  .sel-title { font-family: 'Source Serif 4', Georgia, serif; font-size: 1.02em !important; }
  .sel-meta b { color: #0f172a; font-weight: 600; text-decoration: underline; text-decoration-color: #c7d2fe; text-decoration-thickness: 2px; text-underline-offset: 3px; }
  .sel-venue { font-style: normal !important; }
  .venue-tag { border-radius: 6px !important; letter-spacing: 0.06em !important; text-transform: uppercase; }
</style>

Hello, I’m Jongwoo Kim, a Ph.D. student in Industrial and Systems Engineering at KAIST, advised by [Prof. Mun Yong Yi](https://sites.google.com/view/myyi-kaist) and [Prof. Noseong Park](https://sites.google.com/view/npark). I work at the [Knowledge Innovation Research Center (KIRC)](https://kirc.kaist.ac.kr).

I build practical AI systems for real-world problems, focusing on:

- **World Models and JEPA**: bringing latent predictive learning to real domains such as pathology, graphs, and education.
- **Computational Pathology**: modeling the hierarchical, multi-scale structure of gigapixel slides, from local tissue patterns to the whole slide.
- **Graph Learning**: capturing the right inductive biases for graph-structured data, so that models generalize across graphs.

I’m always looking for practical challenges, regardless of domain.

<div class="home-section" markdown="1">

## News

<ul class="news-list">
  <li><span class="news-date">Nov 2026</span><span>GraPE is accepted to <b>KDD 2027</b>.</span></li>
  <li><span class="news-date">Aug 2026</span><span>Knowledge World Model for learning path recommendation is accepted to <b>CIKM 2026</b>.</span></li>
  <li><span class="news-date">Apr 2026</span><span>FeedEval is accepted to <b>ACL 2026 Findings</b>.</span></li>
  <li><span class="news-date">Jan 2026</span><span>Our work on posterior predictive node classification (co-first author) is accepted to <b>ICLR 2026</b>.</span></li>
  <li><span class="news-date">Sep 2025</span><span>Hierarchical vision-language few-shot learning for gigapixel images (co-first author) is accepted to <b>NeurIPS 2025</b>.</span></li>
</ul>

</div>

<div class="home-section" markdown="1">

## Selected Publications

<span style="font-size:0.85em;color:#555;">† equal contribution. Full list on the <a href="/publications/">Publications</a> page.</span>

<div class="sel-pub">
  <img src="/images/grape.png" alt="GraPE">
  <div>
    <div class="sel-title">GraPE: Graph Prompt Tuning via Mixture of Experts Approach.</div>
    <div class="sel-meta"><b>Jongwoo Kim</b>, Jeongwhan Choi, Seongyeub Chu, Noseong Park, Mun Yi.</div>
    <div class="sel-venue"><span class="venue-tag">KDD</span>ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD), 2027</div>
  </div>
</div>

<div class="sel-pub">
  <img src="/images/nodepfn.png" alt="NodePFN">
  <div>
    <div class="sel-title"><a href="https://openreview.net/forum?id=FmxRzlu0rT">Learning Posterior Predictive Distributions for Node Classification from Synthetic Graph Priors.</a></div>
    <div class="sel-meta">Jeongwhan Choi†, <b>Jongwoo Kim†</b>, Woosung Kang, Noseong Park.</div>
    <div class="sel-venue"><span class="venue-tag" style="background:#92400e;">ICLR</span>International Conference on Learning Representations (ICLR), 2026</div>
  </div>
</div>

<div class="sel-pub">
  <img src="/images/NeurIPS_2025.png" alt="NeurIPS 2025">
  <div>
    <div class="sel-title"><a href="https://arxiv.org/abs/2505.17982">Few-Shot Learning from Gigapixel Images via Hierarchical Vision-Language Alignment and Modeling.</a></div>
    <div class="sel-meta">Bryan Wong†, <b>Jongwoo Kim†</b>, Huazhu Fu, Mun Yi.</div>
    <div class="sel-venue"><span class="venue-tag" style="background:#b45309;">NeurIPS</span>Neural Information Processing Systems (NeurIPS), 2025</div>
  </div>
</div>

<div class="sel-pub">
  <img src="/images/CIKM_2025.png" alt="CIKM 2025">
  <div>
    <div class="sel-title"><a href="https://dl.acm.org/doi/10.1145/3746252.3761099">Leveraging Multi-facet Paths for Heterogeneous Graph Representation Learning.</a></div>
    <div class="sel-meta"><b>Jongwoo Kim</b>, Seongyeub Chu, Hyeongmin Park, Bryan Wong, Keejun Han, Mun Yi.</div>
    <div class="sel-venue"><span class="venue-tag" style="background:#0891b2;">CIKM Oral</span>Conference on Information and Knowledge Management (CIKM), 2025</div>
  </div>
</div>

</div>

<div class="home-section" markdown="1">

## Education

<div class="cv-row"><span><b>Ph.D.</b>, Industrial and Systems Engineering, KAIST</span><span>Aug. 2024 – Present</span></div>
<p class="cv-sub">Advisor: Prof. Mun Yong Yi</p>
<div class="cv-row"><span><b>M.S.</b>, Data Science, KAIST</span><span>Sep. 2022 – Aug. 2024</span></div>
<p class="cv-sub">Thesis: MicroMIL: Spatially Enhanced Multiple Instance Learning for Advanced Cancer Diagnosis in Microscopy. Advisor: Prof. Mun Yong Yi</p>
<div class="cv-row"><span><b>B.S.</b>, Industrial and Systems Engineering, Seoul National University of Science and Technology (Summa Cum Laude)</span><span>Feb. 2016 – Aug. 2022</span></div>
<p class="cv-sub">Advisor: Prof. Youngjung Geum</p>

</div>

<div class="home-section" markdown="1">

## Honors and Awards

<div class="cv-row"><span>Industrial and Social Issues Poster Contest, 3rd Place, KAIST</span><span>Nov. 2025</span></div>
<div class="cv-row"><span>Best Paper Award, Korea Computer Congress</span><span>Jun. 2024</span></div>
<div class="cv-row"><span>Industrial and Social Issues Poster Contest, 2nd Place, KAIST</span><span>Nov. 2022</span></div>
<div class="cv-row"><span>ETRI Human Understanding AI Paper Contest, Minister of Science and ICT Award</span><span>Jun. 2022</span></div>
<div class="cv-row"><span>Capstone Design, 2nd Place, Seoul National University of Science and Technology</span><span>Dec. 2021</span></div>
<div class="cv-row"><span>Superior Academic Performance, Seoul National University of Science and Technology</span><span>Aug. 2020 – Feb. 2022</span></div>

</div>

<div class="home-section" markdown="1">

## Academic Service

Conference reviewer for KDD 2024 and MICCAI 2025.

</div>
