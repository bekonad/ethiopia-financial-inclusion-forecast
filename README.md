<div align="center">

  <h1>📊 Ethiopia Financial Inclusion Forecasting</h1>

  <p>
    <strong>10 Academy – Artificial Intelligence Mastery</strong><br>
    <strong>Week 10 Challenge</strong> • Forecasting Ethiopia's Digital Financial Transformation
  </p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.10-3776AB?logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/Pandas-2.x-150458?logo=pandas&logoColor=white" alt="Pandas" />
    <img src="https://img.shields.io/badge/Streamlit-1.x-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit" />
    <img src="https://img.shields.io/badge/Status-Interim%20Complete-green" alt="Status" />
  </p>

  <p><strong>Date:</strong> 28 Jan 2026 – 03 Feb 2026<br>
  <strong>Location:</strong> Addis Ababa, Ethiopia<br>
  <strong>Author:</strong> Bereket Feleke</p>

</div>

## 🎯 Business Need & Challenge Overview

You are a Data Scientist at **Selam Analytics**, a fintech consulting firm specializing in emerging markets. A consortium (development finance institutions, mobile money operators, **National Bank of Ethiopia**) has engaged you to build a **financial inclusion forecasting system**.

Ethiopia is undergoing rapid digital transformation:
- **Telebirr**: >54 million users since 2021 launch
- **M-Pesa Ethiopia**: >10 million users since 2023
- Interoperable P2P digital transfers now **surpass ATM cash withdrawals** for the first time

Yet the **2024 Global Findex** shows only **49%** of adults (15+) have a financial account — just **+3pp** since 2021.

The consortium wants answers to:
- What drives financial inclusion in Ethiopia?
- How do events (product launches, policy changes, infrastructure investments) affect outcomes?
- How did rates change in 2025, and what will 2026–2027 look like?

**Core indicators** (World Bank Global Findex definitions):
1. **Access** — Account Ownership Rate (% adults with bank or mobile money account)
2. **Usage** — Digital Payment Adoption Rate (% adults making/receiving digital payments)

## 📈 Ethiopia's Historical Trajectory (Global Findex)

| Year  | Account Ownership | Change   | Notes                          |
|-------|-------------------|----------|--------------------------------|
| 2011  | 14%               | —        | Baseline                       |
| 2014  | 22%               | +8pp     |                                |
| 2017  | 35%               | +13pp    | Strong growth                  |
| 2021  | 46%               | +11pp    | Telebirr launch impact         |
| 2024  | 49%               | +3pp     | Slowdown despite mobile growth |

**2024 Usage indicators**:
- Mobile money account ownership: **9.45%**
- Made/received digital payment: **~21–35%**
- Used account to receive wages: **~15%**

## 🚀 Project Deliverables & Progress

| Task | Description                                      | Status     | Notebook / Deliverable                     |
|------|--------------------------------------------------|------------|--------------------------------------------|
| 1    | Data exploration & enrichment (Findex 2025, NDPS, IPS) | ✅ Done     | `notebooks/task1_enrichment.ipynb`         |
| 2    | Exploratory Data Analysis (trends, gaps, correlations) | ✅ Done     | `notebooks/task2_eda.ipynb` + insights     |
| 3    | Event Impact Modeling (association matrix)       | In Progress| `notebooks/task3_impact_modeling.ipynb`    |
| 4    | Forecasting Access & Usage 2025–2027             | —          | —                                          |
| 5    | Interactive Streamlit Dashboard                  | —          | `dashboard/app.py`                         |

**Unit Tests** — 100% pass (data loading, forecasting, pivot handling)  
**CI/CD** — GitHub Actions workflow (`unittests.yml`) running on push/PR

## 🛠️ Project Structure

ethiopia-financial-inclusion-forecast/
├── .github/workflows/         # CI: unittests.yml
├── data/
│   ├── raw/                   # Starter .xlsx + converted .csv
│   └── processed/             # Enriched CSV (Task 1)
├── notebooks/
│   ├── task1_enrichment.ipynb      # Load, explore, enrich
│   ├── task2_eda.ipynb             # Visuals, gaps, insights
│   └── task3_impact_modeling.ipynb # Event matrix (WIP)
├── reports/
│   ├── figures/               # All plots (trajectories, heatmaps, etc.)
│   └── key_insights.md        # 6+ documented insights
├── tests/                     # Pytest files
│   ├── test_data_loading.py
│   └── test_forecasting.py
├── dashboard/                 # Streamlit app (upcoming)
├── src/                       # Reusable code (future)
├── requirements.txt
├── README.md
└── data_enrichment_log.md
text## ⚡ Quick Start

1. Clone the repo:
   ```bash
   git clone https://github.com/bekonad/ethiopia-financial-inclusion-forecast.git
   cd ethiopia-financial-inclusion-forecast

Create & activate virtual environment (Windows):PowerShellpython -m venv .venv
.\.venv\Scripts\Activate.ps1
Install dependencies:PowerShellpython -m pip install --upgrade pip
pip install -r requirements.txt
Explore notebooks:PowerShelljupyter notebook notebooks/
Run unit tests:PowerShellpytest -v
Run dashboard (when ready):PowerShellstreamlit run dashboard/app.py

📊 Key Insights (from Task 2 EDA)

Growth slowdown — Account ownership +3pp only 2021–2024 despite mobile money surge
Gender gap persists — Women 42% vs Men 57% in 2024 (~15pp unchanged)
Active usage low — Mobile money registered ~19.4%, but active ~15% (big gap)
Digital payments lag — Only 21% adoption (P2P dominant, merchant acceptance weak)
Infrastructure leads — Mobile connections 68.4% & internet 21.7% correlate with access
Policy momentum — NDPS 2026-2030 & IPS launch (Dec 2025) expected to drive high usage boost

Full details → reports/key_insights.md
🛠️ Tools & Tech Stack

Python 3.10+
Data: Pandas, NumPy
Visualization: Matplotlib, Seaborn, Plotly
Modeling: Statsmodels (trend regression)
Dashboard: Streamlit
Testing: pytest
CI/CD: GitHub Actions

📄 License
MIT License (unless otherwise specified by 10 Academy)
Last updated: January 31, 2026