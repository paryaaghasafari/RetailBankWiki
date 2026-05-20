# Loading the Corpus into Your RAG Pipeline

> Ingestion guidance for the team building the Northvale Demo Bank RAG demo on top of this wiki. The corpus is **fully local** and **self-contained** — no external URLs, no cloud dependencies. Clone the repo, generate the binary attachments, and load.

---

## What to include in the embedding corpus

**Include** (these are the source documents an end user is asking about):

| Path | Type | Notes |
|---|---|---|
| `docs/Home.md` | Markdown | Wiki landing page |
| `docs/KYC-Customer-Onboarding-Policy.md` | Markdown | |
| `docs/AML-Anti-Money-Laundering-Procedures.md` | Markdown | |
| `docs/Credit-Risk-Assessment-Guidelines.md` | Markdown | |
| `docs/Loan-Approval-Thresholds-and-Limits.md` | Markdown | |
| `docs/Customer-Complaint-Handling-Policy.md` | Markdown | |
| `docs/Sanctions-Screening-Procedures.md` | Markdown | |
| `docs/attachments/compliance-handbook-v8.pdf` | PDF | 5 pages, embeds 2 PNGs |
| `docs/attachments/regulatory-circular-2026-02.pdf` | PDF | 5 pages, embeds 1 PNG |
| `docs/attachments/credit-policy-manual.pdf` | PDF | 10 pages, embeds 1 PNG |
| `docs/attachments/credit-officer-decision-framework.docx` | DOCX | 5 pages |
| `docs/attachments/quarterly-compliance-update-q1-2026.docx` | DOCX | 3 pages |

**Exclude** (these are meta / config — not user-queryable content):

- `README.md` — repo orientation
- `LICENSE`
- `SEEDED-FACTS.md` — fact register for eval design
- `EVAL-QUESTIONS.md` — **ground truth — do not embed**
- `LOAD-CORPUS.md` — this file
- `docs/_Sidebar.md` — wiki navigation chrome
- `mkdocs.yml`, `pyproject.toml`, `.python-version`, `uv.lock`
- `scripts/` directory
- `problem_statement.jpg`
- `docs/attachments/*.png` — the PNGs are also embedded inside the relevant PDFs and described in prose ("Figure description" sections) in the wiki pages, so PNG bytes are redundant for retrieval. (Cite the PNG **path** from a figure-description chunk, but don't OCR or re-embed the bytes.)

---

## Recommended chunking — heading-aware

Every markdown page is structured so a `MarkdownHeaderTextSplitter` keyed on `##` and `###` yields self-contained chunks. The headers used across every policy page are:

```
## Summary
## Definitions
## Contents
## 1. <Section name>          # main sections, numbered 1–N
   ### Key takeaways
   ### Related Procedures
   ### Figure description    # under sections that embed a PNG
## Common Scenarios
## FAQ
## Cross-References
## Attachments
## See also
```

A two-pass splitter is recommended:

1. **Pass 1**: `MarkdownHeaderTextSplitter` on `##` and `###`. This produces one chunk per top-level section and one chunk per sub-section.
2. **Pass 2**: For any chunk exceeding ~800 tokens, run a `RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=120, separators=["\n\n", "\n", ". ", " "])`. The recursive splitter respects paragraph boundaries so it won't split mid-table or mid-prose.

Example (LangChain):

```python
from langchain.text_splitter import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter

headers = [("##", "section"), ("###", "subsection")]
md_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers, strip_headers=False)

char_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=120,
    separators=["\n\n", "\n", ". ", " "],
)

with open("docs/KYC-Customer-Onboarding-Policy.md") as f:
    md_chunks = md_splitter.split_text(f.read())

final_chunks = []
for chunk in md_chunks:
    if len(chunk.page_content) > 3500:    # ~800 tokens
        final_chunks.extend(char_splitter.split_documents([chunk]))
    else:
        final_chunks.append(chunk)
```

Target chunk size is **500–800 tokens** (counted with `tiktoken` `cl100k_base`). The wiki pages are written so most `##` and `###` sub-sections land in this band naturally.

---

## Recommended metadata per chunk

Attach these fields to every chunk for retrieval filtering, ranking, and citation rendering:

| Metadata field | Source | Example |
|---|---|---|
| `source_path` | The file path | `docs/KYC-Customer-Onboarding-Policy.md` |
| `source_type` | `markdown` / `pdf` / `docx` | `markdown` |
| `page_title` | YAML `title` field | `KYC — Customer Onboarding Policy` |
| `slug` | YAML `slug` field | `kyc-customer-onboarding-policy` |
| `section_path` | The header trail | `1. Customer Identification Program (CIP) > Key takeaways` |
| `subdomain` | YAML `subdomain` field | `compliance` |
| `owner` | YAML `owner` field | `Office of the Chief Compliance Officer` |
| `version` | YAML `version` field | `8.0` |
| `effective_date` | YAML `effective_date` field | `2026-01-01` |
| `keywords` | YAML `keywords` field | `["kyc", "cip", "cdd", ...]` |
| `related_attachments` | YAML `related_attachments` field | `["docs/attachments/compliance-handbook-v8.pdf"]` |

The frontmatter is at the top of every `.md` page, between two `---` lines. Parse with `yaml.safe_load`.

---

## Loading PDFs and DOCX

For the binary attachments, the **prose figure descriptions inside the wiki pages** are richer than OCR of the embedded PNGs would be. Trust the markdown for image-grounded queries (Q12 in `EVAL-QUESTIONS.md`).

Recommended loaders (LangChain):

```python
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader

pdf_docs = PyPDFLoader("docs/attachments/compliance-handbook-v8.pdf").load()
docx_docs = Docx2txtLoader("docs/attachments/credit-officer-decision-framework.docx").load()
```

Both PDFs and DOCX files have **headings** (`<h1>`, `<h2>`, `<h3>` equivalents) that survive into the loader output. Run the same two-pass splitter on them — the section structure mirrors the markdown pages.

---

## Retrieval recommendations

- **Embedding model**: OpenAI `text-embedding-3-large` (3072 dims) or Anthropic-compatible equivalent. Pinecone / Chroma both work; both are mentioned in the problem statement.
- **Top-k**: Start with `k=8`, then re-rank to `k=4` for context. Cross-page questions (Q13–Q16 in the eval set) require retrieving from at least two source files, so a too-tight `k` will fail those.
- **Metadata filters**: Filter on `subdomain` and `effective_date` if the user asks about a specific area or a point-in-time policy.
- **Citation rendering**: Cite by `source_path` plus `section_path`. The eval set scores citations at file-path level, but you should display the section so the user can verify quickly.

---

## Validating with the eval set

`EVAL-QUESTIONS.md` contains 20 ground-truth questions structured as YAML blocks. Each block specifies:

- `expected_citations` — file paths that **must** appear in your pipeline's citation output.
- `acceptable_alternatives` — file paths that may substitute (e.g., an attachment that restates the same fact).
- `expected_answer_summary` — the canonical answer for semantic scoring.
- For out-of-scope (Q17–Q20): `expected_behavior` (graceful refusal) and `forbidden_content` (things a hallucinating system would emit).

A simple eval loop in pseudo-code:

```python
import yaml, re

with open("EVAL-QUESTIONS.md") as f:
    blocks = re.findall(r"```yaml\n(.*?)\n```", f.read(), re.S)
questions = [yaml.safe_load(b) for b in blocks]

for q in questions:
    response = rag_pipeline.ask(q["question"])    # your pipeline
    cited = set(response.cited_paths)
    expected = set(q.get("expected_citations", []))
    alts = set(q.get("acceptable_alternatives", []))

    citation_ok = expected.issubset(cited) or expected.issubset(cited | alts)
    # ... and run an LLM-as-judge or semantic-similarity check on the answer
```

---

## Re-generating the binary attachments

If the `docs/attachments/` folder is empty after cloning, regenerate it:

```bash
uv sync
uv run python scripts/generate_images.py
uv run python scripts/generate_pdfs.py
uv run python scripts/generate_docx.py
```

This produces all 9 binaries (4 PNG, 3 PDF, 2 DOCX). Generation is deterministic — identical bytes on every run.

---

## Browsing the wiki visually

The wiki is hosted on GitHub Pages — open <https://paryaaghasafari.github.io/RetailBankWiki/> in a browser for the rendered Wikipedia-style view (left navigation panel, in-page Table of Contents, full-text search).

To run the same site locally instead:

```bash
uv run mkdocs serve
# -> http://127.0.0.1:8000
```

The site uses MkDocs Material with the same `.md` files as the embedding corpus — no duplication.
