# 7.86–7.93 Off-Balance Sheet Items

Credit Conversion Factors (CCFs) for commitments, guarantees, trade finance, and derivatives.

---

### 7.86 Off-balance sheet items will be converted into credit exposure equivalents through the use of credit conversion factors (CCF) { #clause-7-86 }

=== "Clause Text"
    > **7.86** Off-balance sheet items will be converted into credit exposure equivalents through the use of credit conversion factors (CCF). In the case of commitments, the committed but undrawn amount of the exposure would be multiplied by the CCF. For these purposes, commitment means any contractual arrangement that has been offered by the bank and accepted by the client to extend credit, purchase assets or issue credit substitutes.<sup>[32]</sup> It includes any such arrangement that can be unconditionally cancelled by the bank at any time without prior notice to the obligor. It also includes any such arrangement that can be cancelled by the bank if the obligor fails to meet conditions set out in the facility documentation, including conditions that must be met by the obligor prior to any initial or subsequent drawdown under the arrangement. Counterparty risk weightings for over-the-counter (OTC) derivative transactions will not be subject to any specific ceiling. 7.87A 100% CCF will be applied to the following items:
    > 1. Direct credit substitutes, e.g. general guarantees of indebtedness (including standby letters of credit serving as financial guarantees for loans and securities) and acceptances (including endorsements with the character of acceptances).
    > 2. Sale and repurchase agreements and asset sales with recourse<sup>[33]</sup> where the credit risk remains with the bank.
    > 3. The lending of banks’ securities or the posting of securities as collateral by banks, including instances where these arise out of repo-style transactions (i.e. repurchase/reverse repurchase and securities lending/securities borrowing transactions). The risk-weighting treatment for counterparty credit risk must be applied in addition to the credit risk charge on the securities or posted collateral, where the credit risk of the securities lent or posted as collateral remains with the bank. This paragraph does not apply to posted collateral related to derivative transactions that is treated in accordance with the counterparty credit risk standards.
    > 4. Forward asset purchases, forward deposits and partly paid shares and<sup>[34]</sup> securities, which represent commitments with certain drawdown.
    > 5. Off-balance sheet items that are credit substitutes not explicitly included in any other category.

=== "How it works"
    **Table 13 — Off-Balance Sheet CCFs**

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

    **OBS CCF Selection**

    ```mermaid
    flowchart TD
        A[Off-balance sheet item] --> B{Direct credit
    substitute?}
        B -- Yes --> C[**100% CCF**]
        B -- No --> D{Trade finance
    short-term self-liquidating?}
        D -- Yes --> E[**20% CCF**]
        D -- No --> F{Commitment?}
        F -- Unconditionally
    cancellable --> G[**10% CCF**]
        F -- Original maturity
    > 1 year --> H[**40% CCF**]
        F -- NIF / RUF --> I[**50% CCF**]
    ```


???+ note "Footnote [32]"
    Certain arrangements might be exempted from the definition of commitments provided that the following conditions are met: (i) the bank receives no fees or commissions to establish or maintain the arrangements; (ii) the client is required to apply to the bank for the initial and each subsequent drawdown; (iii) the bank has full authority, regardless of the fulfilment by the client of the conditions set out in the facility documentation, over the execution of each drawdown; and (iv) the bank’s decision on the execution of each drawdown is only made after assessing the creditworthiness of the client immediately prior to drawdown. Exempted arrangements that meet the above criteria are limited to certain arrangements for corporates and MSMEs, where counterparties are closely monitored on an ongoing basis.
???+ note "Footnote [33]"
    These items are to be weighted according to the type of asset and not according to the type of counterparty with whom the transaction has been entered into.
???+ note "Footnote [34]"
    These items are to be weighted according to the type of asset and not according to the type of counterparty with whom the transaction has been entered into.

---

### 7.88 A 50% CCF will be applied to note issuance facilities and revolving underwriting facilities regardless of the maturity of the underlying facility { #clause-7-88 }

> **7.88** A 50% CCF will be applied to note issuance facilities and revolving underwriting facilities regardless of the maturity of the underlying facility.

---

### 7.89 A 50% CCF will be applied to certain transaction-related contingent items (e.g. performance bonds, bid bonds, warranties and standby letters of credit related to particular transactions) { #clause-7-89 }

> **7.89** A 50% CCF will be applied to certain transaction-related contingent items (e.g. performance bonds, bid bonds, warranties and standby letters of credit related to particular transactions).

---

### 7.90 A 40% CCF will be applied to commitments, regardless of the maturity of the underlying facility, unless they qualify for a lower CCF { #clause-7-90 }

> **7.90** A 40% CCF will be applied to commitments, regardless of the maturity of the underlying facility, unless they qualify for a lower CCF.

---

### 7.91 A 20% CCF will be applied to both the issuing and confirming banks of short- term self-liquidating trade letters of credit arising from the movement of goods (e.g. documentary credits collateralized by the underlying shipment) { #clause-7-91 }

> **7.91** A 20% CCF will be applied to both the issuing and confirming banks of short- term self-liquidating trade letters of credit arising from the movement of goods (e.g. documentary credits collateralized by the underlying shipment). Short term in this context means with a maturity below one year.

---

### 7.92 A 10% CCF will be applied to commitments that are unconditionally cancellable at any time by the bank without prior notice, or that effectively provide for automatic cancellation due to deterioration in a borrower’s creditworthiness { #clause-7-92 }

> **7.92** A 10% CCF will be applied to commitments that are unconditionally cancellable at any time by the bank without prior notice, or that effectively provide for automatic cancellation due to deterioration in a borrower’s creditworthiness. SAMA may require applying higher CCF to certain commitments as appropriate based on various factors, which may constrain banks’ ability to cancel the commitment in practice.

---

### 7.93 Where there is an undertaking to provide a commitment on an off-balance sheet item, banks are to apply the lower of the two applicable CCFs { #clause-7-93 }

> **7.93** Where there is an undertaking to provide a commitment on an off-balance sheet item, banks are to apply the lower of the two applicable CCFs<sup>[35]</sup>. Exposures that give rise to counterparty credit risk

???+ note "Footnote [35]"
    For example, if a bank has a commitment to open short-term self- liquidating trade letters of credit arising from the movement of goods, a 20% CCF will be applied (instead of a 40% CCF); and if a bank has an unconditionally cancellable commitment described in paragraph 7.92 to issue direct credit substitutes, a 10% CCF will be applied (instead of a 100% CCF).

---
