import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="Hyperliquid | Behavioral & Sentiment Analytics",
    layout="wide"
)

# ===============================
# GLOBAL STYLES
# ===============================
st.markdown("""
<style>
    .block-container {
        padding-top: 2rem;
    }
    .metric-card {
        background-color: #111827;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #1f2937;
    }
    .section-header {
        font-size: 1.3rem;
        font-weight: 600;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
    }
    .section-sub {
        color: #9CA3AF;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# ===============================
# LOAD DATA
# ===============================
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "scripts"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_DIR / "dashboard_data.csv")
    clusters = pd.read_csv(DATA_DIR / "trader_clusters.csv")
    return df, clusters

df, clusters = load_data()

# ===============================
# SIDEBAR
# ===============================
st.sidebar.title("🛠 Analytics Controls")
st.sidebar.caption("Filter protocol behavior by market psychology")

sentiment_order = [
    "Extreme Fear",
    "Fear",
    "Neutral",
    "Greed",
    "Extreme Greed"
]

sentiment_filter = st.sidebar.multiselect(
    "Market Sentiment Regimes",
    options=sentiment_order,
    default=sentiment_order
)

filtered_df = df[df["classification"].isin(sentiment_filter)]

# ===============================
# HEADER
# ===============================
st.title("📊 Hyperliquid Behavioral & Sentiment Dashboard")
st.markdown(
    "A protocol-level deep dive into **trader psychology**, **behavioral archetypes**, "
    "and **revenue dynamics** under different market regimes."
)

st.divider()

# ===============================
# KPI ROW
# ===============================
k1, k2, k3, k4 = st.columns(4)

with k1:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("Total Trading Volume", f"${filtered_df['Size USD'].sum():,.0f}")
    st.caption("Aggregate notional traded")
    st.markdown('</div>', unsafe_allow_html=True)

with k2:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    total_volume = filtered_df["Size USD"].sum()

    if total_volume > 0:
        efficiency = filtered_df["Closed PnL"].sum() / (total_volume / 1_000)
    else:
        efficiency = 0
    st.metric("PnL Efficiency", f"${efficiency:.2f}")
    st.caption("PnL per $1k traded")
    st.markdown('</div>', unsafe_allow_html=True)

with k3:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("Active Traders", filtered_df["Account"].nunique())
    st.caption("Unique market participants")
    st.markdown('</div>', unsafe_allow_html=True)

with k4:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    if not filtered_df.empty:
        top_sentiment = filtered_df["classification"].mode()[0]
    else:
        top_sentiment = "N/A"
    st.metric("Dominant Sentiment", top_sentiment)
    st.caption("Most frequent regime")
    st.markdown('</div>', unsafe_allow_html=True)

# ===============================
# SECTION: REGIME ANALYSIS
# ===============================
st.markdown('<div class="section-header">📈 PnL vs. Market Sentiment</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">How trader profitability shifts across emotional regimes</div>', unsafe_allow_html=True)

fig_pnl = px.box(
    filtered_df,
    x="classification",
    y="Closed PnL",
    color="classification",
    category_orders={"classification": sentiment_order},
    template="plotly_dark"
)
fig_pnl.update_layout(showlegend=False)
st.plotly_chart(fig_pnl, use_container_width=True)

# ===============================
# SECTION: ARCHETYPES
# ===============================
ARCHETYPE_MAP = {
    0: "High-Frequency Scalpers",
    1: "Disciplined Strategists",
    2: "Institutional Whales",
    3: "High-Variance Retail"
}
clusters["Archetype"] = clusters["Cluster"].map(ARCHETYPE_MAP)

st.markdown('<div class="section-header">🎯 Trader Archetype Map</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-sub">'
    'Behavioral clustering based on activity, size, and profitability'
    '</div>',
    unsafe_allow_html=True
)

fig_cluster = px.scatter(
    clusters,
    x="Activity",
    y="Total_PnL",
    size="Avg_Size",
    color="Archetype",
    hover_name="Account",
    log_x=True,
    template="plotly_dark"
)

st.plotly_chart(fig_cluster, use_container_width=True)

# ===============================
# SECTION: REVENUE ENGINE
# ===============================
st.markdown('<div class="section-header">🔮 Protocol Revenue Engine</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-sub">'
    'Daily protocol volume as a proxy for fee generation'
    '</div>',
    unsafe_allow_html=True
)

vol_trend = (
    filtered_df
    .groupby("date")["Size USD"]
    .sum()
    .reset_index()
)

fig_vol = px.area(
    vol_trend,
    x="date",
    y="Size USD",
    template="plotly_dark",
    color_discrete_sequence=["#00CC96"]
)
st.plotly_chart(fig_vol, use_container_width=True)

# ===============================
# FOOTER
# ===============================
st.success("✅ Insights generated using a  behavioral finance framework")
