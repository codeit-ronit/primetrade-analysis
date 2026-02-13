# 📊 Hyperliquid Behavioral & Sentiment Analytics  
### Primetrade.ai – Data Science Intern Assignment

[![Streamlit App](https://img.shields.io/badge/Live-Dashboard-brightgreen)](https://primetradeanalysis.streamlit.app/)

---

## 🧠 Project Overview

This project investigates how **market sentiment (Fear vs. Greed)** influences trader behavior, profitability, and risk dynamics on Hyperliquid.

The objective was not only to analyze performance shifts across emotional regimes but also to:

- Engineer reproducible research pipelines  
- Develop regime-aware execution strategies  
- Build predictive volatility models  
- Identify trader archetypes using clustering  
- Deliver an interactive dashboard for protocol-level insights  

This submission combines **behavioral finance, quantitative research, machine learning, and product thinking**.

---

# 📂 Folder Structure
```
PRIMETRADE_ASSIGNMENT_HYPERLIQUID/

data/ → Raw datasets
fear_greed_index.csv
historical_data.csv

notebooks/
main_analysis.ipynb → Full research notebook

outputs/
figures/ → Exported visualizations
tables/ → Processed & engineered datasets

app.py → Streamlit dashboard
README.md
requirements.txt
.gitignore
```

---

# 🔁 Reproducibility Framework

This project was built with full reproducibility in mind.

### ✔ Virtual Environment
- Isolated environment using `venv`
- All dependencies frozen in `requirements.txt`

### ✔ Clean Data Pipeline
- Raw data stored separately in `/data`
- Processed datasets exported to `/outputs/tables`
- All visualizations exported to `/outputs/figures`
- Dashboard reads from processed outputs (not raw data)

### ✔ Deterministic Modeling
- Fixed random seeds in ML models
- Time-aware split used for predictive modeling
- Class balancing enabled for volatility prediction

---

# 🧮 Part A — Data Preparation & Feature Engineering

## Objectives

- Clean and validate datasets
- Align trade timestamps with daily sentiment
- Engineer behavioral metrics
- Avoid look-ahead bias

## Key Steps

1. Timestamp normalization (daily granularity)
2. Many-to-one merge with sentiment index
3. Validation checks for missing sentiment rows
4. Account-level daily aggregation

### Engineered Features

- Daily PnL
- Daily trading volume
- Trade count
- Average trade size
- Long/Short ratio
- Win rate
- Market activity metrics

All engineered tables were exported for reproducibility.

---

# 📈 Part B — Behavioral & Regime Analysis

## Core Question

Does trader performance shift across sentiment regimes?

## Metrics Used

- Average PnL
- Win rate
- PnL volatility (risk proxy)
- Volume intensity
- Long/Short bias

## Key Findings

- Capital efficiency is ~3.4× higher during Extreme Greed
- Extreme Fear produces highest volume but lowest efficiency
- Fear regimes amplify liquidation risk
- Greed regimes maximize capital productivity

These findings led to regime-aware strategy design.

---

# 🎯 Part C — Regime-Aware Trading Framework

Instead of treating sentiment as emotional context, we modeled it as a **market microstructure regime variable**.

## Strategy 1 — Capital Scaling in Extreme Greed

When Fear & Greed Index > 75:
- Increase position size by 20–30%
- Avoid increasing trade frequency
- Favor trend-aligned setups

Rationale:
Greed regimes exhibit higher capital efficiency and directional persistence.

---

## Strategy 2 — Volatility Defense in Extreme Fear

When Fear & Greed Index < 25:
- Reduce leverage by ~40–50%
- Shift to limit-based execution
- Focus on mean-reversion & spread capture

Rationale:
Fear regimes are liquidity-driven and prone to liquidation cascades.

---

# 🤖 Bonus Part 1 — Predictive Volatility Modeling

## Objective

Predict next-day absolute PnL volatility bucket using:

- Behavioral metrics
- Sentiment value
- Activity patterns

## Model

- Random Forest Classifier
- Balanced class weighting
- Time-based train-test split (no temporal leakage)

## Performance

- Accuracy ≈ 50%
- Baseline (3-class random) ≈ 33%
- ~17% absolute improvement over baseline

## Feature Importance Insights

Top predictive features:
1. Average trade size
2. Same-day PnL
3. Trade frequency

Behavioral momentum and capital intensity are leading indicators of next-day risk.

---

# 🧩 Bonus Part 2 — Trader Archetype Clustering

## Objective

Identify organic trader "DNA" using unsupervised learning.

## Features Used

- Activity
- Average trade size
- Total PnL
- PnL volatility
- Win rate

## Methodology

- RobustScaler (handles fat-tailed distributions)
- KMeans clustering
- Log scaling on activity

## Identified Archetypes

1. High-Frequency Scalper
2. Institutional Whale
3. Disciplined Strategist
4. High-Variance Retailer

## Business Application

| Archetype | Strategic Action | Business Impact |
|-----------|------------------|-----------------|
| Scalper | Maker rebate tiers | Deepens order book |
| Whale | VIP liquidity programs | Reduces capital churn |
| Strategist | Performance incentives | Sustains ecosystem |
| Retailer | Dynamic risk guardrails | Protects insurance fund |

---

# 📊 Interactive Dashboard

A production-style Streamlit dashboard was built to:

- Filter by sentiment regime
- View capital efficiency metrics
- Visualize behavioral clusters
- Analyze protocol revenue trends
  
# How to run 

## 📦 1. Clone the Repository

```bash
git clone <repo_url>
cd PRIMETRADE_ASSIGNMENT_HYPERLIQUID
```

## 🐍 2. Create & Activate Virtual Environment

for macOS / Linux
```bash
python -m venv venv
source venv/bin/activate
```

for Windows
```bash
python -m venv venv
source venv/bin/activate
```

## 📥 3. Install Dependencies
All required libraries are listed in requirements.txt.
```bash
pip install -r requirements.txt
```

## ▶️ Running the Project Locally

You can run either:
•⁠  ⁠The Jupyter Notebook (research workflow)
•⁠  ⁠The StreamlitDashboard (interactive app)

## 📊 Run the Streamlit Dashboard

Make sure your virtual environment is activated, then run:

```bash
streamlit run app.py
```

```bash
http://localhost:8501
```
