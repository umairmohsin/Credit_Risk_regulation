# SAMA Reporting Requirements

Section 4 specifies how banks must report their credit risk capital requirements to SAMA.

---

## 4. Reporting to SAMA { #clause-4 }

=== "Clause Text"
    > **4.** Banks are required to report their minimum capital requirements for credit risk to SAMA using the **Q17 template**. This report must be submitted within **30 days** after the end of each quarter.

=== "Decision Flow"
    ```mermaid
    flowchart TD
        A[Quarter End] --> B[Calculate credit RWA per S5–9]
        B --> C[Complete Q17 Template]
        C --> D{Submission deadline}
        D --> E[Submit to SAMA within 30 calendar days]
        E --> F{Submitted on time?}
        F -- Yes --> G[✅ Compliant]
        F -- No --> H[⚠️ Regulatory breach — escalate]
    ```

=== "Key Facts"
    | Item | Detail |
    |---|---|
    | Reporting template | Q17 |
    | Frequency | Quarterly |
    | Deadline | Within 30 days after quarter end |
    | Basis | Consolidated and standalone (per S2) |

---

## Quarterly Calendar

| Quarter end | Latest submission |
|---|---|
| 31 March | 30 April |
| 30 June | 30 July |
| 30 September | 30 October |
| 31 December | 30 January |

---

## Cross-References

- [S2 — Scope (who must report)](introduction.md#clause-2)
- [S5 — Which RWA calculation approach applies](approaches-overview.md)
