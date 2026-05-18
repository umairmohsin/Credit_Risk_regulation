# 7.55–7.60 Retail Exposures

Qualifying criteria for regulatory retail (75% RW), transactors, other retail, and the SAR 4.5 million granularity cap.

---

### 7.55 The retail exposure class excludes exposures within the real estate exposure class { #clause-7-55 }

> **7.55** The retail exposure class excludes exposures within the real estate exposure class. The retail exposure class includes the following types of exposures:
> 1. Exposures to an individual person or persons; and
> 2. Exposures to MSMEs (as defined in paragraph 7.40) that meet the “regulatory retail” criteria set out in paragraph 7.57 below. Exposures to MSMEs that do not meet these criteria will be treated as corporate MSMEs exposures under paragraph 7.40.

---

### 7.56 Exposures within the retail exposure class will be treated according to paragraphs 7.57to 7.59 below { #clause-7-56 }

> **7.56** Exposures within the retail exposure class will be treated according to paragraphs 7.57to 7.59 below. For the purpose of determining risk weighted assets, the retail exposure class consists of the follow three sets of exposures: 1.“Regulatory retail” exposures that do not arise from exposures to “transactors” (as defined in paragraph 7.58). 2.“Regulatory retail” exposures to “transactors”.
> 3. “Other retail” exposures.

---

### 7.57 “Regulatory retail” exposures are defined as retail exposures that meet all of the criteria listed below { #clause-7-57 }

=== "Clause Text"
    > **7.57** “Regulatory retail” exposures are defined as retail exposures that meet all of the criteria listed below:
    > 1. Product criterion: The exposure takes the form of any of the following: revolving credits and lines of credit (including credit cards, charge cards and overdrafts), personal term loans and leases (e.g. instalment loans, auto loans and leases, student and educational loans, personal finance) and small business facilities and commitments. Mortgage loans, derivatives and other securities (such as bonds and equities), whether listed or not, are specifically excluded from this category.
    > 2. Low value of individual exposures: The maximum aggregated exposure to one counterparty cannot exceed an absolute threshold of SAR 4.46 million.
    > 3. Granularity criterion:<sup>[1819]</sup> No aggregated exposure to one counterparty can exceed 0.2% of the overall regulatory retail portfolio. Defaulted retail exposures are to be excluded from the overall regulatory retail portfolio when assessing the granularity criterion.

=== "How it works"
    **Retail Classification Flow (S7.57–7.60)**

    ```mermaid
    flowchart TD
        A[Retail Exposure] --> B{Passes orientation test?
    Individual or small business}
        B -- No --> Z[Corporate / other treatment]
        B -- Yes --> C{Product type eligible?
    Revolving, LOC, personal loan, lease, SME}
        C -- No --> Z
        C -- Yes --> D{Exposure ≤ SAR 4.5M?}
        D -- No --> Z
        D -- Yes --> E{Granularity: exposure
    < 0.2% of total retail pool?}
        E -- No --> Z
        E -- Yes --> F[**Regulatory Retail — 75% RW**]
    ```

    **Table 10 — Retail Risk Weights**

    | Sub-category | Risk Weight |
    |---|---|
    | Regulatory retail — transactors | **45%** |
    | Regulatory retail — other | **75%** |
    | Other retail (non-qualifying) | **100%** |


---

### 7.58 “Transactors” are obligors in relation to facilities such as credit cards and charge cards where the balance has been repaid in full at each scheduled repayment date for the previous 12 months { #clause-7-58 }

> **7.58** “Transactors” are obligors in relation to facilities such as credit cards and charge cards where the balance has been repaid in full at each scheduled repayment date for the previous 12 months. Obligors in relation to overdraft facilities would also be considered as transactors if there has been no drawdown over the previous 12 months.

---

### 7.59 “Other retail” exposures are defined as exposures to an individual person or persons that do not meet all of the regulatory retail criteria in paragraph 7.57 { #clause-7-59 }

> **7.59** “Other retail” exposures are defined as exposures to an individual person or persons that do not meet all of the regulatory retail criteria in paragraph 7.57.

---

### 7.60 The risk weights that apply to exposures in the retail asset class are as follows { #clause-7-60 }

> **7.60** The risk weights that apply to exposures in the retail asset class are as follows:
> 1. Regulatory retail exposures that do not arise from exposures to transactors (as defined in paragraph 7.58) will be risk weighted at 75%.
> 2. Regulatory retail exposures that arise from exposures to transactors (as defined in paragraph 7.58) will be risk weighted at 45%.
> 3. Other retail exposures will be risk weighted at 100%. Real estate exposure class

???+ note "Footnote [18]"
    Aggregated exposure means gross amount (i.e. not taking any credit risk mitigation into account) of all forms of retail exposures, excluding residential real estate exposures. In case of off-balance sheet claims, the gross amount would be calculated after applying credit conversion factors. In addition, “to one counterparty” means one or several entities that may be considered as a single beneficiary (e.g. in the case of a small business that is affiliated to another small business, the limit would apply to the bank’s aggregated exposure on both businesses).
???+ note "Footnote [19]"
    To apply the 0.2% threshold of the granularity criterion, banks must: first, identify the full set of exposures in the retail exposure class (as defined in paragraph 7.55); second, identify the subset of exposure that meet product criterion and do not exceed the threshold for the value of aggregated exposures to one counterparty (as defined in paragraph 7.57); and third, exclude any exposures that have a value greater than 0.2% of the subset before exclusions

---
