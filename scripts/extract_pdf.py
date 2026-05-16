"""
Extract structured content from SAMA credit risk PDF.
Outputs JSON with clause numbers as keys.

Usage: python scripts/extract_pdf.py
Output: scripts/extracted.json
"""

import json
import re
import sys
from pathlib import Path

try:
    import pdfplumber
except ImportError:
    print("Install dependencies: pip install pdfplumber pymupdf")
    sys.exit(1)

PDF_PATH = Path(__file__).parent.parent / "SAMA_Credit_risk-pages-1.pdf"
OUTPUT_PATH = Path(__file__).parent / "extracted.json"

CLAUSE_RE = re.compile(r'^(\d+\.\d+)\s+(.+)', re.MULTILINE)
SECTION_RE = re.compile(r'^(\d+)\.\s+(.+)')

def clean_text(text: str) -> str:
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract_all_pages():
    pages = []
    with pdfplumber.open(PDF_PATH) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text(x_tolerance=2, y_tolerance=2) or ""
            tables = page.extract_tables() or []
            pages.append({
                "page": i + 1,
                "text": text,
                "tables": tables
            })
    return pages

def build_clause_map(pages):
    full_text = "\n".join(p["text"] for p in pages)
    clauses = {}
    matches = list(CLAUSE_RE.finditer(full_text))
    for idx, m in enumerate(matches):
        clause_id = m.group(1)
        start = m.start()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(full_text)
        clause_text = full_text[start:end].strip()
        clauses[clause_id] = {"text": clause_text, "tables": []}

    # Attach tables from pages
    for page in pages:
        for table in page["tables"]:
            if table:
                clauses.setdefault(f"table_p{page['page']}", {"text": "", "tables": []})
                clauses[f"table_p{page['page']}"]["tables"].append(table)

    return clauses

def main():
    print(f"Reading {PDF_PATH} ...")
    pages = extract_all_pages()
    print(f"  Extracted {len(pages)} pages")
    clauses = build_clause_map(pages)
    print(f"  Found {len(clauses)} clause entries")
    OUTPUT_PATH.write_text(json.dumps(clauses, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  Written to {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
