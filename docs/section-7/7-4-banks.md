# 7.12–7.35 Banks & Covered Bonds

Bank exposures use the External Credit Risk Assessment (ECRA) approach for rated banks and the Standardised Credit Risk Assessment (SCRA) for unrated banks. Covered bonds are also treated under this section.

---

### 7.12 and 7.36 respectively { #clause-7-12 }

> **7.12** and 7.36 respectively. The corporate exposure class does not include exposures to individuals. The corporate exposure class differentiates between the following subcategories:
> 1. General corporate exposures;
> 2. Specialized lending exposures, as defined in paragraph 7.41 General corporate exposures

---

### 7.13 Bank exposures will be risk-weighted based on the following hierarchy { #clause-7-13 }

=== "Clause Text"
    > **7.13** Bank exposures will be risk-weighted based on the following hierarchy: 1.External Credit Risk Assessment Approach (ECRA): This approach applies to all rated exposures to banks. Banks will apply chapter 8 to determine which rating can be used and for which exposures.
    > 2. Standardized Credit Risk Assessment Approach (SCRA): This approach is applicable to all exposures to banks that are unrated. External Credit Risk Assessment Approach (ECRA)<sup>[6]</sup>

=== "How it works"
    **Rated Banks — ECRA vs SCRA**

    ```mermaid
    flowchart TD
        A[Bank Exposure] --> B{External rating?}
        B -- Rated --> C[**ECRA** — use Table 4 below]
        B -- Unrated --> D[**SCRA** — Grade A / B / C]
        C --> E{Rating band — see Table 4}
        D --> F{SCRA Grade?}
        F -- Grade A --> G[**40% RW** general<br/>20% short-term ≤3m]
        F -- Grade B --> H[**75% RW** general<br/>50% short-term ≤3m]
        F -- Grade C --> I[**150% RW**]
    ```

    **Table 4 — Bank ECRA Risk Weights**

    | External Rating | General RW | Short-term (≤3m original maturity) |
    |---|---|---|
    | AAA to AA− | **20%** | 20% |
    | A+ to A− | **30%** | 20% |
    | BBB+ to BBB− | **50%** | 20% |
    | BB+ to B− | **100%** | 50% |
    | Below B− | **150%** | 150% |
    | Unrated | Use SCRA | Use SCRA |
    
    > **Sovereign floor:** Bank RW cannot be lower than the RW of the home sovereign.


???+ note "Footnote [5]"
    For internationally active banks, appropriate prudential standards (e.g. capital and liquidity requirements) and level of supervision should be in accordance with the Basel framework.
???+ note "Footnote [6]"
    An exposure is rated from the perspective of a bank if the exposure is rated by a recognized “eligible credit assessment institution” (ECAI) which has been nominated by the bank (i.e. the bank has informed SAMA of its intention to use the ratings of such ECAI for regulatory purposes in a consistent manner paragraph 8.8 In other words, if an external rating exists but the credit rating agency is not a recognized ECAI by SAMA, or the rating has been issued by an ECAI which has not been nominated by the bank, the exposure would be considered as being unrated from the perspective of the bank

---

### 7.14 Banks will assign to their rated bank exposures the corresponding “base” risk weights determined by the external ratings according to Table 4 { #clause-7-14 }

> **7.14** Banks will assign to their rated bank exposures the corresponding “base” risk weights determined by the external ratings according to Table 4. Such ratings must not incorporate assumptions of implicit government support<sup>[7]</sup>, unless the rating refers to a public bank owned by its government. Banks may continue to use external ratings, which incorporate assumptions of implicit government support for up to a period of five years, from the date of effective implementation of this framework, when assigning the “base” risk weights in Table 4 to their bank exposures. Risk weight table for bank exposures External Credit Risk Assessment Approach (ECRA) Table 4 AAA BBB+ External rating of A+ to BB+ to Below to to counterparty A– B– B– AA– BBB– “Base” risk weight 20% 30% 50% 100% 150% Risk weight for short-term 20% 20% 20% 50% 150% exposures
>
> | AAA to AA– | A+ to A– | BBB+ to BBB– | BB+ to B– |
> | --- | --- | --- | --- |
> | 20% | 30% | 50% | 100% |
> | 20% | 20% | 20% | 50% |

???+ note "Footnote [7]"
    Implicit government support refers to the notion that the government would act to prevent bank creditors from incurring losses in the event of a bank default or bank distress.

---

### 7.15 Exposures to banks with an original maturity of three months or less, as well as exposures to banks that arise from the movement of goods across national borders with an original maturity of six months or less can be assigned a risk weight that correspond to the risk weights for short term exposures in Table 4 { #clause-7-15 }

> **7.15** Exposures to banks with an original maturity of three months or less, as well as exposures to banks that arise from the movement of goods across national<sup>[8]</sup> borders with an original maturity of six months or less can be assigned a risk weight that correspond to the risk weights for short term exposures in Table 4.

???+ note "Footnote [8]"
    This may include on-balance sheet exposures such as loans and off- balance sheet exposures such as self- liquidating trade-related contingent items.

---

### 7.16 Banks must perform due diligence to ensure that the external ratings appropriately and conservatively reflect the creditworthiness of the bank counterparties { #clause-7-16 }

> **7.16** Banks must perform due diligence to ensure that the external ratings appropriately and conservatively reflect the creditworthiness of the bank counterparties. If the due diligence analysis reflects higher risk characteristics than that implied by the external rating bucket of the exposure (i.e. AAA to AA– ; A+ to A– etc.), the bank must assign a risk weight at least one bucket higher than the “base” risk weight determined by the external rating. Due diligence analysis must never result in the application of a lower risk weight than that determined by the external rating. Standardized Credit Risk Assessment Approach (SCRA)
>
> | Grade A | Grade B |
> | --- | --- |
> | 40% | 75% |
> | 20% | 50% |

---

### 7.17 Banks will apply the SCRA to all their unrated bank exposures { #clause-7-17 }

=== "Clause Text"
    > **7.17** Banks will apply the SCRA to all their unrated bank exposures. The SCRA requires banks to classify bank exposures into one of three risk-weight buckets (i.e. Grades A, B and C) and assign the corresponding risk weights in Table 5. Under the SCRA, exposures to banks without an external credit rating may receive a risk weight of 30%, provided that the counterparty bank has a Common Equity Tier 1 ratio which meets or exceeds 14% and a Tier 1 leverage ratio which meets or exceeds 5%. The counterparty bank must also satisfy all the requirements for Grade A classification. For the purposes of SCRA only, “published minimum regulatory requirements” in paragraphs 7.18 to 7.26 excludes liquidity standards. Risk weight table for bank exposures Standardized Credit Risk Assessment Approach (SCRA) Table 5 Credit risk assessment Grade A Grade B Grade C Of counterparty “Base” risk weight 40% 75% 150% Risk weight for short- 20% 50% 150% Term exposures SCRA: Grade A

=== "How it works"
    **Table 5 — SCRA Risk Weights**

    | SCRA Grade | Criteria summary | General RW | Short-term (≤3m) |
    |---|---|---|---|
    | **Grade A** | Meets all minimum regulatory requirements; no specific concern | **40%** | **20%** |
    | **Grade B** | Does not qualify for A; not at material risk of default | **75%** | **50%** |
    | **Grade C** | Elevated credit risk; distress signals present | **150%** | **150%** |
    
    > **Sovereign floor applies.** Grade A / B bank RW cannot go below the home-sovereign RW.


---

### 7.18 Grade A refers to exposures to banks, where the counterparty bank has adequate capacity to meet their financial commitments (including repayments of principal and interest) in a timely manner, for the projected life of the assets or exposures and irrespective of the economic cycles and business conditions { #clause-7-18 }

> **7.18** Grade A refers to exposures to banks, where the counterparty bank has adequate capacity to meet their financial commitments (including repayments of principal and interest) in a timely manner, for the projected life of the assets or exposures and irrespective of the economic cycles and business conditions.

---

### 7.19 A counterparty bank classified into Grade A must meet or exceed the published minimum regulatory requirements and buffers established by its national supervisor as implemented in the jurisdiction where it is incorporated, except for bank-specific minimum regulatory requirements or buffers that may be imposed through supervisory actions (e.g. via the Supervisory Review Process) and not made public { #clause-7-19 }

> **7.19** A counterparty bank classified into Grade A must meet or exceed the published minimum regulatory requirements and buffers established by its national supervisor as implemented in the jurisdiction where it is incorporated, except for bank-specific minimum regulatory requirements or buffers that may be imposed through supervisory actions (e.g. via the Supervisory Review Process) and not made public. If such minimum regulatory requirements and buffers (other than bank-specific minimum requirements or buffers) are not publicly disclosed or otherwise made available by the counterparty bank, then the counterparty bank must be assessed as Grade B or lower.

---

### 7.20 If as part of its due diligence, a bank assesses that a counterparty bank does not meet the definition of Grade A in paragraphs 7.18 and 7.19, exposures to the counterparty bank must be classified as Grade B or Grade C { #clause-7-20 }

> **7.20** If as part of its due diligence, a bank assesses that a counterparty bank does not meet the definition of Grade A in paragraphs 7.18 and 7.19, exposures to the counterparty bank must be classified as Grade B or Grade C. SCRA: Grade B

---

### 7.21 Grade B refers to exposures to banks, where the counterparty bank is subject to substantial credit risk, such as repayment capacities that are dependent on stable or favorable economic or business conditions { #clause-7-21 }

> **7.21** Grade B refers to exposures to banks, where the counterparty bank is subject to substantial credit risk, such as repayment capacities that are dependent on stable or favorable economic or business conditions.

---

### 7.22 A counterparty bank classified into Grade B must meet or exceed the published minimum regulatory requirements (excluding buffers) established by its national supervisor as implemented in the jurisdiction where it is incorporated, except for bank-specific minimum regulatory requirements that may be imposed through supervisory actions (e.g. via the Supervisory Review Process) and not made public { #clause-7-22 }

> **7.22** A counterparty bank classified into Grade B must meet or exceed the published minimum regulatory requirements (excluding buffers) established by its national supervisor as implemented in the jurisdiction where it is incorporated, except for bank-specific minimum regulatory requirements that may be imposed through supervisory actions (e.g. via the Supervisory Review Process) and not made public. If such minimum regulatory requirements are not publicly disclosed or otherwise made available by the counterparty bank then the counterparty bank must be assessed as Grade C.

---

### 7.23 Banks will classify all exposures that do not meet the requirements outlined in paragraphs 7.18 and 7.19 into Grade B, unless the exposure falls within Grade C under paragraphs 7.24 to 7.26 { #clause-7-23 }

> **7.23** Banks will classify all exposures that do not meet the requirements outlined in paragraphs 7.18 and 7.19 into Grade B, unless the exposure falls within Grade C under paragraphs 7.24 to 7.26. SCRA: Grade C

---

### 7.24 Grade C refers to higher credit risk exposures to banks, where the counterparty bank has material default risks and limited margins of safety { #clause-7-24 }

> **7.24** Grade C refers to higher credit risk exposures to banks, where the counterparty bank has material default risks and limited margins of safety. For these counterparties, adverse business, financial, or economic conditions are very likely to lead, or have led, to an inability to meet their financial commitments.

---

### 7.25 At a minimum, if any of the following triggers is breached, a bank must classify the exposure into Grade C { #clause-7-25 }

=== "Clause Text"
    > **7.25** At a minimum, if any of the following triggers is breached, a bank must classify the exposure into Grade C:
    > 1. The counterparty bank does not meet the criteria for being classified as Grade B with respect to its published minimum regulatory requirements, asset out in paragraphs 7.21 and 7.22 or
    > 2. Where audited financial statements are required, the external auditor has issued an adverse audit opinion or has expressed substantial doubt about the counterparty bank’s ability to continue as a going concern in its financial statements or audited reports within the previous 12 months.

=== "How it works"
    **Grade C Triggers (S7.25)**

    A bank is **automatically classified as Grade C** if ANY of the following are met:
    
    1. Net non-performing assets ÷ capital > **10%**
    2. Regulatory capital ratio below the **minimum required** by the supervisor
    3. **Negative net income** in the past 2 years
    4. Bank subject to **enforcement action** by its supervisor related to capital or liquidity
    5. Bank publicly announced a plan to obtain **emergency capital** or liquidity support


---

### 7.26 Even if the triggers set out in paragraph 7.25 are not breached, a bank may assess that the counterparty bank meets the definition in paragraph 7.24 { #clause-7-26 }

> **7.26** Even if the triggers set out in paragraph 7.25 are not breached, a bank may assess that the counterparty bank meets the definition in paragraph 7.24. In that case, the exposure to such counterparty bank must be classified into Grade C.

---

### 7.27 Exposures to banks with an original maturity of three months or less, as well as exposures to banks that arise from the movement of goods across national borders with an original maturity of six months or less, can be assigned a risk weight that correspond to the risk weights for short term exposures in Table 5 { #clause-7-27 }

> **7.27** Exposures to banks with an original maturity of three months or less, as well as exposures to banks that arise from the movement of goods across national borders with an original maturity of six months or less,<sup>[9]</sup> can be assigned a risk weight that correspond to the risk weights for short term exposures in Table 5.

???+ note "Footnote [9]"
    This may include on-balance sheet exposures such as loans and off-balance sheet exposures such as self- liquidating trade-related contingent items.

---

### 7.28 To reflect transfer and convertibility risk under the SCRA, a risk-weight floor based on the risk weight applicable to exposures to the sovereign of the country where the bank counterparty is incorporated will be applied to the risk weight assigned to bank exposures { #clause-7-28 }

> **7.28** To reflect transfer and convertibility risk under the SCRA, a risk-weight floor based on the risk weight applicable to exposures to the sovereign of the country where the bank counterparty is incorporated will be applied to the risk weight assigned to bank exposures. The sovereign floor applies when: i. The exposure is not in the local currency of the jurisdiction of incorporation of the debtor bank; and ii. For a borrowing booked in a branch of the debtor bank in a foreign jurisdiction, when the exposure is not in the local currency of the jurisdiction in which the branch operates. The sovereign floor will not apply to short-term (i.e. with a maturity below one year) self-liquidating, trade-related contingent items that arise from the movement of goods. Exposures to covered bonds

---

### 7.29 shall meet the requirements set out in paragraph 7.33 and shall include any of the following { #clause-7-29 }

=== "Clause Text"
    > **7.29** shall meet the requirements set out in paragraph 7.33 and shall include any of the following:
    > 1. claims on, or guaranteed by, sovereigns, their central banks, public sector entities or multilateral development banks;
    > 2. claims secured by residential real estate that meet the criteria set out in paragraph 7.63 and with a loan-to-value ratio of 80% or lower;
    > 3. claims secured by commercial real estate that meets the criteria set out in paragraph 7.63 and with a loan-to-value ratio of 60% or lower; or
    > 4. Claims on, or guaranteed by banks that qualify for a 30% or lower risk weight. However, such assets cannot exceed 15% of covered bond issuances.

=== "How it works"
    **Covered Bond Eligibility Flow**

    ```mermaid
    flowchart TD
        A[Covered Bond] --> B{Issued by a bank subject
    to regulatory supervision?}
        B -- No --> Z[Not eligible for preferential RW]
        B -- Yes --> C{Pool assets meet
    S7.30 requirements?}
        C -- No --> Z
        C -- Yes --> D{Pool nominal value
    ≥ bond nominal value?}
        D -- No --> Z
        D -- Yes --> E{Meets S7.32 conditions?}
        E -- No --> Z
        E -- Yes --> F[Apply Table 3 covered bond RW]
    ```

    **Table 3 — Covered Bond Risk Weights**

    | Issuing Bank Rating | Covered Bond RW |
    |---|---|
    | AAA to AA− | **10%** |
    | A+ to A− | **20%** |
    | BBB+ to BBB− | **20%** |
    | BB+ to B− | **50%** |
    | Below B− | Use general bank RW |
    | Unrated | Use general bank RW |


---

### 7.30 In order to be eligible for the risk weights set out in paragraph 7.34 the underlying assets (the cover pool) of covered bonds as defined in paragraph { #clause-7-30 }

> **7.30** In order to be eligible for the risk weights set out in paragraph 7.34 the underlying assets (the cover pool) of covered bonds as defined in paragraph

---

### 7.31 The nominal value of the pool of assets assigned to the covered bond instrument (s) by its issuer should exceed its nominal outstanding value by at least 10% { #clause-7-31 }

> **7.31** The nominal value of the pool of assets assigned to the covered bond instrument (s) by its issuer should exceed its nominal outstanding value by at least 10%. The value of the pool of assets for this purpose does not need to be that required by the legislative framework. However, if the legislative framework does not stipulate a requirement of at least 10%, the issuing bank needs to publicly disclose on a regular basis that their cover pool meets the 10% requirement in practice. In addition to the primary assets listed in this paragraph, additional collateral may include substitution assets (cash or short term liquid and secure assets held in substitution of the primary assets to top up the cover pool for management purposes) and derivatives entered into for the purposes of hedging the risks arising in the covered bond program.

---

### 7.32 The conditions set out in paragraphs 7.30 and 7.31 must be satisfied at the inception of the covered bond and throughout its remaining maturity { #clause-7-32 }

> **7.32** The conditions set out in paragraphs 7.30 and 7.31 must be satisfied at the inception of the covered bond and throughout its remaining maturity. Disclosure requirements

---

### 7.33 Exposures in the form of covered bonds are eligible for the treatment set out in paragraph 7.34, provided that the bank investing in the covered bonds can demonstrate to SAMA that { #clause-7-33 }

> **7.33** Exposures in the form of covered bonds are eligible for the treatment set out in paragraph 7.34, provided that the bank investing in the covered bonds can demonstrate to SAMA that:
> 1. It receives portfolio information at least on: the value of the cover pool and outstanding covered bonds; (a) the geographical distribution and type of cover assets, loan size, (b) interest rate and currency risks; the maturity structure of cover assets and covered bonds; and (c) the percentage of loans more than 90 days past due; and (d)
> 2. The issuer makes the information referred to in point (1) available to the bank at least semi-annually.

---

### 7.34 Covered bonds that meet the criteria set out in paragraphs 7.30 to 7.33 shall be risk-weighted based on the issue-specific rating or the issuer’s risk weight according to the rules outlined in chapter 8 { #clause-7-34 }

> **7.34** Covered bonds that meet the criteria set out in paragraphs 7.30 to 7.33 shall be risk-weighted based on the issue-specific rating or the issuer’s risk weight according to the rules outlined in chapter 8. For covered bonds with issue- specific ratings<sup>[10]</sup>, the risk weight shall be determined according to Table 6. For unrated covered bonds, the risk weight would be inferred from the issuer’s ECRA or SCRA risk weight according to Table 7. Risk weight table for rated covered bond exposures Table 6 AAA A+ to BBB+ BB+ to Below Issue-specific rating of the to A– to B– B– covered bond AA– BBB– “Base” risk weight 10% 20% 20% 50% 100% Risk weight table for unrated covered bond exposures Table 7 Risk weight of the 20% 30% 40% 50% 75% 100% 150% issuing bank “Base” risk weight 10% 15% 20% 25% 35% 50% 100%
>
> | AAA to AA– | A+ to A– | BBB+ to BBB– | BB+ to B– |
> | --- | --- | --- | --- |
> | 10% | 20% | 20% | 50% |
>
> | 20% | 30% | 40% | 50% | 75% | 100% |
> | --- | --- | --- | --- | --- | --- |
> | 10% | 15% | 20% | 25% | 35% | 50% |

???+ note "Footnote [10]"
    An exposure is rated from the perspective of a bank if the exposure is rated by a recognized ECAI which has been nominated by the bank (i.e. the bank has informed its supervisor of its intention to use the ratings of such ECAI for regulatory purposes in a consistent manner (see paragraph 8.8). In other words, if an external rating exists but the credit rating agency is not a recognized ECAI by SAMA, or the rating has been issued by an ECAI, which has not been nominated by the bank, the exposure would be considered as being unrated from the perspective of the bank.

---

### 7.35 Banks must perform due diligence to ensure that the external ratings appropriately and conservatively reflect the creditworthiness of the covered bond and the issuing bank { #clause-7-35 }

> **7.35** Banks must perform due diligence to ensure that the external ratings appropriately and conservatively reflect the creditworthiness of the covered bond and the issuing bank. If the due diligence analysis reflects higher risk characteristics than that implied by the external rating bucket of the exposure (i.e. AAA to AA–; A+ to A– etc.), the bank must assign a risk weight at least one bucket higher than the “base” risk weight determined by the external rating. Due diligence analysis must never result in the application of a lower risk weight than that determined by the external rating. Exposures to securities firms and other financial institutions

---
