# 08 — Content Strategy (the hidden hardest problem)

A test platform is only as good as its question bank. Competitors advertise volume: Gurully 30k+ practice questions, Alfa 10k+, Leap 80+ mocks.

## 1. Copyright: we can't use Cambridge / official material

- IELTS material is owned by the IELTS Partners (British Council, IDP, Cambridge University Press & Assessment) and is for **personal, non-commercial use only**. Posting Cambridge IELTS book exercises on a website **infringes copyright even with credit**.
- Many Indian centres photocopy Cambridge books and some platforms host them. That's a legal risk we must not take on, and a liability if centres upload such material to us.
- **Policy for centre-uploaded content:** an upload attestation ("I own or have rights to this content"), a takedown process (Indian IT Act intermediary safe-harbour needs a grievance officer + takedown), and **tenant-private visibility only** (never shared across tenants).
- Legitimate options: (1) original content written by us, (2) AI-assisted original content with expert human QA, (3) licensing from publishers/authors, (4) official free familiarisation material **linked, not copied**.

## 2. Content we need for v1

| Asset | Quantity (v1 target) | Notes |
|---|---|---|
| Listening full tests | 15 (×4 parts, 40 Qs) | scripts + multi-speaker audio + maps/diagrams |
| Academic Reading tests | 10 (×3 passages, 40 Qs) | 700–900-word passages, academic register |
| GT Reading tests | 5 | notices/ads, workplace docs, 1 long text |
| Writing Academic T1 | 40+ | charts (line, bar, pie, table, mixed), maps, process diagrams |
| Writing GT T1 letters | 30+ | formal / semi-formal / informal × 3 bullets |
| Writing T2 prompts | 80+ | opinion, discussion, problem–solution, adv/disadv, two-part; topic spread |
| Item-wise banks | ~50 items per question type | for remedial/adaptive practice |
| Anchor essays (for AI calibration) | 100+ T1/T2 scripts with trainer-agreed bands 4–9 | from pilot centres (with consent) |

## 3. AI-assisted generation pipeline (with humans in the loop)

**Reading**
1. Topic plan (science, history, environment, psychology, technology, health, matching the IELTS spread; GT: workplace/social).
2. Draft an original passage (target word count, academic register, paragraphs labelled A–H for matching tasks).
3. Generate questions per type with an **answer key + evidence span** (character offsets in the passage).
4. **Automatic validation by a second model:** is each question answerable *only* from the passage? Exactly one correct answer? TFNG "Not Given" really not given? Do word-limit answers appear verbatim?
5. Expert human review (an ex-trainer) → publish.
6. After launch: **item statistics** (p-value = % correct, discrimination, time) → retire bad items, calibrate the band tables for each test.

**Listening**
1. Script with speakers, accents, distractors (IELTS loves self-corrections: "on the 13th… no, sorry, the 30th").
2. Questions + key + **timestamp evidence**.
3. Multi-speaker TTS with **British, Australian, NZ and North American** voices; add the standard spoken instructions ("You will hear… First you have some time to look at questions 1 to 5"), pauses, page-turn timing.
   - ElevenLabs: $0.011–0.08 per 1k characters (v3 multi-speaker dialogue $0.08/1k chars); Azure Neural TTS ~$15–30 per 1M characters with 0.5M free/month. **A full 30-min Listening test ≈ 25–30k characters → under ~$2.50 even at the top rate.** Cost isn't the issue; naturalness is. Review every file by ear.
   - Check the TTS licence allows commercial redistribution of the audio.
4. Maps/plans/diagrams: generate as SVG (deterministic, editable) rather than with image models.

**Writing Task 1 (Academic)**: **generate the data, then render the chart programmatically** (Vega/matplotlib). Benefits: unlimited variety, exact styling control, and **ground-truth numbers the AI scorer can check** (did the student report figures correctly? did they identify the main trend for the overview?). Process diagrams and maps: hand-made SVG templates.

**Writing T2 prompts**: low risk to generate; humans curate for topic balance and for realistic IELTS phrasing.

## 4. Quality bar (trainers will judge us by this)
- Zero answer-key errors in published tests: run "Report an issue" (keep it from the old app) → SLA to fix → auto-regrade affected attempts.
- Difficulty consistency between mocks (otherwise students see random band swings and lose faith).
- Style fidelity: instructions worded exactly like IELTS ("Write NO MORE THAN TWO WORDS AND/OR A NUMBER for each answer.").

## 5. Content data model (keep it exam-agnostic for PTE/OET later)
`Exam → Test → Section/Part → Stimulus (passage/audio/image) → QuestionGroup (type + instructions + word limit) → Question (prompt, options, accepted answers[], evidence ref, explanation)`. Store the band conversion table per test.

## Sources
- [IELTS copyright & trade mark statement](https://ielts.org/legal/ielts-copyright-and-trade-mark-statement)
- [Cambridge – copyright](https://www.cambridge.org/us/legal/copyright)
- [Avvo – posting Cambridge IELTS exercises online](https://www.avvo.com/legal-answers/can-i-post-exercises-in-ielts-cambridge-books-on-a-2337568.html)
- [ElevenLabs API pricing](https://elevenlabs.io/pricing/api) · [ElevenLabs vs Azure 2026](https://aloa.co/ai/comparisons/ai-voice-comparison/elevenlabs-vs-azure-speech) · [Speechmatics – best TTS APIs](https://www.speechmatics.com/company/articles-and-news/best-tts-apis-in-2025-top-12-text-to-speech-services-for-developers)
- Volume benchmarks: [Gurully](https://www.gurully.com/), [Alfa IELTS](https://alfaielts.com/ielts-for-businesses), [Leap Scholar](https://leapscholar.com/blog/ielts-prep-by-leap-scholar-app/)
