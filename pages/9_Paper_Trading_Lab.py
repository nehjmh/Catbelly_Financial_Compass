import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf

st.set_page_config(
    page_title="Paper Trading & Pyramid View",
    page_icon="📊",
    layout="wide"
)

# --- DEFAULT PORTFOLIO DATA (ZERO ALLOCATIONS) ---
DEFAULT_POSITIONS = [
    {"Pyramid Layer": "1. Foundation", "Ticker": "VOO", "Shares": 0.0, "Avg Price ($)": 0.0},
    {"Pyramid Layer": "1. Foundation", "Ticker": "QQQ", "Shares": 0.0, "Avg Price ($)": 0.0},
    {"Pyramid Layer": "2. Conviction Stocks", "Ticker": "NVDA", "Shares": 0.0, "Avg Price ($)": 0.0},
    {"Pyramid Layer": "3. Yield Engine", "Ticker": "SPYI", "Shares": 0.0, "Avg Price ($)": 0.0},
]

if "positions_df" not in st.session_state:
    st.session_state.positions_df = pd.DataFrame(DEFAULT_POSITIONS)

# --- NAVIGATION TABS ---
tab_editing, tab_heatmap = st.tabs(["📊 Portfolio Positions & Editing", "🔺 Pyramid Heatmap View"])

# ==============================================================================
# TAB 1: PORTFOLIO POSITIONS & EDITING
# ==============================================================================
with tab_editing:
    st.title("Active Watchlist & Simulated Holdings")

    df_current = st.session_state.positions_df.copy()
    tickers = df_current["Ticker"].tolist()

    # Fetch Live Market Prices
    latest_prices = {}
    if tickers:
        with st.spinner("Fetching live prices..."):
            try:
                price_data = yf.download(tickers, period="5d", progress=False)["Close"]
                if isinstance(price_data, pd.DataFrame) and not price_data.empty:
                    latest_prices = price_data.iloc[-1].to_dict()
                elif isinstance(price_data, pd.Series):
                    latest_prices = {tickers[0]: float(price_data.iloc[-1])}
            except Exception:
                pass

    # Compute Calculated Columns
    live_prices = []
    market_values = []
    returns = []

    for idx, row in df_current.iterrows():
        ticker = row["Ticker"]
        shares = float(row["Shares"])
        avg_px = float(row["Avg Price ($)"])
        live_px = float(latest_prices.get(ticker, avg_px if avg_px > 0 else 0.0))

        mkt_val = shares * live_px
        ret_pct = ((live_px - avg_px) / avg_px * 100) if (avg_px > 0 and shares > 0) else 0.0

        live_prices.append(live_px)
        market_values.append(mkt_val)
        returns.append(ret_pct)

    df_current["Live Price ($)"] = live_prices
    df_current["Market Value ($)"] = market_values

    total_mkt_val = sum(market_values)
    df_current["Weight"] = [(mv / total_mkt_val) if total_mkt_val > 0 else 0.0 for mv in market_values]
    df_current["Return"] = returns

    # Display / Edit Data
    edited_df = st.data_editor(
        df_current,
        column_config={
            "Pyramid Layer": st.column_config.SelectboxColumn(
                "Pyramid Layer",
                options=["1. Foundation", "2. Conviction Stocks", "3. Yield Engine", "4. Tactical / Speculative"],
                required=True
            ),
            "Ticker": st.column_config.TextColumn("Ticker", required=True),
            "Shares": st.column_config.NumberColumn("Shares", min_value=0.0, format="%.2f", step=1.0),
            "Avg Price ($)": st.column_config.NumberColumn("Avg Price ($)", min_value=0.0, format="$%.2f", step=1.0),
            "Live Price ($)": st.column_config.NumberColumn("Live Price ($)", format="$%.2f", disabled=True),
            "Market Value ($)": st.column_config.NumberColumn("Market Value ($)", format="$%.2f", disabled=True),
            "Weight": st.column_config.NumberColumn("Weight", format="%.2f%%", disabled=True),
            "Return": st.column_config.NumberColumn("Return", format="%+.2f%%", disabled=True),
        },
        num_rows="dynamic",
        use_container_width=True,
        hide_index=True,
        key="portfolio_editor"
    )

    # Persist Changes
    st.session_state.positions_df = edited_df[["Pyramid Layer", "Ticker", "Shares", "Avg Price ($)"]]

# ==============================================================================
# TAB 2: PYRAMID HEATMAP VIEW
# ==============================================================================
with tab_heatmap:
    st.title("🔺 Pyramid Portfolio Structure")
    st.markdown("Visual allocation breakdown organized by strategic pyramid tiers.")

    if total_mkt_val > 0:
        summary_df = edited_df.groupby("Pyramid Layer").agg({
            "Market Value ($)": "sum",
            "Weight": "sum"
        }).reset_index()

        for idx, row in summary_df.iterrows():
            st.subheader(f"{row['Pyramid Layer']}")
            st.write(f"**Total Allocation:** ${row['Market Value ($)']:,.2f} ({row['Weight']*100:.1f}%)")
            
            layer_items = edited_df[edited_df["Pyramid Layer"] == row["Pyramid Layer"]]
            st.dataframe(
                layer_items[["Ticker", "Shares", "Live Price ($)", "Market Value ($)", "Weight", "Return"]].style.format({
                    "Shares": "{:.2f}",
                    "Live Price ($)": "${:.2f}",
                    "Market Value ($)": "${:,.2f}",
                    "Weight": "{:.2%}",
                    "Return": "{:+.2f}%"
                }),
                use_container_width=True,
                hide_index=True
            )
            st.markdown("---")
    else:
        st.info("💡 Enter non-zero Shares and Average Prices in the **Portfolio Positions & Editing** tab to activate the Pyramid Heatmap View.")