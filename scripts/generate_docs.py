"""
Generate MkDocs markdown files from extracted_structured.json.

Creates one .md file per logical section, with:
  - Verbatim clause text in blockquotes (bold clause number prefix)
  - [^N] inline markers replaced with <sup>[N]</sup>
  - Footnotes rendered as ???+ note expandable admonitions
  - Tables rendered as markdown pipe tables
  - Placeholder "How it works" tab for diagrams (Phase 3 work)

Usage: python scripts/generate_docs.py
"""

import json
import re
import sys
from pathlib import Path

# Diagram library — maps clause_id -> list of diagram blocks
sys.path.insert(0, str(Path(__file__).parent))
from diagrams_data import get_diagram

# ── Paths ──────────────────────────────────────────────────────────────────
ROOT = Path(__file__).parent.parent
JSON_PATH = ROOT / "scripts" / "extracted_structured.json"
DOCS_ROOT = ROOT / "docs"

# ── Section structure ───────────────────────────────────────────────────────
# Each entry: (output_path, page_title, intro_text, [clause_ids...])
# Clause IDs can be exact ("7.1") or a string range ("7.1-7.3").
# Ranges are inclusive: all extracted clause IDs whose float value falls
# between start and end.
#
# NOTE: 3 and 4 have no numbered clauses — written as prose paragraphs.

SECTION_3_TEXT = (
    "This framework will be effective on **01 January 2023**."
)
SECTION_4_TEXT = (
    "SAMA expects all banks to report their credit RWAs and capital charge using "
    "SAMA's Q17 reporting template, which captures credit RWA computations under the "
    "Standardised Approach (SA) as well as under the IRB Approach."
)

SECTIONS = [
    # ── Overview ────────────────────────────────────────────────────────────
    (
        "overview/introduction.md",
        "Introduction & Scope",
        "Sections 1–4: Legal basis, scope, effective date, and SAMA reporting.",
        "range:1.1-2.2",
        "prose",   # special: append 3 and 4 prose after clauses
    ),
    (
        "overview/approaches-overview.md",
        "Approaches Overview & Due Diligence",
        "Sections 5–6: Standardised vs IRB approach selection and due diligence requirements.",
        "range:5.1-6.3",
        None,
    ),
    # ── Section 7: Individual Exposures ─────────────────────────────────────
    (
        "section-7/index.md",
        "Section 7 — Individual Exposures Overview",
        (
            "Section 7 assigns risk weights to each of the 13 exposure categories "
            "under the Standardised Approach. Use the links below to navigate to each category."
        ),
        None,   # index page — no clauses, nav cards generated separately
        "index",
    ),
    (
        "section-7/7-1-sovereigns.md",
        "7.1–7.3 Sovereigns & Central Banks",
        "Risk weights for exposures to sovereigns, central banks, and certain international institutions.",
        "range:7.1-7.3",
        None,
    ),
    (
        "section-7/7-2-pse.md",
        "7.4–7.7 Public Sector Entities (PSEs)",
        "Treatment of domestic and foreign non-central-government public sector entities.",
        "range:7.4-7.7",
        None,
    ),
    (
        "section-7/7-3-mdb.md",
        "7.8–7.11 Multilateral Development Banks (MDBs)",
        "0% and standard risk weights for eligible and other MDB exposures.",
        "range:7.8-7.11",
        None,
    ),
    (
        "section-7/7-4-banks.md",
        "7.12–7.35 Banks & Covered Bonds",
        (
            "Bank exposures use the External Credit Risk Assessment (ECRA) approach for rated banks "
            "and the Standardised Credit Risk Assessment (SCRA) for unrated banks. "
            "Covered bonds are also treated under this section."
        ),
        "range:7.12-7.35",
        None,
    ),
    (
        "section-7/7-5-securities-firms.md",
        "7.36 Securities Firms & Other Financial Institutions",
        "Risk weight treatment for securities firms and comparable regulated financial institutions.",
        "range:7.36-7.36",
        None,
    ),
    (
        "section-7/7-6-corporates.md",
        "7.37–7.46 Corporates & Specialised Lending",
        (
            "Base risk weights for rated and unrated corporate exposures, SME treatment, "
            "and the five sub-categories of specialised lending."
        ),
        "range:7.37-7.46",
        None,
    ),
    (
        "section-7/7-7-equity.md",
        "7.47–7.54 Equity Exposures",
        "Definition of equity holdings, risk weights for speculative and non-speculative equity.",
        "range:7.47-7.54",
        None,
    ),
    (
        "section-7/7-8-retail.md",
        "7.55–7.60 Retail Exposures",
        (
            "Qualifying criteria for regulatory retail (75% RW), transactors, "
            "other retail, and the SAR 4.5 million granularity cap."
        ),
        "range:7.55-7.60",
        None,
    ),
    (
        "section-7/7-9-real-estate.md",
        "7.61–7.84 Real Estate Exposures",
        (
            "Regulatory real estate definitions, LTV-based risk weight tables for "
            "residential and commercial property, ADC exposures, and FX mismatch add-on."
        ),
        "range:7.61-7.85",
        None,
    ),
    (
        "section-7/7-10-off-balance-sheet.md",
        "7.86–7.93 Off-Balance Sheet Items",
        "Credit Conversion Factors (CCFs) for commitments, guarantees, trade finance, and derivatives.",
        "range:7.86-7.93",
        None,
    ),
    (
        "section-7/7-11-default-other.md",
        "7.94–7.102 Counterparty Credit Risk, Default & Other Assets",
        (
            "Treatment of defaulted exposures, past-due items, higher-risk categories, "
            "and the standard 100% risk weight for other assets."
        ),
        "range:7.94-7.102",
        None,
    ),
    # ── Section 8 ────────────────────────────────────────────────────────────
    (
        "section-8/index.md",
        "Section 8 — External Ratings (ECAIs)",
        (
            "Requirements for using external credit assessments, ECAI eligibility, "
            "mapping of ratings to Credit Quality Steps, and multiple-rating rules."
        ),
        "range:8.1-8.9",
        None,
    ),
    # ── Section 9 ────────────────────────────────────────────────────────────
    (
        "section-9/index.md",
        "Section 9 — Credit Risk Mitigation (CRM) Overview",
        "Section 9 governs collateral, on-balance-sheet netting, guarantees, and credit derivatives.",
        None,
        "index",
    ),
    (
        "section-9/9-1-general.md",
        "9.1–9.15 General CRM Requirements",
        "Legal certainty, eligibility conditions, and maturity mismatch treatment.",
        "range:9.1-9.15",
        None,
    ),
    (
        "section-9/9-2-simple.md",
        "9.16–9.39 Collateral — Simple Approach",
        "Risk weight substitution using recognised financial collateral.",
        "range:9.16-9.39",
        None,
    ),
    (
        "section-9/9-3-comprehensive.md",
        "9.40–9.64 Collateral — Comprehensive Approach",
        (
            "Haircut-adjusted exposure calculation (E* formula), supervisory haircuts, "
            "own estimates, and SFT netting."
        ),
        "range:9.40-9.64",
        None,
    ),
    (
        "section-9/9-4-netting.md",
        "9.65–9.69 On-Balance Sheet Netting",
        "Conditions under which loans and deposits with the same counterparty may be netted.",
        "range:9.65-9.69",
        None,
    ),
    (
        "section-9/9-5-guarantees.md",
        "9.70–9.83 Guarantees & Credit Derivatives",
        "Substitution approach for eligible guarantors and credit derivative protection.",
        "range:9.70-9.83",
        None,
    ),
]


# ── Text helpers ─────────────────────────────────────────────────────────────

# Unicode replacement char sequences from the PDF → likely intended characters
ENCODING_FIXES = [
    ("�", "'"),   # most common: right single quote / apostrophe
    ("�", "'"),        # same in some encodings
]

SUP_REF_RE = re.compile(r'\[\^(\d+)\]')

# Strip page footer that bleeds into footnote/clause text
FOOTER_STRIP_RE = re.compile(
    r'\s*Version\s+Issuance\s+Date\s+Page\s+Number.*',
    re.DOTALL | re.IGNORECASE,
)


def fix_encoding(text: str) -> str:
    for bad, good in ENCODING_FIXES:
        text = text.replace(bad, good)
    return text


def inline_sups_to_html(text: str) -> str:
    """Replace [^N] markers with <sup>[N]</sup> for visual rendering."""
    return SUP_REF_RE.sub(lambda m: f'<sup>[{m.group(1)}]</sup>', text)


def clean_clause_text(raw: str) -> str:
    """
    Clean extracted clause text:
      - Fix encoding
      - Strip page footer bleed
      - Strip the leading clause number (e.g. '7.1 ')
      - Join broken lines into paragraphs
      - Inline footnote markers
    """
    text = fix_encoding(raw)
    text = FOOTER_STRIP_RE.sub('', text)

    # Remove leading clause number (e.g. "7.1 " at the very start)
    text = re.sub(r'^\d+\.\d+(?:\.\d+)?\s+', '', text, count=1)

    # Detect paragraph breaks: two or more newlines → double newline
    text = re.sub(r'\n{2,}', '\n\n', text)

    # Join single-line-breaks (soft wraps from PDF) — but keep double newlines
    # Split on double newline, join single newlines within each paragraph
    paragraphs = text.split('\n\n')
    joined = []
    for para in paragraphs:
        lines = para.split('\n')
        result_lines = []  # final output lines for this paragraph
        buffer = []        # accumulates soft-wrapped regular text
        in_list = False    # True after we've seen a numbered list item

        for line in lines:
            stripped = line.strip()
            if not stripped:
                continue
            # [^N] markers merge with last content (don't break the line)
            if re.fullmatch(r'(\[\^\d+\]\s*)+', stripped):
                if result_lines:
                    result_lines[-1] = result_lines[-1].rstrip() + stripped
                elif buffer:
                    buffer[-1] = buffer[-1].rstrip() + stripped
            elif re.match(r'^\d+\.\s+', stripped):
                # Numbered list item — flush any pre-list buffer first
                if buffer:
                    result_lines.append(' '.join(buffer))
                    buffer = []
                result_lines.append(stripped)
                in_list = True
            else:
                if in_list and result_lines:
                    # Continuation of the last list item (PDF soft-wrap)
                    result_lines[-1] = result_lines[-1].rstrip() + ' ' + stripped
                else:
                    buffer.append(stripped)

        if buffer:
            result_lines.append(' '.join(buffer))

        joined.append('\n'.join(result_lines))

    text = '\n\n'.join(p for p in joined if p)
    return text.strip()


def render_table(table: list[list]) -> str:
    """Render a raw pdfplumber table (list of rows) as a markdown pipe table."""
    if not table:
        return ""

    # Clean cells: strip whitespace and newlines
    cleaned = []
    for row in table:
        if row and any(cell for cell in row if cell):
            cleaned.append([str(cell or '').replace('\n', ' ').strip() for cell in row])

    if not cleaned:
        return ""

    # First row = header
    header = cleaned[0]
    sep = ['---'] * len(header)
    rows = cleaned[1:]

    lines = ['| ' + ' | '.join(header) + ' |']
    lines.append('| ' + ' | '.join(sep) + ' |')
    for row in rows:
        # Pad row if shorter than header
        padded = row + [''] * max(0, len(header) - len(row))
        lines.append('| ' + ' | '.join(padded[:len(header)]) + ' |')

    return '\n'.join(lines)


def render_footnote_admonition(fn_num: str, fn_text: str) -> str:
    """Render a footnote as a collapsible ???+ note admonition."""
    clean_text = fix_encoding(fn_text)
    # Strip any page footer text that bled into the footnote
    clean_text = FOOTER_STRIP_RE.sub('', clean_text).strip()
    # Indent the footnote body by 4 spaces (admonition requirement)
    indented = '\n'.join('    ' + line for line in clean_text.splitlines())
    return f'???+ note "Footnote [{fn_num}]"\n{indented}'


def anchor_id(clause_id: str) -> str:
    """Convert '7.29' → 'clause-7-29'."""
    return 'clause-' + clause_id.replace('.', '-')


def heading_phrase(clean_text: str) -> str:
    """
    Extract the first natural phrase/sentence for use in H3 headings.

    Split rules (in order):
      - Colon or semicolon         →  "… as follows" / "… where applicable"
      - Period followed by space+capital letter  →  true sentence boundary
        (skips decimals like 7.57 and abbreviations like i.e. / e.g.)
      - Exclamation / question mark
    No character-count truncation.
    """
    # Work on footnote-marker-free text so index positions stay consistent
    search_text = re.sub(r'\[\^\d+\]', '', clean_text)
    m = re.search(r'[;:]|\.(?=\s+[A-Z0-9])|[!?]', search_text)
    phrase = search_text[:m.start()].strip() if m else search_text.strip()
    # Strip trailing punctuation / whitespace
    phrase = re.sub(r'[\s;:,.]+$', '', phrase).strip()
    # Guard: if the extracted phrase is very short (< 10 chars) it's a fragment;
    # fall back to word-boundary-truncated text at ~120 chars
    if len(phrase) < 10:
        words = search_text.split()
        phrase = ''
        for w in words:
            if len(phrase) + len(w) + 1 > 120:
                break
            phrase = (phrase + ' ' + w).strip()
    return phrase


# ── Clause rendering ─────────────────────────────────────────────────────────

def render_blockquote(clause_id: str, body_with_sups: str, tables: list, indent: str = '') -> list[str]:
    """Build blockquote lines for clause text + any PDF-extracted tables."""
    paragraphs = body_with_sups.split('\n\n')
    bq_lines = []
    first = True
    for para in paragraphs:
        if not first:
            bq_lines.append(f'{indent}>')
        for line in para.splitlines():
            prefix = f'{indent}> **{clause_id}** ' if first else f'{indent}> '
            bq_lines.append(prefix + line)
            first = False
    for tbl in tables:
        rendered = render_table(tbl)
        if rendered:
            bq_lines.append(f'{indent}>')
            for tbl_line in rendered.splitlines():
                bq_lines.append(f'{indent}> {tbl_line}')
    return bq_lines


def render_clause(clause_id: str, clause_data: dict) -> str:
    """
    Render one clause:
      - H3 heading = clause number + first natural sentence/phrase
      - If diagram exists: tabbed layout (Clause Text | How it works)
      - If no diagram: blockquote directly, no tabs
      - Footnote expandable admonitions below
    """
    raw_text = clause_data.get("text", "")
    footnotes = clause_data.get("footnotes", {})
    tables = clause_data.get("tables", [])

    clean = clean_clause_text(raw_text)
    body_with_sups = inline_sups_to_html(clean)
    aid = anchor_id(clause_id)
    diagram_blocks = get_diagram(clause_id)

    phrase = heading_phrase(clean)
    heading = f'{clause_id} {phrase}' if phrase else clause_id

    lines = [
        f'### {heading} {{ #{aid} }}',
        '',
    ]

    if diagram_blocks:
        # Tabbed layout: clause text in tab 1, diagram(s) in tab 2
        lines.append('=== "Clause Text"')
        for bq_line in render_blockquote(clause_id, body_with_sups, tables, indent='    '):
            lines.append(bq_line)

        lines.append('')
        lines.append('=== "How it works"')
        for block in diagram_blocks:
            btype = block["type"]
            btitle = block.get("title", "")
            bcontent = block["content"]
            if btitle:
                lines.append(f'    **{btitle}**')
                lines.append('')
            if btype == "mermaid":
                lines.append('    ```mermaid')
                for ln in bcontent.splitlines():
                    lines.append('    ' + ln)
                lines.append('    ```')
            elif btype in ("matrix", "steps"):
                for ln in bcontent.splitlines():
                    lines.append('    ' + ln)
            lines.append('')
    else:
        # No diagram — plain blockquote, no tabs
        for bq_line in render_blockquote(clause_id, body_with_sups, tables):
            lines.append(bq_line)

    # Footnote admonitions
    if footnotes:
        lines.append('')
        for fn_num in sorted(footnotes.keys(), key=lambda x: int(x)):
            lines.append(render_footnote_admonition(fn_num, footnotes[fn_num]))

    lines.append('')
    lines.append('---')
    lines.append('')

    return '\n'.join(lines)


# ── Section file generation ───────────────────────────────────────────────────

def clauses_in_range(all_clauses: dict, range_spec: str) -> list[str]:
    """
    Given "range:7.1-7.3", return sorted clause IDs in [7.1, 7.3] inclusive.
    Uses float comparison on the clause ID's decimal value.
    """
    if not range_spec or not range_spec.startswith("range:"):
        return []
    parts = range_spec[6:].split('-')
    if len(parts) != 2:
        return []

    def clause_sort_key(cid: str) -> float:
        # "7.12" → 7.12, "7.100" → 7.100 but we need lexicographic within section
        parts = cid.split('.')
        major = int(parts[0])
        minor = int(parts[1]) if len(parts) > 1 else 0
        return major * 10000 + minor

    start_key = clause_sort_key(parts[0])
    # Handle "7.3" as end meaning everything from start up to and including 7.3
    end_parts = parts[1].split('.')
    end_key = int(end_parts[0]) * 10000 + (int(end_parts[1]) if len(end_parts) > 1 else 9999)

    result = [
        cid for cid in all_clauses
        if start_key <= clause_sort_key(cid) <= end_key
    ]
    return sorted(result, key=clause_sort_key)


def generate_section(
    out_path: Path,
    page_title: str,
    intro: str,
    clause_ids: list[str],
    all_clauses: dict,
    special: str | None,
) -> None:
    """Write one section markdown file."""
    out_path.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        f'# {page_title}',
        '',
        intro,
        '',
        '---',
        '',
    ]

    if special == "index":
        # Index pages get a nav-card hint; actual cards added in Phase 4 UI work
        lines.append(
            '!!! tip "Navigation"\n'
            '    Use the sidebar or the cards below to jump to each sub-section.\n'
        )
        out_path.write_text('\n'.join(lines), encoding='utf-8')
        print(f'  [index]  {out_path.relative_to(ROOT)}')
        return

    if special == "prose":
        # Append 3 and 4 as plain prose sections after clauses
        pass  # handled below

    # Render clauses
    for cid in clause_ids:
        if cid in all_clauses:
            lines.append(render_clause(cid, all_clauses[cid]))
        else:
            lines.append(f'<!-- TODO: clause {cid} not found in extracted data -->\n\n---\n')

    # 3 and 4 prose appended to introduction.md
    if special == "prose":
        lines += [
            '## Section 3 — Implementation Timeline { #section-3 }',
            '',
            SECTION_3_TEXT,
            '',
            '---',
            '',
            '## Section 4 — SAMA Reporting Requirements { #section-4 }',
            '',
            SECTION_4_TEXT,
            '',
        ]

    out_path.write_text('\n'.join(lines), encoding='utf-8')
    print(f'  [ok]     {out_path.relative_to(ROOT)}  ({len(clause_ids)} clauses)')


# ── mkdocs.yml nav update ─────────────────────────────────────────────────────

NEW_NAV = """nav:
  - Home: index.md
  - Overview:
    - overview/introduction.md
    - Introduction 1–4: overview/introduction.md
    - Approaches & Due Diligence 5–6: overview/approaches-overview.md
  - Section 7 — Individual Exposures:
    - section-7/index.md
    - Sovereigns & Central Banks 7.1–7.3: section-7/7-1-sovereigns.md
    - Public Sector Entities 7.4–7.7: section-7/7-2-pse.md
    - Multilateral Dev. Banks 7.8–7.11: section-7/7-3-mdb.md
    - Banks & Covered Bonds 7.12–7.35: section-7/7-4-banks.md
    - Securities Firms 7.36: section-7/7-5-securities-firms.md
    - Corporates & Spec. Lending 7.37–7.46: section-7/7-6-corporates.md
    - Equity 7.47–7.54: section-7/7-7-equity.md
    - Retail 7.55–7.60: section-7/7-8-retail.md
    - Real Estate 7.61–7.85: section-7/7-9-real-estate.md
    - Off-Balance Sheet 7.86–7.93: section-7/7-10-off-balance-sheet.md
    - Default & Other Assets 7.94–7.102: section-7/7-11-default-other.md
  - Section 8 — External Ratings:
    - Section 8 Overview: section-8/index.md
  - Section 9 — Credit Risk Mitigation:
    - section-9/index.md
    - General Requirements 9.1–9.15: section-9/9-1-general.md
    - Simple Approach 9.16–9.39: section-9/9-2-simple.md
    - Comprehensive Approach 9.40–9.64: section-9/9-3-comprehensive.md
    - On-Balance Sheet Netting 9.65–9.69: section-9/9-4-netting.md
    - Guarantees & Credit Derivatives 9.70–9.83: section-9/9-5-guarantees.md
  - Downloads: downloads/index.md
"""


def update_mkdocs_nav() -> None:
    mkdocs_path = ROOT / "mkdocs.yml"
    content = mkdocs_path.read_text(encoding='utf-8')
    # Replace nav block
    content = re.sub(r'\nnav:.*', '\n' + NEW_NAV.rstrip(), content, flags=re.DOTALL)
    mkdocs_path.write_text(content, encoding='utf-8')
    print(f'  [ok]     mkdocs.yml nav updated')


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    if not JSON_PATH.exists():
        print(f"ERROR: Run extract_pdf.py first — {JSON_PATH} not found")
        sys.exit(1)

    data = json.loads(JSON_PATH.read_text(encoding='utf-8'))
    all_clauses = data["clauses"]

    print(f"Generating docs from {len(all_clauses)} clauses ...")
    print()

    for entry in SECTIONS:
        out_rel, title, intro, range_spec, special = entry
        out_path = DOCS_ROOT / out_rel

        if range_spec:
            cids = clauses_in_range(all_clauses, range_spec)
        else:
            cids = []

        generate_section(out_path, title, intro, cids, all_clauses, special)

    print()
    update_mkdocs_nav()
    print()
    print("Done. Run 'mkdocs serve' to preview.")


if __name__ == "__main__":
    main()
