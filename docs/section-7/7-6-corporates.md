# 7.37–7.46 Corporates & Specialised Lending

Base risk weights for rated and unrated corporate exposures, SME treatment, and the five sub-categories of specialised lending.

---

### 7.37 Exposures to corporates include exposures (loans, bonds, receivables, etc.) to incorporated entities, associations, partnerships, proprietorships, trusts, funds and other entities with similar characteristics, except those, which qualify for one of the other exposure classes { #clause-7-37 }

> **7.37** Exposures to corporates include exposures (loans, bonds, receivables, etc.) to incorporated entities, associations, partnerships, proprietorships, trusts, funds and other entities with similar characteristics, except those, which qualify for one of the other exposure classes. The treatment associated with subordinated debt and equities of these counterparties is addressed in paragraphs 7.46 to 7.54. The corporate exposure class includes exposures to insurance companies and other financial corporates that do not meet the definitions of exposures to banks, or securities firms and other financial institutions, as determined in paragraphs

---

### 7.38 For corporate exposures, banks will assign “base” risk weights according to Table 8 { #clause-7-38 }

=== "Clause Text"
    > **7.38** For corporate exposures, banks will assign “base” risk weights according to Table 8. Banks must perform due diligence to ensure that the external ratings appropriately and conservatively reflect the creditworthiness of the counterparties. Banks which have assigned risk weights to their rated bank exposures based on paragraph 7.14 must assign risk weights for all their corporate exposures according to Table 8. If the due diligence analysis reflects higher risk characteristics than that implied by the external rating bucket of the exposure (i.e. AAA to AA–; A+ to A– etc.), the bank must assign a risk weight at least one bucket higher than the “base” risk weight determined by the external rating. Due diligence analysis must never result in the application of a lower risk weight than that determined by the external rating.
    >
    > | AAA to AA– | A+ to A– | BBB+ to BBB– | BB+ to BB– | Below BB– |
    > | --- | --- | --- | --- | --- |
    > | 20% | 50% | 75% | 100% | 150% |

=== "How it works"
    **Table 6 — Corporate Base Risk Weights (ECRA)**

    | External Rating | Risk Weight |
    |---|---|
    | AAA to AA− | **20%** |
    | A+ to A− | **50%** |
    | BBB+ to BBB− | **75%** |
    | BB+ to BB− | **100%** |
    | Below BB− | **150%** |
    | Unrated | **100%** |
    
    > **SME corporates:** 85% RW if qualifying under S7.40 criteria.

    **Corporate RW Decision**

    ```mermaid
    flowchart TD
        A[Corporate Exposure] --> B{Specialised lending?}
        B -- Yes --> C[S7.41–7.45 Specialised Lending RW]
        B -- No --> D{MSME?}
        D -- Yes --> E[**85% RW** — SME corporate]
        D -- No --> F{Rated?}
        F -- Yes --> G[Table 6 ECRA RW]
        F -- No --> H[**100% RW** — Unrated]
    ```


---

### 7.39 Where banks have overseas operations, unrated corporate exposures of banks incorporated in jurisdictions that allow the use of external ratings for regulatory purposes will receive a 100% risk weight, with the exception of unrated exposures to corporate micro, small or medium-sized entities (MSMEs), as described in paragraph 7.40 { #clause-7-39 }

> **7.39** Where banks have overseas operations, unrated corporate exposures of banks incorporated in jurisdictions that allow the use of external ratings for regulatory purposes will receive a 100% risk weight, with the exception of unrated exposures to corporate micro, small or medium-sized entities (MSMEs), as described in paragraph 7.40. Risk weight table for corporate exposures Table 8 AAA A+ to BBB+ BB+ Below Unrated External rating to A– to to BB– of AA– BBB– BB– counterparty “Base” risk weight 20% 50% 75% 100% 150% 100%

---

### 7.40 The definitions of MSMEs shall continue to apply as per SAMA Circular No { #clause-7-40 }

> **7.40** The definitions of MSMEs shall continue to apply as per SAMA Circular No. 381000064902, Date: 15 March 2017 or any subsequent circulars, corporate MSMEs for the purpose of capital requirements are defined as corporate exposures where the reported annual revenues for the consolidated group of which the corporate MSME counterparty is a part is less than or equal to SAR 200 million for the most recent financial year. For unrated exposures to corporate MSMEs, an 85% risk weight will be applied. Exposures to MSMEs that meet the criteria in paragraphs 7.57 will be treated as regulatory retail MSME exposures and risk weighted at 75%. Specialized lending

---

### 7.41 A corporate exposure will be treated as a specialized lending exposure if such lending possesses some or all of the following characteristics, either in legal form or economic substance { #clause-7-41 }

> **7.41** A corporate exposure will be treated as a specialized lending exposure if such lending possesses some or all of the following characteristics, either in legal form or economic substance:
> 1. The exposure is not related to real estate and is within the definitions of object finance, project finance or commodities finance under paragraph 7.42. If the activity is related to real estate, the treatment would be determined in accordance with paragraphs 7.61 to 7.83;
> 2. The exposure is typically to an entity (often a special purpose vehicle (SPV)) that was created specifically to finance and/or operate physical assets;
> 3. The borrowing entity has few or no other material assets or activities, and therefore little or no independent capacity to repay the obligation, apart from the income that it receives from the asset(s) being financed. The primary source of repayment of the obligation is the income generated by the asset(s), rather than the independent capacity of the borrowing entity; and
> 4. The terms of the obligation give the lender a substantial degree of control over the asset(s) and the income that it generates.

---

### 7.42 Exposures described in paragraph 7.41 will be classified in one of the following three subcategories of specialized lending { #clause-7-42 }

=== "Clause Text"
    > **7.42** Exposures described in paragraph 7.41 will be classified in one of the following three subcategories of specialized lending:
    > 1. Project finance Refers to the method of funding in which the lender looks primarily to the revenues generated by a single project, both as the source of repayment and as security for the loan. This type of financing is usually for large, complex and expensive installations such as power plants, chemical processing plants, mines, transportation infrastructure, environment, media, and telecoms. Project finance may take the form of financing the construction of a new capital installation, or refinancing of an existing installation, with or without improvements. 2. Object finance Refers to the method of funding the acquisition of equipment (e.g. ships, aircraft, satellites, railcars, and fleets) where the repayment of the loan is dependent on the cash flows generated by the specific assets that have been financed and pledged or assigned to the lender.
    > 3. Commodities finance Refers to short-term lending to finance reserves, inventories, or receivables of exchange-traded commodities (e.g. crude oil, metals, or crops), where the loan will be repaid from the proceeds of the sale of the commodity and the borrower has no independent capacity to repay the loan.

=== "How it works"
    **Table 7 — Specialised Lending Risk Weights**

    | Sub-category | Strong | Good | Satisfactory | Weak | Default |
    |---|---|---|---|---|---|
    | Project finance (pre-op) | **130%** | **130%** | **130%** | **130%** | **130%** |
    | Project finance (operational) | **80%** | **100%** | **130%** | **150%** | **150%** |
    | Object finance | **100%** | **100%** | **130%** | **150%** | **150%** |
    | Commodities finance | **100%** | **100%** | **130%** | **150%** | **150%** |
    | IPRE (income-producing) | **70%** | **90%** | **110%** | **130%** | **150%** |
    
    > High-quality project finance (S7.45): **80%** in operational phase.


---

### 7.43 Banks will assign to their specialized lending exposures the risk weights determined by the issue-specific external ratings, if these are available, according to Table 8 { #clause-7-43 }

> **7.43** Banks will assign to their specialized lending exposures the risk weights determined by the issue-specific external ratings, if these are available, according to Table 8. Issuer ratings must not be used (i.e. paragraph 8.13 does not apply in the case of specialized lending exposures).

---

### 7.44 For specialized lending exposures for which an issue-specific external rating is not available, and for all specialized lending exposures of banks incorporated in jurisdictions that do not allow the use of external ratings for regulatory purposes, the following risk weights will apply { #clause-7-44 }

> **7.44** For specialized lending exposures for which an issue-specific external rating is not available, and for all specialized lending exposures of banks incorporated in jurisdictions that do not allow the use of external ratings for regulatory purposes, the following risk weights will apply:
> 1. Object and commodities finance exposures will be risk-weighted at 100%;
> 2. Project finance exposures will be risk-weighted at 130% during the pre- operational phase and 100% during the operational phase. Project finance exposures in the operational phase, which are deemed to be high quality, as described in paragraph 7.45, will be risk weighted at 80%. For this purpose, operational phase is defined as the phase in which the entity that was specifically created to finance the project has a positive net cash flow that is sufficient to cover any remaining (a) contractual obligation, and Declining long-term debt. (b)

---

### 7.45 A high quality project finance exposure refers to an exposure to a project finance entity that is able to meet its financial commitments in a timely manner and its ability to do so is assessed to be robust against adverse changes in the economic cycle and business conditions { #clause-7-45 }

> **7.45** A high quality project finance exposure refers to an exposure to a project finance entity that is able to meet its financial commitments in a timely manner and its ability to do so is assessed to be robust against adverse changes in the economic cycle and business conditions. The following conditions must also be met:
> 1. The project finance entity is restricted from acting to the detriment of the creditors (e.g. by not being able to issue additional debt without the consent of existing creditors); 2.The project finance entity has sufficient reserve funds or other financial arrangements to cover the contingency funding and working capital requirements of the project;<sup>[11]</sup>
> 3. The revenues are availability-based or subject to a rate-of-return regulation or take-or-pay contract;
> 4. The project finance entity’s revenue depends on one main counterparty and this main counterparty shall be a central government, PSE or a corporate entity with a risk weight of 80% or lower;
> 5. The contractual provisions governing the exposure to the project finance entity provide for a high degree of protection for creditors in case of a default of the project finance entity;
> 6. The main counterparty or other counterparties which similarly comply with the eligibility criteria for the main counterparty will protect the creditors from the losses resulting from a termination of the project;
> 7. All assets and contracts necessary to operate the project have been pledged to the creditors to the extent permitted by applicable law; and
> 8. Creditors may assume control of the project finance entity in case of its default. Subordinated debt, equity and other capital instruments

???+ note "Footnote [11]"
    Availability-based revenues mean that once construction is completed, the project finance entity is entitled to payments from its contractual counterparties (e.g. the government), as long as contract conditions are fulfilled. Availability payments are sized to cover operating and maintenance costs, debt service costs and equity returns as the project finance entity operates the project. Availability payments are not subject to swings in demand, such as traffic levels, and are adjusted typically only for lack of performance or lack of availability of the asset to the public

---

### 7.46 The treatment described in paragraphs 7.50 to 7.52. applies to subordinated debt, equity and other regulatory capital instruments issued by either corporates or banks, provided that such instruments are not deducted from regulatory capital or risk-weighted at 250% according to the Regulatory Capital Under Basel III Framework (Article 4.4 – Section A of SAMA Circular No { #clause-7-46 }

> **7.46** The treatment described in paragraphs 7.50 to 7.52. applies to subordinated debt, equity and other regulatory capital instruments issued by either corporates or banks, provided that such instruments are not deducted from regulatory capital or risk-weighted at 250% according to the Regulatory Capital Under Basel III Framework (Article 4.4 – Section A of SAMA Circular No. 341000015689, Date: 19 December 2012), or risk weighted at 1250% according to paragraph 7.54. It also excludes equity investments in funds treated under chapter 24.

---
