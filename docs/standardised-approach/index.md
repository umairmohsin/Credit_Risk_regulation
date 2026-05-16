# Standardised Approach

The Standardised Approach (SA) assigns risk weights to credit exposures based on counterparty type and — where available — external credit ratings.

---

## Master Exposure-Type Selector

Use this flowchart to identify which section of S7 governs your exposure:

```mermaid
flowchart TD
    A[Identify the counterparty / exposure] --> B{Counterparty type?}

    B --> C[Sovereign or Central Bank]
    B --> D[Non-central-government PSE]
    B --> E[Multilateral Development Bank]
    B --> F[Bank or NBFIs]
    B --> G[Securities Firm]
    B --> H[Corporate]
    B --> I[Retail]
    B --> J[Real Estate]
    B --> K[Other]

    C --> C1[S7.1–7.3 → Table 1]
    D --> D1[S7.4–7.6 → Table 2 or sovereign treatment]
    E --> E1[S7.7–7.9 → 0% or Table 3]
    F --> F1{ECRA or SCRA?}
    F1 -- External rating available --> F2[S7.10–7.14 ECRA → Table 4]
    F1 -- No external rating --> F3[S7.15–7.19 SCRA → Grade A/B/C]
    G --> G1[S7.20–7.22 → bank treatment or Table 4]
    H --> H1{Rated or unrated?}
    H1 -- Rated --> H2[S7.23–7.25 → Table 6]
    H1 -- Unrated --> H3[S7.26 → 100% RW]
    I --> I1{Qualifying retail?}
    I1 -- Yes --> I2[S7.29–7.31, 75% RW]
    I1 -- No --> I3[S7.32 → 100% RW]
    J --> J1{Type of real estate?}
    J1 -- Residential --> J2[S7.33–7.43 → Table 9/10]
    J1 -- Commercial --> J3[S7.44–7.54 → Table 11/12]
    J1 -- ADC --> J4[S7.55–7.59 → 150% RW]
    K --> K1[S7.60–7.102 → see section]
```

---

## Sections in This Chapter

| Section | Content |
|---|---|
| [Individual Exposures S7](individual-exposures.md) | All 13 exposure sub-categories, 12 risk weight tables |
| [External Ratings S8](external-ratings.md) | ECAI eligibility, rating mapping, multiple ratings rules |
| [Credit Risk Mitigation S9](crm.md) | Collateral, guarantees, netting — simple and comprehensive |
