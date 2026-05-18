# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Project Is

A navigable knowledge base for the SAMA "Minimum Capital Requirements for Credit Risk" circular (v2.1, Dec 2022) — Basel III Standardised Approach, Sections 1–9 only (~90 pages). Built with MkDocs Material, deployed to Vercel.

**Purpose:** A consultant reference tool — every clause is verbatim, cross-linked by number, and paired with a Mermaid decision flowchart.

## Build & Serve Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Serve locally (live reload)
mkdocs serve

# Build static site
mkdocs build

# Extract clause text from PDF
python scripts/extract_pdf.py
```

The built site lands in `site/`. Vercel runs `pip install -r requirements.txt && mkdocs build` automatically on push.

## Architecture

```
docs/
├── index.md                          # Master nav hub + SA framework Mermaid diagram
├── overview/                         # Sections 1–6
│   ├── introduction.md               # S1–3: Legal basis, scope, effective date
│   ├── sama-requirements.md          # S4: Q17 reporting
│   └── approaches-overview.md        # S5–6: SA vs IRB, due diligence
└── standardised-approach/            # Sections 7–9
    ├── index.md                      # Master exposure-type flowchart
    ├── individual-exposures.md       # S7: All 13 exposure categories, Tables 1–13
    ├── external-ratings.md           # S8: ECAIs, rating mapping, multiple ratings
    └── crm.md                        # S9: Collateral, netting, guarantees
```

`mkdocs.yml` uses `mkdocs-awesome-pages-plugin` — nav order is controlled by `.pages` files in each directory.

## Clause Rendering Pattern

Every clause follows this structure:

```markdown
### 7.1 Short title { #clause-7-1 }

=== "Clause Text"
    > **7.1** Verbatim text from document...

=== "Decision Flow"
    ```mermaid
    flowchart TD
        ...
    ```
```

- Anchor format: `{ #clause-X-Y }` for clauses, `{ #table-N }` for tables
- Cross-links: `[S7.34](#clause-7-34)` (same page) or `[S9 CRM](crm.md#clause-9-1)`
- Tables use standard markdown pipe syntax with `| --- |` separators

## Key Content Facts (for editing)

- **ECAI ratings map**: S&P/Moody's/Fitch → Credit Quality Steps 1–6
- **Sovereign floor**: Bank and corporate RWs cannot go below the home-sovereign RW
- **SCRA grades**: A=40%, B=75%, C=150% (short-term: A=20%, B=50%, C=150%)
- **Retail qualifying test**: 4 criteria — orientation, product, SAR 4.5M cap, 0.2% granularity
- **CRM substitution formula**: `E* = max{0, E×(1+He) − C×(1−Hc−Hfx)}`
- **Maturity mismatch formula**: `Pa = P × (t−0.25)/(T−0.25)`
- **Haircut scaling**: `H = H₁₀ × √((NR+TM−1)/10)`
