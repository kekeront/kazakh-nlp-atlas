"""Identity-layer tests for kb_ingest — every case here was a live stress-test failure."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from kb_ingest import ARXIV_RE, area_slug, canonical_id, parse_source


def test_arxiv_re_matches_all_source_forms():
    forms = [
        "arXiv 2405.04434",
        "arXiv:2405.04434v2",
        "arxiv.org/abs/2405.04434",
        "https://arxiv.org/abs/2405.04434",
        "https://arxiv.org/pdf/2405.04434v2",
        "http://arxiv.org/abs/2405.04434v5",  # arXiv API entry-id form
        "2405.04434",
    ]
    for form in forms:
        m = ARXIV_RE.search(form)
        assert m and m.group(1) == "2405.04434", f"failed on: {form}"


def test_same_paper_all_forms_one_node_id():
    ids = set()
    for s in [
        "arXiv 2405.04434 — DeepSeek-V2",
        "arxiv.org/abs/2405.04434",
        "https://arxiv.org/pdf/2405.04434v2",
    ]:
        src = parse_source(s)
        ids.add(canonical_id(src["arxiv_id"], src["doi"], src["title"], src["hf_repo"]))
    assert ids == {"arxiv:2405.04434"}


def test_cyrillic_titles_get_distinct_ids():
    a = canonical_id(None, None, "Қазақ тілінің ұлттық корпусы")
    b = canonical_id(None, None, "Ғылыми мақала: Ңұсқаулық Әдістеме")
    assert a and b and a != b
    assert a.startswith("title:қазақ")


def test_hf_repo_becomes_id_not_junk_title():
    src = parse_source("https://huggingface.co/Qwen/Qwen3-Embedding-0.6B config.json")
    nid = canonical_id(src["arxiv_id"], src["doi"], src["title"], src["hf_repo"])
    assert nid == "hf:qwen/qwen3-embedding-0.6b"


def test_hf_dataset_url_parses():
    src = parse_source("https://huggingface.co/datasets/issai/kazqad-retrieval")
    assert src["hf_repo"] == "issai/kazqad-retrieval"


def test_empty_identifier_returns_none_not_empty_title_id():
    assert canonical_id(None, None, "") is None
    assert canonical_id(None, None, "···—···") is None


def test_doi_url_and_bare_doi_merge():
    a = parse_source("doi 10.3390/app15042034 MDPI")
    b = parse_source("https://doi.org/10.3390/app15042034")
    assert (
        canonical_id(a["arxiv_id"], a["doi"], a["title"])
        == canonical_id(b["arxiv_id"], b["doi"], b["title"])
        == "doi:10.3390/app15042034"
    )


def test_area_slug_truncates_gapfill_questions():
    long_area = (
        "decoder-to-embedder: turning the ~500M Kazakh backbone into a SOTA "
        "embedder (joint vs post-hoc vs adapter), benchmark landscape"
    )
    assert area_slug(long_area) == "decoder-to-embedder"
    assert area_slug("sota-slm") == "sota-slm"
    assert len(area_slug("x" * 200)) <= 40
    assert area_slug("") == "unknown"
