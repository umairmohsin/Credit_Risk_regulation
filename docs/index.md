# SAMA Credit Risk Framework

**Minimum Capital Requirements for Credit Risk** — Saudi Central Bank (SAMA), Version 2.1, December 2022  
Implementing Basel III Standardised Approach for credit risk capital adequacy.

---

## What This Is

This knowledge base materialises the SAMA Credit Risk circular into a navigable reference for practitioners. Every clause is preserved verbatim, cross-linked by number, and paired with a decision flowchart so you can answer *"which rule applies here?"* without memorising the document.

**Scope:** Sections 1–9 only (Introduction through Standardised Approach: Credit Risk Mitigation).  
**Legal authority:** Royal Decree M/36 dated 15/04/1428H; Banking Control Law Article 3(A).  
**Effective date:** 01 January 2023.

---

## How to Navigate

| You want to… | Go to… |
|---|---|
| Understand what this regulation covers | [Introduction & Scope](overview/introduction.md) |
| See SAMA reporting obligations | [SAMA Reporting Requirements](overview/sama-requirements.md) |
| Choose between SA and IRB approaches | [Approaches Overview](overview/approaches-overview.md) |
| Find the risk weight for a specific counterparty | [Individual Exposures S7](standardised-approach/individual-exposures.md) |
| Understand ECAI / external rating rules | [External Ratings S8](standardised-approach/external-ratings.md) |
| Apply collateral, guarantees, or netting | [Credit Risk Mitigation S9](standardised-approach/crm.md) |

---

## Framework Overview

```mermaid
flowchart TD
    A[Bank Identifies Exposure] --> B{Approach Approved?}
    B -- SA default --> C[Standardised Approach S6–9]
    B -- SAMA approval granted --> D[IRB Approach S10–16]
    
    C --> E{Exposure Type S7}
    E --> E1[Sovereign S7.1–7.3]
    E --> E2[PSE S7.4–7.6]
    E --> E3[MDB S7.7–7.9]
    E --> E4[Banks S7.10–7.19]
    E --> E5[Securities Firms S7.20–7.22]
    E --> E6[Corporate S7.23–7.28]
    E --> E7[Retail S7.29–7.32]
    E --> E8[Real Estate S7.33–7.59]
    E --> E9[Other Exposures S7.60–7.102]

    E1 & E2 & E3 & E4 & E5 & E6 & E7 & E8 & E9 --> F[Assign Risk Weight]
    F --> G{CRM Applicable? S9}
    G -- Yes --> H[Adjust Exposure/RW via CRM]
    G -- No --> I[Compute RWA = RW × EAD]
    H --> I
    I --> J[Report via Q17 Template S4]
```

---

## Section Map

```mermaid
flowchart LR
    S1[S1 Introduction] --> S5[S5 Approaches]
    S2[S2 Scope] --> S5
    S3[S3 Implementation] --> S5
    S4[S4 Reporting] --> S5
    S5 --> S6[S6 Due Diligence]
    S6 --> S7[S7 Individual Exposures]
    S8[S8 External Ratings] -.->|rating inputs| S7
    S7 --> S9[S9 CRM]
    S9 -.->|RW adjustment| S7
```

---

## Quick Reference: Key Risk Weights

| Exposure | Best RW | Worst RW | Key driver |
|---|---|---|---|
| Sovereign (rated) | 0% (AAA–AA−) | 150% (below B−) | External rating |
| Bank ECRA | 20% (AAA–AA−) | 150% (below B−) | Sovereign + bank rating |
| Bank SCRA Grade A | 40% | — | Due diligence |
| Bank SCRA Grade B | 75% | — | Due diligence |
| Bank SCRA Grade C | 150% | — | Due diligence |
| Corporate (rated) | 20% (AAA–AA−) | 150% (below B−) | External rating |
| Corporate (unrated) | 100% | — | General |
| Retail (qualifying) | 75% | — | Granularity test |
| Residential RE (LTV ≤50%) | 20% | — | LTV band |
| CRE (general) | 100% | — | LTV-based floor |

---

*Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/). Source: SAMA circular, v2.1, Dec 2022.*
