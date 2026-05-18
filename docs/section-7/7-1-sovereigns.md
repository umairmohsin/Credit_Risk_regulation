# 7.1–7.3 Sovereigns & Central Banks

Risk weights for exposures to sovereigns, central banks, and certain international institutions.

---

### 7.1 Exposures to sovereigns and their central banks will be risk-weighted based on the external rating of the sovereign as follows { #clause-7-1 }

=== "Clause Text"
    > **7.1** Exposures to sovereigns and their central banks will be risk-weighted based on the external rating of the sovereign as follows: Risk weight table for sovereigns and central banks Table 1 External rating AAA to A+ to BBB+ BB+ to Below Unrated AA– A– to B– B– BBB– Risk weight 0% 20% 50% 100% 150% 100%
    >
    > | AAA to AA– | A+ to A– | BBB+ to BBB– | BB+ to B– | Below B– |
    > | --- | --- | --- | --- | --- |
    > | 0% | 20% | 50% | 100% | 150% |

=== "How it works"
    **Table 1 — Sovereign Risk Weights**

    | External Rating | Risk Weight |
    |---|---|
    | AAA to AA− | **0%** |
    | A+ to A− | **20%** |
    | BBB+ to BBB− | **50%** |
    | BB+ to B− | **100%** |
    | Below B− | **150%** |
    | Unrated | **100%** |

    **Decision Flow**

    ```mermaid
    flowchart TD
        A[Exposure to Sovereign / Central Bank] --> B{External rating available?}
        B -- No --> G[**100% RW** — Unrated]
        B -- Yes --> C{Rating band?}
        C -- AAA to AA− --> D[**0% RW**]
        C -- A+ to A− --> E[**20% RW**]
        C -- BBB+ to BBB− --> F[**50% RW**]
        C -- BB+ to B− --> H[**100% RW**]
        C -- Below B− --> I[**150% RW**]
    ```


---

### 7.2 A 0% risk weight can be applied to banks’ exposures to Saudi sovereign (or SAMA) of incorporation denominated in Saudi Riyal and funded in Saudi Riyal (SAR) { #clause-7-2 }

=== "Clause Text"
    > **7.2** A 0% risk weight can be applied to banks’ exposures to Saudi sovereign (or SAMA) of incorporation denominated in Saudi Riyal and funded<sup>[2]</sup> in Saudi Riyal (SAR).<sup>[3]</sup> Exposures to Saudi sovereign of incorporation denominated in foreign currencies should be treated according to the Saudi sovereign external rating.

=== "How it works"
    **SAR Preferential Treatment**

    **Two conditions must BOTH be met to apply 0% risk weight:**
    
    1. The exposure is denominated in **Saudi Riyals (SAR)**
    2. The exposure is **funded** in SAR (bank has matching SAR liabilities)
    
    If either condition fails → apply standard sovereign RW from Table 1 (S7.1).


???+ note "Footnote [2]"
    This is to say that the bank would also have corresponding liabilities denominated in the domestic currency.
???+ note "Footnote [3]"
    This lower risk weight may be extended to the risk-weighting of collateral and guarantees under the CRM framework (chapter 9)

---

### 7.3 Sovereign exposures to the member countries of Gulf Cooperation Council (GCC) will also be risk-weighted based on the external rating of the respective country as per Table 1 { #clause-7-3 }

> **7.3** Sovereign exposures to the member countries of Gulf Cooperation Council (GCC) will also be risk-weighted based on the external rating of the respective country as per Table 1.

---
