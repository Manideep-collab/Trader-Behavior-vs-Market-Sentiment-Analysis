# Trader Behavior vs Market Sentiment Analysis

## Primetrade.ai – Data Science Intern Assignment

### 1. Objective

This project investigates how Bitcoin market sentiment (Fear vs Greed) influences trader behavior, performance, and risk exposure on Hyperliquid.

The goal is to:

1. Evaluate regime-dependent performance differences
2. Identify behavioral shifts across sentiment regimes
3. Segment traders into behavioral archetypes
4. Propose actionable strategy adjustments
5. Explore predictive modeling potential

### 2. Methodology

**Data Preparation**

- Cleaned ~211k trade-level records
- Removed invalid trade sizes (0.02% of dataset)
- Winsorized extreme trade sizes at the 99th percentile
- Aggregated trade-level data to daily trader metrics
- Merged with daily Fear & Greed Index data

**Daily features constructed:**

- Daily PnL
- Trade count
- Trading volume
- Average trade size
- Win rate
- Directional bias

Sentiment was consolidated into binary regimes (Fear vs Greed) for hypothesis testing.

### 3. Key Findings

1️ **Profitability Differences Are Modest**

- Mean PnL is slightly higher in Fear regimes.
- Median PnL and win rate are slightly higher in Greed regimes.
- Mann–Whitney test (p ≈ 0.055) suggests borderline statistical significance.

**Conclusion:**
Performance differences exist but are not strongly statistically significant.

2️ **Volatility Is Regime-Dependent**

- Fear regimes exhibit the highest PnL volatility.
- Greed regimes show lower dispersion.
- Neutral markets are the most stable.

**Conclusion:**
Sentiment influences risk dispersion more strongly than central profitability.

3️ **Behavioral Shift in Fear Regimes**

- Trade frequency increases significantly during Fear periods.
- Traders appear more reactive in high-uncertainty environments.

**Conclusion:**
Fear amplifies trading intensity and outcome variability.

4️ **Activity Level Amplifies Sentiment Sensitivity**

Segmenting traders by activity revealed:

- High Activity traders show greater volatility sensitivity in Fear regimes.
- Low Activity traders remain comparatively more stable.

**Conclusion:**
Sentiment sensitivity is heterogeneous across trader types.

### 4. Predictive Modeling (Bonus)

A logistic regression model was trained to predict next-day profitability using behavioral and sentiment features.

**Model Performance:**

- Accuracy: 66.5%
- ROC-AUC: 0.64

**Findings:**

- The model shows modest predictive power.
- Stronger recall for profitable days than loss days.
- Sentiment contributes signal, but financial returns remain noisy.

**Conclusion:**
Sentiment-aware risk management may be more practical than short-term return prediction.

### 5. Trader Clustering (Bonus)

Unsupervised KMeans clustering identified three behavioral archetypes:

- **Cluster 0 – Active & Controlled Traders**
  - High frequency
  - Moderate volatility
  - Highest win rate
  - Disciplined risk management

- **Cluster 1 – Lower Activity, Lower Precision**
  - Lower frequency
  - Lower win rate
  - Elevated volatility relative to activity

- **Cluster 2 – High-Risk, High-Return Traders**
  - Very high PnL
  - Extremely high volatility
  - Largest position sizes

**Conclusion:**
Trader behavior is highly heterogeneous. Risk exposure varies more dramatically than average profitability.

### 6. Strategy Recommendations

🔹 **1. Dynamic Risk Reduction During Fear**

Reduce leverage and tighten controls in high-volatility sentiment regimes.

🔹 **2. Stable Exposure During Greed**

Greed regimes show more consistent median profitability and lower volatility.

🔹 **3. Segment-Specific Risk Controls**

High Activity traders require stricter regime-aware limits.

### 7. Interactive Dashboard (Streamlit)

A lightweight Streamlit application was built to:

- Filter by regime and trader segment
- Visualize PnL distributions
- Explore cluster summaries
- View model performance

This demonstrates the ability to operationalize analytical insights into an interactive decision-support tool.

### Final Conclusion

The strongest signal in this study is not raw directional profitability but volatility amplification under sentiment extremes.

Market sentiment primarily influences risk dispersion and trader behavior rather than consistent return predictability.

Dynamic, sentiment-aware risk management — particularly segment-specific controls — emerges as the most actionable insight.