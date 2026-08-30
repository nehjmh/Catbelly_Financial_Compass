import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, date

st.set_page_config(
    page_title="Bitcoin, Ethereum & Solana",
    page_icon="🪙",
    layout="wide"
)

st.title("🪙 Bitcoin, Ethereum & Solana: Macro Assets & Layer-1 Infrastructure")
st.markdown("""
*Analyzing the foundational layers of store of value, institutional settlement, and high-frequency utility.*
""")

st.markdown("---")

# Shared data fetcher for all three assets
@st.cache_data(ttl=3600)
def load_crypto_data(ticker_symbol):
    try:
        crypto = yf.Ticker(ticker_symbol)
        hist = crypto.history(period="max")
        if not hist.empty:
            hist = hist.reset_index()
            # Handle timezone formatting safely
            if 'Date' in hist.columns:
                hist['Date'] = pd.to_datetime(hist['Date']).dt.tz_localize(None)
            return hist
    except Exception as e:
        pass
    return pd.DataFrame()

# Create Tabs for the 3 Assets
tab_btc, tab_eth, tab_sol = st.tabs([
    "Bitcoin (Store of Value)", 
    "Ethereum (Settlement Layer)", 
    "Solana (Execution Layer)"
])

# ==============================================================================
# TAB 1: BITCOIN (PRESERVING FULL ORIGINAL LAYOUT & RAINBOW CHART)
# ==============================================================================
with tab_btc:
    st.header("₿ Bitcoin: The Case for Bitcoin in a Modern Income & Growth Portfolio")
    st.markdown("""
    ### *“The Second Amendment of Money” — Emergent Hard Money & Macro Hedge*
    Bitcoin has evolved from a peer-to-peer electronic cash experiment into a primary monetary reserve asset. Below is the multi-faceted thesis for why a strategic allocation belongs in a modern portfolio.
    """)

    st.markdown("---")

    # SECTION 1: THE CORE THESIS & THINKERS
    st.subheader("🧠 1. Strategic Foundation & Institutional Thesis")

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

    # SECTION 2: LIVE BITCOIN METRICS & ARR / CAGR METRICS
    st.subheader("📊 2. Performance & ARR (Annualized Return) Analytics")

    df_btc = load_crypto_data("BTC-USD")

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

    # SECTION 3: INTERACTIVE BITCOIN RAINBOW GRAPH
    st.subheader("🌈 3. The Bitcoin Rainbow Graph (Logarithmic Valuation Model)")
    st.markdown("""
    The Rainbow Chart uses a logarithmic growth curve to model Bitcoin's long-term valuation channels. 
    It provides perspective on historical market cycles, highlighting periods of extreme undervaluation (*"Fire Sale"*) versus cycle euphoria (*"Maximum Bubble"*).
    """)

    if not df_btc.empty:
        df_rainbow = df_btc.copy()
        
        genesis_date = pd.to_datetime("2009-01-09")
        df_rainbow["Days"] = (df_rainbow["Date"] - genesis_date).dt.days
        df_rainbow = df_rainbow[df_rainbow["Days"] > 0]

        log_days = np.log(df_rainbow["Days"])
        log_price = np.log(df_rainbow["Close"])
        
        b, a = np.polyfit(log_days, log_price, 1)
        df_rainbow["Base_Log"] = a + b * log_days

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

        fig_btc = go.Figure()

        for i in range(len(bands) - 1):
            name_upper, offset_upper, color = bands[i]
            _, offset_lower, _ = bands[i+1]

            y_upper = np.exp(df_rainbow["Base_Log"] + offset_upper)
            y_lower = np.exp(df_rainbow["Base_Log"] + offset_lower)

            fig_btc.add_trace(go.Scatter(
                x=df_rainbow["Date"], y=y_upper, mode='lines',
                line=dict(width=0, color=color), showlegend=False, hoverinfo='skip'
            ))
            fig_btc.add_trace(go.Scatter(
                x=df_rainbow["Date"], y=y_lower, mode='lines',
                line=dict(width=0), fill='tonexty', fillcolor=color,
                opacity=0.4, name=name_upper
            ))

        fig_btc.add_trace(go.Scatter(
            x=df_rainbow["Date"], y=df_rainbow["Close"], mode='lines',
            name='BTC Actual Price ($USD)', line=dict(color='black', width=2)
        ))

        fig_btc.update_layout(
            title="Bitcoin Logarithmic Rainbow Valuation Model",
            yaxis_type="log", xaxis_title="Date", yaxis_title="Price ($USD) - Log Scale",
            height=650, legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            template="plotly_white"
        )

        st.plotly_chart(fig_btc, use_container_width=True)

    st.markdown("---")
    st.subheader("🎯 4. Practical Allocation Strategy")

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        * **Conservative (1% - 2%):** Serves as an institutional macro tail-risk hedge against sovereign debt expansion with negligible portfolio draw-down impact.
        * **Moderate (3% - 5%):** Enhances portfolio Risk-Adjusted Return (Sharpe Ratio) while allowing meaningful upside participation in structural monetary adoption cycles.
        * **Rebalancing Rule:** Rebalance annually or when position drift exceeds +50% of target weight to lock in parabolic gains into core cash flow assets.
        """)
    with col_b:
        st.markdown("""
        * **Spot ETFs (IBIT, FBTC):** Highly liquid, tax-advantaged holding inside traditional brokerage or retirement accounts.
        * **Self-Custody (BitKey / Cold Storage):** Direct protocol ownership removing third-party counterparty risk, honoring Satoshi's foundational vision.
        """)


# ==============================================================================
# TAB 2: ETHEREUM (SETTLEMENT & INSTITUTIONAL FRAMEWORK)
# ==============================================================================
with tab_eth:
    st.header("Ξ Ethereum: Institutional Settlement & Tokenization")
    st.write("Exploring Ethereum's role as the foundational settlement layer for global finance and real-world asset (RWA) tokenization.")
    
    df_eth = load_crypto_data("ETH-USD")
    
    if not df_eth.empty:
        curr_eth = df_eth['Close'].iloc[-1]
        prev_eth = df_eth['Close'].iloc[-2]
        chg_eth = ((curr_eth - prev_eth) / prev_eth) * 100
        high_eth = df_eth['Close'].max()
        low_eth = df_eth['Close'].min()
        
        e1, e2, e3 = st.columns(3)
        e1.metric("Current ETH Price", f"${curr_eth:,.2f}", f"{chg_eth:+.2f}% 1D")
        e2.metric("52-Week / Max High", f"${high_eth:,.2f}")
        e3.metric("52-Week / Max Low", f"${low_eth:,.2f}")
        
        st.line_chart(df_eth.set_index('Date')['Close'])

    st.markdown("---")
    st.subheader("🏛️ Tom Lee's Thesis on Ethereum & Institutional Settlement")
    st.markdown("""
    * **Foundational Settlement:** *"Ethereum functions increasingly as the foundational settlement layer for global institutional finance, where immutable security matters more than raw transactional speed."*
    * **Real-World Asset Tokenization:** *"The tokenization of real-world assets (RWAs) will migrate trillions of dollars of traditional equities, debt, and real estate onto the Ethereum blockchain, fundamentally lowering friction and transaction costs."*
    * **Compressed Clearing Cycles:** *"Smart contracts act as automated trust mechanisms, bypassing traditional intermediaries and radically compressing the clearing and settlement cycle from days down to seconds."*
    * **Deflationary Tokenomics:** *"As institutional adoption scales, Ethereum's tokenomics—specifically supply burn mechanisms—create a deflationary pressure model that behaves much like digital sovereign debt collateral."*
    """)


# ==============================================================================
# TAB 3: SOLANA (EXECUTION & AGENTIC WEB)
# ==============================================================================
with tab_sol:
    st.header("⚡ Solana: High-Frequency Execution & Agentic Web")
    st.write("Analyzing Solana as the high-throughput execution layer engineered for consumer scale, microtransactions, and AI agent liquidity.")
    
    df_sol = load_crypto_data("SOL-USD")
    
    if not df_sol.empty:
        curr_sol = df_sol['Close'].iloc[-1]
        prev_sol = df_sol['Close'].iloc[-2]
        chg_sol = ((curr_sol - prev_sol) / prev_sol) * 100
        high_sol = df_sol['Close'].max()
        low_sol = df_sol['Close'].min()
        
        s1, s2, s3 = st.columns(3)
        s1.metric("Current SOL Price", f"${curr_sol:,.2f}", f"{chg_sol:+.2f}% 1D")
        s2.metric("52-Week / Max High", f"${high_sol:,.2f}")
        s3.metric("52-Week / Max Low", f"${low_sol:,.2f}")
        
        st.line_chart(df_sol.set_index('Date')['Close'])

    st.markdown("---")
    st.subheader("⚡ Tom Lee's Thesis on Solana & AI Agent Infrastructure")
    st.markdown("""
    * **High-Frequency Utility:** *"Solana represents the high-frequency execution layer, engineered explicitly for consumer-scale applications, microtransactions, and massive parallel processing."*
    * **Multi-Chain Architecture:** *"The convergence of traditional finance (TradFi) and decentralized finance (DeFi) requires a multi-chain architecture where high-throughput chains like Solana handle high-velocity retail and machine-to-machine traffic."*
    * **Instant Machine Speed for AI Agents:** *"AI agents require native digital money to execute autonomous economic transactions, and traditional banking rails are far too slow and high-friction for machine speed."*
    * **Programmable Agent Liquidity:** *"Cryptocurrency and tokenized assets provide the exact machine-readable, programmable liquidity layers that autonomous AI systems need to buy data, compute, and services instantly."*
    """)

st.markdown("---")
st.caption("Catbelly Compass • Layer-1 Asset Architecture Module")