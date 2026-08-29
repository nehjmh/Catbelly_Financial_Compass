import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Building a Portfolio",
    page_icon="🏛️",
    layout="wide"
)

st.title("🏛️ Building a Modern Portfolio: The Pyramid Model")
st.markdown(
    "Forget the outdated '60/40' stock-and-bond model. Modern wealth building focuses on a solid "
    "index & hard-asset foundation, targeted individual convictions, and optional income engines—without "
    "diluting your growth across hundreds of mediocre holdings."
)

st.markdown("---")

# --- PHILOSOPHY OVERVIEW ---
st.subheader("💡 Portfolio Architecture Principles")

col_p1, col_p2, col_p3 = st.columns(3)

with col_p1:
    st.info("### 🛑 No Dead-Weight Bonds")
    st.markdown(
        "Traditional 60/40 portfolios rely heavily on low-yield bonds that often fail to beat inflation. "
        "We focus on real productive assets, equity compounders, and scarce stores of value instead."
    )

with col_p2:
    st.success("### 🎯 Focused Diversification")
    st.markdown(
        "Over-diversification ('diworsification') dilutes your best ideas. Holding 500 random stocks "
        "guarantees average results. A structured pyramid keeps your portfolio concentrated yet resilient."
    )

with col_p3:
    st.warning("### ⚡ Modern Hard Assets")
    st.markdown(
        "A true foundation extends beyond paper equities. Allocating room for gold, silver, and Bitcoin "
        "provides monetary hedges against currency debasement and macro shifts."
    )

st.markdown("---")

# --- INTERACTIVE PYRAMID BUILDER ---
st.subheader("🛠️ Interactive Portfolio Pyramid Builder")
st.markdown("Adjust the sliders below to customize your pyramid layers. Ensure your total equals **100%**.")

col_build, col_summary = st.columns([3, 2])

with col_build:
    st.markdown("#### 1️⃣ Level 1: Foundation (Broad Indices & Stores of Value)")
    f_equity = st.slider("Broad Equity Indices (SPY, QQQ, IWM) %", 30, 80, 50, step=5)
    f_hard = st.slider("Hard Assets (Gold, Silver, Bitcoin / IBIT) %", 0, 30, 10, step=5)
    
    st.markdown("#### 2️⃣ Level 2: High-Conviction Stock Picks")
    f_stocks = st.slider("Individual Stock Picks (e.g., NVDA, AAPL, COST) %", 10, 50, 25, step=5)
    
    st.markdown("#### 3️⃣ Level 3: Income & Yield Engine (Optional)")
    include_income = st.checkbox("Include High-Yield / Income Engine?", value=True)
    if include_income:
        f_income = st.slider("Income & Distribution ETFs (SPYI, QQQI, REITs) %", 5, 30, 15, step=5)
    else:
        f_income = 0

total_alloc = f_equity + f_hard + f_stocks + f_income

with col_summary:
    st.markdown("#### 📊 Target Allocation Summary")
    
    alloc_df = pd.DataFrame([
        {"Layer": "Level 1: Broad Indices (SPY/QQQ/IWM)", "Allocation": f"{f_equity}%"},
        {"Layer": "Level 1: Hard Assets (Gold/Silver/BTC)", "Allocation": f"{f_hard}%"},
        {"Layer": "Level 2: High-Conviction Stocks", "Allocation": f"{f_stocks}%"},
        {"Layer": "Level 3: Income Engine", "Allocation": f"{f_income}%"}
    ])
    st.table(alloc_df)
    
    if total_alloc == 100:
        st.success(f"✅ Perfect Allocation! Total = {total_alloc}%")
    elif total_alloc > 100:
        st.error(f"⚠️ Over-Allocated: Total = {total_alloc}% (Reduce by {total_alloc - 100}%)")
    else:
        st.warning(f"⚠️ Under-Allocated: Total = {total_alloc}% (Add {100 - total_alloc}%)")

st.markdown("---")

# --- LAYER DETAILS & TICKER GUIDE ---
st.subheader("📚 Ticker Guide by Pyramid Layer")

t1, t2, t3 = st.tabs(["🏛️ Level 1: Foundation", "🛠️ Level 2: Conviction Stocks", "💵 Level 3: Yield Engine"])

with t1:
    col_l1a, col_l1b = st.columns(2)
    with col_l1a:
        st.markdown("### Broad Equity Anchors")
        st.markdown(
            "* **SPY / VOO / SPLG:** S&P 500 broad US mega-cap coverage.\n"
            "* **QQQ / QQQM:** Nasdaq 100 top non-financial growth leaders.\n"
            "* **IWM / VTWO:** Russell 2000 small-cap growth & value exposure."
        )
    with col_l1b:
        st.markdown("### Scarce Hard Assets")
        st.markdown(
            "* **Bitcoin ETFs (IBIT / FBTC):** Digital scarcity & non-sovereign monetary asset.\n"
            "* **Gold (GLD / IAU):** Classic monetary reserve & geopolitical hedge.\n"
            "* **Silver (SLV):** Dual monetary & industrial demand driver."
        )

with t2:
    st.markdown("### Picking Your High-Conviction Winners")
    st.markdown(
        "Level 2 is where you pick 3 to 10 companies you thoroughly understand. "
        "Rather than buying 100 random stocks, focus on companies with clear competitive moats, "
        "strong profit margins, and secular growth tailwinds."
    )
    st.info(
        "💡 **Rule of Thumb:** If you can't explain how a company makes money in two sentences, "
        "it belongs in Level 1 (Index Funds), not Level 2 (Stock Picks)."
    )

with t3:
    st.markdown("### High-Yield Income Without Bonds")
    st.markdown(
        "If cash flow is a priority, Level 3 lets you stack income-generating assets without relying "
        "on low-yielding Treasuries."
    )
    
    inc_df = pd.DataFrame([
        {"Ticker / Category": "SPYI / QQQI", "Strategy": "Option-Income Equity Funds", "Primary Role": "High monthly distribution yields with upside cap mitigation."},
        {"Ticker / Category": "Public REITs (O, PLD, AMT)", "Strategy": "Real Estate Investment Trusts", "Primary Role": "Contractual commercial real estate rental income."},
        {"Ticker / Category": "SCHD / VIG", "Strategy": "Dividend Growth Equities", "Primary Role": "Growing annual payouts backed by strong balance sheets."}
    ])
    st.table(inc_df)