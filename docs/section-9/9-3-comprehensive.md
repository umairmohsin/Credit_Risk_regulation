# 9.40–9.64 Collateral — Comprehensive Approach

Haircut-adjusted exposure calculation (E* formula), supervisory haircuts, own estimates, and SFT netting.

---

### 9.40 In the comprehensive approach, when taking collateral, banks must calculate their adjusted exposure to a counterparty in order to take account of the risk mitigating effect of that collateral { #clause-9-40 }

> **9.40** In the comprehensive approach, when taking collateral, banks must calculate their adjusted exposure to a counterparty in order to take account of the risk mitigating effect of that collateral. Banks must use the applicable supervisory haircuts to adjust both the amount of the exposure to the counterparty and the value of any collateral received in support of that counterparty to take account<sup>[45]</sup> of possible future fluctuations in the value of either, as occasioned by market movements. Unless either side of the transaction is cash or a zero haircut is applied, the volatility-adjusted exposure amount is higher than the nominal exposure and the volatility-adjusted collateral value is lower than the nominal collateral value. 9.41The size of the haircuts that banks must use depends on the prescribed holding period for the transaction. For the purposes of chapter 9, the holding period is the period of time over which exposure or collateral values are assumed to move before the bank can close out the transaction. The supervisory prescribed minimum holding period is used as the basis for the calculation of the standard supervisory haircuts.

???+ note "Footnote [45]"
    Exposure amounts may vary where, for example, securities are being lent.

---

### 9.42 The holding period, and thus the size of the individual haircuts depends on the type of instrument, type of transaction, residual maturity and the frequency of marking to market and remargining as provided in paragraphs 9.49 to 9.50 { #clause-9-42 }

> **9.42** The holding period, and thus the size of the individual haircuts depends on the type of instrument, type of transaction, residual maturity and the frequency of marking to market and remargining as provided in paragraphs 9.49 to 9.50. For example, repo-style transactions subject to daily marking-to-market and to daily remargining will receive a haircut based on a 5-business day holding period and secured lending transactions with daily mark-to-market and no remargining clauses will receive a haircut based on a 20-business day holding period. Haircuts must be scaled up using the square root of time formula depending on the actual frequency of remargining or marking to market. This formula is included in paragraph 9.58.

---

### 9.43 Additionally, where the exposure and collateral are held in different currencies, banks must apply an additional haircut to the volatility-adjusted collateral amount in accordance with paragraphs 9.51 and 9.81 to 0 to take account of possible future fluctuations in exchange rates { #clause-9-43 }

> **9.43** Additionally, where the exposure and collateral are held in different currencies, banks must apply an additional haircut to the volatility-adjusted collateral amount in accordance with paragraphs 9.51 and 9.81 to 0 to take account of possible future fluctuations in exchange rates.

---

### 9.44 The effect of master netting agreements covering securities financing transactions (SFTs) can be recognized for the calculation of capital requirements subject to the conditions and requirements in paragraphs 9.61 to 9.64 { #clause-9-44 }

> **9.44** The effect of master netting agreements covering securities financing transactions (SFTs) can be recognized for the calculation of capital requirements subject to the conditions and requirements in paragraphs 9.61 to 9.64 . Where SFTs are subject to a master netting agreement whether they are held in the banking book or trading book, a bank may choose not to recognize the netting effects in calculating capital. In that case, each transaction will be subject to a capital charge as if there were no master netting agreement. The comprehensive approach: eligible financial collateral

---

### 9.45 The following collateral instruments are eligible for recognition in the comprehensive approach { #clause-9-45 }

> **9.45** The following collateral instruments are eligible for recognition in the comprehensive approach: (1) All of the instruments listed in paragraph 9.34; (2) Equities and convertible bonds that are not included in a main index but which are listed on a recognized security exchange; (3) UCITS/mutual funds which include the instruments in point (2). The comprehensive approach: calculation of capital requirement

---

### 9.46 For a collateralized transaction, the exposure amount after risk mitigation is calculated using the formula that follows, where { #clause-9-46 }

=== "Clause Text"
    > **9.46** For a collateralized transaction, the exposure amount after risk mitigation is calculated using the formula that follows, where: * (1) E= the exposure value after risk mitigation (2) E = current value of the exposure (3) H= haircut appropriate to the exposure e (4) C = the current value of the collateral received (5) H= haircut appropriate to the collateral c (6)H= haircut appropriate for currency mismatch between the fx collateral and exposure

=== "How it works"
    **Comprehensive Approach — E* Formula**

    **Adjusted exposure after risk mitigation:**
    
    > **E\* = max{0, E×(1+He) − C×(1−Hc−Hfx)}**
    
    Where:
    - **E\*** = exposure value after risk mitigation (the amount that attracts a risk weight)
    - **E** = current exposure value
    - **He** = haircut appropriate to the exposure (for volatile securities lent)
    - **C** = current value of collateral received
    - **Hc** = haircut for collateral (volatility of collateral value)
    - **Hfx** = haircut for FX mismatch between exposure and collateral (8% for 10-day holding period, standard)
    
    If E\* > 0, apply the counterparty's risk weight to E\*.
    If E\* = 0 or negative, exposure is fully covered.


---

### 9.47 In the case of maturity mismatches, the value of the collateral received (collateral amount) must be adjusted in accordance with paragraphs 9.10 to 0 { #clause-9-47 }

> **9.47** In the case of maturity mismatches, the value of the collateral received (collateral amount) must be adjusted in accordance with paragraphs 9.10 to 0 .
>
> | Residual maturity | Sovereigns | Other issuers |
> | --- | --- | --- |
> | < 1 year | 0.5 | 1 |
> | >1 year, < 3years | 2 | 3 |
> | >3 years, < 5years |  | 4 |
> | >5 years, < 10years | 4 | 6 |

---

### 9.48 The exposure amount after risk mitigation (E*) must be multiplied by the risk weight of the counterparty to obtain the risk-weighted asset amount for the collateralized transaction { #clause-9-48 }

> **9.48** The exposure amount after risk mitigation (E*) must be multiplied by the risk weight of the counterparty to obtain the risk-weighted asset amount for the collateralized transaction.

---

### 9.49 The following supervisory haircuts in table 14 below (assuming daily mark-to- market, daily remargining and a 10 business day holding period), expressed as percentages, must be used to determine the haircuts appropriate to the collateral (H) and to the exposure (H) { #clause-9-49 }

> **9.49** The following supervisory haircuts in table 14 below (assuming daily mark-to- market, daily remargining and a 10 business day holding period), expressed as percentages, must be used to determine the haircuts appropriate to the collateral (H) and to the exposure (H): ce Supervisory haircuts for comprehensive approach Table 14 Issue rating for Securitization Residual Sovereigns Other debt securities exposures maturity issuers < 1 year 0.5 1 2 >1 year, 2 3 8 < 3years AAA to AA–/A-1 >3 years, 4 < 5years >5 years, 4 6 16 < 10years > 10 years 12 < 1 year 1 2 4 >1 year, 3 4 12 A+ to BBB–/ < 3years A-2/A-3/P-3 and unrated bank >3 years, 6 securities < 5years 9.34(3)(b) 12 >5 years, 6 24 < 10years > 10 years 20 BB+ to BB– All 15 Not Not eligible eligible Main index equities 20 (including convertible bonds) and gold Other equities and 30 convertible bonds listed on a recognized exchange UCITS/mutual funds Highest haircut applicable to any security in which the fund can invest, unless the bank can apply the look-through approach (LTA) for equity investments in funds, in which case the bank may use a weighted average of haircuts applicable to instruments held by the fund. Cash in the same currency 0

---

### 9.50 In paragraph 9.49 { #clause-9-50 }

> **9.50** In paragraph 9.49 : (1) “Sovereigns” includes: PSEs that are treated as sovereigns by SAMA, as well as multilateral development banks receiving a 0% risk weight. (2) “Other issuers” includes: PSEs that are not treated as sovereigns by SAMA. (3) “Securitization exposures” refers to exposures that meet the definition set forth in the securitization framework. (4) “Cash in the same currency” refers to eligible cash collateral specified in paragraph 9.34(1).

---

### 9.51 The haircut for currency risk (H) where exposure and collateral are fx denominated in different currencies is 8% (also based on a 10-business day holding period and daily mark-to-market) { #clause-9-51 }

> **9.51** The haircut for currency risk (H) where exposure and collateral are fx denominated in different currencies is 8% (also based on a 10-business day holding period and daily mark-to-market).

---

### 9.52 For SFTs and secured lending transactions, a haircut adjustment may need to be applied in accordance with paragraphs 9.55 to 9.58 { #clause-9-52 }

=== "Clause Text"
    > **9.52** For SFTs and secured lending transactions, a haircut adjustment may need to be applied in accordance with paragraphs 9.55 to 9.58.

=== "How it works"
    **Haircut Scaling Formula**

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


---

### 9.53 For SFTs in which the bank lends, or posts as collateral, non-eligible instruments, the haircut to be applied on the exposure must be 30% { #clause-9-53 }

> **9.53** For SFTs in which the bank lends, or posts as collateral, non-eligible instruments, the haircut to be applied on the exposure must be 30%. For transactions in which the bank borrows non-eligible instruments, credit risk mitigation may not be applied.

---

### 9.54 Where the collateral is a basket of assets, the haircut (H) on the basket must be calculated using the formula that follows, where { #clause-9-54 }

> **9.54** Where the collateral is a basket of assets, the haircut (H) on the basket must be calculated using the formula that follows, where: (1) ais the weight of the asset (as measured by units of currency) i in the basket (2) Hthe haircut applicable to that asset i The comprehensive approach: adjustment for different holding periods and non- daily mark-to-market or remargining

---

### 9.55 For some transactions, depending on the nature and frequency of the revaluation and remargining provisions, different holding periods and thus different haircuts must be applied { #clause-9-55 }

> **9.55** For some transactions, depending on the nature and frequency of the revaluation and remargining provisions, different holding periods and thus different haircuts must be applied. The framework for collateral haircuts distinguishes between repo-style transactions (i.e. repo/reverse repos and securities lending/borrowing),” other capital markets-driven transactions” (i.e. OTC derivatives transactions and margin lending) and secured lending. In capital- market-driven transactions and repo-style transactions, the documentation contains remargining clauses; in secured lending transactions, it generally does not. 9.56The minimum holding period for various products is summarized in table 15 below: Minimum holding periods Table 15 Summary of minimum holding periods and remargining/revaluation periods Minimum Transaction type Minimum holding period remargining /revaluation period Repo-style transaction five business days daily remargining Other capital 10 business days daily remargining market transactions Secured lending 20 business days daily revaluation
>
> | Minimum holding period |
> | --- |
> | five business days |
> | 10 business days |
> | 20 business days |

---

### 9.57 Regarding the minimum holding periods set out in paragraph 9.56, if a netting set includes both repo-style and other capital market transactions, the minimum holding period of ten business days must be used { #clause-9-57 }

> **9.57** Regarding the minimum holding periods set out in paragraph 9.56, if a netting set includes both repo-style and other capital market transactions, the minimum holding period of ten business days must be used. Furthermore, a higher minimum holding period must be used in the following cases: (1) For all netting sets where the number of trades exceeds 5,000 at any point during a quarter, a 20-business day minimum holding period for the following quarter must be used. (2) For netting sets containing one or more trades involving illiquid collateral, a minimum holding period of 20 business days must be used. "Illiquid collateral" must be determined in the context of stressed market conditions and will be characterized by the absence of continuously active markets where a counterparty would, within two or fewer days, obtain multiple price quotations that would not move the market or represent a price reflecting a market discount. Examples of situations where trades are deemed illiquid for this purpose include, but are not limited to, trades that are not marked daily and trades that are subject to specific accounting treatment for valuation purposes (e.g. repo-style transactions referencing securities whose fair value is determined by models with inputs that are not observed in the market). (3) If a bank has experienced more than two margin call disputes on a particular netting set over the previous two quarters that have lasted longer than the bank's estimate of the margin period of risk (as defined in The Counterparty Credit Risk (CCR) Framework), then for the subsequent two quarters the bank must use a minimum holding period that is twice the level that would apply excluding the application of this sub-paragraph.

---

### 9.58 When the frequency of remargining or revaluation is longer than the minimum, the minimum haircut numbers must be scaled up depending on the actual number of business days between remargining or revaluation { #clause-9-58 }

> **9.58** When the frequency of remargining or revaluation is longer than the minimum, the minimum haircut numbers must be scaled up depending on the actual number of business days between remargining or revaluation. The 10-business day haircuts provided in paragraphs 9.49 to 9.50 are the default haircuts and thesehaircuts must be scaled up or down using the formula below, where: H = haircut (1) (2) H= 10-business day haircut for instrument 10 T= minimum holding period for the type of transaction. (3)M N= actual number of business days between remargining for capital (4) R market transactions or revaluation for secured transactions The comprehensive approach: exemptions under the comprehensive approach for qualifying repo-style transactions involving core market participants

---

### 9.59 For repo-style transactions with core market participants as defined in paragraph { #clause-9-59 }

> **9.59** For repo-style transactions with core market participants as defined in paragraph

---

### 9.60 Where, under the comprehensive approach, a foreign supervisor applies a specific carve-out to repo-style transactions in securities issued by its domestic government, banks are allowed to adopt the same approach to the same transactions { #clause-9-60 }

> **9.60** Where, under the comprehensive approach, a foreign supervisor applies a specific carve-out to repo-style transactions in securities issued by its domestic government, banks are allowed to adopt the same approach to the same transactions. The comprehensive approach: treatment under the comprehensive approach of SFTs covered by master netting agreements

---

### 9.61 The effects of bilateral netting agreements covering SFTs may be recognized on a counterparty-by-counterparty basis if the agreements are legally enforceable in each relevant jurisdiction upon the occurrence of an event of default and regardless of whether the counterparty is insolvent or bankrupt { #clause-9-61 }

> **9.61** The effects of bilateral netting agreements covering SFTs may be recognized on a counterparty-by-counterparty basis if the agreements are legally enforceable in each relevant jurisdiction upon the occurrence of an event of default and regardless of whether the counterparty is insolvent or bankrupt. In addition, netting agreements must: (1) Provide the non-defaulting party the right to terminate and close out in a timely manner all transactions under the agreement upon an event of default, including in the event of insolvency or bankruptcy of the counterparty; (2) Provide for the netting of gains and losses on transactions (including the value of any collateral) terminated and closed out under it so that a single net amount is owed by one party to the other; (3) Allow for the prompt liquidation or set-off of collateral upon the event of default; and (4) Be, together with the rights arising from the provisions required in (1) to (3) above, legally enforceable in each relevant jurisdiction upon the occurrence of an event of default and regardless of the counterparty’s insolvency or bankruptcy.

---

### 9.62 Netting across positions in the banking and trading book may only be recognized when the netted transactions fulfil the following conditions { #clause-9-62 }

> **9.62** Netting across positions in the banking and trading book may only be recognized when the netted transactions fulfil the following conditions: (1) All transactions are marked to market daily<sup>[46]</sup>; and (2) The collateral instruments used in the transactions are recognized as eligible financial collateral in the banking book.

???+ note "Footnote [46]"
    The holding period for the haircuts depends, as in other repo-style transactions, on the frequency of margining.

---

### 9.63 The formula in paragraph 9.64 will be used to calculate the counterparty credit risk capital requirements for SFTs with netting agreements { #clause-9-63 }

> **9.63** The formula in paragraph 9.64 will be used to calculate the counterparty credit risk capital requirements for SFTs with netting agreements. This formula includes the current exposure, an amount for systematic exposure of the securities based on the net exposure, an amount for the idiosyncratic exposure of the securities based on the gross exposure, and an amount for currency mismatch. All other rules regarding the calculation of haircuts under the comprehensive approach stated in paragraphs 9.40 to 9.60 equivalently apply for banks using bilateral netting agreements for SFTs.

---

### 9.64 Banks using standard supervisory haircuts for SFTs conducted under a master netting agreement must use the formula that follows to calculate their exposure amount, where { #clause-9-64 }

> **9.64** Banks using standard supervisory haircuts for SFTs conducted under a master netting agreement must use the formula that follows to calculate their exposure amount, where: * (1) Eis the exposure value of the netting set after risk mitigation (2) Eis the current value of all cash and securities lent, sold with an i agreement to repurchase or otherwise posted to the counterparty under the netting agreement (3) Cis the current value of all cash and securities borrowed, purchased j with an agreement to resell or otherwise held by the bank under the netting agreement (4) (5) (6) Eis the net current value of each security issuance under the netting s set(always a positive value) (7) His the haircut appropriate to Eas described in tables of s s paragraphs 9.49 to 9.50, as applicable (a) Hhas a positive sign if the security is lent, sold with an agreement s to repurchased, or transacted in manner similar to either securities lending or a repurchase agreement (b) Hhas a negative sign if the security is borrowed, purchased with an s agreement to resell, or transacted in a manner similar to either a securities borrowing or reverse repurchase agreement (8) N is the number of security issues contained in the netting set (except that issuances where the value Es is less than one tenth of the value of the largest Es in the netting set are not included the count) (9) Eis the absolute value of the net position in each currency fx fx different from the settlement currency (10) His the haircut appropriate for currency mismatch of currency fx fx Collateralized OTC derivatives, exchange traded derivatives and long settlement transactions

---
