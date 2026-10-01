# Test Content (personal-reference, local only)

⚠️ Third-party material collected for local development. It's git-ignored and must never be committed, deployed or shown to anyone. Replace it with original content (`../content/`) before any demo.

## Mock Test 1 — IELTS Academic (computer-delivered)

| Module | Folder | Parts | Questions | Time |
|---|---|---|---|---|
| Listening | `listening-test-1/` | 4 × (`.md` questions, `.mpeg` audio, `.srt` transcript) | 1–40 | ~30 min + 2 min review |
| Reading | `reading-test-1/` | 3 passages | 1–40 (portal numbered them 41–80) | 60 min |
| Writing | `writing-test-1/` | Task 1 (bar chart, `.jpeg`) + Task 2 (discussion essay) | — | 60 min |

File format: see [../content/README.md](../content/README.md). Each file has front matter, question groups (`type`, `instructions`, `word_limit`, `{{n}}` blanks) and an answer-key table with evidence.

## Status
Complete: all 80 Listening/Reading answers keyed; both Writing tasks ready for AI scoring.

## Adding more tests
1. Create `listening-test-N/`, `reading-test-N/`, `writing-test-N/` with raw pastes and audio.
2. Transcribe: `python tools/transcribe.py test-content/listening-test-N/*.mpeg` (writes `.srt`, skips parts already done).
3. Ask Claude to clean them into the format and fill answer keys from the transcript or passage.
