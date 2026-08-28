import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf

st.set_page_config(
    page_title="Reverse Screener",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Reverse Screener & Stock Valuation Lab")
st.markdown(
    "Analyze individual stock fundamentals against target quality metrics, compare market price against analyst consensus, "
    "and estimate intrinsic value using a 2-Stage Discounted Cash Flow (DCF) model."
)

st.markdown("---")

# Ticker Input Controls
col_input, col_preset = st.columns([1, 2])

with col_input:
    ticker_input = st.text_input("Enter Stock Ticker Symbol:", value="AAPL").strip().upper()

with col_preset:
    st.write("##### Quick Load Benchmark Stocks:")
    q_cols = st.columns(5)
    if q_cols[0].button("AAPL"): ticker_input = "AAPL"
    if q_cols[1].button("MSFT"): ticker_input = "MSFT"
    if q_cols[2].button("NVDA"): ticker_input = "NVDA"
    if q_cols[3].button("GOOGL"): ticker_input = "GOOGL"
    if q_cols[4].button("AMZN"): ticker_input = "AMZN"

if not ticker_input:
    st.warning("Please enter a valid ticker symbol to run the analysis.")
    st.stop()

# --- DATA FETCHING ENGINE ---
@st.cache_data(ttl=3600)
def fetch_stock_data(symbol: str):
    ticker = yf.Ticker(symbol)
    info = ticker.info
    hist = ticker.history(period="5y")
    return info, hist

with st.spinner(f"Fetching fundamental data for {ticker_input}..."):
    try:
        info, hist = fetch_stock_data(ticker_input)
        if not info or ("regularMarketPrice" not in info and "currentPrice" not in info):
            st.error(f"Could not retrieve fundamental data for ticker '{ticker_input}'. Please check the symbol.")
            st.stop()
    except Exception as e:
        st.error(f"Error loading ticker data: {e}")
        st.stop()

# --- EXTRACT KEY METRICS ---
company_name = info.get("longName", ticker_input)
sector = info.get("sector", "N/A")
industry = info.get("industry", "N/A")

current_price = info.get("currentPrice") or info.get("regularMarketPrice") or hist["Close"].iloc[-1]
prev_close = info.get("previousClose", current_price)
price_change_pct = ((current_price - prev_close) / prev_close) * 100 if prev_close else 0.0

analyst_target = info.get("targetMeanPrice", current_price)
high_52w = info.get("fiftyTwoWeekHigh", hist["High"].max())

# Calculate 200-Week Moving Average (200 weeks ~ 1000 trading days)
if len(hist) >= 200:
    weekly_close = hist["Close"].resample("W").last()
    ma_200w = weekly_close.rolling(window=200).mean().iloc[-1]
    if pd.isna(ma_200w):
        ma_200w = hist["Close"].tail(1000).mean()
else:
    ma_200w = hist["Close"].mean()

# --- TOP METRIC BANNER (PRICE & TARGETS ON SAME LINE) ---
st.subheader(f"📌 {company_name} ({ticker_input})")
st.caption(f"**Sector:** {sector} | **Industry:** {industry}")

col_price, col_target, col_52w, col_200w = st.columns(4)

with col_price:
    st.metric(
        label="Current Price", 
        value=f"${current_price:,.2f}", 
        delta=f"{price_change_pct:+.2f}% Daily"
    )

with col_target:
    pct_to_target = ((analyst_target - current_price) / current_price) * 100
    st.metric(
        label="Analyst Target Price", 
        value=f"${analyst_target:,.2f}", 
        delta=f"{pct_to_target:+.2f}% Target Upside"
    )

with col_52w:
    dist_52w = ((current_price - high_52w) / high_52w) * 100
    st.metric(
        label="52-Week High", 
        value=f"${high_52w:,.2f}",
        delta=f"{dist_52w:.2f}% vs High"
    )

with col_200w:
    dist_200w = ((current_price - ma_200w) / ma_200w) * 100
    st.metric(
        label="200-Week Moving Avg", 
        value=f"${ma_200w:,.2f}",
        delta=f"{dist_200w:+.2f}% vs Baseline"
    )

st.markdown("---")

# --- TABULAR ANALYSIS & DCF ENGINE ---
tab_scorecard, tab_dcf = st.tabs(["📊 Fundamental Scorecard", "🧮 2-Stage DCF Valuation"])

with tab_scorecard:
    st.subheader("📊 Fundamental Quality Benchmarks")
    st.write("Evaluating key financial metrics against standard high-quality business hurdles:")

    # Retrieve quality metrics safely
    roic = info.get("returnOnCapital") or ((info.get("returnOnAssets") or 0) * 100) # Fallback to ROA if ROIC absent
    roe = (info.get("returnOnEquity") or 0) * 100
    op_margin = (info.get("operatingMargins") or 0) * 100
    pe_ratio = info.get("trailingPE") or info.get("forwardPE") or 0
    earnings_growth = (info.get("earningsGrowth") or info.get("revenueGrowth") or 0.10) * 100
    peg_ratio = info.get("pegRatio") or (pe_ratio / earnings_growth if earnings_growth > 0 else 0)
    debt_to_equity = info.get("debtToEquity", 0)

    # Scoring Logic
    score = 0
    if roic >= 15.0: score += 1
    if roe >= 15.0: score += 1
    if op_margin >= 20.0: score += 1
    if 0 < peg_ratio <= 1.5: score += 1
    if debt_to_equity < 1.5: score += 1

    # Overall Score Summary Banner
    s_col1, s_col2 = st.columns([1, 2])
    with s_col1:
        st.metric(
            label="Overall Fundamental Score", 
            value=f"{score} / 5 Passes",
            delta="High Quality" if score >= 4 else "Moderate Quality" if score >= 2 else "Watchlist / Low Quality",
            delta_color="normal" if score >= 3 else "inverse"
        )
    with s_col2:
        st.info(
            f"**Evaluation Summary:** {ticker_input} passes **{score} out of 5** core fundamental criteria. "
            "Companies scoring 4 or 5 generally demonstrate high capital efficiency, strong operational margins, and prudent leverage."
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # Detailed Benchmark Breakdown Table
    scorecard_data = [
        {"Metric": "ROIC (Return on Invested Capital)", "Current Value": f"{roic:.2f}%", "Benchmark Target": "> 15.0%", "Status": "🟢 Pass" if roic >= 15 else "🔴 Fail"},
        {"Metric": "ROE (Return on Equity)", "Current Value": f"{roe:.2f}%", "Benchmark Target": "> 15.0%", "Status": "🟢 Pass" if roe >= 15 else "🔴 Fail"},
        {"Metric": "Operating Margin", "Current Value": f"{op_margin:.2f}%", "Benchmark Target": "> 20.0%", "Status": "🟢 Pass" if op_margin >= 20 else "🔴 Fail"},
        {"Metric": "PEG Ratio", "Current Value": f"{peg_ratio:.2f}" if peg_ratio else "N/A", "Benchmark Target": "< 1.50", "Status": "🟢 Pass" if 0 < peg_ratio <= 1.5 else "🔴 Fail"},
        {"Metric": "Debt-to-Equity Ratio", "Current Value": f"{debt_to_equity:.2f}", "Benchmark Target": "< 1.50", "Status": "🟢 Pass" if debt_to_equity < 1.5 else "🔴 Fail"}
    ]

    st.dataframe(pd.DataFrame(scorecard_data), use_container_width=True, hide_index=True)

with tab_dcf:
    st.subheader("🧮 2-Stage Discounted Cash Flow (DCF) Fair Value Calculator")
    st.write("Estimate intrinsic value based on projected Free Cash Flow (FCF) per share discounted back to present value.")

    fcf = info.get("freeCashflow", 0)
    shares_outer = info.get("sharesOutstanding", 1)
    fcf_per_share = fcf / shares_outer if fcf and shares_outer else (current_price * 0.04) # Default fallback estimate

    col_dcf1, col_dcf2 = st.columns([1, 1])

    with col_dcf1:
        st.markdown("##### **Model Parameters**")
        base_fcf = st.number_input("Base FCF per Share ($):", min_value=0.01, value=float(max(0.50, round(fcf_per_share, 2))), step=0.25)
        growth_stage1 = st.slider("Stage 1 Growth Rate (Years 1-5) (%):", min_value=0.0, max_value=40.0, value=12.0, step=0.5) / 100
        growth_terminal = st.slider("Terminal Perpetual Growth Rate (%):", min_value=0.5, max_value=5.0, value=2.5, step=0.25) / 100
        discount_rate = st.slider("Required Rate of Return / Discount Rate (%):", min_value=5.0, max_value=18.0, value=9.0, step=0.5) / 100

    # DCF Calculations
    years_s1 = 5
    pv_cash_flows = 0.0
    projected_fcfs = []

    curr_f = base_fcf
    for yr in range(1, years_s1 + 1):
        curr_f *= (1 + growth_stage1)
        pv_fcf = curr_f / ((1 + discount_rate) ** yr)
        pv_cash_flows += pv_fcf
        projected_fcfs.append({"Year": f"Year {yr}", "Projected FCF": f"${curr_f:.2f}", "Present Value": f"${pv_fcf:.2f}"})

    # Terminal Value calculation
    terminal_value = (curr_f * (1 + growth_terminal)) / (discount_rate - growth_terminal)
    pv_terminal_value = terminal_value / ((1 + discount_rate) ** years_s1)
    intrinsic_value = pv_cash_flows + pv_terminal_value

    with col_dcf2:
        st.markdown("##### **Valuation Summary**")
        margin_of_safety = ((intrinsic_value - current_price) / intrinsic_value) * 100

        res_col1, res_col2 = st.columns(2)
        res_col1.metric("Estimated Fair Value", f"${intrinsic_value:,.2f}")
        res_col2.metric("Margin of Safety", f"{margin_of_safety:+.1f}%", 
                        delta="Undervalued" if margin_of_safety > 0 else "Overvalued",
                        delta_color="normal" if margin_of_safety > 0 else "inverse")

        st.markdown("<br>", unsafe_allow_html=True)
        st.write("**Projected Year 1–5 Cash Flow Breakdown:**")
        st.dataframe(pd.DataFrame(projected_fcfs), use_container_width=True, hide_index=True)