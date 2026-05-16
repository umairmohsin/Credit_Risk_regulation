# Introduction, Scope & Implementation Timeline

Sections 1–3 establish the legal basis for the regulation, which banks must comply, and when.

---

## 1. Introduction { #clause-1 }

=== "Clause Text"
    > **1.** These minimum capital requirements for credit risk are based on the Basel Committee on Banking Supervision (BCBS) standards issued in December 2017. These requirements supersede the following SAMA circulars:
    >
    > - Circular No. 341000003699 dated 14/01/1434H
    > - Circular No. 351000116305 dated 22/06/1435H
    > - Circular No. 371000042256 dated 30/01/1437H
    > - Circular No. 381000088501 dated 06/04/1438H
    >
    > The authority for this regulation derives from Royal Decree M/36 dated 15/04/1428H (Banking Control Law, Article 3(A)).

=== "Key Facts"
    | Item | Detail |
    |---|---|
    | Basel standard | BCBS December 2017 |
    | SAMA legal authority | Royal Decree M/36, 15/04/1428H |
    | Article | Banking Control Law, Article 3(A) |
    | Superseded circulars | 4 circulars (2013–2017) |

---

## 2. Scope of Application { #clause-2 }

=== "Clause Text"
    > **2.** These requirements apply on a consolidated basis and on a standalone basis to all domestic banks licensed to operate in Saudi Arabia. These requirements do not apply to branches of foreign banks operating in Saudi Arabia.

=== "Decision Flow"
    ```mermaid
    flowchart TD
        A[Is this a Saudi-licensed bank?] --> B{Domestic or Foreign Branch?}
        B -- Domestic bank --> C{Standalone or Group?}
        B -- Foreign branch in KSA --> D[❌ Not in scope]
        C -- Standalone entity --> E[✅ Apply on standalone basis]
        C -- Part of banking group --> F[✅ Apply on consolidated basis]
        F --> G[Also apply standalone per S2]
    ```

---

## 3. Implementation Timeline { #clause-3 }

=== "Clause Text"
    > **3.** Banks are required to apply these minimum capital requirements for credit risk starting from **01 January 2023**.

=== "Key Facts"
    | Item | Detail |
    |---|---|
    | Effective date | 01 January 2023 |
    | Transition | No phase-in — full application from effective date |

---

## Cross-References

- [S4 — Reporting obligations](sama-requirements.md)
- [S5 — Choice of SA vs IRB approach](approaches-overview.md)
- [S6 — Due diligence requirements](approaches-overview.md#clause-6)
