# 01 — IELTS Test Format (what our test player must replicate)

> Scope for the current build: **Listening, Reading, Writing** (Academic + General Training). Speaking is noted for later.
> Last researched: 2026-10-01.

## 1. Big picture

| Module | Academic | General Training | Time (computer-delivered) | Questions |
|---|---|---|---|---|
| Listening | same | same | ~30 min audio + **2 min review** (no 10-min transfer time on computer) | 40 (4 parts × 10) |
| Reading | 3 long academic texts | 3 sections, everyday → workplace → general interest | 60 min | 40 |
| Writing | Task 1 = describe visual data/process (150 w) + Task 2 essay (250 w) | Task 1 = **letter** (150 w) + Task 2 essay (250 w) | 60 min | 2 tasks |
| Speaking (later) | same | same | 11–14 min, face-to-face | 3 parts |

- Listening, Reading and Writing are taken together on the same day; Speaking is separate.
- The existing app lists mocks as "151 Min / 82 Ques": 30 + 60 + 60 min ≈ 150, 40 + 40 + 2 writing tasks = 82.

## 2. Listening

- 4 parts, 10 questions each, **audio played once only**.
- Parts 1–2: everyday social situations (Part 1 = conversation, e.g. booking or enquiry; Part 2 = monologue, e.g. a tour guide).
- Parts 3–4: education/training (Part 3 = discussion between up to 4 people, e.g. students and a tutor; Part 4 = academic lecture monologue, **no break in the middle**).
- Accents: British, Australian, New Zealand, North American (2026 blogs claim more "modern" contexts like video calls and podcasts. This isn't confirmed officially).
- **Computer version:** answers are typed while listening; 2 minutes to review at the end. Paper had 10 minutes to transfer answers.

**Question types** (ielts.org):
1. Multiple choice (single answer, or choose TWO/THREE from a list)
2. Matching
3. Plan / map / diagram labelling
4. Form / note / table / flow-chart / summary completion
5. Sentence completion
6. Short-answer questions

## 3. Reading

**Academic:** 3 texts, 2,150–2,750 words in total, taken from books, journals, magazines and newspapers and written for non-specialists. Texts may be narrative, descriptive or argumentative, and may include diagrams.

**General Training:**
- Section 1, social survival: 2–3 short texts (notices, ads, timetables)
- Section 2, workplace survival: 2 texts (job descriptions, contracts, training material)
- Section 3, general interest: 1 long text

**Question types** (official list, 11 families; prep sites split them into 14):

| # | Type | Skill tested | Marking notes |
|---|---|---|---|
| 1 | Multiple choice | detail + gist | single letter, or a set of letters (order-free) |
| 2 | True / False / Not Given | factual information | most-failed type; "NG" vs "False" is the classic trap |
| 3 | Yes / No / Not Given | writer's opinions/claims | |
| 4 | Matching information (which paragraph contains…) | scanning | letters can repeat |
| 5 | Matching headings | main idea vs detail | list has more headings than paragraphs |
| 6 | Matching features (people/dates → statements) | relationships | |
| 7 | Matching sentence endings | main ideas | |
| 8 | Sentence completion | detail | word limit ("NO MORE THAN TWO WORDS") |
| 9 | Summary / note / table / flow-chart completion | detail / main idea | from text OR from a word box |
| 10 | Diagram label completion | relating text to a visual | |
| 11 | Short-answer questions | specific facts | word limit |

The Academic and GT conversion tables differ (GT needs more correct answers for the same band). See [02-scoring-criteria.md](02-scoring-criteria.md).

## 4. Writing

| | Task 1 | Task 2 |
|---|---|---|
| Min words | 150 | 250 |
| Suggested time | 20 min | 40 min |
| Weight | 1× | **2×** ("Task 2 contributes twice as much as Task 1") |
| Academic | Describe a graph, table, chart, map or process diagram. Needs an **overview** and key features with data | Essay: opinion / discussion / problem–solution / advantages–disadvantages / two-part question |
| General Training | **Letter** (formal / semi-formal / informal) covering **3 bullet points** | Essay (same types, slightly more personal topics) |
| Criteria | Task **Achievement**, CC, LR, GRA | Task **Response**, CC, LR, GRA |

GT letter conventions (the AI should check these for Task Achievement and tone):

| Type | Recipient | Opening | Closing |
|---|---|---|---|
| Formal | name unknown | Dear Sir/Madam | Yours faithfully |
| Semi-formal | surname known | Dear Mr Brown | Yours sincerely |
| Informal | friend | Dear Sam / Hi Sam | Best wishes / Take care |

## 5. Computer-delivered (CD-IELTS) interface — must-have features of our player

These come from the official familiarisation test and IDP/British Council descriptions:

- **Countdown timer** that flashes/alerts at **10 min and 5 min** remaining.
- **Highlight** text (passage and questions) and **notes** attached to highlights.
- **Split screen**: passage on the left, questions on the right, each scrolling independently.
- **Navigation bar** at the bottom showing every question number, answered vs unanswered, and a **flag for review** marker. Clicking a number jumps to that question.
- **Live word count** in Writing.
- Listening: typed answers during the audio; volume control; **no pause or rewind**; 2-minute review at the end.
- Drag-and-drop for some matching types; radio buttons and checkboxes for MCQ; text inputs for completion.
- Writing: plain text editor (no spell check, no autocorrect, no grammar hints — this is critical for realism).
- Official free familiarisation test (untimed) for UI reference: <https://ielts.idp.com/about/ielts-familiarisation-tests>

> Product implication: the closer our player is to the real thing, the more trainers trust it. This is the #1 credibility signal for coaching centres. Competitors advertise "pixel-perfect CD-IELTS simulation".

## 6. 2026 changes (verified against ielts.org)

| Change | Status | Source |
|---|---|---|
| **Paper-based IELTS ends from mid-2026**; all tests are delivered on computer (last paper date in most markets: 27 June 2026) | ✅ Official | [ielts.org – Updates to test delivery](https://ielts.org/news-and-insights/updates-to-ielts-test-delivery) |
| New **"Writing on Paper"** option in some markets: Listening/Reading on computer, Writing handwritten | ✅ Official (IDP India lists "IELTS on Computer (Writing on Paper)") | same |
| One Skill Retake also available for Writing on Paper (same delivery mode) | ✅ Official | same |
| Test construct, skills and score interpretation **unchanged** | ✅ Official | same |
| UKVI SELT only in fully digital format | ✅ Official | same |
| "Writing now strictly penalises templates" | ⚠️ Blog claim. The 2023 descriptors *already* penalise memorised/formulaic language (LR band 4–3) | PW/Shiksha blogs |

**Implication:** CD-IELTS is now *the* IELTS. A CD-faithful player is mandatory, not a nice-to-have. Consider a **"handwritten writing" practice mode** (student uploads a photo of handwritten script → OCR → AI score) for students choosing Writing on Paper. Mark this P2.

## 7. One Skill Retake (OSR) — relevant for analytics

- Launched in India June 2024 (first at Bathinda, Punjab), now in ~47 Indian locations. Computer-delivered only.
- Fee ~₹12,650 (2026) vs full test ₹19,000 (from 1 Apr 2026, GST included; UKVI ₹19,250).
- **Product hook:** a "Retake advisor". If a student has a past real score (e.g. L7 R7 W6 S7), the platform focuses them on the single skill to retake.

## 8. Speaking (deferred — notes for later)

- Part 1, 4–5 min: familiar topics. Part 2, 3–4 min: cue card with 1 min prep and up to 2 min talk. Part 3, 4–5 min: abstract discussion.
- Criteria: Fluency & Coherence, Lexical Resource, Grammatical Range & Accuracy, Pronunciation (equal weight).
- The existing app (screenshots) routes speaking to a mobile AI assistant "Ena", so the market already expects AI speaking.

## Sources
- [IELTS Academic format in detail – ielts.org](https://ielts.org/organisations/ielts-for-organisations/test-types/ielts-academic-test/academic-test-format-in-detail)
- [IELTS GT Reading format – ielts.org](https://ielts.org/take-a-test/test-types/ielts-general-training-test/ielts-general-training-format-reading)
- [IELTS GT Writing format – ielts.org](https://ielts.org/take-a-test/test-types/ielts-general-training-test/ielts-general-training-format-writing)
- [Updates to IELTS test delivery – ielts.org](https://ielts.org/news-and-insights/updates-to-ielts-test-delivery)
- [IDP – 5 key features of IELTS on computer](https://ielts.idp.com/nepal/about/news-and-articles/article-key-features-of-ielts-on-computer)
- [British Council – IELTS on computer changes](https://takeielts.britishcouncil.org/blog/ielts-on-computer-changes-updates)
- [MOSAIC – CD IELTS tips (timer flashes at 10/5 min)](https://engage.mosaicbc.org/blog/a-look-at-the-computer-delivered-ielts-ytpl6)
- [IDP familiarisation tests](https://ielts.idp.com/about/ielts-familiarisation-tests)
- [IDP – One Skill Retake launches in India](https://careers.idp.com/news/-IELTS-One-Skill-Retake-launches-in-India)
- [IDP India – test fee](https://ieltsidpindia.com/information/ielts-test-fee) · [PW – fee ₹19,000](https://www.pw.live/study-abroad/ielts/exams/ielts-exam-fees)
- [Kanan – 14 reading question types](https://www.kanan.co/ielts/academic/reading/question-types/)
- [IDP – GT Task 1 letter](https://ielts.idp.com/prepare/article-ielts-general-training-writing-task-1-write-a-letter)
