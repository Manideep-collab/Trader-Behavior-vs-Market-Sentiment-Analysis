# 📊 Trader Behavior vs Market Sentiment Analysis

**Primetrade.ai – Junior Data Scientist Assignment**

---

## 📌 Overview
This project analyzes how Bitcoin market sentiment (Fear vs Greed) influences trader behavior and performance on Hyperliquid.

### Objective
- Examine profitability differences across sentiment regimes
- Analyze behavioral shifts in trade frequency and risk exposure
- Segment traders into behavioral archetypes
- Develop actionable regime-aware strategy recommendations
- Explore predictive modeling of next-day profitability
- Build an interactive dashboard for insight exploration

This assignment demonstrates a full data science workflow: cleaning, statistical analysis, modeling, segmentation, and deployment.

## 🗂 Repository Structure
```
Trader-Behavior-vs-Market-Sentiment-Analysis/
│
├── PrimeTrade.ipynb          # Main analysis notebook
├── Summary.md                # Executive summary of findings
├── app.py                    # Streamlit interactive dashboard
├── requirements.txt          # Python dependencies
├── .gitignore                # Ignored datasets & cache files
└── Data Science Intern project.pdf  # Assignment brief
```

⚠️ Raw datasets are excluded from the repository.

## 📊 Data Sources
- **Fear & Greed Index** – Daily sentiment classification and score
- **Historical Trade Data** – Trade-level records with:
  - Account
  - Trade size
  - Closed PnL
  - Direction (Long/Short)
  - Timestamp

## 🔍 Methodology
1️⃣ **Data Cleaning & Preparation**
- Removed invalid trade sizes
- Capped extreme outliers at 99th percentile
- Converted timestamps to daily resolution
- Aggregated trade-level data to daily trader metrics

**Features constructed:**
- Daily PnL
- Trade count
- Daily volume
- Average trade size
- Win rate
- Long ratio

Merged with sentiment data for regime-based analysis.

2️⃣ **Regime-Based Analysis**
Compared performance across Fear, Greed, and Neutral regimes using mean/median, volatility, and Mann–Whitney U test (non-parametric).

3️⃣ **Trader Segmentation**
Segmented traders by activity level and behavioral metrics; applied KMeans clustering to identify archetypes.

4️⃣ **Predictive Modeling (Bonus)**
Built a Logistic Regression model to predict next-day profitability.

- Accuracy: 66.5%
- ROC-AUC: 0.64

Findings: sentiment provides modest signal; returns remain noisy.

5️⃣ **Interactive Dashboard (Streamlit)**
Lightweight app lets users:
- Filter by sentiment regime
- Compare activity segments
- View PnL distributions
- Explore cluster summaries
- Review model performance

## 🚀 How to Run This Project
1️⃣ Clone repository
```bash
git clone https://github.com/Manideep-collab/Trader-Behavior-vs-Market-Sentiment-Analysis.git
cd Trader-Behavior-vs-Market-Sentiment-Analysis
```

2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

3️⃣ Run notebook
```bash
jupyter notebook PrimeTrade.ipynb
```

4️⃣ Launch dashboard
```bash
streamlit run app.py
```

## 📈 Key Insights
- Fear regimes exhibit higher volatility and trading intensity
- Greed regimes show slightly more stable median profitability
- Activity level amplifies sentiment sensitivity
- High-risk traders exhibit extreme volatility dispersion
- Risk management is more actionable than directional prediction

## 🧠 Strategic Recommendations
- Reduce leverage and tighten risk controls during Fear regimes
- Maintain stable exposure during Greed regimes
- Apply segment-specific risk limits

## 🛠 Technologies Used
- Python
- Pandas
- NumPy
- Seaborn & Matplotlib
- Scikit-learn
- Streamlit

## 📬 Author
**Manideep Palnati**  
Junior Data Science Candidate
