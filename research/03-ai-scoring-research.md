# 03 — AI Scoring: Research, Accuracy Evidence, Proposed Pipeline, Cost

> Goal: AI writing evaluation that coaching-centre trainers **trust** (they'll compare it with their own marking on day one). Listening and Reading need no AI. They're deterministic answer-key marking.

## 1. What the research says (2024–2026)

| Finding | Number | Source |
|---|---|---|
| Zero-shot LLMs give only **moderate** agreement with human raters | QWK ≈ 0.68 typical | arXiv / ACL survey results |
| GPT-4o vs official IELTS examiner scores (with example essays in the prompt) | r = 0.71, **RMSE ≈ 1.05 bands** | PACLIC 2024 "LLMs for L2 English writing" |
| Fine-tuned models beat bigger zero-shot models | fine-tuned GPT-3.5 QWK 0.78 vs zero-shot GPT-4 lower (TOEFL data) | same body of work |
| **Anchor essays** (scored examples across the *full* band range) are the strongest prompt lever; anchors across the whole scale beat anchors at a few levels; 30–100 anchors recover most recoverable error | — | "Anchor is the key" (ScienceDirect 2026); NHSJS 2026 |
| **Halo effect**: a high score on one criterion inflates the others | — | "LLM Judges as Raters" audit (arXiv 2608.29517) |
| **Version instability**: the same essays get different score distributions after model updates | — | same audit; also GPT-4 temporal drift in other studies |
| Test–retest variance: the same essay scored twice can differ | — | same audit; ERIC study on ChatGPT (21 essays) recommends human oversight |
| A small transformer (DistilBERT + features) trained on 1,200 Kaggle essays reached MAE 0.67, **45% within ±0.5 band, 75% within ±1.0**; under-predicts 8–9 | — | arXiv 2512.24460 (IELTS revision platform) |
| Conservative feedback (grammar/spelling fixes) produced reliable improvement; aggressive coherence rewrites *hurt* | +0.15 vs −0.05 bands | same paper |
| Fine-tuned Llama-3 (M-LoRA) + human-feedback PPO for IELTS scoring | — | Nature Sci. Reports 2026 |

**Takeaways**
1. A raw "here is the rubric, give a band" prompt is **not good enough**. Expect ±1 band error, which trainers will notice immediately.
2. The fixes are known: **anchors + per-criterion evaluation + evidence-first reasoning + repeat sampling + model version pinning + human calibration set**.
3. Position AI as **"trainer assistant"**, not "examiner replacement". Low-confidence scores go to a trainer queue. This is also the honest marketing line, and it's what Gurully/Alfa do ("AI & Trainer Evaluation").
4. Every trainer override is labelled training/calibration data. That's our **data flywheel and moat**: thousands of Indian-student essays with trainer bands.

## 2. Public datasets (for calibration & evaluation, check licences before commercial use)

| Dataset | Size | Notes |
|---|---|---|
| [Kaggle – IELTS Writing Scored Essays](https://www.kaggle.com/datasets/mazlumi/ielts-writing-scored-essays-dataset) | ~1,200 (≈500 T1, ≈700 T2) | prompt, essay, overall score |
| HuggingFace IELTS T2 set (referenced in ACL paper) | ~10,324 T2 essays | prompt, essay, comments, band |
| [KevSun/IELTS_essay_scoring](https://huggingface.co/KevSun/IELTS_essay_scoring) | model trained on ~18,000 essays | outputs per-criterion scores. Useful as a 2nd opinion/baseline |
| [Jackrong/IELTS-writing-feedback-reasoning](https://huggingface.co/datasets/Jackrong/IELTS-writing-feedback-reasoning) | — | T2 with reasoning-style feedback |
| [upmyielts/ielts-writing-feedback1](https://huggingface.co/datasets/upmyielts/ielts-writing-feedback1) | — | feedback + bands |
| [chillies/mistral-7b-ielts-evaluator](https://huggingface.co/chillies/mistral-7b-ielts-evaluator-q4) | model | open-weights evaluator baseline |

⚠️ Scores in public sets are often self-reported or scored by teachers, not official. Use them for **evaluation and sanity checks**, not as ground truth. Our real ground truth = **a calibration set double-marked by senior trainers (ideally ex-examiners) at partner centres**.

## 3. Proposed writing-evaluation pipeline

```
submit ─► 1. deterministic pre-checks ─► 2. feature extraction ─► 3. LLM criterion scoring (×N)
                                                                          │
         6. trainer review queue ◄── 5. confidence & aggregation ◄────────┘
                    │                          │
                    └──► overrides saved ──► calibration set / regression tests
                                               │
                                     4. feedback generation (separate call)
```

**1. Pre-checks (no LLM, instant)**
- Word count (CD-IELTS counts like a word processor). ≤20 words → band 1 everywhere. Flag under-length.
- Copied-rubric detection: n-gram overlap with the prompt. Strip copied text before scoring.
- Language detection (non-English → 0). Empty or gibberish detection.
- **Template/memorised detection:** similarity against a library of common Indian-coaching templates ("In this contemporary era…", "This essay will discuss…"). Feeds LR. Show the student *why* it's penalised.
- Paste-event and typing-timeline flags from the editor (for trainers; not a score input).

**2. Feature extraction (cheap, explainable)**
- LanguageTool (self-hostable, open source): grammar, spelling, punctuation errors with categories → errors per 100 words, % error-free sentences.
- Lexical: MTLD/type-token, share of words above CEFR B2 (word lists), repetition.
- Syntax: sentence length variety, subordinate-clause ratio (spaCy dependency parse).
- Cohesion: linker inventory and density, paragraph count.
- Academic Task 1: compare numbers mentioned with the **source data of the chart** (we own it if we generate charts) → factual-accuracy signal for TA. Check for an overview sentence.
- GT Task 1: bullet-point coverage (each of the 3 bullets addressed?), register (salutation/closing matches formal/semi/informal).

**3. LLM criterion scoring**
- **One criterion per pass** (or strictly separated sections with evidence quoted *before* each band), to reduce the halo effect.
- Cached system prompt = official descriptors (section 5–9 of [02](02-scoring-criteria.md)) + **anchor essays covering bands 4–9** with expert rationales + the computed features as "evidence hints".
- Structured output (JSON schema): `{criterion, evidence_quotes[], strengths[], issues[], band:int}`.
- Bands are integers per criterion (as examiners do).
- **Run N = 3 samples** (or 2 different models). Take the median per criterion.

**4. Feedback generation (separate call, can use a cheaper model)**
- Top 3 priorities to reach the target band ("To move LR from 6 → 7: …").
- Inline corrections (from LanguageTool + LLM), each tagged by type.
- One improved paragraph (not a full rewrite; full rewrites encourage memorisation and the research shows aggressive rewrites don't help).
- **Indian-English error patterns** called out explicitly: articles (a/an/the), present continuous for permanent states ("I am living in…"), "discuss about", "revert back", "passed out" (= graduated), prepositions, subject–verb agreement, "If people will…" conditionals, tense shifts.
- Optional explanation summary in the student's language (Malayalam / Hindi / Punjabi / Gujarati / Tamil / Telugu). The essay feedback itself stays in English.

**5. Confidence & routing**
- Confidence is low when: sample spread ≥ 1 band on any criterion, the result sits on a borderline (e.g. 6.25/6.75 averages), it disagrees with the feature-based baseline model by ≥ 1 band, or the essay is very short or off-topic.
- Low confidence → show "Provisional score — your trainer will review" and put it in the trainer queue, ordered by priority.
- Always display **criterion bands + a range** (e.g. "Writing 6.0–6.5"), never false precision.

**6. Trainer review**
- Side-by-side: essay with highlights | AI criterion bands + evidence | override per criterion + comment (voice note optional) → student notified.
- Each override is stored with `(essay, AI bands, trainer bands, model_id, prompt_version)`.

## 4. Quality targets & monitoring (define before launch)

| Metric | Target for launch | How |
|---|---|---|
| Exact criterion agreement with senior trainer | ≥ 50% | calibration set ≥ 200 essays, double-marked |
| Writing band within ±0.5 of trainer | **≥ 80%** | same |
| MAE (writing band) | ≤ 0.5 | same |
| QWK per criterion | ≥ 0.70 | same |
| Test–retest (same essay, 2 runs) identical band | ≥ 90% | nightly job |
| Drift alarm | mean shift > 0.25 band on regression set | run on every prompt/model change |

- **Pin the model ID** and version the prompt. Store `model_id + prompt_version` with every score so we can tell scores apart across versions.
- Publish accuracy numbers to centres (honesty is the differentiator; competitors claim "98% accuracy" with no method).

## 5. Cost estimate per evaluation (Claude API, prices cached 2026-09-25)

| Model | Input $/MTok | Output $/MTok | Cache read $/MTok |
|---|---|---|---|
| Claude Opus 5.5 (`claude-opus-5-5`) | 4.00 | 20.00 | 0.20 |
| Claude Sonnet 5.5 (`claude-sonnet-5-5`) | 2.00 | 10.00 | 0.20 |
| Claude Haiku 4.5 (`claude-haiku-4-5`) | 1.00 | 5.00 | — |

Batch API = 50% off (fine for "results in a few minutes" flows, not for instant feedback).

**Assumptions for one Task 2 scoring pass:** about 8k tokens of cached prompt (descriptors + anchors), 1k uncached (essay + features + instructions), about 3k output (reasoning + JSON).

| | Per pass | × 3 samples + 1 feedback call | ≈ ₹ (₹88/$) |
|---|---|---|---|
| Sonnet 5.5 | 8k×0.20 + 1k×2 + 3k×10 ≈ **$0.034** | ≈ $0.13 | **≈ ₹11 per task** |
| Opus 5.5 | ≈ $0.067 | ≈ $0.27 | ≈ ₹24 per task |

→ **A full Writing test (T1 + T2) costs roughly ₹15–50 in AI** depending on model and samples. Cut cost by sampling twice and adding a 3rd sample only when the first two disagree, using the Batch API for non-urgent mocks, and keeping prompts cacheable. Listening/Reading cost ≈ ₹0 in AI. **This matters for credit pricing** (see [07](07-product-brainstorm.md)).
⚠️ Thinking tokens bill as output. Measure real usage on 50 essays before fixing prices.

## 6. Speaking (later) — notes
- Pipeline: record → speech-to-text (with timestamps, filler words, pauses) → fluency metrics (words/min, pause rate, self-corrections) → pronunciation assessment API (e.g. Azure Pronunciation Assessment) → LLM scoring of FC/LR/GRA from the transcript.
- **Fairness risk:** pronunciation models can penalise Indian accents. IELTS rewards intelligibility, not native-like accent (mother-tongue *influence on clarity* is the issue, e.g. TH→T/D, V/W merging, "ischool"). Must validate on Indian speakers.

## Sources
- [PACLIC 2024 – LLMs for L2 English writing (GPT-4o vs Llama-3 on IELTS)](https://aclanthology.org/2024.paclic-1.36.pdf)
- [LLM Judges as Raters – audit of severity, halo, reliability, version instability (arXiv 2608.29517)](https://arxiv.org/pdf/2608.29517) (local copy in `sources/`)
- [Anchor is the key – LLM AES through prompting (ScienceDirect 2026)](https://www.sciencedirect.com/science/article/pii/S1075293526000413)
- [Prompt design for LLM essay scoring: rubrics to calibration (NHSJS 2026)](https://nhsjs.com/2026/prompt-design-for-llm-essay-scoring-from-rubrics-to-calibration/)
- [IELTS Writing Revision Platform with AES + adaptive feedback (arXiv 2512.24460)](https://arxiv.org/html/2512.24460v1)
- [Reliability of ChatGPT in grading IELTS (ERIC EJ1457168)](https://files.eric.ed.gov/fulltext/EJ1457168.pdf) (local copy in `sources/`)
- [Enhancing IELTS writing AES with M-LoRA Llama-3 + PPO (Nature Sci. Rep.)](https://www.nature.com/articles/s41598-026-43318-w)
- [Exploring LLM autoscoring reliability with Generalizability Theory (arXiv 2507.19980)](https://arxiv.org/pdf/2507.19980)
- [LLMs can perform multi-dimensional analytic writing assessment (arXiv 2502.11368)](https://arxiv.org/pdf/2502.11368)
- [First-language bias in LLM AES on TOEFL essays (arXiv 2607.14605)](https://arxiv.org/pdf/2607.14605). Relevant to Indian L1 fairness
- [EssayJudge benchmark (arXiv 2502.11916)](https://arxiv.org/pdf/2502.11916)
- Indian-English error patterns: [IDP – common grammar mistakes](https://ielts.idp.com/canada/prepare/article-common-grammar-mistakes), [amirulkhan.in – 45 Indian English errors](https://www.amirulkhan.in/english/indian-english-errors), [TalkDrill – Indian pronunciation](https://www.talkdrill.com/blog/pronunciation/indian-english/indian-english-pronunciation/)
- Claude pricing: Anthropic API model table (cached 2026-09-25, via the claude-api skill)
