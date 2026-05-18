# 7.4–7.7 Public Sector Entities (PSEs)

Treatment of domestic and foreign non-central-government public sector entities.

---

### 7.4 Exposures to the Bank for International Settlements, the International Monetary Fund, the European Central Bank, the European Union, the European Stability Mechanism and the European Financial Stability Facility may receive a 0% risk weight { #clause-7-4 }

=== "Clause Text"
    > **7.4** Exposures to the Bank for International Settlements, the International Monetary Fund, the European Central Bank, the European Union, the European Stability Mechanism and the European Financial Stability Facility may receive a 0% risk weight. Exposures to Public Sector Entities (PSEs)

=== "How it works"
    **PSE Treatment Decision**

    ```mermaid
    flowchart TD
        A[Domestic PSE Exposure] --> B{SAMA-designated treatment?}
        B -- Sovereign treatment --> C[Apply **Table 1** sovereign RW<br/>based on country rating]
        B -- Bank treatment --> D{External rating?}
        D -- Rated --> E[Apply **Table 4** bank ECRA RW]
        D -- Unrated --> F[Apply **SCRA** Grade A / B / C]
    ```


---

### 7.5 For the purposes of RWA treatment, domestic PSEs in general include government authorities, administrative and/or statutory bodies responsible to the government, which may be owned, controlled, and/or mostly funded by the government and not involved in any commercial undertakings { #clause-7-5 }

=== "Clause Text"
    > **7.5** For the purposes of RWA treatment, domestic PSEs in general include government authorities, administrative and/or statutory bodies responsible to the government, which may be owned, controlled, and/or mostly funded by the government and not involved in any commercial undertakings. 7.6Exposures to domestic PSEs will be risk-weighted based on the external rating of the Saudi sovereign external rating Risk weight table for PSEs Based on external rating of sovereign Table 2 External rating of the AAA to A+ to BBB+ to BB+ to Below Unrated sovereign AA– A– BBB– B– B– Risk weight 20% 50% 100% 100% 150% 100%
    >
    > | AAA to AA– | A+ to A– | BBB+ to BBB– | BB+ to B– | Below B– |
    > | --- | --- | --- | --- | --- |
    > | 20% | 50% | 100% | 100% | 150% |

=== "How it works"
    **Foreign PSE Treatment**

    Foreign PSEs (including GCC countries) are treated as **bank exposures**:
    
    - Apply **ECRA** if the PSE has an external rating → use Table 4 bank RWs
    - Apply **SCRA** if unrated → Grade A (40%), Grade B (75%), Grade C (150%)
    
    *Exception:* where a foreign supervisor allows sovereign treatment for its domestic PSEs,
    SAMA may permit the same treatment for Saudi banks' exposures to those PSEs.


---

### 7.7 Foreign PSEs, including PSEs in GCC countries, shall be assigned a risk weight based on the external rating of the PSE respective country’s sovereign rating { #clause-7-7 }

> **7.7** Foreign PSEs, including PSEs in GCC countries, shall be assigned a risk weight based on the external rating of the PSE respective country’s sovereign rating. Exposures to multilateral development banks (MDBs)

---
