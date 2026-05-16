# External Ratings — S8

Section 8 governs which external credit assessment institutions (ECAIs) are eligible, how their ratings map to risk weights, and how banks must handle multiple ratings on a single exposure.

---

## 8.1 Eligible ECAIs { #clause-8-1 }

=== "Clause Text"
    > **8.1** Banks may use credit ratings from the following External Credit Assessment Institutions (ECAIs) that are eligible in Saudi Arabia:
    >
    > - Standard & Poor's (S&P)
    > - Moody's Investors Service
    > - Fitch Ratings

=== "Key Facts"
    | ECAI | Short-term scale | Long-term scale |
    |---|---|---|
    | S&P | A-1+, A-1, A-2, A-3, B, C, D | AAA → D |
    | Moody's | P-1, P-2, P-3, NP | Aaa → C |
    | Fitch | F1+, F1, F2, F3, B, C, D | AAA → D |

---

## 8.2 Eight Criteria for ECAI Eligibility { #clause-8-2 }

=== "Clause Text"
    > **8.2** For a credit assessment institution to be recognised as eligible, it must satisfy the following criteria:
    >
    > 1. **Objectivity** — The methodology must be rigorous, systematic, and subject to validation.
    > 2. **Independence** — The ECAI must be free from political or economic pressure.
    > 3. **International access / Transparency** — Ratings must be publicly available.
    > 4. **Disclosure** — Methodologies and assumptions must be disclosed.
    > 5. **Resources** — The ECAI must have sufficient resources.
    > 6. **Credibility** — The rating must be accepted by market participants.
    > 7. **Coverage** — Sufficient market coverage.
    > 8. **Governance** — Robust internal governance.

---

## 8.3–8.4 Rating Mapping Table { #clause-8-3 }

=== "Clause Text"
    > **8.3** Banks must use the following mapping table to translate ECAI ratings to the credit quality steps used in the risk weight tables.
    >
    > **8.4** The mapping applies to long-term ratings. For short-term ratings, see Table 13 ([S7.18](individual-exposures.md#clause-7-18)).

=== "Mapping Table"
    | Credit Quality Step | S&P | Moody's | Fitch | Typical RW context |
    |---|---|---|---|---|
    | 1 | AAA to AA− | Aaa to Aa3 | AAA to AA− | 0–20% |
    | 2 | A+ to A− | A1 to A3 | A+ to A− | 20–50% |
    | 3 | BBB+ to BBB− | Baa1 to Baa3 | BBB+ to BBB− | 50–100% |
    | 4 | BB+ to BB− | Ba1 to Ba3 | BB+ to BB− | 100% |
    | 5 | B+ to B− | B1 to B3 | B+ to B− | 100–150% |
    | 6 | CCC+ and below | Caa1 and below | CCC+ and below | 150% |

---

## 8.5 Issue vs Issuer Ratings { #clause-8-5 }

=== "Clause Text"
    > **8.5** Where a bank's exposure is to a specific issue that has a rating, this rating should be used. Where the exposure is not to a specific rated issue:
    >
    > - If the borrower has a specific rated issue and the bank's exposure is **senior** to that issue in all respects, the bank may apply the rating for that issue (but one notch higher than the issue rating, i.e. one quality step better).
    > - If the borrower only has an issuer rating, use the issuer rating.
    > - A **short-term** rating should only be used for short-term claims.

=== "Decision Flow"
    ```mermaid
    flowchart TD
        A[Exposure to rated entity] --> B{Is there a specific issue rating for THIS exposure?}
        B -- Yes --> C[Use the issue rating directly]
        B -- No --> D{Does borrower have another rated issue?}
        D -- Yes --> E{Is bank's exposure senior in all respects?}
        E -- Yes --> F[Use rated issue rating — apply one quality step better]
        E -- No --> G[Cannot use that issue rating]
        D -- No --> H{Does borrower have an issuer rating?}
        H -- Yes --> I[Use issuer rating]
        H -- No --> J[Treat as unrated]
        G --> H
    ```

---

## 8.6 Multiple Ratings Rule { #clause-8-6 }

=== "Clause Text"
    > **8.6** When there is only one rating for a specific claim, that rating is used to determine the risk weight.
    >
    > When there are two ratings and they correspond to different risk weights, the **higher** risk weight (more conservative) applies.
    >
    > When there are three or more ratings, use the two ratings that give the **two lowest risk weights** and then apply the **higher** of those two (i.e. the second-lowest risk weight).

=== "Decision Flow"
    ```mermaid
    flowchart TD
        A[How many ECAI ratings exist?] --> B{Count}
        B -- 1 rating --> C[Use that rating → apply risk weight]
        B -- 2 ratings --> D[Both map to different RWs?]
        D -- Different RWs --> E[Apply the HIGHER risk weight]
        D -- Same RW --> F[Apply that risk weight]
        B -- 3+ ratings --> G[Find the two lowest RWs]
        G --> H[Of those two, apply the HIGHER one]
    ```

=== "Example"
    | ECAI | Rating | Risk Weight |
    |---|---|---|
    | S&P | A+ | 20% |
    | Moody's | Baa1 | 50% |
    | Fitch | A− | 20% |
    
    Three ratings → two lowest RWs are 20% and 20% → apply 20%.

---

## 8.7 No Unsolicited Ratings { #clause-8-7 }

=== "Clause Text"
    > **8.7** Banks may only use **solicited** ratings from eligible ECAIs. Unsolicited ratings must not be used to determine risk weights.

---

## 8.8 Short-Term Ratings { #clause-8-8 }

=== "Clause Text"
    > **8.8** Short-term ratings may only be applied to short-term exposures. They must not be generalised to derive risk weights for long-term exposures.
    >
    > See Table 13 in [S7.18](individual-exposures.md#clause-7-18) for the short-term rating to risk weight mapping.

=== "Short-Term Rating Mapping (Table 13)"
    | S&P | Moody's | Fitch | Risk Weight |
    |---|---|---|---|
    | A-1+ / A-1 | P-1 | F1+ / F1 | 20% |
    | A-2 | P-2 | F2 | 50% |
    | A-3 | P-3 | F3 | 100% |
    | Other / unrated | NP | Other | 150% |

---

## Cross-References

- [S7.1 Sovereigns](individual-exposures.md#clause-7-1) — uses CQS from S8
- [S7.10 Banks ECRA](individual-exposures.md#clause-7-10) — uses CQS from S8
- [S7.23 Corporates](individual-exposures.md#clause-7-23) — uses CQS from S8
- [S7.18 Short-term bank ratings](individual-exposures.md#clause-7-18) — Table 13
