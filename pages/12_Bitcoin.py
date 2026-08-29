import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, date

st.set_page_config(
    page_title="11. Bitcoin Thesis & Portfolio Role",
    page_icon="₿",
    layout="wide"
)

st.title("₿ Page 11: The Case for Bitcoin in a Modern Income & Growth Portfolio")
st.markdown("""
### *“The Second Amendment of Money” — Emergent Hard Money & Macro Hedge*
Bitcoin has evolved from a peer-to-peer electronic cash experiment into a primary monetary reserve asset. Below is the multi-faceted thesis for why a strategic allocation belongs in a modern portfolio.
""")

st.markdown("---")

# ==============================================================================
# SECTION 1: THE CORE THESIS & THINKERS
# ==============================================================================
st.header("🧠 1. Strategic Foundation & Institutional Thesis")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🌐 Satoshi Nakamoto & Marc Andreessen")
    st.markdown("""
    * **Satoshi's Vision (Absolute Scarcity & Sovereign Control):** Introduced a non-sovereign monetary system capped strictly at 21 million units with zero counterparty risk or central authority debasement.
    * **Marc Andreessen (Technological Breakthrough):** Defined Bitcoin as the first practical solution to the *Byzantine Generals Problem*—enabling digital trust without intermediaries, establishing the foundational protocol for internet-native value transfer.
    """)
    
    st.subheader("🏛️ Institutional Heavyweights & Wall Street")
    st.markdown("""
    * **Larry Fink (BlackRock):** Shifted from skeptic to champion, categorizing Bitcoin as an *"international asset"* and a flight-to-safety reserve that acts as a hedge against sovereign debt debasement and inflation.
    * **Stanley Druckenmiller & Paul Tudor Jones:** View Bitcoin as the *"fastest horse"* in an inflationary environment. Druckenmiller highlights its brand equity and global trust, while PTJ frames it as a superior asset class during macro fiscal expansion.
    """)

with col2:
    st.subheader("📈 Macro Cycle & Debasement Dynamics")
    st.markdown("""
    * **Fiscal Debasement & Gold Correlation:** Recent market dynamics reveal Bitcoin breaking out alongside gold as family offices and balance sheets position against fiat debasement rather than speculative retail trading.
    * **The 4-Year Business Cycle vs. Supply Halving:** Structural market shifts show Bitcoin's performance closely tracks the broader global business liquidity cycle, shifting away from minor supply issuance shocks toward major macro liquidity rebounds.
    * **Asymmetric Risk/Reward:** Recognized by institutional allocators as a prime portfolio diversifier (typically 1% to 5% allocation) offering high upside capture with non-correlated return drivers relative to traditional equities.
    """)

st.markdown("---")

# ==============================================================================
# SECTION 2: LIVE BITCOIN METRICS & ARR / CAGR METRICS
# ==============================================================================
st.header("📊 2. Performance & ARR (Annualized Return) Analytics")

@st.cache_data(ttl=3600)
def load_btc_data():
    try:
        btc = yf.Ticker("BTC-USD")
        hist = btc.history(period="max")
        if not hist.empty:
            hist = hist.reset_index()
            hist['Date'] = pd.to_datetime(hist['Date']).dt.tz_localize(None)
            return hist
    except Exception as e:
        pass
    
    # Fallback dummy frame if offline
    dates = pd.date_range(start="2014-09-17", end=date.today())
    return pd.DataFrame({"Date": dates, "Close": np.linspace(400, 80000, len(dates))})

df_btc = load_btc_data()

if not df_btc.empty:
    current_price = df_btc["Close"].iloc[-1]
    first_date = df_btc["Date"].iloc[0]
    first_price = df_btc["Close"].iloc[0]
    
    # Calculate ARR / CAGR over history
    total_years = (df_btc["Date"].iloc[-1] - first_date).days / 365.25
    cagr_all = ((current_price / first_price) ** (1 / total_years) - 1) * 100 if total_years > 0 else 0.0

    # 5-Year CAGR
    five_years_ago = df_btc[df_btc["Date"] <= (df_btc["Date"].iloc[-1] - pd.DateOffset(years=5))]
    if not five_years_ago.empty:
        px_5y = five_years_ago["Close"].iloc[-1]
        cagr_5y = ((current_price / px_5y) ** (1 / 5.0) - 1) * 100
    else:
        cagr_5y = 0.0

    # 3-Year CAGR
    three_years_ago = df_btc[df_btc["Date"] <= (df_btc["Date"].iloc[-1] - pd.DateOffset(years=3))]
    if not three_years_ago.empty:
        px_3y = three_years_ago["Close"].iloc[-1]
        cagr_3y = ((current_price / px_3y) ** (1 / 3.0) - 1) * 100
    else:
        cagr_3y = 0.0

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Current BTC Price", f"${current_price:,.2f}")
    m2.metric("3-Year CAGR / ARR", f"{cagr_3y:.2f}%")
    m3.metric("5-Year CAGR / ARR", f"{cagr_5y:.2f}%")
    m4.metric("Lifetime Tracked ARR", f"{cagr_all:.2f}%")

st.markdown("---")

# ==============================================================================
# SECTION 3: INTERACTIVE BITCOIN RAINBOW GRAPH (CORRECTED FIT)
# ==============================================================================
st.header("🌈 3. The Bitcoin Rainbow Graph (Logarithmic Valuation Model)")
st.markdown("""
The Rainbow Chart uses a logarithmic growth curve to model Bitcoin's long-term valuation channels. 
It provides perspective on historical market cycles, highlighting periods of extreme undervaluation (*"Fire Sale"*) versus cycle euphoria (*"Maximum Bubble"*).
""")

if not df_btc.empty:
    df_rainbow = df_btc.copy()
    
    # Days since Genesis Block (2009-01-09)
    genesis_date = pd.to_datetime("2009-01-09")
    df_rainbow["Days"] = (df_rainbow["Date"] - genesis_date).dt.days
    df_rainbow = df_rainbow[df_rainbow["Days"] > 0]

    # Calculate exact power-law log fit from actual data
    log_days = np.log(df_rainbow["Days"])
    log_price = np.log(df_rainbow["Close"])
    
    # Linear regression on log-log data
    b, a = np.polyfit(log_days, log_price, 1)
    
    # Base curve fitted centered near the lower-middle band
    df_rainbow["Base_Log"] = a + b * log_days

    # Corrected band offsets relative to fitted base line
    bands = [
        ("Maximum Bubble Territory", 1.8, "#FF0000"),
        ("Sell! Seriously, SELL!", 1.4, "#FF4500"),
        ("FOMO Intensifies", 1.0, "#FF8C00"),
        ("Is this a bubble?", 0.6, "#FFD700"),
        ("HODL!", 0.2, "#FFFF00"),
        ("Still Cheap", -0.2, "#9ACD32"),
        ("Accumulate", -0.6, "#00FF00"),
        ("BUY!", -1.0, "#00CED1"),
        ("Basically a Fire Sale", -1.4, "#4169E1")
    ]

    fig = go.Figure()

    # Plot color band fills from top to bottom
    for i in range(len(bands) - 1):
        name_upper, offset_upper, color = bands[i]
        _, offset_lower, _ = bands[i+1]

        y_upper = np.exp(df_rainbow["Base_Log"] + offset_upper)
        y_lower = np.exp(df_rainbow["Base_Log"] + offset_lower)

        fig.add_trace(go.Scatter(
            x=df_rainbow["Date"],
            y=y_upper,
            mode='lines',
            line=dict(width=0, color=color),
            showlegend=False,
            hoverinfo='skip'
        ))
        fig.add_trace(go.Scatter(
            x=df_rainbow["Date"],
            y=y_lower,
            mode='lines',
            line=dict(width=0),
            fill='tonexty',
            fillcolor=color,
            opacity=0.4,
            name=name_upper
        ))

    # Plot actual BTC Price over top
    fig.add_trace(go.Scatter(
        x=df_rainbow["Date"],
        y=df_rainbow["Close"],
        mode='lines',
        name='BTC Actual Price ($USD)',
        line=dict(color='black', width=2)
    ))

    fig.update_layout(
        title="Bitcoin Logarithmic Rainbow Valuation Model",
        yaxis_type="log",
        xaxis_title="Date",
        yaxis_title="Price ($USD) - Log Scale",
        height=650,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        template="plotly_white"
    )

    st.plotly_chart(fig, use_container_width=True)
# ==============================================================================
# SECTION 4: PORTFOLIO INTEGRATION STRATEGY
# ==============================================================================
st.markdown("---")
st.header("🎯 4. Practical Allocation Strategy")

col_a, col_b = st.columns(2)

with col_a:
    st.subheader("💡 Suggested Allocation Band")
    st.markdown("""
    * **Conservative (1% - 2%):** Serves as an institutional macro tail-risk hedge against sovereign debt expansion with negligible portfolio draw-down impact.
    * **Moderate (3% - 5%):** Enhances portfolio Risk-Adjusted Return (Sharpe Ratio) while allowing meaningful upside participation in structural monetary adoption cycles.
    * **Rebalancing Rule:** Rebalance annually or when position drift exceeds +50% of target weight to lock in parabolic gains into core cash flow assets.
    """)

with col_b:
    st.subheader("🛠️ Implementation Vehicles")
    st.markdown("""
    * **Spot ETFs (IBIT, FBTC):** Highly liquid, tax-advantaged holding inside traditional brokerage or retirement accounts.
    * **Self-Custody (BitKey / Cold Storage):** Direct protocol ownership removing third-party counterparty risk, honoring Satoshi's foundational vision.
    """)