<div align="center">

  <h1>📈 Ethiopia Financial Inclusion Forecasting</h1>

  <p>
    <strong>My Week 10 Challenge Project – 10 Academy AI Mastery</strong><br>
    Forecasting Ethiopia's Digital Financial Transformation using Time Series Methods
  </p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.10-3776AB?logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/Pandas-2.x-150458?logo=pandas&logoColor=white" alt="Pandas" />
    <img src="https://img.shields.io/badge/Streamlit-1.x-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit" />
    <img src="https://img.shields.io/badge/Tests-Passing-brightgreen" alt="Tests Passing" />
    <img src="https://img.shields.io/badge/Status-Interim%20Complete-green" alt="Status" />
  </p>

  <p><strong>Author:</strong> Bereket Feleke</p>
  <p><strong>Location:</strong> Addis Ababa, Ethiopia</p>
  <p><strong>Challenge Dates:</strong> 28 Jan 2026 – 03 Feb 2026</p>

</div>

## 🎯 Project Overview – Why I Built This

I am a Data Scientist participating in the **10 Academy Week 10 Challenge**.  
I built this forecasting system to answer real questions from a consortium (development finance institutions, mobile money operators, **National Bank of Ethiopia**):

- What drives financial inclusion in Ethiopia?
- How do major events (product launches like Telebirr/M-Pesa, policies like NDPS, infrastructure investments) impact access and usage?
- How did rates change in 2025, and what will 2026–2027 look like?

Despite rapid growth (Telebirr >54M users since 2021, M-Pesa >10M since 2023, P2P transfers surpassing ATM withdrawals), the **2024 Global Findex** shows only **49%** account ownership (+3pp since 2021) — progress is slowing.  
My goal: build a reproducible system to forecast **Access** (account ownership) and **Usage** (digital payments) for 2025–2027.

## 📊 Ethiopia's Historical Trajectory (Global Findex)

| Year  | Account Ownership | Change   | Notes                          |
|-------|-------------------|----------|--------------------------------|
| 2011  | 14%               | —        | Baseline                       |
| 2014  | 22%               | +8pp     | Early growth                   |
| 2017  | 35%               | +13pp    | Strong acceleration            |
| 2021  | 46%               | +11pp    | Telebirr launch impact         |
| 2024  | 49%               | +3pp     | Noticeable slowdown            |

**2024 Usage highlights**:
- Mobile money account ownership: **9.45%**
- Digital payments (made/received): **~21–35%**
- Wages received via account: **~15%**

## 🛠️ What I Delivered in This Repo

| Task | What I Did                                       | Status     | Notebook / Output                          |
|------|--------------------------------------------------|------------|--------------------------------------------|
| 1    | Loaded, explored & enriched data (Findex 2025, NDPS/IPS 2025, penetration metrics) | ✅ Done     | `task1_enrichment.ipynb` + enriched CSV    |
| 2    | EDA: trends, gender gaps, event timeline, correlations, 6 key insights | ✅ Done     | `task2_eda.ipynb` + figures + insights.md  |
| 3    | Event impact modeling (association matrix, magnitude/lag) | In Progress| `task3_impact_modeling.ipynb`              |
| 4    | Forecasting Access & Usage 2025–2027 (baseline + scenarios) | —          | —                                          |
| 5    | Interactive Streamlit dashboard                  | —          | `dashboard/app.py` (planned)               |

**Unit Tests** → 11/11 passing (data loading, forecasting, pivot handling)  
**CI** → GitHub Actions auto-runs tests on push/PR

## 📁 Repository Structure
ethiopia-financial-inclusion-forecast/
├── .github/workflows/         # CI: unittests.yml
├── data/
│   ├── raw/                   # Starter .xlsx + converted .csv
│   └── processed/             # My enriched CSV
├── notebooks/
│   ├── task1_enrichment.ipynb      # Data prep & 2025 enrichment
│   ├── task2_eda.ipynb             # Visuals & insights
│   └── task3_impact_modeling.ipynb # Event matrix (in progress)
├── reports/
│   ├── figures/               # Plots (trajectories, heatmaps, timeline)
│   └── key_insights.md        # My 6 documented insights
├── tests/                     # Pytest files
│   ├── test_data_loading.py
│   └── test_forecasting.py
├── dashboard/                 # Streamlit app (coming soon)
├── src/                       # Reusable code (future)
├── requirements.txt
├── README.md                  # This file
└── data_enrichment_log.md     # My enrichment notes
text## ⚡ How to Run My Project

1. Clone my repo:
   ```bash
   git clone https://github.com/bekonad/ethiopia-financial-inclusion-forecast.git
   cd ethiopia-financial-inclusion-forecast

Create & activate virtual environment (Windows):PowerShellpython -m venv .venv
.\.venv\Scripts\Activate.ps1
Install dependencies:PowerShellpython -m pip install --upgrade pip
pip install -r requirements.txt
Explore my notebooks:PowerShelljupyter notebook notebooks/
Run unit tests:PowerShellpytest -v
(Future) Launch dashboard:PowerShellstreamlit run dashboard/app.py

📌 My Key Insights (from Task 2 EDA)

Growth is slowing — Account ownership only +3pp (2021–2024) despite mobile money surge
Gender gap remains stubborn — Women 42% vs Men 57% in 2024 (~15pp gap unchanged)
Active usage is the bottleneck — Mobile money registered ~19.4%, but active ~15%
Digital payments lag behind access — Only 21% adoption (P2P dominant, merchant weak)
Infrastructure is a leading driver — Mobile connections 68.4% & internet 21.7% correlate strongly
Recent policies matter — NDPS 2026-2030 & IPS/Ethiopay (Dec 2025) expected to drive high usage boost

Full details → reports/key_insights.md
🛠️ Tech Stack I Used

Language: Python 3.10+
Core: Pandas, NumPy
Visualization: Matplotlib, Seaborn, Plotly
Modeling: Statsmodels
Dashboard: Streamlit (in progress)
Testing: pytest + GitHub Actions CI

📄 License
MIT License (unless restricted by 10 Academy rules)
Last updated: January 31, 2026