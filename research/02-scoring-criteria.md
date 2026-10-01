# 02 — IELTS Scoring Criteria (the rules our scoring engine implements)

> Primary source: the official **Writing Band Descriptors (updated May 2023)**, saved at [sources/ielts-writing-band-descriptors-2023.pdf](sources/ielts-writing-band-descriptors-2023.pdf), with raw text in [sources/ielts-writing-band-descriptors-2023.raw.txt](sources/ielts-writing-band-descriptors-2023.raw.txt). Plus the ielts.org "scoring in detail" page.

## 1. Overall band

- Bands run 0–9 in half-band steps.
- **Overall = mean of the 4 module bands, rounded to the nearest half band.** Official tie rules:
  - average ending **.25 → round UP** to the next half band (6.25 → 6.5)
  - average ending **.75 → round UP** to the next whole band (6.75 → 7.0)
  - anything below those thresholds rounds down (6.125 → 6.0)
- Our build has no Speaking, so any "overall" is a **3-module estimate**. The existing app shows a big "Band Score 6" for L/R/W only, with a disclaimer underneath. We should label it **"Estimated L/R/W average"** and never present it as an IELTS overall.

```
overall = floor(mean(bands) * 2 + 0.5) / 2
```
Checks: 6.25 → floor(13.0)/2 = 6.5 ✓ · 6.75 → floor(14.0)/2 = 7.0 ✓ · 6.125 → floor(12.75)/2 = 6.0 ✓. **Don't use banker's rounding** (Python `round()` sends 12.5 → 12). Keep these three cases as a unit test.

## 2. Band meanings (for student-facing copy)

| Band | User | Meaning (short) |
|---|---|---|
| 9 | Expert | fully operational command; appropriate, accurate, fluent |
| 8 | Very good | fully operational; occasional unsystematic inaccuracies |
| 7 | Good | operational command; occasional inaccuracies; handles complex language well |
| 6 | Competent | generally effective despite some inaccuracies |
| 5 | Modest | partial command; many mistakes |
| 4 | Limited | basic competence in familiar situations |
| 3 | Extremely limited | conveys general meaning in very familiar situations |
| 2 | Intermittent | great difficulty |
| 1 | Non-user | isolated words |
| 0 | Did not attempt | |

## 3. Listening & Reading — raw score → band

1 mark per correct answer, 40 questions, **no negative marking** (so unattempted questions are pure loss. Analytics should flag these).

Official anchor points (ielts.org): Listening 16→5, 23→6, 30→7, 35→8 · Academic Reading 15→5, 23→6, 30→7, 35→8.

| Band | Listening (Ac + GT) | Academic Reading | GT Reading |
|---|---|---|---|
| 9.0 | 39–40 | 39–40 | 40 |
| 8.5 | 37–38 | 37–38 | 39 |
| 8.0 | 35–36 | 35–36 | 37–38 |
| 7.5 | 32–34 | 33–34 | 36 |
| 7.0 | 30–31 | 30–32 | 34–35 |
| 6.5 | 26–29 | 27–29 | 32–33 |
| 6.0 | 23–25 | 23–26 | 30–31 |
| 5.5 | 18–22 | 19–22 | 27–29 |
| 5.0 | 16–17 | 15–18 | 23–26 |
| 4.5 | 13–15 | 13–14 | 19–22 |
| 4.0 | 10–12 | 10–12 | 15–18 |
| 3.5 | 8–9 ⚠️ | 8–9 ⚠️ | 12–14 |
| 3.0 | 6–7 ⚠️ | 6–7 ⚠️ | 9–11 |
| 2.5 | 4–5 ⚠️ | 4–5 ⚠️ | 6–8 |

⚠️ = widely published by prep sites, but not on ielts.org. IELTS equates each real test version, so cut-offs shift by ±1 between versions. **Our platform should say "estimated band"** and store the conversion table per test (so a content team can adjust it for harder/easier mocks later).

### Answer-matching rules (auto-marking engine)
These are common sources of "my answer was right!" disputes. Get them right and document them for trainers:
- Case-insensitive. Trim whitespace, and collapse multiple spaces.
- **Spelling must be correct** (British or American spelling both accepted).
- Respect the word limit: "NO MORE THAN TWO WORDS AND/OR A NUMBER". Exceeding it = wrong.
- Numbers: digits or words both accepted (`3` / `three`). Dates and times have multiple valid forms.
- Hyphenated words count as one word. Articles are usually optional where the key says so.
- Plurals: only if the key allows it (store **alternative accepted answers** per question, e.g. `["bus", "buses"]` with `(s)` notation).
- Multi-answer MCQ ("Choose TWO letters"): each letter = 1 mark, order-independent.
- Matching: letters can repeat if the instructions say "you may use any letter more than once".
- T/F/NG: accept `TRUE`/`T` etc. only if our UI allows free typing. Better: use radio buttons, as CD-IELTS does.

## 4. Writing — how the band is built

- Examiners score **each task** on 4 criteria, each a whole band 0–9, **weighted equally**:
  - Task 1: **Task Achievement (TA)**, Coherence & Cohesion (CC), Lexical Resource (LR), Grammatical Range & Accuracy (GRA)
  - Task 2: **Task Response (TR)**, CC, LR, GRA
- Task band = mean of its 4 criteria.
- **Writing band: Task 2 counts double** → `W = (T1 + 2·T2) / 3`, reported to a half band.
  - ⚠️ The exact rounding of the Writing band isn't published. Prep sites disagree: some say round to the nearest 0.5, others say round down. **Decision for us:** round to the nearest half band, document it, and show the criterion bands so nothing is hidden.
- Global rules from the descriptors:
  - "A script must **fully fit the positive features** of the descriptor at a particular level." In the original PDF, **bolded text marks negative features that cap a rating**. pdftotext loses the bold, so check the PDF when building prompts.
  - **≤ 20 words → Band 1** on every criterion.
  - **Copied rubric** (text copied from the question) is discounted from the response.
  - **Band 0:** didn't attempt, wrote in a language other than English throughout, or there's proof the answer was **totally memorised**.
  - Under-length: no automatic penalty formula. It shows up through TA/TR (not enough development) and LR band 3 ("inadequate … may be due to the response being significantly underlength").
  - Memorised/formulaic language is penalised under LR (band 4: "inappropriate use of lexical chunks (e.g. memorised phrases, formulaic language and/or language from the input material)").

## 5. Writing Task 1 — Task Achievement (verbatim, May 2023)

| Band | Descriptor |
|---|---|
| 9 | All the requirements of the task are fully and appropriately satisfied. There may be extremely rare lapses in content. |
| 8 | The response covers all the requirements of the task appropriately, relevantly and sufficiently. *(Academic)* Key features are skilfully selected, and clearly presented, highlighted and illustrated. *(GT)* All bullet points are clearly presented, and appropriately illustrated or extended. There may be occasional omissions or lapses in content. |
| 7 | The response covers the requirements of the task. The content is relevant and accurate – there may be a few omissions or lapses. The format is appropriate. *(Academic)* Key features which are selected are covered and clearly highlighted but could be more fully or more appropriately illustrated or extended. *(Academic)* It presents a **clear overview**, the data are appropriately categorised, and main trends or differences are identified. *(GT)* All bullet points are covered and clearly highlighted but could be more fully or more appropriately illustrated or extended. It presents a clear purpose. The tone is consistent and appropriate to the task. Any lapses are minimal. |
| 6 | The response focuses on the requirements of the task and an appropriate format is used. *(Academic)* Key features which are selected are covered and adequately highlighted. A relevant overview is attempted. Information is appropriately selected and supported using figures/data. *(GT)* All bullet points are covered and adequately highlighted. The purpose is generally clear. There may be minor inconsistencies in tone. Some irrelevant, inappropriate or inaccurate information may occur in areas of detail or when illustrating or extending the main points. Some details may be missing (or excessive) and further extension or illustration may be needed. |
| 5 | The response generally addresses the requirements of the task. The format may be inappropriate in places. *(Academic)* Key features which are selected are not adequately covered. The recounting of detail is mainly mechanical. There may be no data to support the description. *(GT)* All bullet points are presented but one or more may not be adequately covered. The purpose may be unclear at times. The tone may be variable and sometimes inappropriate. There may be a tendency to focus on details (without referring to the bigger picture). The inclusion of irrelevant, inappropriate or inaccurate material in key areas detracts from the task achievement. There is limited detail when extending and illustrating the main points. |
| 4 | The response is an attempt to address the task. *(Academic)* Few key features have been selected. *(GT)* Not all bullet points are presented. *(GT)* The purpose of the letter is not clearly explained and may be confused. The tone may be inappropriate. The format may be inappropriate. Key features/bullet points which are presented may be irrelevant, repetitive, inaccurate or inappropriate. |
| 3 | The response does not address the requirements of the task (possibly because of misunderstanding of the data/diagram/situation). Key features/bullet points which are presented may be largely irrelevant. Limited information is presented, and this may be used repetitively. |
| 2 | The content barely relates to the task. |
| 1 | Responses of 20 words or fewer are rated at Band 1. The content is wholly unrelated to the task. Any copied rubric must be discounted. |
| 0 | Did not attend/attempt, used a language other than English throughout, or proof the answer was totally memorised. |

**Task 1 Academic rule of thumb (examiners and trainers):** no overview → TA is capped at about 5–6. That is the single most common Task 1 failure, so the AI must explicitly check "overview present?".

## 6. Writing Task 2 — Task Response (verbatim, May 2023)

| Band | Descriptor |
|---|---|
| 9 | The prompt is appropriately addressed and explored in depth. A clear and fully developed position is presented which directly answers the question/s. Ideas are relevant, fully extended and well supported. Any lapses in content or support are extremely rare. |
| 8 | The prompt is appropriately and sufficiently addressed. A clear and well-developed position is presented in response to the question/s. Ideas are relevant, well extended and supported. There may be occasional omissions or lapses in content. |
| 7 | The main parts of the prompt are appropriately addressed. A clear and developed position is presented. Main ideas are extended and supported but there may be a tendency to over-generalise or there may be a lack of focus and precision in supporting ideas/material. |
| 6 | The main parts of the prompt are addressed (though some may be more fully covered than others). An appropriate format is used. A position is presented that is directly relevant to the prompt, although the conclusions drawn may be unclear, unjustified or repetitive. Main ideas are relevant, but some may be insufficiently developed or may lack clarity, while some supporting arguments and evidence may be less relevant or inadequate. |
| 5 | The main parts of the prompt are incompletely addressed. The format may be inappropriate in places. The writer expresses a position, but the development is not always clear. Some main ideas are put forward, but they are limited and are not sufficiently developed and/or there may be irrelevant detail. There may be some repetition. |
| 4 | The prompt is tackled in a minimal way, or the answer is tangential, possibly due to some misunderstanding of the prompt. The format may be inappropriate. A position is discernible, but the reader has to read carefully to find it. Main ideas are difficult to identify and such ideas that are identifiable may lack relevance, clarity and/or support. Large parts of the response may be repetitive. |
| 3 | No part of the prompt is adequately addressed, or the prompt has been misunderstood. No relevant position can be identified, and/or there is little direct response to the question/s. There are few ideas, and these may be irrelevant or insufficiently developed. |
| 2 | The content is barely related to the prompt. No position can be identified. There may be glimpses of one or two ideas without development. |
| 1 | Responses of 20 words or fewer are rated at Band 1. The content is wholly unrelated to the prompt. Any copied rubric must be discounted. |
| 0 | As Task 1. |

## 7. Coherence & Cohesion (both tasks; *[T2]* = Task 2-only sentence)

| Band | Descriptor |
|---|---|
| 9 | The message can be followed effortlessly. Cohesion is used in such a way that it very rarely attracts attention. Any lapses in coherence or cohesion are minimal. Paragraphing is skilfully managed. |
| 8 | The message can be followed with ease. Information and ideas are logically sequenced, and cohesion is well managed. Occasional lapses in coherence and cohesion may occur. Paragraphing is used sufficiently and appropriately. |
| 7 | Information and ideas are logically organised, and there is a clear progression throughout the response. (A few lapses may occur, but these are minor.) A range of cohesive devices including reference and substitution is used flexibly but with some inaccuracies or some over/under use. *[T2]* Paragraphing is generally used effectively to support overall coherence, and the sequencing of ideas within a paragraph is generally logical. |
| 6 | Information and ideas are generally arranged coherently and there is a clear overall progression. Cohesive devices are used to some good effect but cohesion within and/or between sentences may be faulty or mechanical due to misuse, overuse or omission. The use of reference and substitution may lack flexibility or clarity and result in some repetition or error. *[T2]* Paragraphing may not always be logical and/or the central topic may not always be clear. |
| 5 | Organisation is evident but is not wholly logical and there may be a lack of overall progression. Nevertheless, there is a sense of underlying coherence to the response. The relationship of ideas can be followed but the sentences are not fluently linked to each other. There may be limited/overuse of cohesive devices with some inaccuracy. The writing may be repetitive due to inadequate and/or inaccurate use of reference and substitution. *[T2]* Paragraphing may be inadequate or missing. |
| 4 | Information and ideas are evident but not arranged coherently, and there is no clear progression within the response. Relationships between ideas can be unclear and/or inadequately marked. There is some use of basic cohesive devices, which may be inaccurate or repetitive. There is inaccurate use or a lack of substitution or referencing. *[T2]* There may be no paragraphing and/or no clear main topic within paragraphs. |
| 3 | There is no apparent logical organisation. Ideas are discernible but difficult to relate to each other. Minimal use of sequencers or cohesive devices. Those used do not necessarily indicate a logical relationship between ideas. There is difficulty in identifying referencing. *[T2]* Any attempts at paragraphing are unhelpful. |
| 2 | There is little relevant message, or the entire response may be off-topic. There is little evidence of control of organisational features. |
| 1 | ≤ 20 words → Band 1. The writing fails to communicate any message and appears to be by a virtual non-writer. |

## 8. Lexical Resource (both tasks)

| Band | Descriptor |
|---|---|
| 9 | Full flexibility and precise use are evident (*T2:* widely evident) within the scope of the task. A wide range of vocabulary is used accurately and appropriately with very natural and sophisticated control of lexical features. Minor errors in spelling and word formation are extremely rare and have minimal impact on communication. |
| 8 | A wide resource is fluently and flexibly used to convey precise meanings. There is skilful use of uncommon and/or idiomatic items when appropriate, despite occasional inaccuracies in word choice and collocation. Occasional errors in spelling and/or word formation may occur, but have minimal impact on communication. |
| 7 | The resource is sufficient to allow some flexibility and precision. There is some ability to use less common and/or idiomatic items. An awareness of style and collocation is evident, though inappropriacies occur. There are only a few errors in spelling and/or word formation and they do not detract from overall clarity. |
| 6 | The resource is generally adequate and appropriate for the task. The meaning is generally clear in spite of a rather restricted range or a lack of precision in word choice. If the writer is a risk-taker, there will be a wider range of vocabulary used but higher degrees of inaccuracy or inappropriacy. There are some errors in spelling and/or word formation, but these do not impede communication. |
| 5 | The resource is limited but minimally adequate for the task. Simple vocabulary may be used accurately but the range does not permit much variation in expression. There may be frequent lapses in the appropriacy of word choice and a lack of flexibility is apparent in frequent simplifications and/or repetitions. Errors in spelling and/or word formation may be noticeable and may cause some difficulty for the reader. |
| 4 | The resource is limited and inadequate for or unrelated to the task. Vocabulary is basic and may be used repetitively. There may be inappropriate use of lexical chunks (e.g. memorised phrases, formulaic language and/or language from the input material). Inappropriate word choice and/or errors in word formation and/or in spelling may impede meaning. |
| 3 | The resource is inadequate (which may be due to the response being significantly underlength). Possible over-dependence on input material or memorised language. Control of word choice and/or spelling is very limited, and errors predominate. These errors may severely impede meaning. |
| 2 | The resource is extremely limited with few recognisable strings, apart from memorised phrases. There is no apparent control of word formation and/or spelling. |
| 1 | ≤ 20 words → Band 1. No resource is apparent, except for a few isolated words. |

## 9. Grammatical Range & Accuracy (both tasks)

| Band | Descriptor |
|---|---|
| 9 | A wide range of structures is used with full flexibility and control. Punctuation and grammar are used appropriately throughout. Minor errors are extremely rare and have minimal impact on communication. |
| 8 | A wide range of structures is flexibly and accurately used. The majority of sentences are error-free, and punctuation is well managed. Occasional, non-systematic errors and inappropriacies occur, but have minimal impact on communication. |
| 7 | A variety of complex structures is used with some flexibility and accuracy. Grammar and punctuation are generally well controlled, and error-free sentences are frequent. A few errors in grammar may persist, but these do not impede communication. |
| 6 | A mix of simple and complex sentence forms is used but flexibility is limited. Examples of more complex structures are not marked by the same level of accuracy as in simple structures. Errors in grammar and punctuation occur, but rarely impede communication. |
| 5 | The range of structures is limited and rather repetitive. Although complex sentences are attempted, they tend to be faulty, and the greatest accuracy is achieved on simple sentences. Grammatical errors may be frequent and cause some difficulty for the reader. Punctuation may be faulty. |
| 4 | A very limited range of structures is used. Subordinate clauses are rare and simple sentences predominate. Some structures are produced accurately but grammatical errors are frequent and may impede meaning. Punctuation is often faulty or inadequate. |
| 3 | Sentence forms are attempted, but errors in grammar and punctuation predominate (except in memorised phrases or those taken from the input material). This prevents most meaning from coming through. Length may be insufficient to provide evidence of control of sentence forms. |
| 2 | There is little or no evidence of sentence forms (except in memorised phrases). |
| 1 | ≤ 20 words → Band 1. No rateable language is evident. |

## 10. Measurable proxies per criterion (for the AI pipeline — see 03)

| Criterion | Deterministic signals we can compute | Needs LLM judgement |
|---|---|---|
| TA / TR | word count vs 150/250; prompt-overlap (copied rubric); GT: all 3 bullets addressed?; Academic T1: overview sentence present? data figures cited? **data accuracy vs the chart's source data** (we generate the charts, so we know the true values) | position clarity, idea development, relevance, over-generalisation |
| CC | paragraph count; linker frequency per 100 words (overuse is a 5–6 signal); repeated nouns vs pronoun reference | logical progression, mechanical vs natural cohesion |
| LR | lexical diversity (MTLD); share of less-common words (CEFR B2+/C1+ lists); spelling errors (LanguageTool); repeated words; template-phrase matches | collocation naturalness, precision, appropriacy |
| GRA | error count per 100 words by type; % error-free sentences; ratio of complex sentences (subordinate clauses via a parser); punctuation errors | whether errors "impede communication" |

## 11. Speaking (later) — criteria names only
Fluency & Coherence · Lexical Resource · Grammatical Range & Accuracy · Pronunciation (equal weight). Public speaking band descriptors exist on ielts.org; fetch them when Speaking is scoped.

## Sources
- [Official Writing Band Descriptors (May 2023) PDF – ielts.org](https://ielts.org/cdn/Guides/ielts-writing-band-descriptors.pdf) (local copy in `sources/`)
- [IELTS scoring in detail – ielts.org](https://ielts.org/take-a-test/your-results/ielts-scoring-in-detail)
- [Calculate IELTS band scores – IDP Australia](https://ielts.com.au/australia/results/band-score-calculation)
- [IDP Qatar – conversion tables](https://ifi.qa/using-conversion-tables-to-find-out-your-ielts-listening-and-reading-scores/)
- [AECC – Listening score chart](https://www.aeccglobal.com/exams/ielts/listening-band-scores)
- [IELTS Buddy – scores and marking](https://www.ieltsbuddy.com/ielts-scores.html)
