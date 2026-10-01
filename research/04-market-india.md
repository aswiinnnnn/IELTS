# 04 — Indian Market: Demand, Segments, Economics, Regulation

## 1. The headline: Indian IELTS demand has collapsed, but not evenly

| Data point | Source |
|---|---|
| IDP India IELTS volumes **−42% (FY24), −50% (FY25)**, then **−27%** in the 6 months to Dec 2025 | PIE News / IDP results |
| Outside India, IDP's IELTS volumes **grew** in the same periods | PIE News |
| IDP FY26: revenue −9% (A$795m), placements −27%, testing volumes −8%; ~1,250 roles cut; global IELTS venues **~1,500 → <600**; 15 Indian placement offices consolidated | PIE News, Investing.com |
| Driver: **Canada study-permit caps** (Jan 2024, cut a further 10% for 2025 to 437k). **74% of Indian study-permit applications refused in Aug 2025** (vs ~32% in Aug 2023) | PIE News, Gulf News |
| Tighter rules in Australia, UK, US too | PIE News |
| PTE Academic: 1.23M tests in 2023 (from 822k); about 1.04M in 2025 (−5%). Pearson cites **India market-share gains** (Chandigarh centre: 14k tests/month) | StudyTravel, Pearson |
| IELTS still has about 49% share among Indian English-test takers | lingobright/industry stats |
| IDP has run **all** IELTS in India since buying British Council's India IELTS business (£130m, Aug 2021): ~75–78 centres | IDP |

### What this means for us
1. **The "Punjab student → Canada" segment that built the IELTS coaching industry is shrinking fast.** Many centres are closing or diversifying. Our customers are **cost-sensitive and want to diversify revenue**.
2. **Pay-as-you-go credits suit a shrinking market.** No big annual licence. Centres pay as students come in.
3. **Multi-exam is a survival feature for centres** (PTE, OET, German, Duolingo, CELPIP). Ship IELTS first, but model "exam" as data so PTE/OET can be added without a rewrite.
4. Target the **segments still growing** (below).

## 2. Segments (who our centres serve)

| Segment | Geography | Test / target | Status | Notes |
|---|---|---|---|---|
| **Healthcare professionals (nurses)** → UK, Ireland, Australia, NZ, Gulf | **Kerala** (85–95% of India's nurse emigration in the late 2010s); also Karnataka, TN | IELTS **Academic** (NMC/NMBI/AHPRA) or **OET**; also **German (B1/B2)** for Germany | **Growing / resilient** | Our screenshot sample (Medcity, 18 Kerala branches, 121k+ trained) is exactly this. High targets: **L7 R7 S7, W6.5, overall 7** |
| Students → UK, Ireland, Australia, Europe, NZ | pan-India, metros | IELTS Academic 6.0–7.0 | Shrinking but large | UKVI version for UK visas |
| Students → Canada | Punjab, Gujarat, Haryana | IELTS Academic / GT | **Collapsed** (permit caps, refusals) | Historic core of the coaching market |
| PR / migration | Punjab, Gujarat, Kerala, Andhra/Telangana | IELTS **GT** (CLB for Canada, Australia points) | Mixed | Competition from CELPIP / PTE Core |
| Work visas (UK care, Gulf) | Kerala, Punjab | IELTS GT / UKVI, OET | Steady | |

### Nurse-specific registration rules (build a "goal preset" for each)

| Regulator | Required IELTS (Academic) | Combining sittings |
|---|---|---|
| **NMC (UK)** | Overall 7.0; L/R/S ≥ 7.0; **W ≥ 6.5** (writing lowered from 7.0 in 2024) | ✅ 2 sittings within 12 months |
| **NMBI (Ireland)** | Overall 7.0; L/R/S 7.0; W 6.5 | ❌ single sitting only |
| **AHPRA/NMBA (Australia)** | Overall 7; L/R/S 7; W 6.5 (updated 23 Apr 2026) | ✅ 2 sittings within 6 months (per blog sources, verify) |

→ **Product idea:** "Goal presets" (NMC UK, NMBI Ireland, AHPRA Australia, Canada SDS/CLB, UK university 6.5…). The dashboard then shows *the gap per module against the real requirement* instead of a generic band.

## 3. Coaching-centre economics (what our customer earns)

| Item | Value | Source |
|---|---|---|
| IELTS exam fee (IDP India, from 1 Apr 2026) | ₹19,000 (UKVI ₹19,250), GST included; One Skill Retake ~₹12,650 | IDP / PW |
| Typical IELTS coaching course fee | **₹12,000–26,000** (Punjab IBT ₹12k–26k; Kerala Camford ₹15,500; Ahmedabad ₹20,000); online ₹2,999–56,000 | Collegedunia, Yocket, GeeksforGeeks |
| Punjab + Chandigarh coaching industry (pre-collapse) | ~₹1,100 crore, ~6 lakh test-takers/yr (old figure, pre-2024) | GeeksforGeeks citing media |
| Batch sizes | 2–4 (premium) to 6–10 typical; larger in budget centres | institute websites |
| B2C prep apps (competing for the student's wallet) | Leap Scholar IELTS Prep: **₹99–199** for 50–75+ mocks; ielts.camp $10–20/mo; Writing9 ~$10–15/mo; LexiBot from $2/mo | see [05](05-competitors.md) |
| Generic coaching SaaS | Classplus ₹15k–50k/yr (+3–10% rev share); Teachmint paid ₹15k–40k/yr | Edmingle, igniterapp |

**Implication for pricing:** if a student pays the centre about ₹15,000, the centre can comfortably spend **₹300–1,000 per student** on the platform (2–7% of the fee) *if* it visibly improves results and saves trainer time. B2C apps at ₹99 set a low price anchor for *content volume*. Our value must be **trainer workflow + trusted evaluation + centre branding + analytics**, not "number of mocks".

## 4. India-specific product requirements

| Area | Requirement |
|---|---|
| **Payments** | Razorpay (UPI, cards, netbanking; ~2% + 18% GST; Subscriptions/UPI AutoPay available). Centres buy credit packs; GST invoices (18% on SaaS) with the centre's GSTIN. |
| **Communication** | **WhatsApp is the default channel** for students *and* parents. WhatsApp Business API (India): utility/auth ≈ ₹0.115/msg, marketing ≈ ₹0.86/msg (+18% GST); 1,000 free service msgs/number/month from 1 Oct 2026. Use it for test reminders, result-ready, low-credit alerts. |
| **Devices & bandwidth** | Many students practise on **low-end Android phones on mobile data**. Real CD-IELTS is a desktop experience, so: (a) a full mock needs desktop/laptop or the centre's lab; (b) sectional practice must work well on mobile; (c) pre-download listening audio before the timer starts; autosave every answer; resume after disconnect. |
| **Centre labs** | Many centres run mocks in a computer lab "like the real test centre": kiosk/fullscreen mode, headphone check, trainer-started synchronous sessions. |
| **Languages** | UI in English (the exam is English), with **instructions/explanations optionally in Malayalam, Hindi, Punjabi, Gujarati, Tamil, Telugu**. ielts.camp localises instructions in 5 languages for Central Asia; same idea. |
| **Data protection — DPDP Act 2023 + DPDP Rules 2025** | Applies to all personal data of people in India. **Under-18 = child → verifiable parental consent**; no tracking/behavioural monitoring or targeted ads to children; penalties up to ₹200 crore. Some IELTS students are 17 (Class 12). Need an **age gate + parent consent flow**, consent records, data-deletion on request, breach notification. The centre is likely the *data fiduciary*, we are the *processor*. Put that in the contract. |
| **Trust signals** | Indian centres sell on results ("band 8 achievers" walls). Give them shareable result cards and success analytics they can market with (with student consent). |

## 5. Market-size framing (rough, to refine)

- Supply side: IELTS is taught at thousands of centres. Gurully alone claims **2,100+ institutes** (multi-exam, global) for its institute software. Medcity alone has 18 branches.
- Bottom-up model to fill in with real pilot data: `#centres × students/centre/year × ₹/student`. Example: 500 centres × 300 students × ₹500 = **₹7.5 crore/year**. Treat as illustrative only.

## Sources
- [PIE News – IDP warns of further volume drops](https://thepienews.com/idp-warns-of-further-student-volume-drops-as-revenue-plummets/) · [IDP reports revenue loss](https://thepienews.com/idp-reports-revenue-loss-in-challenging-period/) · [IDP to consolidate 15 India locations](https://thepienews.com/idp-to-consolidate-15-india-student-placement-locations/)
- [Investing.com – IDP FY26 slides](https://www.investing.com/news/company-news/idp-education-fy26-slides-margins-hold-at-60-despite-27-volume-drop-93CH-4868527)
- [PIE News – Canada permit caps "worse than Covid"](https://thepienews.com/impact-of-canadas-study-permit-caps-worse-than-covid/) · [Gulf News – 75% of Indian applicants rejected](https://gulfnews.com/world/asia/india/canada-rejects-75-of-indian-student-applicants-as-scrutiny-tightens-1.500332160)
- [IDP – acquisition of British Council IELTS India](https://careers.idp.com/news/idp-delivers-ielts-test-in-india)
- [Pearson – why PTE is rising](https://in.pearson.com/our-story/news-room/2024/06/study-abroad--why-pte-is-rising-in-the-popularity-stakes.html) · [StudyTravel – PTE growth 2023](https://studytravel.network/magazine/news/2/30454) · [lingobright – test-taker stats](https://www.lingobright.com/statistics/ielts-test-taker-statistics-worldwide-and-by-country/)
- [NMC – IELTS Academic requirements](https://www.nmc.org.uk/registration/joining-the-register/english-language-requirements/accepted-english-language-tests/ielts-academic/) · [IDP India – nursing in Ireland](https://ieltsidpindia.com/information/english-language-requirements/nursing-in-ireland) · [Medcity – AHPRA 2026](https://medcityacademy.com/ahpra-english-requirements-nurses-2026/) · [IDP – nurse requirements AU/NZ/US](https://ielts.idp.com/about/news-and-articles/article-ielts-score-requirements-nurses)
- [Medcity International Academy](https://medcityinternationalacademy.com/) · [Medcity centres](https://medcityinternationalacademy.com/centers/)
- Kerala nurse migration/Germany: [German Navigator](https://german-navigator.com/germany-nursing-recruitment-agency-in-kerala/), [Nursing News India – Germany–Kerala MoU](https://nursingnews.in/germany-sings-mou-with-kerala-to-hire-nurses/), [karangupta.com – OET for Indian nurses](https://www.karangupta.com/blog/oet-for-indian-nurses-and-doctors-occupational-english-test-preparation-guide)
- Coaching fees: [GeeksforGeeks – Punjab](https://www.geeksforgeeks.org/ielts/best-ielts-coaching-in-punjab/), [Yocket – Kerala](https://prep.yocket.com/ielts/top-10-ielts-coaching-centres-in-kerala), [Collegedunia](https://collegedunia.com/coaching/ielts-institutes)
- [Edmingle – LMS pricing in India 2026](https://www.edmingle.com/blog/lms-pricing-in-india/) · [igniterapp – coaching app cost](https://www.igniterapp.com/coaching-app-cost-india)
- [Razorpay – SaaS payment gateway TCO](https://razorpay.com/blog/best-payment-gateway-pricing-saas-india-tco-guide) · [Razorpay – recurring billing costs](https://razorpay.com/blog/cheapest-payment-gateway-for-recurring-billing-e-nach-upi-autopay-and-subscription/)
- [WhatsApp API pricing India 2026 – MyOperator](https://myoperator.com/blog/whatsapp-business-api-pricing-india-2026) · [AiSensy](https://aisensy.com/pricing)
- DPDP: [Mondaq – children & DPDP Rules 2025](https://www.mondaq.com/india/privacy-protection/1710322/childrens-day-under-the-dpdp-act-2023-and-dpdp-rules-2025-the-new-compliance-frontier-for-edtech-gaming-social-media-and-consumer-platforms), [ORF – child data safety](https://www.orfonline.org/english/expert-speak/dpdp-rules-and-the-future-of-child-data-safety), [Wikipedia – DPDP Rules 2025](https://en.wikipedia.org/wiki/Digital_Personal_Data_Protection_Rules,_2025)
