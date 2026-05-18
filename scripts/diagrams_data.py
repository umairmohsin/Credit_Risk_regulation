"""
Diagram content for each clause's "How it works" tab.

Structure:
  CLAUSE_DIAGRAMS: dict mapping clause_id -> list of diagram blocks.

Each diagram block is a dict:
  {
    "type": "matrix" | "mermaid" | "steps",
    "title": str,        # tab or section heading
    "content": str,      # rendered content (markdown table, mermaid code, numbered steps)
  }

For clauses with BOTH a lookup table and a flow, list both — they'll be
rendered as two sub-sections inside the "How it works" tab.

Decision matrices use HTML <table> for richer styling (striped rows, coloured
cells); Mermaid flows use ≤8 nodes per diagram and are split into sub-flows.
"""

# ─── S7.1–7.3  Sovereigns ─────────────────────────────────────────────────

CLAUSE_DIAGRAMS = {

"7.1": [
    {
        "type": "matrix",
        "title": "Table 1 — Sovereign Risk Weights",
        "content": """\
| External Rating | Risk Weight |
|---|---|
| AAA to AA− | **0%** |
| A+ to A− | **20%** |
| BBB+ to BBB− | **50%** |
| BB+ to B− | **100%** |
| Below B− | **150%** |
| Unrated | **100%** |
""",
    },
    {
        "type": "mermaid",
        "title": "Decision Flow",
        "content": """\
flowchart TD
    A[Exposure to Sovereign / Central Bank] --> B{External rating available?}
    B -- No --> G[**100% RW** — Unrated]
    B -- Yes --> C{Rating band?}
    C -- AAA to AA− --> D[**0% RW**]
    C -- A+ to A− --> E[**20% RW**]
    C -- BBB+ to BBB− --> F[**50% RW**]
    C -- BB+ to B− --> H[**100% RW**]
    C -- Below B− --> I[**150% RW**]
""",
    },
],

"7.2": [
    {
        "type": "steps",
        "title": "SAR Preferential Treatment",
        "content": """\
**Two conditions must BOTH be met to apply 0% risk weight:**

1. The exposure is denominated in **Saudi Riyals (SAR)**
2. The exposure is **funded** in SAR (bank has matching SAR liabilities)

If either condition fails → apply standard sovereign RW from Table 1 (S7.1).
""",
    },
],

"7.4": [
    {
        "type": "mermaid",
        "title": "PSE Treatment Decision",
        "content": """\
flowchart TD
    A[Domestic PSE Exposure] --> B{SAMA-designated treatment?}
    B -- Sovereign treatment --> C[Apply **Table 1** sovereign RW<br/>based on country rating]
    B -- Bank treatment --> D{External rating?}
    D -- Rated --> E[Apply **Table 4** bank ECRA RW]
    D -- Unrated --> F[Apply **SCRA** Grade A / B / C]
""",
    },
],

"7.5": [
    {
        "type": "steps",
        "title": "Foreign PSE Treatment",
        "content": """\
Foreign PSEs (including GCC countries) are treated as **bank exposures**:

- Apply **ECRA** if the PSE has an external rating → use Table 4 bank RWs
- Apply **SCRA** if unrated → Grade A (40%), Grade B (75%), Grade C (150%)

*Exception:* where a foreign supervisor allows sovereign treatment for its domestic PSEs,
SAMA may permit the same treatment for Saudi banks' exposures to those PSEs.
""",
    },
],

"7.9": [
    {
        "type": "matrix",
        "title": "MDB Eligibility — 0% Risk Weight",
        "content": """\
| MDB | 0% RW |
|---|---|
| World Bank Group (IBRD, IDA, IFC, MIGA) | ✓ |
| Asian Development Bank (ADB) | ✓ |
| African Development Bank | ✓ |
| European Bank for Reconstruction & Development (EBRD) | ✓ |
| Inter-American Development Bank | ✓ |
| European Investment Bank (EIB) | ✓ |
| European Investment Fund (EIF) | ✓ |
| Nordic Investment Bank | ✓ |
| Caribbean Development Bank | ✓ |
| Islamic Development Bank (IsDB) | ✓ |
| Council of Europe Development Bank | ✓ |
| International Finance Facility for Immunization | ✓ |
| Asian Infrastructure Investment Bank (AIIB) | ✓ |
""",
    },
],

"7.11": [
    {
        "type": "matrix",
        "title": "Other MDB Risk Weights (ECRA)",
        "content": """\
| External Rating | Risk Weight |
|---|---|
| AAA to AA− | **20%** |
| A+ to A− | **50%** |
| BBB+ to BBB− | **50%** |
| BB+ to B− | **100%** |
| Below B− | **150%** |
| Unrated | **50%** |
""",
    },
],

"7.13": [
    {
        "type": "mermaid",
        "title": "Rated Banks — ECRA vs SCRA",
        "content": """\
flowchart TD
    A[Bank Exposure] --> B{External rating?}
    B -- Rated --> C[**ECRA** — use Table 4 below]
    B -- Unrated --> D[**SCRA** — Grade A / B / C]
    C --> E{Rating band — see Table 4}
    D --> F{SCRA Grade?}
    F -- Grade A --> G[**40% RW** general<br/>20% short-term ≤3m]
    F -- Grade B --> H[**75% RW** general<br/>50% short-term ≤3m]
    F -- Grade C --> I[**150% RW**]
""",
    },
    {
        "type": "matrix",
        "title": "Table 4 — Bank ECRA Risk Weights",
        "content": """\
| External Rating | General RW | Short-term (≤3m original maturity) |
|---|---|---|
| AAA to AA− | **20%** | 20% |
| A+ to A− | **30%** | 20% |
| BBB+ to BBB− | **50%** | 20% |
| BB+ to B− | **100%** | 50% |
| Below B− | **150%** | 150% |
| Unrated | Use SCRA | Use SCRA |

> **Sovereign floor:** Bank RW cannot be lower than the RW of the home sovereign.
""",
    },
],

"7.17": [
    {
        "type": "matrix",
        "title": "Table 5 — SCRA Risk Weights",
        "content": """\
| SCRA Grade | Criteria summary | General RW | Short-term (≤3m) |
|---|---|---|---|
| **Grade A** | Meets all minimum regulatory requirements; no specific concern | **40%** | **20%** |
| **Grade B** | Does not qualify for A; not at material risk of default | **75%** | **50%** |
| **Grade C** | Elevated credit risk; distress signals present | **150%** | **150%** |

> **Sovereign floor applies.** Grade A / B bank RW cannot go below the home-sovereign RW.
""",
    },
],

"7.25": [
    {
        "type": "steps",
        "title": "Grade C Triggers (S7.25)",
        "content": """\
A bank is **automatically classified as Grade C** if ANY of the following are met:

1. Net non-performing assets ÷ capital > **10%**
2. Regulatory capital ratio below the **minimum required** by the supervisor
3. **Negative net income** in the past 2 years
4. Bank subject to **enforcement action** by its supervisor related to capital or liquidity
5. Bank publicly announced a plan to obtain **emergency capital** or liquidity support
""",
    },
],

"7.29": [
    {
        "type": "mermaid",
        "title": "Covered Bond Eligibility Flow",
        "content": """\
flowchart TD
    A[Covered Bond] --> B{Issued by a bank subject\nto regulatory supervision?}
    B -- No --> Z[Not eligible for preferential RW]
    B -- Yes --> C{Pool assets meet\nS7.30 requirements?}
    C -- No --> Z
    C -- Yes --> D{Pool nominal value\n≥ bond nominal value?}
    D -- No --> Z
    D -- Yes --> E{Meets S7.32 conditions?}
    E -- No --> Z
    E -- Yes --> F[Apply Table 3 covered bond RW]
""",
    },
    {
        "type": "matrix",
        "title": "Table 3 — Covered Bond Risk Weights",
        "content": """\
| Issuing Bank Rating | Covered Bond RW |
|---|---|
| AAA to AA− | **10%** |
| A+ to A− | **20%** |
| BBB+ to BBB− | **20%** |
| BB+ to B− | **50%** |
| Below B− | Use general bank RW |
| Unrated | Use general bank RW |
""",
    },
],

"7.38": [
    {
        "type": "matrix",
        "title": "Table 6 — Corporate Base Risk Weights (ECRA)",
        "content": """\
| External Rating | Risk Weight |
|---|---|
| AAA to AA− | **20%** |
| A+ to A− | **50%** |
| BBB+ to BBB− | **75%** |
| BB+ to BB− | **100%** |
| Below BB− | **150%** |
| Unrated | **100%** |

> **SME corporates:** 85% RW if qualifying under S7.40 criteria.
""",
    },
    {
        "type": "mermaid",
        "title": "Corporate RW Decision",
        "content": """\
flowchart TD
    A[Corporate Exposure] --> B{Specialised lending?}
    B -- Yes --> C[S7.41–7.45 Specialised Lending RW]
    B -- No --> D{MSME?}
    D -- Yes --> E[**85% RW** — SME corporate]
    D -- No --> F{Rated?}
    F -- Yes --> G[Table 6 ECRA RW]
    F -- No --> H[**100% RW** — Unrated]
""",
    },
],

"7.42": [
    {
        "type": "matrix",
        "title": "Table 7 — Specialised Lending Risk Weights",
        "content": """\
| Sub-category | Strong | Good | Satisfactory | Weak | Default |
|---|---|---|---|---|---|
| Project finance (pre-op) | **130%** | **130%** | **130%** | **130%** | **130%** |
| Project finance (operational) | **80%** | **100%** | **130%** | **150%** | **150%** |
| Object finance | **100%** | **100%** | **130%** | **150%** | **150%** |
| Commodities finance | **100%** | **100%** | **130%** | **150%** | **150%** |
| IPRE (income-producing) | **70%** | **90%** | **110%** | **130%** | **150%** |

> High-quality project finance (S7.45): **80%** in operational phase.
""",
    },
],

"7.57": [
    {
        "type": "mermaid",
        "title": "Retail Classification Flow (S7.57–7.60)",
        "content": """\
flowchart TD
    A[Retail Exposure] --> B{Passes orientation test?\nIndividual or small business}
    B -- No --> Z[Corporate / other treatment]
    B -- Yes --> C{Product type eligible?\nRevolving, LOC, personal loan, lease, SME}
    C -- No --> Z
    C -- Yes --> D{Exposure ≤ SAR 4.5M?}
    D -- No --> Z
    D -- Yes --> E{Granularity: exposure\n< 0.2% of total retail pool?}
    E -- No --> Z
    E -- Yes --> F[**Regulatory Retail — 75% RW**]
""",
    },
    {
        "type": "matrix",
        "title": "Table 10 — Retail Risk Weights",
        "content": """\
| Sub-category | Risk Weight |
|---|---|
| Regulatory retail — transactors | **45%** |
| Regulatory retail — other | **75%** |
| Other retail (non-qualifying) | **100%** |
""",
    },
],

"7.69": [
    {
        "type": "matrix",
        "title": "Table 11 — Residential Real Estate RW (Whole Loan)",
        "content": """\
| LTV | General residential | Qualifying criteria not met |
|---|---|---|
| ≤ 50% | **20%** | 70% |
| 50% < LTV ≤ 60% | **25%** | 70% |
| 60% < LTV ≤ 80% | **30%** | 70% |
| 80% < LTV ≤ 90% | **40%** | 70% |
| 90% < LTV ≤ 100% | **50%** | 70% |
| > 100% | **70%** | 70% |

> Applies to residential real estate that meets S7.63 qualifying criteria.
""",
    },
    {
        "type": "mermaid",
        "title": "Residential RE Classification",
        "content": """\
flowchart TD
    A[Residential RE Exposure] --> B{Meets S7.63\nqualifying criteria?}
    B -- No --> C[**70% flat RW**]
    B -- Yes --> D{Repayment materially\ndependent on property cash flows?}
    D -- Yes --> E[**IPRE treatment** — S7.41–7.43]
    D -- No --> F{LTV band?}
    F --> G[Apply Table 11 LTV-based RW]
""",
    },
],

"7.77": [
    {
        "type": "matrix",
        "title": "Table 12 — Commercial Real Estate RW (Whole Loan)",
        "content": """\
| LTV | General CRE | Qualifying criteria not met |
|---|---|---|
| ≤ 60% | **60%** | 110% |
| > 60% | **80%** | 110% |

> Flat **110%** applies when S7.63 qualifying criteria are not met.
""",
    },
],

"7.82": [
    {
        "type": "matrix",
        "title": "ADC Exposure Risk Weights",
        "content": """\
| ADC Type | Risk Weight |
|---|---|
| Residential ADC — meets S7.83 pre-sale criteria | **100%** |
| Residential ADC — does not meet pre-sale criteria | **150%** |
| Commercial ADC | **150%** |
| Land (no development plan) | **150%** |
""",
    },
],

"7.86": [
    {
        "type": "matrix",
        "title": "Table 13 — Off-Balance Sheet CCFs",
        "content": """\
| Item Type | CCF |
|---|---|
| Direct credit substitutes (guarantees, standby LCs backing financial obligations) | **100%** |
| Sale & repurchase agreements, asset sales with recourse | **100%** |
| Forward asset purchases, partly paid shares / securities | **100%** |
| Note issuance facilities (NIFs), revolving underwriting facilities (RUFs) | **50%** |
| Performance bonds, bid bonds, warranties, standby LCs (non-financial) | **50%** |
| Commitments with original maturity > 1 year | **40%** |
| Commitments — unconditionally cancellable at any time | **10%** |
| Trade finance (short-term self-liquidating L/Cs) — issuing bank | **20%** |
| Trade finance — confirming bank | **20%** |
| Short-term self-liquidating trade L/Cs collateralised by shipment | **20%** |

> **CCF of 0%** applies to commitments that are unconditionally cancellable by the bank
> at any time without prior notice, subject to supervisory review.
""",
    },
    {
        "type": "mermaid",
        "title": "OBS CCF Selection",
        "content": """\
flowchart TD
    A[Off-balance sheet item] --> B{Direct credit\nsubstitute?}
    B -- Yes --> C[**100% CCF**]
    B -- No --> D{Trade finance\nshort-term self-liquidating?}
    D -- Yes --> E[**20% CCF**]
    D -- No --> F{Commitment?}
    F -- Unconditionally\ncancellable --> G[**10% CCF**]
    F -- Original maturity\n> 1 year --> H[**40% CCF**]
    F -- NIF / RUF --> I[**50% CCF**]
""",
    },
],

"7.96": [
    {
        "type": "matrix",
        "title": "Defaulted Exposure Risk Weights",
        "content": """\
| Exposure Type | Specific Provision | Risk Weight |
|---|---|---|
| Unsecured / general | < 20% of outstanding | **150%** |
| Unsecured / general | ≥ 20% of outstanding | **100%** |
| Residential real estate (LTV ≤ 100%) | Any | **100%** |
| Residential real estate (LTV > 100%) | Any | **150%** |
| SL, equity, higher-risk categories | — | Previous RW or **150%** |
""",
    },
],

"8.5": [
    {
        "type": "matrix",
        "title": "Long-Term Rating Mapping — Credit Quality Steps",
        "content": """\
| CQS | S&P | Moody's | Fitch | RW (Sovereign) | RW (Bank) | RW (Corporate) |
|---|---|---|---|---|---|---|
| 1 | AAA to AA− | Aaa to Aa3 | AAA to AA− | **0%** | **20%** | **20%** |
| 2 | A+ to A− | A1 to A3 | A+ to A− | **20%** | **30%** | **50%** |
| 3 | BBB+ to BBB− | Baa1 to Baa3 | BBB+ to BBB− | **50%** | **50%** | **75%** |
| 4 | BB+ to BB− | Ba1 to Ba3 | BB+ to BB− | **100%** | **100%** | **100%** |
| 5 | B+ to B− | B1 to B3 | B+ to B− | **100%** | **100%** | **150%** |
| 6 | CCC+ and below | Caa1 and below | CCC+ and below | **150%** | **150%** | **150%** |
""",
    },
],

"8.8": [
    {
        "type": "steps",
        "title": "Multiple External Ratings Rule",
        "content": """\
When an exposure has **two** ratings from different ECAIs:

- Apply the **higher risk weight** of the two.

When an exposure has **three or more** ratings:

1. Identify the two **lowest risk weights** (best ratings).
2. If they agree → use that risk weight.
3. If they disagree → use the **higher** of the two lowest risk weights.
""",
    },
],

"9.3": [
    {
        "type": "mermaid",
        "title": "CRM Technique Selection",
        "content": """\
flowchart TD
    A[CRM protection available] --> B{Type of protection?}
    B -- Financial collateral --> C{Method?}
    C -- Simple approach --> D[S9.32–9.39<br/>Substitute collateral RW]
    C -- Comprehensive approach --> E[S9.40–9.64<br/>Haircut-adjusted EAD]
    B -- On-balance-sheet netting --> F[S9.65–9.69<br/>Net loans vs deposits]
    B -- Guarantee / credit derivative --> G[S9.70–9.83<br/>Substitute guarantor RW]
    D & E & F & G --> H[Compute reduced RWA]
""",
    },
],

"9.10": [
    {
        "type": "steps",
        "title": "Maturity Mismatch Adjustment (Pa formula)",
        "content": """\
A **maturity mismatch** exists when the CRM protection expires before the underlying exposure.

**Adjusted protection value:**

> **Pa = P × (t − 0.25) / (T − 0.25)**

Where:
- **Pa** = adjusted protection value
- **P** = nominal protection value
- **t** = residual maturity of protection (in years), capped at T
- **T** = residual maturity of underlying exposure (in years)

**Minimum protection maturity:** If t < 0.25 years → **zero credit recognised** (Pa = 0).

*Applies to:* Comprehensive approach, guarantees, and credit derivatives — NOT the simple approach for financial collateral (S9.11).
""",
    },
],

"9.46": [
    {
        "type": "steps",
        "title": "Comprehensive Approach — E* Formula",
        "content": """\
**Adjusted exposure after risk mitigation:**

> **E\\* = max{0, E×(1+He) − C×(1−Hc−Hfx)}**

Where:
- **E\\*** = exposure value after risk mitigation (the amount that attracts a risk weight)
- **E** = current exposure value
- **He** = haircut appropriate to the exposure (for volatile securities lent)
- **C** = current value of collateral received
- **Hc** = haircut for collateral (volatility of collateral value)
- **Hfx** = haircut for FX mismatch between exposure and collateral (8% for 10-day holding period, standard)

If E\\* > 0, apply the counterparty's risk weight to E\\*.
If E\\* = 0 or negative, exposure is fully covered.
""",
    },
],

"9.52": [
    {
        "type": "steps",
        "title": "Haircut Scaling Formula",
        "content": """\
Standard supervisory haircuts assume a **10-business day** holding period.
When the actual minimum holding period (TM) differs, scale using:

> **H = H₁₀ × √((NR + TM − 1) / 10)**

Where:
- **H** = scaled haircut
- **H₁₀** = supervisory haircut for 10-day holding period
- **NR** = actual number of business days between revaluation/remargining
- **TM** = minimum holding period for the transaction type

**Standard minimum holding periods (TM):**

| Transaction type | TM |
|---|---|
| Repo-style transactions | 5 business days |
| Other capital-markets transactions | 10 business days |
| Secured lending | 20 business days |
""",
    },
],

"9.69": [
    {
        "type": "mermaid",
        "title": "On-Balance Sheet Netting — Conditions",
        "content": """\
flowchart TD
    A[Loan + Deposit same counterparty] --> B{Legally enforceable\nnetting agreement?}
    B -- No --> Z[No netting — gross treatment]
    B -- Yes --> C{Ability to determine\nexposures at any time?}
    C -- No --> Z
    C -- Yes --> D{Credit exposures and\ndeposits monitored on net basis?}
    D -- No --> Z
    D -- Yes --> E[**Netting recognised**<br/>Apply RW to net exposure]
""",
    },
],

"9.78": [
    {
        "type": "mermaid",
        "title": "Guarantee / Credit Derivative — Substitution",
        "content": """\
flowchart TD
    A[Guarantee or Credit Derivative] --> B{Eligible guarantor?\nSovereign, bank, corp rated A− or better}
    B -- No --> Z[No CRM relief]
    B -- Yes --> C{Protection covers\nfull exposure amount?}
    C -- Yes --> D[**Full substitution**<br/>Apply guarantor's RW to full exposure]
    C -- No --> E{Proportional or\ntranche protection?}
    E -- Proportional --> F[**Pro-rata substitution**<br/>Protected portion: guarantor RW<br/>Unprotected: original RW]
    E -- Tranche --> G[**Tranche treatment**<br/>Per S9.79–9.80 rules]
""",
    },
],

}  # end CLAUSE_DIAGRAMS


def get_diagram(clause_id: str) -> list[dict]:
    """Return diagram blocks for a clause, or empty list if none defined."""
    return CLAUSE_DIAGRAMS.get(clause_id, [])
