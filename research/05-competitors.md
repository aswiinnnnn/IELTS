# 05 — Competitor Landscape

## 1. Direct competitors: B2B IELTS platforms for institutes (our category)

| Product | HQ / focus | Exams | Key features | Pricing model | Notes |
|---|---|---|---|---|---|
| **[Gurully](https://www.gurully.com/ielts-institute-software)** | Ahmedabad, India (founded 2019) | CD-IELTS, PTE, Duolingo, CELPIP | CD-IELTS mocks (Ac + GT), **instant AI scoring for Writing & Speaking** + trainer review, built-in LMS, student mgmt, **per-student test allotment & attempt limits**, multi-level trainer permissions, **white-label**, setup "in 10 minutes" | Not public; "tiered by institute size", demo → trial → purchase | Claims **2,100+ institutes**. Most direct Indian competitor. 150+ PTE mocks, 30k+ practice Qs |
| **[Alfa IELTS](https://alfaielts.com/ielts-for-businesses)** | India (sibling of Alfa PTE) | IELTS + PTE | 10,000+ practice Qs, full/sectional mocks, "real CD-IELTS simulation", **paper or computer writing submission**, AI + trainer evaluation, **trainer mode (log into student accounts)**, unified IELTS & PTE partner panel, online classes, upload own content, white-label (logo, name, URL, colours) | **Per-student accounts: 30/60/90/180/365-day plans, min 5 students. Credits that never expire**, usable for IELTS or PTE | Closest to our credit model. "Credits never expire" is a market expectation now |
| **[ScoreMentor.AI](https://scorementor.ai/for-institutions)** | — | 12+ exams (PTE, IELTS, TOEFL, CELPIP, OET, NAATI, GRE…) | Official-UI mocks, AI scoring, **batch comparison & multi-branch analytics**, faculty roles, white-label (logo, domain), 24/7 AI tutor | Custom quote | Marketing claims (95% pass rate, 2M students) look inflated |
| **[ielts.camp](https://ielts.camp/)** | Central Asia focus | IELTS Academic | Pixel-perfect CD simulator, AI graders for W & S on official descriptors, diagnostic test, AI study plans, spaced-repetition vocab, **instructions in 5 languages**, teacher dashboard (cohort analytics, assign mocks, review AI feedback, CSV export) | B2C $19.99/mo → $119.99/yr | Good UX benchmark. Localisation idea transfers to Indian languages |
| **The app in our screenshots** (white-labelled for Medcity, `testprep.medcityinternationalacademy.com`) | Unknown vendor | IELTS (+ "Ena" AI assistant on mobile for speaking) | Online tests (CD mocks, item-wise, sectional), assigned tests, remedial tests, test history, question-wise review, topic-wise scores, credits ("ENA Credits"), video lessons | Credits | See teardown in [06](06-existing-app-teardown.md). Dated UI, analytics bugs |
| [Cathoven](https://www.cathoven.com/) | — | IELTS | Claims "examiner-level AI scoring (98% accuracy)", 10+ yrs of scoring data | B2C | Accuracy claim unverified |
| [Prep Edu](https://prepedu.com/en/) | Vietnam (2021) | IELTS, TOEIC… | AI "Virtual Speaking Room", courses | B2C + B2B | Strong in SE Asia, shows the AI-speaking direction |

## 2. B2C apps competing for the same student

| Product | Price (2026) | Notable |
|---|---|---|
| **[IELTS Prep by LeapScholar](https://leapscholar.com/blog/ielts-prep-by-leap-scholar-app/)** | **₹99 (3 mo) / ₹199 (lifetime)** | 5M+ downloads, 4.7★; 80+ mocks (21 R, 19 L, 18 W, 22 S); **AI speaking** is the most-used feature (cue-card mode with countdown); IELTS + PTE toggle; WhatsApp funnel. **Sets the price anchor for students** |
| [Writing9](https://writing9.com) | ~$10–15/mo, free tier | Essay checker, 4-criteria estimates |
| [LexiBot](https://www.lexibot.me/) | from $2/mo | Unlimited writing checks, speaking practice |
| [UpScore.ai](https://upscore.ai/pricing) | free 1 mock; Pro $9.99/mo | Mock tests + writing analysis |
| [Engnovate](https://engnovate.com/) | free | High-volume free practice, band calculators |
| [Smalltalk2Me](https://smalltalk2.me/) | — | AI speaking/writing; publishes comparisons |
| IELTS Ninja, IELTSMaterial, Kanan, Yocket, Leverage Edu | courses / content | Content-led, lots of free SEO material |
| Official: IDP familiarisation test, British Council free practice tests, Cambridge books | free / paid | The gold standard for content |

## 3. Generic Indian coaching SaaS (what centres may already use)

| Product | Pricing | Relevance |
|---|---|---|
| Classplus | ₹15k–50k/yr + 3–10% revenue share | Branded app, live classes, fee collection. Not IELTS-specific (no CD player, no AI writing scoring) |
| Teachmint | freemium; paid ₹15k–40k/yr, ₹1L+ for multi-faculty | Same |
| Edmingle, Learnyst | similar | LMS |

→ Centres may keep Classplus for classes/fees and use us for **IELTS testing + evaluation**. **Integrate, don't replace**: SSO/deep links, CSV import of students, and later a webhook or API.

## 4. Feature comparison (what's table stakes vs differentiating)

| Capability | Gurully | Alfa | ScoreMentor | ielts.camp | Screenshot app | **Us (planned)** |
|---|---|---|---|---|---|---|
| CD-IELTS-faithful player | ✅ | ✅ | ✅ | ✅ | partial | ✅ table stakes |
| Academic + GT | ✅ | ✅ | ✅ | Ac only | ✅ | ✅ |
| AI writing score | ✅ | ✅ | ✅ | ✅ | ✅ (no criterion detail shown) | ✅ **+ evidence, confidence, range** |
| Trainer review/override | ✅ | ✅ | ? | ✅ | "Teacher remarks" | ✅ **prioritised review queue** |
| White-label | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ |
| Credits / per-student plans | attempt limits | ✅ credits never expire | ? | ❌ | ✅ | ✅ **transparent ledger** |
| Multi-branch analytics | ? | ? | ✅ | ❌ | ❌ | ✅ |
| Goal presets (NMC/AHPRA…) | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ **differentiator** |
| Honest analytics (ranges, no fake bands from 5 Qs) | ? | ? | ? | ? | ❌ | ✅ **differentiator** |
| Indian-language explanations | ❌ | ❌ | ❌ | (other languages) | ❌ | ✅ |
| WhatsApp notifications | ? | ? | ? | ❌ | ❌ | ✅ |
| Published AI accuracy method | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ **differentiator** |
| Multi-exam (PTE/OET…) | ✅ | PTE | ✅ | ❌ | ❌ | later (architecture-ready) |
| Speaking AI | ✅ | ✅ | ✅ | ✅ | via mobile "Ena" | later |

## 5. Where we can win
1. **Trainer time saved**: an AI-first evaluation queue where the trainer only checks the low-confidence scripts. That's measurable ROI ("trainers spend 70% less time marking").
2. **Trustworthy, honest scoring**: criterion bands with quoted evidence, ranges, published accuracy. Competitors all claim "98%" with no method.
3. **Outcome-focused analytics for owners**: branch and batch performance, "students exam-ready vs target", predicted pass rate per batch.
4. **Healthcare/Kerala vertical first**: goal presets for NMC/NMBI/AHPRA, Academic-heavy, OET next. Under-served by Punjab-centric players.
5. **Modern UX**: the existing app looks 2015-era (screenshots). Fast, clean, mobile-friendly practice + desktop-faithful mocks.

## Sources
- [Gurully – IELTS institute software](https://www.gurully.com/ielts-institute-software) · [Gurully – institute software](https://www.gurully.com/institute-software) · [G2 reviews](https://www.g2.com/products/gurully-practice-platform/reviews)
- [Alfa IELTS for businesses](https://alfaielts.com/ielts-for-businesses)
- [ScoreMentor for institutions](https://scorementor.ai/for-institutions)
- [ielts.camp](https://ielts.camp/)
- [Leap Scholar IELTS Prep app](https://leapscholar.com/blog/ielts-prep-by-leap-scholar-app/) · [pricing](https://leapscholar.com/blog/ielts-prep-by-leap-scholar/)
- [Smalltalk2Me – AI IELTS writing checkers 2026](https://smalltalk2.me/blog/tpost/ki8ben5e31-best-ai-ielts-writing-checkers-in-2026-a) · [IELTSbiz – 7 best writing checkers](https://ieltsbiz.com/blog/best-ielts-writing-checker-tools) · [UpScore pricing](https://upscore.ai/pricing) · [LexiBot](https://www.lexibot.me/)
- [myvega.ai – test prep software for institutes 2026](https://www.myvega.ai/blog/best-test-prep-software-for-tutors)
- [Edmingle – LMS pricing India](https://www.edmingle.com/blog/lms-pricing-in-india/) · [Techjockey – Classplus](https://www.techjockey.com/detail/classplus)
