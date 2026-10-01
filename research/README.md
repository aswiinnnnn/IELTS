# IELTS SaaS for Indian Coaching Centres — Research Pack

Researched 2026-10-01. Scope of the first build: **Listening, Reading, Writing** (Academic + General Training) with AI evaluation. Speaking comes later.
Business model: B2B2C SaaS. Centres buy **credits**, students get logins, and credits are consumed per test.

## Files

| File | What's inside |
|---|---|
| [01-ielts-test-format.md](01-ielts-test-format.md) | Module formats, all question types, CD-IELTS interface features we must replicate, 2026 changes (paper ends), One Skill Retake |
| [02-scoring-criteria.md](02-scoring-criteria.md) | Overall band rounding, L/R raw→band tables (Ac + GT), answer-matching rules, **full official Writing band descriptors (May 2023)**, measurable proxies per criterion |
| [03-ai-scoring-research.md](03-ai-scoring-research.md) | LLM essay-scoring research and accuracy numbers, public datasets, proposed scoring pipeline, quality targets, **cost per evaluation** |
| [04-market-india.md](04-market-india.md) | Demand collapse data, segments (Kerala nurses!), regulator targets (NMC/NMBI/AHPRA), centre economics, payments, WhatsApp, DPDP Act |
| [05-competitors.md](05-competitors.md) | Gurully, Alfa IELTS, ScoreMentor, ielts.camp, Leap Scholar, Writing9…, feature matrix, where we can win |
| [06-existing-app-teardown.md](06-existing-app-teardown.md) | Screen-by-screen critique of the sample app (bugs, UX gaps, ideas worth keeping) |
| [07-product-brainstorm.md](07-product-brainstorm.md) | Roles, feature ideas by area, **credits system design**, MVP scope, design direction, open questions |
| [08-content-strategy.md](08-content-strategy.md) | Copyright constraints, content volumes, AI-assisted content pipeline (reading, listening TTS, generated Task 1 charts) |
| [sources/](sources/) | Official Writing band descriptors PDF + extracted text, two research PDFs |
| [screenshots/](screenshots/) | The 9 screenshots of the existing app |

## Ten things that should shape the product

1. **Indian IELTS demand is down sharply.** IDP India volumes fell 42% (FY24), 50% (FY25), then another 27% in the half-year to Dec 2025, mainly because of Canada's study-permit caps. Our centres are cost-squeezed, so **pay-as-you-go credits** fit. Centres are also diversifying, so design the content model **exam-agnostic** (PTE/OET/German later).
2. **The healthcare segment is resilient.** Kerala nurses heading to the UK, Ireland and Australia need IELTS Academic **L/R/S 7, W 6.5**. The sample app's owner (Medcity, 18 branches) is exactly this customer. A **"goal presets"** feature (NMC/NMBI/AHPRA) is cheap and differentiating.
3. **From mid-2026 IELTS is computer-only.** A pixel-faithful CD-IELTS player (timer alerts, highlight/notes, split view, navigator, word count, 2-min listening review) is table stakes.
4. **Zero-shot "give me a band" LLM scoring is around ±1 band off.** That's not good enough. Use anchors, per-criterion scoring with evidence, repeat sampling, a pinned model, and a **trainer review queue for low-confidence scripts**.
5. **Trainer overrides are the moat.** They build a calibration dataset of Indian students' essays that no competitor publishes against.
6. **Honest analytics beat fake precision.** The old app shows bands from 5 questions, counts abandoned tests as 0, and predicts "trending to 1.5". Show accuracy %, ranges and gap to goal instead.
7. **AI cost is low but not zero.** About ₹10–25 per AI-scored writing task and about ₹0 for L/R. Price credits per action accordingly.
8. **Content is the hardest problem.** Cambridge/official material can't be used commercially. Plan for original, AI-assisted, expert-reviewed content. Generate Task 1 charts from data so the AI can fact-check the descriptions.
9. **India specifics:** WhatsApp notifications (₹0.12/utility message), Razorpay + GST invoices, low-end Android practice + desktop/lab mocks, explanations in regional languages, and **DPDP parental consent for under-18s**.
10. **Competitors already exist** (Gurully claims 2,100+ institutes; Alfa sells non-expiring credits). Win on **trainer time saved, trustworthy scoring, owner analytics, modern UX, and the healthcare vertical**, not on mock count.

## Next steps (suggested)
1. Answer the open questions in [07 §7](07-product-brainstorm.md#7-open-questions-for-the-founders) (design partner, content approach, pricing).
2. Interview 5–10 centre owners/trainers (Kerala + Punjab) to validate credit pricing and the trainer-queue idea.
3. Build the calibration set early (200 double-marked essays). It gates the AI-scoring launch.
4. Then write the PRD and the data model, and pick a stack.
