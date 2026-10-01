# Content Bank

Source of truth for the tests the app imports. One markdown file = one part/passage (Reading passage, Listening part, or Writing task).

## Sourcing policy (read before adding anything)

| Allowed | Not allowed |
|---|---|
| Original content written by us (human or AI-drafted + expert-reviewed) | Questions, passages, audio or scripts copied or paraphrased from **Cambridge IELTS books** or any official IELTS material |
| Content licensed in writing (keep the licence in `licences/`) | "Free practice" pages from IELTS / British Council / IDP. These are for personal practice, not commercial reuse |
| Centre-owned content uploaded by a tenant (tenant-private, with copyright attestation) | Material from other prep sites/apps |

Why: IELTS material is owned by the IELTS Partners and licensed for personal, non-commercial use only ([IELTS copyright statement](https://ielts.org/legal/ielts-copyright-and-trade-mark-statement)). See [research/08-content-strategy.md](../research/08-content-strategy.md).
To license Cambridge material, contact Cambridge University Press & Assessment permissions: <https://www.cambridge.org/us/legal/copyright>.

**Style references (look, don't copy)** for trainers checking that our wording and difficulty match the real test:
- [IDP – IELTS familiarisation tests (computer)](https://ielts.idp.com/about/ielts-familiarisation-tests)
- [IDP – practice tests](https://ielts.idp.com/about/practice-tests)
- [British Council – free Academic Listening practice](https://takeielts.britishcouncil.org/prepare/ielts-free-practice-mock-tests/academic/listening)

## Folder layout

```
content/
  reading/academic/   AR-<test>-P<1-3>.md
  reading/general/    GR-<test>-S<1-3>.md
  listening/          L-<test>-P<1-4>.md   (+ audio/L-<test>-P<n>.mp3 once produced)
  writing/academic/   WA-T1-<nnn>.md, WA-T2-<nnn>.md
  writing/general/    WG-T1-<nnn>.md (letters), WG-T2-<nnn>.md
```

## File format

YAML front matter, then fixed `##` sections. The importer parses these. Keep headings exact.

```markdown
---
id: AR-001-P1
exam: ielts
module: reading            # reading | listening | writing
variant: academic          # academic | general
test: AR-001
part: 1
source: original           # original | licensed | tenant
author: <name>
review_status: draft       # draft | reviewed | published
reviewer:
word_count: 0
---

## Stimulus
Passage text (paragraphs labelled **A**, **B**… when any question needs them).
Listening: the script, with speaker tags `[WOMAN, British]` and `[PAUSE 30s]` markers.
Writing: the task prompt; chart data as a fenced `csv` block.

## Questions 1–6
type: matching_headings      # see types below
instructions: Choose the correct heading for each paragraph from the list below.
word_limit:                  # e.g. "NO MORE THAN TWO WORDS" for completion types
options: |                   # headings / MCQ options / word box, if any
  i. ...
1. Paragraph B
...

## Answer key
| Q | Answer | Also accept | Evidence (exact quote / timestamp) | Explanation |
```

**Blanks** in notes/forms/sentences/summaries: `{{n}}` where `n` is the question number, e.g. `move nearer to his {{1}}`. The player renders an input there; the importer links it to question `n`.

**Listening front matter** adds: `audio: <file>` (relative to the md file), `duration: "mm:ss"`, `questions: "1-10"`. Evidence = transcript timestamp `[mm:ss]`.

**MCQ / matching options** are lettered `A.`, `B.`… Answers use the letter. A shared option list for matching goes under `options:` once per group.

**Question `type` values:** `mcq_single`, `mcq_multi`, `tfng`, `ynng`, `matching_information`, `matching_headings`, `matching_features`, `matching_endings`, `sentence_completion`, `summary_completion`, `summary_completion_wordbox`, `note_completion`, `table_completion`, `flowchart_completion`, `form_completion`, `diagram_labelling`, `map_labelling`, `short_answer`.

**Every answer needs an evidence quote.** That's what lets the review screen highlight the proof, and what lets QA reject ambiguous items.

## Review checklist (before `review_status: published`)
- [ ] Each question has exactly one defensible answer; the evidence quote is verbatim.
- [ ] TFNG: NOT GIVEN items are truly absent from the text (not just implied).
- [ ] Completion answers appear verbatim in the text and fit the word limit.
- [ ] Instructions match official IELTS wording.
- [ ] Length/difficulty matches the slot (Passage 1 easiest → Passage 3 hardest).
- [ ] No sentences lifted from any published IELTS source.
