# Credit Risk Regulation Knowledge Base

A navigable reference tool for the **SAMA "Minimum Capital Requirements for Credit Risk"** circular (v2.1, Dec 2022), covering the Basel III Standardised Approach — Sections 1–9.

Every clause is rendered verbatim, cross-linked by number, and paired with a Mermaid decision flowchart for quick consultant reference.

---

> **Content Notice**
> All regulatory content in this repository is owned by the **Saudi Central Bank (SAMA)**.
> This tool is for reference purposes only. Always refer to the [SAMA official website](https://www.sama.gov.sa) for the latest and authoritative version of the circular.

---

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Serve locally with live reload
mkdocs serve
```

Then open `http://127.0.0.1:8000` in your browser.

```bash
# Build static site
mkdocs build
```

The built site lands in `site/`. Vercel runs `pip install -r requirements.txt && mkdocs build` automatically on push.
