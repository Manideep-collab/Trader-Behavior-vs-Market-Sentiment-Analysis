import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Trader Behavior Dashboard", layout="wide")

# Load Data
@st.cache_data
def load_data():
    merged = pd.read_csv("merged_data.csv")
    traders = pd.read_csv("trader_summary.csv")
    return merged, traders

merged_data, trader_summary = load_data()

# Title
st.title("📊 Trader Behavior vs Market Sentiment")
st.markdown("Interactive exploration of regime-based trader performance and behavioral segmentation.")

# Sidebar Filters

st.sidebar.header("Filters")

selected_regime = st.sidebar.selectbox(
    "Select Market Regime",
    options=merged_data['regime'].unique()
)

selected_segment = st.sidebar.selectbox(
    "Select Activity Segment",
    options=merged_data['activity_segment'].unique()
)

filtered_data = merged_data[
    (merged_data['regime'] == selected_regime) &
    (merged_data['activity_segment'] == selected_segment)
]

# Key Metrics

st.subheader("📈 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Avg Daily PnL", f"${filtered_data['daily_pnl'].mean():,.2f}")
col2.metric("Median Daily PnL", f"${filtered_data['daily_pnl'].median():,.2f}")
col3.metric("Avg Trade Count", f"{filtered_data['trade_count'].mean():.2f}")

#  PnL Distribution

st.subheader("Daily PnL Distribution")

fig1, ax1 = plt.subplots()
sns.histplot(filtered_data['daily_pnl'], bins=50, ax=ax1)
ax1.set_title("PnL Distribution")
st.pyplot(fig1)

#  Trade Frequency Boxplot

st.subheader("Trade Frequency")

fig2, ax2 = plt.subplots()
sns.boxplot(
    data=merged_data[merged_data['regime'] == selected_regime],
    x='activity_segment',
    y='trade_count',
    ax=ax2
)
ax2.set_title("Trade Count by Segment")
st.pyplot(fig2)

#  Cluster Summary

st.subheader("Trader Archetypes (Cluster Summary)")

cluster_summary = trader_summary.groupby('cluster').mean(numeric_only=True)

st.dataframe(cluster_summary)

#  Model Performance Summary

st.subheader("Predictive Model Performance")

st.markdown("""
- Accuracy: **66.5%**
- ROC-AUC: **0.64**
- Model demonstrates modest predictive power.
- Stronger signal observed in volatility than directional profitability.
""")

st.markdown("---")
st.markdown("Built for Primetrade.ai Data Science Intern Assignment")
