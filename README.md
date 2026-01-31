<div align="center">

  <h1>📊 Ethiopia Financial Inclusion Forecasting</h1>

  <p>
    <strong>10 Academy – Artificial Intelligence Mastery</strong><br>
    Week 10 Challenge • Forecasting Ethiopia's Digital Financial Transformation
  </p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.10-3776AB?logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/Pandas-2.x-150458?logo=pandas&logoColor=white" alt="Pandas" />
    <img src="https://img.shields.io/badge/Streamlit-1.x-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit" />
    <img src="https://img.shields.io/badge/Tests-Passing-brightgreen" alt="Tests Passing" />
    <img src="https://img.shields.io/badge/Status-Interim%20Complete-green" alt="Status" />
  </p>

  <p>
    Challenge Period: 28 January 2026 – 03 February 2026<br>
    Location: Addis Ababa, Ethiopia
    Author: Bereket Feleke
  </p>

</div>

## Table of Contents

- [Challenge Overview](#challenge-overview) 📋
- [Historical Trajectory](#historical-trajectory) 📈
- [Project Deliverables & Status](#project-deliverables--status) ✅
- [Repository Structure](#repository-structure) 📁
- [Setup & Execution Instructions](#setup--execution-instructions) ⚙️
- [Key Insights from Exploratory Analysis](#key-insights-from-exploratory-analysis) 🔍
- [Technology Stack](#technology-stack) 🛠️
- [License](#license) 📜

## Challenge Overview 📋

This repository contains the solution for the Week 10 Challenge:  
**Forecasting Financial Inclusion in Ethiopia** using time series methods.

Ethiopia is undergoing rapid digital financial transformation:
- Telebirr: >54 million users since 2021 launch 🚀
- M-Pesa Ethiopia: >10 million users since 2023 📱
- Interoperable P2P digital transfers now surpass ATM cash withdrawals 🔄

Despite these advancements, the **2024 Global Findex** reports only **49%** of adults (aged 15+) have a financial account — an increase of **+3 percentage points** since 2021.

The consortium (development finance institutions, mobile money operators, National Bank of Ethiopia) requires a forecasting system to address:
- Drivers of financial inclusion in Ethiopia
- Impact of events (product launches, policy changes, infrastructure investments) on outcomes
- Changes in 2025 and projections for 2026–2027

**Core indicators** (World Bank Global Findex definitions):
1. **Access** — Account Ownership Rate (% adults with bank or mobile money account)
2. **Usage** — Digital Payment Adoption Rate (% adults making/receiving digital payments)

## Historical Trajectory 📈

| Year  | Account Ownership | Change   | Notes                          |
|-------|-------------------|----------|--------------------------------|
| 2011  | 14%               | —        | Baseline                       |
| 2014  | 22%               | +8pp     | Early growth                   |
| 2017  | 35%               | +13pp    | Strong acceleration            |
| 2021  | 46%               | +11pp    | Telebirr launch impact         |
| 2024  | 49%               | +3pp     | Noticeable slowdown            |

**2024 Usage indicators**:
- Mobile money account ownership: **9.45%** 📱
- Made/received digital payment: **~21–35%** 💳
- Wages received via account: **~15%** 💼

## Project Deliverables & Status ✅

| Task | Description                                      | Status     | Notebook / Output                          |
|------|--------------------------------------------------|------------|--------------------------------------------|
| 1    | Data exploration & enrichment                    | Complete   | `notebooks/task1_enrichment.ipynb`         |
| 2    | Exploratory Data Analysis (trends, gaps, correlations) | Complete   | `notebooks/task2_eda.ipynb`                |
| 3    | Event Impact Modeling (association matrix)       | In Progress| `notebooks/task3_impact_modeling.ipynb`    |
| 4    | Forecasting Access & Usage 2025–2027             | Planned    | —                                          |
| 5    | Interactive Streamlit Dashboard                  | Planned    | `dashboard/app.py`                         |

**Unit Tests** — 11 tests passing  
**Continuous Integration** — GitHub Actions workflow (`unittests.yml`) executes pytest on push/PR

## Repository Structure 📁

```text
ethiopia-financial-inclusion-forecast/
├── .github/
│   └── workflows/
│       └── unittests.yml                # Continuous integration pipeline
├── data/
│   ├── raw/                             # Original .xlsx files + converted .csv
│   └── processed/                       # Enriched dataset (Task 1 output)
├── notebooks/
│   ├── task1_enrichment.ipynb           # Data loading, exploration, enrichment
│   ├── task2_eda.ipynb                  # Visualizations, trends, gaps, insights
│   └── task3_impact_modeling.ipynb      # Event impact association matrix
├── reports/
│   ├── figures/                         # Generated plots (trajectories, heatmaps, timelines)
│   └── key_insights.md                  # Documented insights from EDA
├── tests/
│   ├── test_data_loading.py             # Tests for data loading & schema validation
│   └── test_forecasting.py              # Tests for modeling & aggregation logic
├── dashboard/                           # Streamlit application (planned)
├── src/                                 # Reusable modules (future)
├── requirements.txt                     # Project dependencies
├── README.md                            # This document
└── data_enrichment_log.md               # Record of data additions & sources
Setup & Execution Instructions ⚙️

Clone the repositoryBashgit clone https://github.com/bekonad/ethiopia-financial-inclusion-forecast.git
cd ethiopia-financial-inclusion-forecast
Create and activate virtual environment (Windows/PowerShell)PowerShellpython -m venv .venv
.\.venv\Scripts\Activate.ps1
Install dependenciesPowerShellpython -m pip install --upgrade pip
pip install -r requirements.txt
Launch Jupyter notebooksPowerShelljupyter notebook notebooks/
Execute unit testsPowerShellpytest -v
(Future) Launch dashboardPowerShellstreamlit run dashboard/app.py

Key Insights from Exploratory Analysis (Task 2) 🔍

Growth slowdown — account ownership increased only +3 percentage points (2021–2024) despite mobile money expansion
Persistent gender gap — women at 42% vs men at 57% in 2024 (~15 percentage point gap unchanged)
Active usage bottleneck — mobile money registered ~19.4%, but active usage remains ~15%
Digital payments lag — only 21% adoption (P2P dominant, merchant acceptance limited)
Infrastructure as driver — mobile connections at 68.4% and internet at 21.7% correlate strongly with access
Policy potential — NDPS 2026-2030 and IPS/Ethiopay launches (December 2025) expected to accelerate usage

Full documentation → reports/key_insights.md
Technology Stack 🛠️

Language: Python 3.10+
Data processing: Pandas, NumPy
Visualization: Matplotlib, Seaborn, Plotly
Modeling: Statsmodels
Dashboard: Streamlit (planned)
Testing & CI: pytest + GitHub Actions

License 📜
MIT License (unless otherwise specified by 10 Academy)
Last updated: 31 January 2026