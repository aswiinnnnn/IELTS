# 06 — Teardown of the Existing App (screenshots)

The app is white-labelled for **Medcity International Academy** (Kerala; IELTS/OET/German/NCLEX coaching for nurses, 18 branches) at `testprep.medcityinternationalacademy.com`. It has an "ENA Credits" wallet and an AI assistant "Ena" on mobile for speaking. Vendor unknown. Screenshots are in [screenshots/](screenshots/).

## Screen by screen

| # | Screen | What it does | Problems | What we do instead |
|---|---|---|---|---|
| [1](screenshots/1.jpg) | **Question-wise review** | Question palette grouped by question type (Summary/Notes Completion, MCQ, Matching…), each tile shows 1/0; filters by section/item type/options; Prev/Next; per-question **time spent**; "Report an issue" | Tiles show two numbers (score and Q no.) and it's unclear which is which; red/green only; no visible transcript or passage evidence; no "why is this the answer"; lots of wasted space | Review mode that **reuses the exam player**: the student sees their answer vs the key, **the passage sentence / transcript timestamp that proves it**, and an explanation. Filter "show only wrong / unattempted / slow" |
| [2](screenshots/2.jpg) | **Topic-wise scores** | Per question type: time, attempted/total, correct/total, **band score per type** | **Bands per question type are statistically meaningless**: "Sentence Completion 1/5 → Band 2", "Matching 5/5 → Band 9". A band is defined on 40 questions. 4 unattempted Listening questions aren't flagged (no negative marking, so free marks lost) | Show **accuracy % per question type**, compared with the student's own average and the batch, plus a confidence hint ("only 5 questions, practise more"). Flag **unattempted** and **spelling/word-limit** losses separately |
| [3](screenshots/3.jpg) | **IELTS scores** | Big orange "Band Score 6", bars for L7 / R5.5 / W5.5, "6 Band Score" line, disclaimer that Speaking is missing; Teacher Remarks: "System evaluated test" | The headline "6" looks like an IELTS overall but is a 3-module average (disclaimer in small print). **No Writing criterion breakdown** (TA/CC/LR/GRA). "Teacher remarks" is empty boilerplate | Headline = **gap to goal** ("NMC target: L7 ✅ R7 ❌ −1.5, W6.5 ❌ −1.0"). Writing shows 4 criterion bands per task + evidence. Teacher comment only when a human actually reviewed |
| [4](screenshots/4.jpg)/[5](screenshots/5.jpg) | **Online tests – CD-IELTS mocks** | Flat list: name, minutes, question count, "Take Test" / "View Analysis"; tabs for About IELTS, CD mocks, item-wise, sectional | No credit cost shown before starting; tooltip duplicates the name; no difficulty/status/progress; long undifferentiated list | Cards with **credit cost, duration, status (not started / in progress / done + score)**, recommended next test, "resume" for interrupted tests |
| [6](screenshots/6.jpg) | **Test history** | Table: name (truncated "IELTS Compute…"), date, Ques, Attempt, **Correct N/A**, Score, **%age N/A**, Type, Analysis | Truncated names; two columns always N/A; no per-module breakdown | Timeline of attempts with L/R/W chips, trend, filters |
| [7](screenshots/7.jpg) | **Assigned tests** | Pending/attempted/expired tabs, due-date search; empty state links to online tests and study material | Fine but bare; no notifications | Assignments with due dates + **WhatsApp reminder**; trainer sees completion per batch |
| [8](screenshots/8.jpg) | **About IELTS** | 7 strategy/intro videos, 1 each | Thin content; video-only | Short guides per question type linked from analytics ("you miss TFNG → watch this 4-min lesson → do 10 TFNG questions") |
| [9](screenshots/9.jpg) | **Dashboard "Where you stand"** | Line chart per module, "No. of tests attempted: 4", "Band scores trending towards: 1.5" | **Data bugs:** header says *Total Tests Taken: 2* but the chart shows 4 attempts, including a **band 0** (probably an abandoned/unattempted test counted as a score). Smoothed spline curve invents values between attempts. A linear trend pulled down by the 0 predicts **"trending towards 1.5"**: wrong and demoralising. "Switch to old version" button shows a half-finished migration | Exclude incomplete attempts (show them as "abandoned"). Discrete points with straight lines. **No extrapolated "trend" band**. Instead "best / latest / average of last 3" and readiness vs goal |

## Cross-cutting problems
- **Visual design:** dated Bootstrap look, low information density, inconsistent buttons, tiny fonts in tables, no dark mode, desktop-only feel.
- **Analytics honesty:** fake precision (bands from 5 questions, trend extrapolation) hurts trust with trainers who know IELTS well.
- **No goal context:** a nurse needing W6.5 for NMC sees the same generic dashboard as a Canada student.
- **No trainer/owner value visible** (these are student screens, but nothing suggests batch/branch insight exists).
- **Credits opaque:** "ENA Credits 10" is shown, but not what a test costs or how to get more.

## What's worth keeping (good ideas in the old app)
- Question palette **grouped by question type** with per-question time spent.
- **Remedial test** button (auto-generated practice from mistakes). Make it smarter.
- "Report an issue" on each question (content QA loop).
- Item-wise tests (practice by question type), not just full mocks.
- Assigned-by-centre vs all tests vs remedials split.
- Clear disclaimer that L/R/W-only averages aren't an official overall.
