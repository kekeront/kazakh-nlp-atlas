"""
audit_tokenizers.py — Day 2 engineering core.

Audits how well six production subword tokenizers preserve morphological
boundaries in Kazakh, Russian, and English word-forms from hand-annotated
test sets.

Produces paper/experiments/results.csv and prints a mean-TPW/TPC summary.
MBA and SIS metrics are stubs for Day 3 (see their docstrings).
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict
from dataclasses import dataclass, fields
from pathlib import Path
from typing import Optional

import pandas as pd
import tiktoken
from transformers import AutoTokenizer, PreTrainedTokenizerBase

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parent.parent
EXPERIMENTS = ROOT / "paper" / "experiments"
RESULTS_CSV = EXPERIMENTS / "results.csv"

TESTSET_FILES: dict[str, Path] = {
    "kazakh": EXPERIMENTS / "kazakh_testset_seed.tsv",
    "russian": EXPERIMENTS / "russian_testset_seed.tsv",
    "english": EXPERIMENTS / "english_testset_seed.tsv",
}

# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class WordRecord:
    word: str
    morpheme_split: str
    gloss: str
    pos: str
    category: str
    notes: str


@dataclass
class ResultRow:
    language: str
    tokenizer: str
    word: str
    morpheme_split: str
    category: str
    n_chars: int
    n_tokens: int
    tpw: int
    tpc: float
    tokens_str: str
    mba: Optional[float]
    sis: Optional[float]


# ---------------------------------------------------------------------------
# TSV loading
# ---------------------------------------------------------------------------

_EXPECTED_COLS = ["word", "morpheme_split", "gloss", "pos", "category", "notes"]


def load_testset(path: Path) -> list[WordRecord]:
    """Parse a TSV test set, skipping blank and comment lines.

    Raises FileNotFoundError if the file is missing, ValueError if the header
    row is absent or columns are mismatched.
    """
    if not path.exists():
        raise FileNotFoundError(f"Test set not found: {path}")

    records: list[WordRecord] = []
    header_seen = False

    with path.open(encoding="utf-8") as fh:
        for lineno, raw in enumerate(fh, start=1):
            line = raw.rstrip("\n")
            if not line or line.startswith("#"):
                continue
            cols = line.split("\t")
            if not header_seen:
                if cols != _EXPECTED_COLS:
                    raise ValueError(
                        f"{path.name} line {lineno}: expected header "
                        f"{_EXPECTED_COLS}, got {cols}"
                    )
                header_seen = True
                continue
            if len(cols) < len(_EXPECTED_COLS):
                # Pad missing trailing fields (e.g. an empty 'notes' column)
                cols += [""] * (len(_EXPECTED_COLS) - len(cols))
            records.append(WordRecord(*cols[: len(_EXPECTED_COLS)]))

    if not header_seen:
        raise ValueError(f"{path.name}: no header row found")

    return records


# ---------------------------------------------------------------------------
# Tokenizer wrappers
# ---------------------------------------------------------------------------

# Prefix markers that different tokenizers use to signal word-initial tokens.
# We strip them for human-readable tokens_str output.
_LEADING_SPACE_MARKERS = ("▁", "Ġ", "Ċ", "Ā")

# Special tokens we exclude from the token count (BOS, EOS, CLS, SEP, etc.).
# We rely on encode(..., add_special_tokens=False) for HF tokenizers instead
# of filtering by ID, which is more robust across vocab differences.


def _clean_token(tok: str) -> str:
    """Strip leading-space markers for display; keeps the token semantically identical."""
    for marker in _LEADING_SPACE_MARKERS:
        tok = tok.replace(marker, "")
    return tok


def tokenize_tiktoken(enc: tiktoken.Encoding, word: str) -> tuple[int, str]:
    """Tokenize with a tiktoken encoding; returns (n_tokens, tokens_str)."""
    ids = enc.encode(word)
    tokens = [enc.decode_single_token_bytes(i).decode("utf-8", errors="replace") for i in ids]
    return len(tokens), "|".join(_clean_token(t) for t in tokens)


def tokenize_hf(tok: PreTrainedTokenizerBase, word: str) -> tuple[int, str]:
    """Tokenize with a HuggingFace tokenizer; returns (n_tokens, tokens_str).

    Uses add_special_tokens=False so BOS/EOS/CLS do not inflate counts.
    """
    ids = tok.encode(word, add_special_tokens=False)
    tokens = tok.convert_ids_to_tokens(ids)
    return len(tokens), "|".join(_clean_token(t) for t in tokens)


# ---------------------------------------------------------------------------
# Metric stubs (Day 3)
# ---------------------------------------------------------------------------

def compute_mba(word: str, morpheme_split: str, tokens_str: str) -> Optional[float]:
    """Morphological Boundary Alignment (stub — implement Day 3).

    Intended formula:
        MBA(w, t) = |B_t ∩ B_m| / |B_t|
    where B_t = set of character offsets of token boundaries in w,
          B_m = set of character offsets of morpheme boundaries derived
                from the morpheme_split field (e.g. "үй-лер-іміз" → {3, 7}).
    Returns the fraction of token boundaries that land on a morpheme boundary.
    """
    # TODO Day 3: morphological boundary alignment
    return None


def compute_sis(word: str, morpheme_split: str, tokens_str: str) -> Optional[float]:
    """Suffix Integrity Score (stub — implement Day 3).

    Intended formula:
        SIS(s, t) = 1 if suffix s appears as a single contiguous substring
                    in the token sequence (tokens_str), else 0.
    Averages over all suffixes in morpheme_split to give a word-level score.
    """
    # TODO Day 3: suffix integrity score
    return None


# ---------------------------------------------------------------------------
# Tokenizer loading
# ---------------------------------------------------------------------------

# TODO: LLaMA-3 (meta-llama/Meta-Llama-3-8B) was originally planned but requires
# HuggingFace gated access. Swap "llama3" entry below once access is granted and
# the token is set in HF_TOKEN / huggingface-cli login.

def load_tokenizers() -> dict[str, object]:
    """Load all six tokenizers; skip any that fail to download."""
    tokenizers: dict[str, object] = {}

    try:
        tokenizers["cl100k_base"] = tiktoken.get_encoding("cl100k_base")
    except Exception as exc:
        print(f"ERROR: cl100k_base failed to load: {exc}", file=sys.stderr)

    hf_models = [
        "gpt2",
        "xlm-roberta-base",
        "google/mt5-base",
        "bigscience/bloom-560m",
        "Qwen/Qwen2-0.5B",
    ]
    for model_id in hf_models:
        try:
            tokenizers[model_id] = AutoTokenizer.from_pretrained(model_id)
        except OSError as exc:
            print(f"ERROR: {model_id} failed to download — {exc}", file=sys.stderr)
        except Exception as exc:
            print(f"ERROR: {model_id} unexpected failure — {exc}", file=sys.stderr)

    return tokenizers


# ---------------------------------------------------------------------------
# Core audit loop
# ---------------------------------------------------------------------------

def audit(
    languages: list[str],
    tokenizers: dict[str, object],
) -> list[ResultRow]:
    rows: list[ResultRow] = []

    for lang in languages:
        path = TESTSET_FILES[lang]
        try:
            records = load_testset(path)
        except (FileNotFoundError, ValueError) as exc:
            print(f"ERROR: skipping {lang}: {exc}", file=sys.stderr)
            continue

        for name, tok in tokenizers.items():
            for rec in records:
                if isinstance(tok, tiktoken.Encoding):
                    n_tokens, tokens_str = tokenize_tiktoken(tok, rec.word)
                else:
                    n_tokens, tokens_str = tokenize_hf(tok, rec.word)  # type: ignore[arg-type]

                n_chars = len(rec.word)
                tpc = n_tokens / n_chars if n_chars > 0 else 0.0

                rows.append(
                    ResultRow(
                        language=lang,
                        tokenizer=name,
                        word=rec.word,
                        morpheme_split=rec.morpheme_split,
                        category=rec.category,
                        n_chars=n_chars,
                        n_tokens=n_tokens,
                        tpw=n_tokens,
                        tpc=round(tpc, 4),
                        tokens_str=tokens_str,
                        mba=compute_mba(rec.word, rec.morpheme_split, tokens_str),
                        sis=compute_sis(rec.word, rec.morpheme_split, tokens_str),
                    )
                )

    return rows


# ---------------------------------------------------------------------------
# I/O helpers
# ---------------------------------------------------------------------------

def write_csv(rows: list[ResultRow], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    col_names = [f.name for f in fields(ResultRow)]
    with out_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=col_names)
        writer.writeheader()
        for row in rows:
            writer.writerow({f.name: getattr(row, f.name) for f in fields(row)})


def print_summary(rows: list[ResultRow]) -> None:
    if not rows:
        print("No results to summarise.", file=sys.stderr)
        return
    df = pd.DataFrame([{f.name: getattr(r, f.name) for f in fields(r)} for r in rows])
    summary = (
        df.groupby(["language", "tokenizer"])[["tpw", "tpc"]]
        .mean()
        .round(3)
        .reset_index()
    )
    summary.columns = ["language", "tokenizer", "mean_tpw", "mean_tpc"]
    print("\n=== Mean tokens-per-word and tokens-per-char by (language, tokenizer) ===")
    print(summary.to_string(index=False))
    print()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Audit subword tokenizers for morphological boundary preservation."
    )
    parser.add_argument(
        "--testsets",
        nargs="+",
        choices=list(TESTSET_FILES.keys()),
        default=list(TESTSET_FILES.keys()),
        help="Which language test sets to include (default: all three).",
    )
    args = parser.parse_args()

    tokenizers = load_tokenizers()
    if not tokenizers:
        print("ERROR: no tokenizers loaded — aborting.", file=sys.stderr)
        sys.exit(1)

    rows = audit(args.testsets, tokenizers)
    write_csv(rows, RESULTS_CSV)
    print(f"Wrote {len(rows)} rows → {RESULTS_CSV}")
    print_summary(rows)


if __name__ == "__main__":
    main()
