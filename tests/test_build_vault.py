"""Offline guards for the deterministic vault builder — no network, no HF."""

from __future__ import annotations

import importlib.util
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "build_vault", Path(__file__).resolve().parent.parent / "scripts" / "build_vault.py"
)
bv = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(bv)


def test_slug_basic_kebab():
    assert (
        bv.slug("SentencePiece: A Simple Tokenizer", "x")
        == "sentencepiece-a-simple-tokenizer"
    )


def test_slug_non_ascii_falls_back_to_hash():
    # Cyrillic / math folds to empty -> stable hash keyed on the node id.
    out = bv.slug("Қазақ $μ$", "arxiv:1234.5678")
    assert out.startswith("n-") and len(out) == 10


def test_slug_dirty_doi_paren_survives():
    stem = bv.slug("doi:10.1145/3746252.3761077)", "doi:10.1145/3746252.3761077)")
    assert ")" not in stem and stem  # illegal char stripped, non-empty


def test_truncate_stem_cuts_on_boundary():
    long = "-".join(["word"] * 40)
    out = bv.truncate_stem(long, 80)
    assert len(out) <= 80 and not out.endswith("-")


def test_verdict_prefix_parsing():
    confirmed = {
        "verification": {
            "verdict": "CONFIRMED (numbers) — but does NOT support the plan"
        }
    }
    refuted = {
        "verification": {"verdict": "REFUTED (framing) — not the only datapoint"}
    }
    plausible = {"verification": {"verdict": "PLAUSIBLE pending T4 pilot"}}
    assert bv.claim_status(confirmed) == ("success", "CONFIRMED")
    assert bv.claim_status(refuted) == ("failure", "REFUTED")
    assert bv.claim_status(plausible) == ("question", "PLAUSIBLE")
    assert bv.claim_status({"uncertain": True}) == ("warning", "UNCERTAIN")
    assert bv.claim_status({}) == ("note", "CLAIM")


def test_is_paper_classifier():
    assert bv.is_paper({"arxiv_id": "1", "abstract": "text"})
    assert not bv.is_paper({"arxiv_id": "1", "abstract": ""})
    assert not bv.is_paper({"arxiv_id": None, "abstract": "text"})


def test_collision_suffixing():
    a = {
        "id": "arxiv:1",
        "arxiv_id": "1",
        "abstract": "x",
        "title": "Same Title",
        "topics": ["t"],
    }
    b = {
        "id": "arxiv:2",
        "arxiv_id": "2",
        "abstract": "x",
        "title": "Same Title",
        "topics": ["t"],
    }
    stems = bv.compute_filestems([a, b], ["t"])
    assert stems["arxiv:1"] != stems["arxiv:2"]  # collision broken
    assert len(set(stems.values())) == 2


def test_full_build_has_no_dangling_links():
    """Build the real KB in-memory (no links file) and assert validation passes."""
    nodes = bv.load_nodes()
    ctx = bv.build_context(nodes, {})
    files = bv.render_all(nodes, ctx)
    bv.validate(files, ctx)  # raises SystemExit on any dangling [[link]]
    assert len(files) == len(nodes) + len(ctx["topics"]) + 1  # nodes + MoCs + Home
