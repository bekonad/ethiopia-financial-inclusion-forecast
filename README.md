# 📊 Ethiopia Financial Inclusion Forecasting

**10 Academy – Artificial Intelligence Mastery**  
Week 10 Challenge • Forecasting Ethiopia's Digital Financial Transformation  
**Author:** Bereket Feleke  
**Challenge Period:** 28 January 2026 – 03 February 2026  
**Location:** Addis Ababa, Ethiopia

---

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-3776AB?logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Pandas-2.x-150458?logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/Streamlit-1.x-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit" />
  <img src="https://img.shields.io/badge/Tests-Passing-brightgreen" alt="Tests Passing" />
  <img src="https://img.shields.io/badge/Status-Interim%20Complete-green" alt="Status" />
</p>

---

## Table of Contents

- [Challenge Overview](#challenge-overview) 📋  
- [Historical Trajectory](#historical-trajectory) 📈  
- [Project Deliverables & Status](#project-deliverables--status) ✅  
- [Repository Structure](#repository-structure) 📁  
- [Setup & Execution Instructions](#setup--execution-instructions) ⚙️  
- [Key Insights from Exploratory Analysis](#key-insights-from-exploratory-analysis) 🔍  
- [Technology Stack](#technology-stack) 🛠️  
- [License](#license) 📜  

---

## Challenge Overview 📋

This repository contains the solution for the **Week 10 Challenge: Forecasting Financial Inclusion in Ethiopia** using time series and exploratory data analysis techniques.  

Ethiopia is experiencing rapid digital financial transformation:

- Telebirr: >54 million users since 2021 launch 🚀  
- M-Pesa Ethiopia: >10 million users since 2023 📱  
- Interoperable P2P digital transfers now surpass ATM cash withdrawals 🔄  

Despite this growth, the **2024 Global Findex** reports **49% of adults** (aged 15+) have a financial account — a modest **+3 percentage points** increase since 2021.  

The project aims to:

- Identify drivers of financial inclusion in Ethiopia  
- Assess event impacts (product launches, policies, infrastructure)  
- Forecast 2025–2027 account ownership and digital usage trends  

**Core indicators (Global Findex):**  

1. **Access** – Account Ownership Rate (% adults with bank or mobile money account)  
2. **Usage** – Digital Payment Adoption Rate (% adults making/receiving digital payments)  

---

## Historical Trajectory 📈

| Year  | Account Ownership | Change | Notes                          |
|-------|-----------------|--------|--------------------------------|
| 2011  | 14%              | —      | Baseline                       |
| 2014  | 22%              | +8pp   | Early growth                   |
| 2017  | 35%              | +13pp  | Strong acceleration            |
| 2021  | 46%              | +11pp  | Telebirr launch impact         |
| 2024  | 49%              | +3pp   | Noticeable slowdown            |

**2024 Usage Indicators:**  

- Mobile money account ownership: **9.45%** 📱  
- Made/received digital payment: **~21–35%** 💳  
- Wages received via account: **~15%** 💼  

---

## Project Deliverables & Status ✅

| Task | Description                                      | Status     | Notebook / Output                          |
|------|--------------------------------------------------|------------|--------------------------------------------|
| 1    | Data exploration & enrichment                    | Complete   | `notebooks/task1_enrichment.ipynb`         |
| 2    | Exploratory Data Analysis (trends, gaps, correlations) | Complete   | `notebooks/task2_eda.ipynb`                |
| 3    | Event Impact Modeling (association matrix)       | In Progress| `notebooks/task3_impact_modeling.ipynb`    |
| 4    | Forecasting Access & Usage 2025–2027             | Planned    | —                                          |
| 5    | Interactive Streamlit Dashboard                  | Planned    | `dashboard/app.py`                         |

**Unit Tests:** 11 tests passing  
**Continuous Integration:** GitHub Actions workflow (`unittests.yml`) runs pytest on push/PR  

---

## Repository Structure 📁

```text
ethiopia-financial-inclusion-forecast/
├── .github/
│   └── workflows/unittests.yml           # CI pipeline
├── data/
│   ├── raw/                             # Original .xlsx files + converted .csv
│   └── processed/                       # Enriched dataset (Task 1 output)
├── notebooks/
│   ├── task1_enrichment.ipynb           # Data loading, exploration, enrichment
│   ├── task2_eda.ipynb                  # Visualizations, trends, gaps, insights
│   └── task3_impact_modeling.ipynb      # Event impact association matrix
├── reports/
│   ├── figures/                         # Plots (trajectories, heatmaps, timelines)
│   └── key_insights.md                  # Documented insights from EDA
├── tests/
│   ├── test_data_loading.py             # Schema and data validation
│   └── test_forecasting.py              # Forecast logic & unit tests
├── dashboard/                           # Streamlit app (Task 5)
├── src/                                 # Reusable modules
├── requirements.txt                     # Python dependencies
├── README.md                            # Project documentation
└── data_enrichment_log.md               # Record of data additions & sources
````

---

## Setup & Execution Instructions ⚙️

**Clone the repository:**

```bash
git clone https://github.com/bekonad/ethiopia-financial-inclusion-forecast.git
cd ethiopia-financial-inclusion-forecast
```

**Create & activate virtual environment (Windows / PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Install dependencies:**

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

**Launch Jupyter notebooks:**

```powershell
jupyter notebook notebooks/
```

**Run unit tests:**

```powershell
pytest -v
```

**Launch dashboard (planned):**

```powershell
streamlit run dashboard/app.py
```

---

## Key Insights from Exploratory Analysis 🔍

1. **Growth slowdown:** Account ownership rose only **+3pp** (2021–2024) despite mobile money expansion
2. **Persistent gender gap:** Women at 42% vs men at 57% in 2024 (~15pp gap)
3. **Active usage bottleneck:** Mobile money registered ~19.4%, but active usage remains ~15%
4. **Digital payments lag:** Only 21% adoption; P2P dominant, merchant acceptance limited
5. **Infrastructure as driver:** Mobile connections 68.4%, Internet 21.7% — strong correlation with access
6. **Policy potential:** NDPS 2026–2030 & IPS/Ethiopay launches (Dec 2025) expected to accelerate usage

Full documentation → `reports/key_insights.md`

---

## Technology Stack 🛠️

* **Language:** Python 3.10+
* **Data Processing:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn, Plotly
* **Modeling:** Statsmodels
* **Dashboard:** Streamlit
* **Testing & CI:** pytest + GitHub Actions

---

## License 📜

MIT License (unless otherwise specified by 10 Academy)

**Last updated:** 31 January 2026

```  

Do you want me to do that next?
```
