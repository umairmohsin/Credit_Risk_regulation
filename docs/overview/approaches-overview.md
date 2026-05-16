# Approaches Overview & Due Diligence

Sections 5–6 explain which credit risk measurement approaches are available and what banks must do to use them.

---

## 5. Approaches for Computing Credit Risk Capital Requirements { #clause-5 }

=== "Clause Text"
    > **5.** Banks may use the following approaches to compute minimum capital requirements for credit risk:
    >
    > - The **Standardised Approach (SA)** as set out in chapters 6 to 9 of this document
    > - The **Internal Ratings-Based (IRB) Approach** as set out in chapters 10 to 16, subject to prior approval by SAMA
    >
    > Additionally, banks must apply the relevant requirements for:
    > - **Securitisation exposures** (chapters 18–23)
    > - **Equity investments in funds** (chapter 24)
    > - **Unsettled transactions** (chapter 25)

=== "Decision Flow"
    ```mermaid
    flowchart TD
        A[Bank needs credit RWA] --> B{Has SAMA approval for IRB?}
        B -- No --> C[✅ Use Standardised Approach SA]
        B -- Yes --> D[✅ Use IRB Approach]
        C --> E{Exposure type?}
        D --> E
        E -- Standard credit exposure --> F[SA: Chapters 6–9]
        E -- Securitisation --> G[Chapters 18–23]
        E -- Equity in funds --> H[Chapter 24]
        E -- Unsettled transaction --> I[Chapter 25]
        F --> J[Apply due diligence S6]
    ```

=== "Scope of This Document"
    This knowledge base covers **Sections 1–9 only**: the Standardised Approach.
    
    IRB (chapters 10–16), securitisation (chapters 18–23), equity in funds (24), and unsettled transactions (25) are out of scope.

---

## 6. Due Diligence { #clause-6 }

### 6.1 { #clause-6-1 }

=== "Clause Text"
    > **6.1** When using the Standardised Approach, banks must perform due diligence to ensure that they have an adequate understanding of the risk profile and characteristics of their counterparties.

=== "Key Point"
    Due diligence is a **mandatory ongoing obligation**, not a one-time onboarding step. It applies to every counterparty where the bank holds an SA exposure.

---

### 6.2 { #clause-6-2 }

=== "Clause Text"
    > **6.2** Banks are required to conduct due diligence at **least annually**.

=== "Key Facts"
    | Requirement | Detail |
    |---|---|
    | Minimum frequency | Annual |
    | Trigger for more frequent review | Material change in counterparty risk profile |

---

### 6.3 { #clause-6-3 }

=== "Clause Text"
    > **6.3** For banking groups using the SA, the due diligence requirement applies at the **solo entity level**. Banks must be able to demonstrate to SAMA that due diligence has been performed.

=== "Decision Flow"
    ```mermaid
    flowchart TD
        A[Banking Group on SA] --> B[Each solo entity performs own due diligence]
        B --> C[Annual minimum frequency per S6.2]
        C --> D{SAMA requests evidence?}
        D -- Yes --> E[Provide documentation of due diligence performed]
        D -- No --> F[Maintain records for future review]
    ```

---

## Cross-References

- [S2 — Scope of application](introduction.md#clause-2)
- [S4 — Reporting requirements](sama-requirements.md#clause-4)
- [S7 — Individual exposure risk weights](../standardised-approach/individual-exposures.md)
- [S8 — External credit ratings](../standardised-approach/external-ratings.md)
- [S9 — Credit Risk Mitigation](../standardised-approach/crm.md)
