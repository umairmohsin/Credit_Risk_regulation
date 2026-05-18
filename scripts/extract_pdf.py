"""
Extract structured content from SAMA credit risk PDF.

Font-size based detection (confirmed against SAMA Basel III PDF):
  Body text      : size=14pt (overview sections) or 11pt (clauses) or 10pt (list items)
  Inline sup ref : size=9pt, x0 > 70 (mid-text) — e.g. "... chapter 8.¹ The..."
  Footnote label : size=7pt, x0 ≈ 57 (left margin) — the "1  Footnote text..."
  Footnote text  : size=11pt, in footnote zone

Strategy per page:
  1. Find footnote zone start y: first size-7 digit at x0 < 80 below 45% of page height.
  2. Split chars into body (above) and footnote zone (at/below).
  3. Body text: reconstruct lines, inserting [^N] where size-9 digit chars appear.
  4. Footnote zone: parse {N: text} from lines starting with size-7 digit at left margin.
  5. Strip page header/footer lines.

Output: scripts/extracted_structured.json
  {
    "sections": {"7": "Individual Exposures", ...},
    "clauses": {
      "7.29": {
        "text": "Verbatim text with [^14] inline ref...",
        "footnotes": {"14": "Footnote text verbatim"},
        "tables": [[row, ...], ...]
      }
    }
  }

Usage: python scripts/extract_pdf.py
"""

import json
import re
import sys
from pathlib import Path

try:
    import pdfplumber
except ImportError:
    print("Install dependencies: pip install pdfplumber")
    sys.exit(1)

PDF_PATH = Path(__file__).parent.parent / "SAMA_Credit_risk-pages-1.pdf"
OUTPUT_PATH = Path(__file__).parent / "extracted_structured.json"

# Font size thresholds
FOOTNOTE_LABEL_SIZE_MAX = 7.5   # Footnote NUMBER label at left margin (size ~7pt)
FOOTNOTE_LABEL_X0_MAX = 85.0    # Footnote labels are within 85pt of left edge
                                 # (varies 57-72pt across pages; inline refs start at ~93pt+)
INLINE_SUP_SIZE_MIN = 8.5        # Inline superscript ref mid-text (size ~9pt)
INLINE_SUP_SIZE_MAX = 9.5
INLINE_SUP_X0_MIN = 88.0         # Inline refs are always further right than footnote labels

# Page footer marker
FOOTER_MARKER = "Version"

# Clause: "7.29" or "7.29.1" style
CLAUSE_RE = re.compile(r'(?:^|\n)(\d+\.\d+(?:\.\d+)?)\s+')

# Section heading detection
SECTION_RE = re.compile(r'^(\d+)\.\s+([A-Z][^\n]{3,80})$', re.MULTILINE)


def chars_to_lines(chars: list, y_tol: float = 3.0) -> list[tuple[float, list]]:
    """Group chars into lines by top-y bucket, return sorted [(y_bucket, [char, ...]), ...]."""
    if not chars:
        return []
    buckets: dict[float, list] = {}
    for c in chars:
        key = round(c['top'] / y_tol) * y_tol
        buckets.setdefault(key, []).append(c)
    return sorted(buckets.items())


def is_footnote_label(char: dict) -> bool:
    """True if char is a footnote label number (size ~7pt, within left margin zone)."""
    return (
        char['size'] <= FOOTNOTE_LABEL_SIZE_MAX
        and char['text'].strip().isdigit()
        and char['x0'] < FOOTNOTE_LABEL_X0_MAX
    )


def is_inline_sup(char: dict) -> bool:
    """True if char is an inline superscript reference (size ~9pt, mid-text)."""
    return (
        INLINE_SUP_SIZE_MIN <= char['size'] <= INLINE_SUP_SIZE_MAX
        and char['text'].strip().isdigit()
        and char['x0'] >= INLINE_SUP_X0_MIN
    )


def find_footnote_zone_y(chars: list, page_height: float) -> float | None:
    """
    Find y where footnote zone begins: first size-7 digit at left margin
    in the lower 55% of the page.
    Returns None if no footnotes on this page.
    """
    mid = page_height * 0.45
    for c in sorted(chars, key=lambda c: c['top']):
        if c['top'] > mid and is_footnote_label(c):
            return c['top']
    return None


def strip_footer_lines(
    lines: list[tuple[float, list]], page_height: float
) -> list[tuple[float, list]]:
    """Remove page header/footer lines (Version/Issuance Date block at bottom)."""
    footer_y = page_height * 0.90
    result = []
    skip_from_y: float | None = None

    for y, lchars in lines:
        if y >= footer_y:
            continue
        text = ''.join(c['text'] for c in sorted(lchars, key=lambda c: c['x0'])).strip()
        if FOOTER_MARKER in text and skip_from_y is None:
            skip_from_y = y
        if skip_from_y is not None and y >= skip_from_y:
            continue
        result.append((y, lchars))
    return result


def build_line_text_with_sups(lchars: list) -> str:
    """
    Reconstruct text from a line's chars, replacing inline superscript
    digit sequences with [^N] markers.
    """
    sorted_chars = sorted(lchars, key=lambda c: c['x0'])
    result = ''
    i = 0
    while i < len(sorted_chars):
        c = sorted_chars[i]
        if is_inline_sup(c):
            # Collect consecutive inline-sup digit chars
            num = c['text']
            j = i + 1
            while j < len(sorted_chars) and is_inline_sup(sorted_chars[j]):
                num += sorted_chars[j]['text']
                j += 1
            result += f'[^{num}]'
            i = j
        else:
            result += c['text']
            i += 1
    return result


def extract_page(page) -> tuple[str, dict[str, str]]:
    """
    Process one page.
    Returns (body_text, footnotes_dict).
    body_text has [^N] markers where inline superscript refs appear.
    footnotes_dict: {number_str: text_str}
    """
    chars = page.chars
    page_height = page.height

    fn_zone_y = find_footnote_zone_y(chars, page_height)

    body_chars = [c for c in chars if fn_zone_y is None or c['top'] < fn_zone_y]
    foot_chars = [c for c in chars if fn_zone_y is not None and c['top'] >= fn_zone_y]

    # Build body text
    body_lines = chars_to_lines(body_chars)
    body_lines = strip_footer_lines(body_lines, page_height)
    body_parts = [build_line_text_with_sups(lchars) for _y, lchars in body_lines]
    body_text = '\n'.join(body_parts)

    # Build footnote dict
    footnotes: dict[str, str] = {}
    if foot_chars:
        foot_lines = chars_to_lines(foot_chars)
        current_key: str | None = None
        current_parts: list[str] = []

        for _y, lchars in foot_lines:
            lchars_sorted = sorted(lchars, key=lambda c: c['x0'])
            first_non_space = next(
                (c for c in lchars_sorted if c['text'].strip()), None
            )
            if first_non_space is not None and is_footnote_label(first_non_space):
                # Save previous
                if current_key is not None:
                    footnotes[current_key] = ' '.join(current_parts).strip()
                # Start new footnote: collect label digits then rest of line
                fn_num = ''
                rest_chars = []
                collecting_label = True
                for c in lchars_sorted:
                    if collecting_label and is_footnote_label(c):
                        fn_num += c['text']
                    else:
                        collecting_label = False
                        rest_chars.append(c)
                current_key = fn_num
                rest_text = ''.join(c['text'] for c in rest_chars).strip()
                current_parts = [rest_text] if rest_text else []
            elif current_key is not None:
                line_str = ''.join(c['text'] for c in lchars_sorted).strip()
                if line_str:
                    current_parts.append(line_str)

        if current_key is not None and current_parts:
            footnotes[current_key] = ' '.join(current_parts).strip()

    return body_text, footnotes


def extract_all_pages() -> list[dict]:
    pages = []
    with pdfplumber.open(PDF_PATH) as pdf:
        total = len(pdf.pages)
        print(f"  PDF has {total} pages")
        for i, page in enumerate(pdf.pages):
            body_text, footnotes = extract_page(page)
            tables = page.extract_tables() or []
            pages.append({
                "page": i + 1,
                "body_text": body_text,
                "footnotes": footnotes,
                "tables": tables,
            })
            if (i + 1) % 10 == 0:
                print(f"  ... processed page {i + 1}/{total}")
    return pages


def normalise(text: str) -> str:
    return re.sub(r'[ \t]+', ' ', text).strip()


def build_structured_map(pages: list[dict]) -> dict:
    """
    Join all body text, split by clause number, attach footnotes.
    """
    full_body = ""
    page_boundaries: list[tuple[int, int, int, dict]] = []

    for p in pages:
        start = len(full_body)
        full_body += p["body_text"] + "\n"
        end = len(full_body)
        page_boundaries.append((start, end, p["page"], p["footnotes"]))

    def footnotes_for_range(cs: int, ce: int) -> dict[str, str]:
        merged: dict[str, str] = {}
        for pb_start, pb_end, _pno, fn in page_boundaries:
            if pb_start < ce and pb_end > cs:
                merged.update(fn)
        return merged

    matches = list(CLAUSE_RE.finditer(full_body))
    clauses: dict[str, dict] = {}

    for idx, m in enumerate(matches):
        clause_id = m.group(1)
        char_start = m.start()
        char_end = matches[idx + 1].start() if idx + 1 < len(matches) else len(full_body)
        raw = full_body[char_start:char_end]
        text = re.sub(r'[ \t]+', ' ', raw).strip()
        text = re.sub(r'\n+', '\n', text)

        all_footnotes = footnotes_for_range(char_start, char_end)
        refs_in_text = set(re.findall(r'\[\^(\d+)\]', text))
        # Primary: footnotes explicitly referenced inline in this clause
        referenced_fns = {k: v for k, v in all_footnotes.items() if k in refs_in_text}
        # Fallback: footnotes on the same page with NO inline ref anywhere in the document
        # (some footnotes are general page notes not linked via superscript)
        unreferenced_page_fns = {
            k: v for k, v in all_footnotes.items()
            if k not in refs_in_text
        }
        # Will be resolved after all clauses are built (see post-processing below)

        clauses[clause_id] = {
            "text": text,
            "footnotes": referenced_fns,
            "_page_fns": unreferenced_page_fns,  # temporary, removed after post-processing
            "tables": [],
        }

    # Post-process: attach unreferenced page footnotes only to the LAST clause on each page.
    # Step 1: collect all globally inline-referenced footnote numbers.
    globally_referenced = set()
    for cv in clauses.values():
        globally_referenced.update(cv["footnotes"].keys())

    # Step 2: for each page, find the LAST clause that starts on that page.
    clause_ids_ordered = [m.group(1) for m in matches]
    last_clause_for_page: dict[int, str] = {}
    for idx, m in enumerate(matches):
        cid = m.group(1)
        for pb_start, pb_end, pno, _fn in page_boundaries:
            if pb_start <= m.start() < pb_end:
                last_clause_for_page[pno] = cid  # keeps overwriting → last wins
                break

    # Step 3: attach unreferenced page footnotes to that last clause only.
    for pb_start, pb_end, pno, page_fns in page_boundaries:
        last_cid = last_clause_for_page.get(pno)
        if last_cid is None or last_cid not in clauses:
            continue
        for fn_num, fn_text in page_fns.items():
            if fn_num not in globally_referenced:
                clauses[last_cid]["footnotes"][fn_num] = fn_text

    # Step 4: remove temporary key.
    for cv in clauses.values():
        cv.pop("_page_fns", None)

    # Attach tables to first clause on each page
    for p in pages:
        if not p["tables"]:
            continue
        for pb_start, pb_end, pno, _fn in page_boundaries:
            if pno != p["page"]:
                continue
            for m in matches:
                if pb_start <= m.start() < pb_end:
                    cid = m.group(1)
                    if cid in clauses:
                        clauses[cid]["tables"].extend(p["tables"])
                    break
            break

    sections: dict[str, str] = {}
    for m in SECTION_RE.finditer(full_body):
        sections[m.group(1)] = m.group(2).strip()

    return {"sections": sections, "clauses": clauses}


def main():
    if not PDF_PATH.exists():
        print(f"ERROR: PDF not found at {PDF_PATH}")
        sys.exit(1)

    print(f"Reading {PDF_PATH} ...")
    pages = extract_all_pages()
    print("Building structured clause map ...")
    structured = build_structured_map(pages)

    clause_count = len(structured["clauses"])
    fn_count = sum(len(v["footnotes"]) for v in structured["clauses"].values())
    section_count = len(structured["sections"])

    # Sample output
    print("\nSample clauses (first 5):")
    for k in sorted(structured["clauses"].keys())[:5]:
        c = structured["clauses"][k]
        fn_label = f"  [{len(c['footnotes'])} fn]" if c["footnotes"] else ""
        preview = c["text"][:80].replace('\n', ' ')
        print(f"  S{k}: {preview}...{fn_label}")

    clauses_with_fn = {k: v for k, v in structured["clauses"].items() if v["footnotes"]}
    if clauses_with_fn:
        print(f"\nClauses with footnotes ({len(clauses_with_fn)}):")
        for k, v in list(clauses_with_fn.items())[:12]:
            for fn_num, fn_text in v["footnotes"].items():
                print(f"  S{k} [^{fn_num}]: {fn_text[:90]}...")

    OUTPUT_PATH.write_text(
        json.dumps(structured, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    print(f"\nDone.")
    print(f"  Sections detected : {section_count}")
    print(f"  Clauses extracted : {clause_count}")
    print(f"  Footnotes linked  : {fn_count}")
    print(f"  Output written to : {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
