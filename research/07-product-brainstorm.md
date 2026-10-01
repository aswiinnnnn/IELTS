# 07 — Product Brainstorm: SaaS for Indian IELTS Coaching Centres

> Working name: TBD. Model: **B2B2C**. We sell to coaching centres. Centres buy **credits** and give their students logins. Students spend credits by taking tests. Speaking is out of scope for v1.

## 1. Users & roles

| Role | Who | Core job | What they need from us |
|---|---|---|---|
| **Platform admin** (us) | our team | run the SaaS | tenants, content bank, credit pricing, AI cost/accuracy monitoring, support impersonation (audited) |
| **Centre owner** | e.g. Medcity MD (18 branches) | grow enrolments, prove results, control cost | branch & batch performance, credit usage/spend, "students exam-ready", marketing-ready results, branding |
| **Branch manager / counsellor** | per branch | onboard students, sell courses | bulk student import, allocate credits, batch creation, low-credit alerts |
| **Trainer** | faculty | teach, assign, evaluate writing | assign tests to batches, **writing review queue**, batch weakness heatmap, override AI scores, comment |
| **Student** | nurse (Kerala), student-visa or PR aspirant | reach target band, fast | realistic mocks, instant honest feedback, clear next step, goal tracker, mobile practice |
| **Parent** (optional) | for under-18 students | consent, progress | DPDP consent flow, WhatsApp progress summaries |

Hierarchy: **Tenant (centre brand) → Branches → Batches → Students**, with trainers assigned to batches.

## 2. Feature ideas, grouped (★ = MVP candidate)

### A. Test experience
- ★ **CD-IELTS-faithful player** (timer alerts at 10/5 min, highlight + notes, split view, question navigator with flags, word count, listening plays once, 2-min review). See [01 §5](01-ielts-test-format.md).
- ★ Full mock (L+R+W), **sectional** (one module), **item-wise** (one question type, e.g. 10 TFNG), **timed vs practice mode** (practice = untimed, instant check per question).
- ★ Autosave every answer; **resume after disconnect**; audio pre-buffered before the timer starts.
- Centre **lab mode**: trainer starts a synchronous mock for a batch; fullscreen; headphone check; attendance.
- Writing-on-paper practice: upload a photo of the handwritten script → OCR → AI score (matches the 2026 "Writing on Paper" option). *P2*
- Accessibility: font size, high contrast (IELTS on computer also offers colour/size settings).

### B. Scoring & feedback
- ★ Instant L/R marking with an accepted-answer list, word-limit and spelling rules ([02 §3](02-scoring-criteria.md)).
- ★ **AI writing evaluation**: 4 criterion bands per task, quoted evidence, inline corrections, top-3 priorities to the target band, one improved paragraph, confidence + range. See [03](03-ai-scoring-research.md).
- ★ **Trainer review queue** sorted by AI confidence; one-click accept or per-criterion override + comment (text/voice).
- ★ **Review mode**: every L/R question shows the student's answer, the key, the **evidence sentence highlighted in the passage / the transcript timestamp**, and an explanation.
- Indian-English error coach: tracks each student's recurring errors (articles, tenses, prepositions) across essays → personalised micro-drills.
- Spelling/word-limit loss report for Listening ("you lost 3 marks to spelling: 'accommodation', 'February'…").
- Template detector: "this opening looks memorised. Examiners penalise this under Lexical Resource".

### C. Analytics (honest by design)
- ★ **Goal presets**: NMC UK, NMBI Ireland, AHPRA Australia, UKVI, university 6.5, Canada CLB… → per-module gap to target ([04 §2](04-market-india.md)).
- ★ Student dashboard: latest / best / average-of-last-3 per module; **accuracy by question type** (not bands); time per question; unattempted count.
- ★ Trainer: **batch heatmap** (students × question types), who's falling behind, who hasn't practised in 7 days, pending reviews.
- ★ Owner: branch comparison, credits consumed vs students active, **"exam-ready" count** (students at/above goal on their last 2 mocks), trend over months.
- Readiness predictor: "likely band range in the real test" from recent mocks (shown as a range, with N).
- Never: per-type bands, extrapolated trends, abandoned tests counted as 0 (all were bugs in the old app, see [06](06-existing-app-teardown.md)).

### D. Practice & learning
- ★ **Remedial sets**: auto-built from the student's weakest question types (old app had this; make it adaptive).
- Short lessons per question type (text + 3-min video), linked from analytics.
- Vocabulary from the student's own mistakes and from passages (spaced repetition).
- Writing Task 1 chart generator → unlimited Task 1 practice with known ground truth.
- Daily streaks and goals (light gamification. The audience is adults with a deadline, so keep it practical).

### E. Centre operations
- ★ Multi-tenant + **white-label** (logo, colours, centre name, subdomain `centre.ourapp.in`; custom domain later).
- ★ Bulk student import (CSV/Excel), batch management, trainer assignment, assignments with due dates.
- ★ **Credits wallet & ledger** (see §3).
- ★ Notifications: email + **WhatsApp** (test assigned, due tomorrow, result ready, trainer reviewed, low credits).
- Student lifecycle: active / completed course / archived (archived students don't count toward anything, and their data is retained or deleted per policy).
- Exportable reports (PDF result card with the centre's branding; CSV).
- Content: centres can add **their own questions/tests** (with a copyright attestation; see [08](08-content-strategy.md)).

### F. Platform / compliance
- ★ DPDP: consent capture, age gate + parent consent for under-18, data export/delete, processor agreement with centres.
- ★ Audit log (score overrides, credit movements, impersonation).
- ★ AI cost & accuracy dashboard (internal).
- Integrations: Classplus/Teachmint deep links, webhook API, Google SSO. *Later*

## 3. Credits system design

**Principles:** transparent, never surprising, simple enough for a branch manager.

- **Wallet hierarchy:** Tenant wallet → (optional) branch allocation → student allocation. Allocation is a ledger *transfer*, not a copy.
- **Immutable ledger:** every movement is a row (`purchase`, `allocate`, `reserve`, `consume`, `refund`, `expire`, `adjust`) with actor, reason and balance-after. Balances are derived from the ledger (or checked against it). Credits are money, so no silent edits.
- **Reserve on start → consume on submit/score.** If the platform fails (audio didn't load, AI error), refund automatically. If the student abandons, the trainer can refund (configurable).
- **Price list (credits per action), example hypothesis:**

| Action | Our marginal cost | Credits (hypothesis) |
|---|---|---|
| Item-wise practice set (L/R) | ~₹0 | 0 (free, drives engagement) or 1 |
| Sectional Listening or Reading test | ~₹0 | 1 |
| Writing Task (AI evaluated) | ~₹5–25 AI | 2 per task |
| Full mock L+R+W | ~₹15–50 AI | 5 |
| Trainer re-evaluation | ₹0 | 0 |
| Speaking (future) | STT + AI | TBD |

- **Credit pack pricing (hypothesis to validate with pilots):** e.g. ₹20–40 per credit with volume tiers. A student doing about 8 full mocks + 20 sectionals + 10 extra writing tasks ≈ 80 credits ≈ ₹1,600–3,200 retail, or less at volume. Compare with the ₹15k course fee and ₹19k exam fee. **Competitor reference: Alfa sells per-student plans + non-expiring credits; Leap sells B2C at ₹99–199.** Possibly also offer a per-student "unlimited L/R" seat with credits only for AI writing.
- **Credits never expire** (Alfa does this; expiry is a sales objection). Revenue recognition is an accounting question, so check with a CA.
- Purchase via Razorpay with an automatic **GST invoice**. Low-balance WhatsApp alert to the owner.

## 4. MVP scope (proposal)

**In (v1):**
1. Multi-tenant org model, roles, white-label basics, subdomains.
2. Content admin: create tests (L/R/W) with all official question types; audio upload; answer keys with alternatives.
3. CD-faithful test player (desktop) + responsive practice mode (mobile).
4. L/R auto-marking, review mode with evidence/explanations.
5. AI writing evaluation (Academic T1, GT T1 letter, T2) + trainer review queue.
6. Student / trainer / owner dashboards (honest analytics, goal presets).
7. Credits wallet, ledger, Razorpay purchase, GST invoice.
8. Notifications (email first, WhatsApp right after).
9. DPDP basics, audit log.
10. Starter content: ~10 Academic + 5 GT full mocks + item-wise banks (see [08](08-content-strategy.md)).

**Out (later):** Speaking (AI), native mobile apps (ship a PWA first), custom domains, PTE/OET/German, live classes/LMS, handwritten-writing OCR, adaptive/IRT difficulty, public API, B2C direct sales.

## 5. Design direction (vs the old app)
- Clean, modern, calm UI (exam anxiety is real): one primary action per screen.
- **Student home = "Next best action"** (e.g. "Do Writing Task 2 #14. Your TR is your weakest criterion") + goal gap + streak.
- The exam player looks like real CD-IELTS (neutral, unbranded), while the rest of the app carries the centre's brand.
- Mobile-first for practice and results, desktop-first for full mocks.
- Every number is explainable: tap a band → see how it was computed.

## 6. Tech considerations (to decide later. Options, not decisions)
- Web app + PWA; a single Postgres with `tenant_id` on every row (+ row-level security) is enough for a long time. Don't do DB-per-tenant.
- Object storage + CDN for audio/images; audio pre-fetch.
- Background job queue for AI scoring (retry, idempotent, cost logging per job).
- LanguageTool self-hosted for grammar features; Claude API for criterion scoring (pin the model ID, version prompts).
- Ledger as an append-only table; credit reservation inside the same DB transaction as attempt creation.

## 7. Open questions for the founders
1. **Design partner:** can we pilot with Medcity (or a similar centre) and get senior trainers to double-mark 200+ essays for calibration?
2. **Content:** in-house writers, AI-assisted generation with expert QA, or licensing? (Biggest cost/risk. See [08](08-content-strategy.md).)
3. **Academic vs GT priority** for the first content batch (Kerala nurses → Academic; PR → GT).
4. **Pricing:** pure credits, or seat + credits? Do credits expire?
5. **Brand:** our brand visible to students ("powered by") or fully white-label?
6. **Speaking timeline:** when? It's the most-used AI feature in B2C (Leap), so centres will ask early.
7. **Multi-exam:** is OET (Kerala nurses) the second exam, or PTE?
8. **Who is the data fiduciary** under DPDP: centre or us? (Affects contracts and consent UX.)
