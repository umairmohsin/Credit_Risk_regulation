# 9.1–9.15 General CRM Requirements

Legal certainty, eligibility conditions, and maturity mismatch treatment.

---

### 9.1 Banks use a number of techniques to mitigate the credit risks to which they are exposed { #clause-9-1 }

> **9.1** Banks use a number of techniques to mitigate the credit risks to which they are exposed. For example, exposures may be collateralized by first-priority claims, in whole or in part with cash or securities, a loan exposure may be guaranteed by a third party, or a bank may buy a credit derivative to offset various forms of credit risk. Additionally, banks may agree to net loans owed to them against<sup>[39]</sup> deposits from the same counterparty.

???+ note "Footnote [39]"
    In this section, “counterparty” is used to denote a party to whom a bank has an on- or off-balance sheet credit exposure. That exposure may, for example, take the form of a loan of cash or securities (where the counterparty would traditionally be called the borrower), of securities posted as collateral, of a commitment or of exposure under an over-the-counter (OTC) derivatives contract.

---

### 9.2 The framework set out in this chapter is applicable to banking book exposures that are risk-weighted under the standardized approach { #clause-9-2 }

> **9.2** The framework set out in this chapter is applicable to banking book exposures that are risk-weighted under the standardized approach. General requirements

---

### 9.3 No transaction in which credit risk mitigation (CRM) techniques are used shall receive a higher capital requirement than an otherwise identical transaction where such techniques are not used { #clause-9-3 }

=== "Clause Text"
    > **9.3** No transaction in which credit risk mitigation (CRM) techniques are used shall receive a higher capital requirement than an otherwise identical transaction where such techniques are not used.

=== "How it works"
    **CRM Technique Selection**

    ```mermaid
    flowchart TD
        A[CRM protection available] --> B{Type of protection?}
        B -- Financial collateral --> C{Method?}
        C -- Simple approach --> D[S9.32–9.39<br/>Substitute collateral RW]
        C -- Comprehensive approach --> E[S9.40–9.64<br/>Haircut-adjusted EAD]
        B -- On-balance-sheet netting --> F[S9.65–9.69<br/>Net loans vs deposits]
        B -- Guarantee / credit derivative --> G[S9.70–9.83<br/>Substitute guarantor RW]
        D & E & F & G --> H[Compute reduced RWA]
    ```


---

### 9.4 The requirements of chapter 19 in Pillar 3 Disclosure Requirements Framework must be fulfilled for banks to obtain capital relief in respect of any CRM techniques { #clause-9-4 }

> **9.4** The requirements of chapter 19 in Pillar 3 Disclosure Requirements Framework must be fulfilled for banks to obtain capital relief in respect of any CRM techniques.

---

### 9.5 The effects of CRM must not be double-counted { #clause-9-5 }

> **9.5** The effects of CRM must not be double-counted. Therefore, no additional supervisory recognition of CRM for regulatory capital purposes will be granted on exposures for which the risk weight already reflects that CRM. Consistent with paragraph 8.14, principal-only ratings will also not be allowed within the CRM framework.

---

### 9.6 While the use of CRM techniques reduces or transfers credit risk, it may simultaneously increase other risks (i.e. residual risks) { #clause-9-6 }

> **9.6** While the use of CRM techniques reduces or transfers credit risk, it may simultaneously increase other risks (i.e. residual risks). Residual risks include legal, operational, liquidity and market risks. Therefore, banks must employ robust procedures and processes to control these risks, including strategy; consideration of the underlying credit; valuation; policies and procedures; systems; control of roll-off risks; and management of concentration risk arising from the bank’s use of CRM techniques and its interaction with the bank’s overall credit risk profile. Where these risks are not adequately controlled, SAMA may impose additional capital charges or take other supervisory actions in the supervisory review process.

---

### 9.7 In order for CRM techniques to provide protection, the credit quality of the counterparty must not have a material positive correlation with the employed CRM technique or with the resulting residual risks (as defined in paragraph 9.6) { #clause-9-7 }

> **9.7** In order for CRM techniques to provide protection, the credit quality of the counterparty must not have a material positive correlation with the employed CRM technique or with the resulting residual risks (as defined in paragraph 9.6) . For example, securities issued by the counterparty (or by any counterparty- related entity) provide little protection as collateral and are thus ineligible.

---

### 9.8 In the case where a bank has multiple CRM techniques covering a single exposure (e.g. a bank has both collateral and a guarantee partially covering an exposure), the bank must subdivide the exposure into portions covered by each type of CRM technique (e.g. portion covered by collateral, portion covered by guarantee) and the risk-weighted assets of each portion must be calculated separately { #clause-9-8 }

> **9.8** In the case where a bank has multiple CRM techniques covering a single exposure (e.g. a bank has both collateral and a guarantee partially covering an exposure), the bank must subdivide the exposure into portions covered by each type of CRM technique (e.g. portion covered by collateral, portion covered by guarantee) and the risk-weighted assets of each portion must be calculated separately. When credit protection provided by a single protection provider has differing maturities, they must be subdivided into separate protection as well. Legal requirements

---

### 9.9 In order for banks to obtain capital relief for any use of CRM techniques, all documentation used in collateralized transactions, on-balance sheet netting agreements, guarantees and credit derivatives must be binding on all parties and legally enforceable in all relevant jurisdictions { #clause-9-9 }

> **9.9** In order for banks to obtain capital relief for any use of CRM techniques, all documentation used in collateralized transactions, on-balance sheet netting agreements, guarantees and credit derivatives must be binding on all parties and legally enforceable in all relevant jurisdictions. Banks must have conducted sufficient legal review to verify this and have a well-founded legal basis to reach this conclusion, and undertake such further review as necessary to ensure continuing enforceability. General treatment of maturity mismatches

---

### 9.10 For the purposes of calculating risk-weighted assets, a maturity mismatch occurs when the residual maturity of a credit protection arrangement (e.g. hedge) is less than that of the underlying exposure { #clause-9-10 }

=== "Clause Text"
    > **9.10** For the purposes of calculating risk-weighted assets, a maturity mismatch occurs when the residual maturity of a credit protection arrangement (e.g. hedge) is less than that of the underlying exposure.

=== "How it works"
    **Maturity Mismatch Adjustment (Pa formula)**

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


---

### 9.11 In the case of financial collateral, maturity mismatches are not allowed under the simple approach (see paragraph 9.33) { #clause-9-11 }

> **9.11** In the case of financial collateral, maturity mismatches are not allowed under the simple approach (see paragraph 9.33).

---

### 9.12 Under the other approaches, when there is a maturity mismatch the credit protection arrangement may only be recognized if the original maturity of the arrangement is greater than or equal to one year, and its residual maturity is greater than or equal to three months { #clause-9-12 }

> **9.12** Under the other approaches, when there is a maturity mismatch the credit protection arrangement may only be recognized if the original maturity of the arrangement is greater than or equal to one year, and its residual maturity is greater than or equal to three months. In such cases, credit risk mitigation may be partially recognized as detailed below in paragraph 9.13 .

---

### 9.13 When there is a maturity mismatch with recognized credit risk mitigants, the following adjustment applies, where { #clause-9-13 }

> **9.13** When there is a maturity mismatch with recognized credit risk mitigants, the following adjustment applies, where: P= value of the credit protection adjusted for maturity mismatch (1)a P = credit protection amount (e.g. collateral amount, guarantee (2) amount) adjusted for any haircuts t = min {T, residual maturity of the credit protection arrangement (3) expressed in years} T = min {five years, residual maturity of the exposure expressed in (4) years}

---

### 9.14 The maturity of the underlying exposure and the maturity of the hedge must both be defined conservatively { #clause-9-14 }

> **9.14** The maturity of the underlying exposure and the maturity of the hedge must both be defined conservatively. The effective maturity of the underlying must be gauged as the longest possible remaining time before the counterparty is scheduled to fulfil its obligation, taking into account any applicable grace period. For the hedge, (embedded) options that may reduce the term of the hedge must be taken into account so that the shortest possible effective maturity is used. For example: where, in the case of a credit derivative, the protection seller has a call option, the maturity is the first call date. Likewise, if the protection buyer owns the call option and has a strong incentive to call the transaction at the first call date, for example because of a step-up in cost from this date on, the effective maturity is the remaining time to the first call date. Currency mismatches 9.15Currency mismatches are allowed under all approaches. Under the simple approach there is no specific treatment for currency mismatches, given that a minimum risk weight of 20% (floor) is generally applied. Under the comprehensive approach and in case of guarantees and credit derivatives, a specific adjustment for currency mismatches is prescribed in paragraph 9.51 and

---
