"""Transcribe listening audio to an .srt subtitle file next to each audio file.

Usage: python tools/transcribe.py <audio> [<audio> ...] [--model medium.en]
Writes <audio-stem>.srt beside each file; skips files that already have one.
Whisper output is auto-generated: verify spellings against the audio before using it as an answer key.
"""
import sys
import types
from pathlib import Path

# ponytail: PyAV's DLL is blocked by Windows App Control here; we decode with soundfile instead,
# so stub `av` just to let faster_whisper import. Drop this if PyAV loads on the machine.
sys.modules.setdefault("av", types.ModuleType("av"))

import numpy as np
import soundfile as sf
from faster_whisper import WhisperModel


def load_16k_mono(path):
    audio, sr = sf.read(path, dtype="float32", always_2d=True)
    audio = audio.mean(axis=1)
    # ponytail: linear-interp resample (no anti-alias filter); fine for speech ASR, use scipy resample_poly if quality matters
    n = int(len(audio) * 16000 / sr)
    return np.interp(np.linspace(0, len(audio) - 1, n), np.arange(len(audio)), audio).astype(np.float32)


def srt_time(seconds):
    ms = round(seconds * 1000)
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def main():
    args = sys.argv[1:]
    model_name = "medium.en"
    if "--model" in args:
        i = args.index("--model")
        model_name = args[i + 1]
        del args[i:i + 2]
    if not args:
        sys.exit(__doc__)

    try:
        model = WhisperModel(model_name, device="cuda", compute_type="float16")
        list(model.transcribe(np.zeros(16000, dtype=np.float32))[0])  # segments are lazy: consume to hit CUDA libs now
    except Exception as e:
        print(f"CUDA unavailable ({e.__class__.__name__}), using CPU", file=sys.stderr)
        model = WhisperModel(model_name, device="cpu", compute_type="int8")

    for path in map(Path, args):
        out = path.with_suffix(".srt")
        if out.exists():
            print(f"skip {out} (exists; delete it to redo)", flush=True)
            continue
        segments, _ = model.transcribe(load_16k_mono(path), language="en", beam_size=5)
        blocks = [
            f"{i}\n{srt_time(s.start)} --> {srt_time(s.end)}\n{s.text.strip()}\n"
            for i, s in enumerate(segments, 1)
        ]
        out.write_text("\n".join(blocks), encoding="utf-8")
        print(f"wrote {out} ({len(blocks)} cues)", flush=True)


if __name__ == "__main__":
    main()
