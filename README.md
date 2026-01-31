# Ethiopia Financial Inclusion Forecasting

**10 Academy – Artificial Intelligence Mastery**  
**Week 10 Challenge**  
**Forecasting Financial Inclusion in Ethiopia**  
Build a forecasting system that tracks Ethiopia's digital financial transformation using time series methods.

**Date:** 28 Jan 2026 – 03 Feb 2026  
**Prepared by:** Bereket Feleke 
**Location:** Addis Ababa, Ethiopia

## Overview & Business Need

Ethiopia is experiencing rapid digital financial growth:  
- Telebirr: >54 million users since 2021 launch  
- M-Pesa Ethiopia: >10 million users since 2023  
- Interoperable P2P digital transfers now surpass ATM cash withdrawals  

Yet the **2024 Global Findex** shows only **49%** of adults (15+) have a financial account (+3pp since 2021) — progress is slowing despite infrastructure and product launches.

A consortium (development finance institutions, mobile money operators, National Bank of Ethiopia) engaged **Selam Analytics** to answer:  
- What drives financial inclusion in Ethiopia?  
- How do events (product launches, policy changes, infrastructure investments) affect inclusion outcomes?  
- How did rates change in 2025, and what will 2026–2027 look like?

**Core indicators** (World Bank Global Findex definitions):  
1. **Access** – Account Ownership Rate (% adults with bank/mobile money account)  
2. **Usage** – Digital Payment Adoption Rate (% adults making/receiving digital payments)

## Global Findex Trajectory (Ethiopia)

| Year  | Account Ownership | Change  |
|-------|-------------------|---------|
| 2011  | 14%               | —       |
| 2014  | 22%               | +8pp    |
| 2017  | 35%               | +13pp   |
| 2021  | 46%               | +11pp   |
| 2024  | 49%               | +3pp    |

**2024 Usage indicators**:
- Mobile money account ownership: 9.45%
- Made/received digital payment: ~21–35%
- Used account to receive wages: ~15%

## Project Deliverables

1. Enrich and understand the unified financial inclusion dataset  
2. Perform exploratory data analysis (trends, gaps, correlations)  
3. Model event impacts (association matrix, magnitude/lag estimates)  
4. Forecast Access & Usage for 2025–2027 (baseline + scenarios)  
5. Build interactive Streamlit dashboard  

## Repository Structure
ethiopia-financial-inclusion-forecast/
├── .github/workflows/         # CI: unittests.yml
├── data/
│   ├── raw/                   # Starter data (.xlsx → .csv)
│   └── processed/             # Enriched CSV
├── notebooks/
│   ├── task1_enrichment.ipynb      # Task 1: Load, explore, enrich
│   ├── task2_eda.ipynb             # Task 2: Visualizations & insights
│   └── task3_impact_modeling.ipynb # Task 3: Event impact matrix
├── reports/
│   ├── figures/               # Plots (trajectories, heatmaps, etc.)
│   └── key_insights.md        # 6+ documented insights
├── tests/                     # Unit tests (pytest)
│   ├── test_data_loading.py
│   └── test_forecasting.py
├── dashboard/                 # Task 5: Streamlit app (in progress)
├── src/                       # Future reusable modules
├── requirements.txt
├── README.md
└── data_enrichment_log.md
text## Setup Instructions

1. Clone the repo:
   ```bash
   git clone https://github.com/bekonad/ethiopia-financial-inclusion-forecast.git
   cd ethiopia-financial-inclusion-forecast

Create & activate virtual environment (Windows/PowerShell):PowerShellpython -m venv .venv
.\.venv\Scripts\Activate.ps1
Install dependencies:PowerShellpython -m pip install --upgrade pip
pip install -r requirements.txt
Run notebooks:PowerShelljupyter notebook notebooks/
Run dashboard (when ready):PowerShellstreamlit run dashboard/app.py
Run unit tests:PowerShellpytest -v

Current Progress (as of 31 Jan 2026)

 Task 1: Data loading, exploration, enrichment (Findex 2025, NDPS Dec 2025, IPS launch) → PR #1
 Task 2: EDA notebook (trends, gaps, event timeline, correlations, 6 insights) → PR #2
 Task 3: Event impact modeling (matrix, magnitude/lag)
 Task 4: Forecasting 2025–2027 (baseline, optimistic/pessimistic scenarios)
 Task 5: Interactive Streamlit dashboard
 Unit tests (data loading + forecasting)
 GitHub Actions CI (unittests.yml)

Key Insights (from Task 2)

Slowdown in access — +3pp only 2021–2024 despite mobile money growth
Persistent gender gap — ~15pp (women 42% vs men 57% in 2024)
Mobile money vs active usage — Registered up to ~19.4%, but active remains low (~15%)
Digital payments lag — Only 21% adoption in 2024 (P2P dominant)
Infrastructure leads — Mobile 68.4% & internet 21.7% in late 2025 correlate with access
Policy events matter — NDPS/IPS (Dec 2025) expected to drive high usage impact

Full details: reports/key_insights.md
License
MIT License (unless otherwise specified by 10 Academy)

Last updated: January 31, 2026