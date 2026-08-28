import streamlit as st

st.set_page_config(
    page_title="Catbelly Financial Compass",
    page_icon="🗺️",
    layout="wide"
)

# Header Section
st.title("🗺️ Catbelly Financial Compass")
st.markdown("Welcome to the **Catbelly Financial Compass**! This interactive curriculum guides you step-by-step from foundational financial literacy and budgeting to advanced valuation, portfolio engineering, and paper trading.")

st.markdown("---")

# ==============================================================================
# PHASE 1: FOUNDATIONS & FINANCIAL LITERACY
# ==============================================================================
st.header("🌱 Phase 1: Foundations & Financial Literacy")
st.caption("Establish baseline financial knowledge, set spending guidelines, and demystify financial vocabulary.")

col_p1_1, col_p1_2 = st.columns(2)

with col_p1_1:
    st.markdown("""
    #### 1. Financial Literacy Test
    Assess your baseline financial knowledge through interactive questions covering fundamental investing principles, compounding, risk management, and key financial concepts.
    """)
    st.page_link("pages/1_Financial_Literacy_Test.py", label="Take Literacy Test", icon="🧠")

    st.markdown("""
    #### 3. Financial Decoder
    Demystify complex balance sheet terms, financial metrics, and evaluate multi-vehicle compounding engines against consumer inflation and M2 currency debasement hurdles.
    """)
    st.page_link("pages/3_Financial_Decoder.py", label="Open Financial Decoder", icon="🎟️")

with col_p1_2:
    st.markdown("""
    #### 2. Budgeting 101
    Establish structural budgeting rules, track monthly cash inflows vs. outflows, optimize discretionary spending, and direct persistent free cash flow toward investment vehicles.
    """)
    st.page_link("pages/2_Budgeting_101.py", label="Open Budgeting Tool", icon="💡")

st.markdown("---")

# ==============================================================================
# PHASE 2: EQUITY PRINCIPLES & BACKTESTING
# ==============================================================================
st.header("📉 Phase 2: Equity Principles & Backtesting")
st.caption("Understand why stock ownership builds real wealth, open accounts, and run historical market simulations.")

col_p2_1, col_p2_2 = st.columns(2)

with col_p2_1:
    st.markdown("""
    #### 4. Why Stocks?
    Explore the historical case for equities, inflation hedging, purchasing power protection, and why ownership in cash-flowing businesses remains a premier engine for long-term wealth creation.
    """)
    st.page_link("pages/4_Why_Stocks.py", label="Explore Equity Principles", icon="📈")

    st.markdown("""
    #### 6. Random Backtest
    Run Monte Carlo simulations and historical asset backtests to stress-test portfolio returns across randomized market environments, drawdowns, and volatility cycles.
    """)
    st.page_link("pages/6_Random_Backtest.py", label="Run Backtests", icon="🎲")

with col_p2_2:
    st.markdown("""
    #### 5. Opening Your First Brokerage
    A practical walkthrough for setting up a taxable brokerage, Roth IRA, or traditional retirement account, including execution types, account choices, and transfer protocols.
    """)
    st.page_link("pages/5_Opening_Your_First_Brokerage.py", label="Read Brokerage Guide", icon="🏛️")

st.markdown("---")

# ==============================================================================
# PHASE 3: ADVANCED ANALYSIS & IMPLEMENTATION
# ==============================================================================
st.header("🧬 Phase 3: Advanced Analysis & Implementation")
st.caption("Evaluate company fundamentals, engineer multi-asset portfolios, analyze macroeconomic shifts, and model digital asset valuation.")

col_p3_1, col_p3_2 = st.columns(2)

with col_p3_1:
    st.markdown("""
    #### 7. Reverse Screener
    Type in any ticker to evaluate quality metrics against target benchmarks (ROIC, ROE, Margins, PEG), check the 200-week moving average, run 2-stage DCF fair value estimates, and view analyst consensus targets.
    """)
    st.page_link("pages/7_Reverse_Screener.py", label="Open Reverse Screener", icon="🔍")

    st.markdown("""
    #### 9. Paper Trading Lab
    Practice trade execution with real-time price lookups. Track target allocations, maintain a simulated portfolio, and visualize holdings across your allocation pyramid.
    """)
    st.page_link("pages/9_Paper_Trading_Lab.py", label="Open Paper Trading Lab", icon="🧪")

    st.markdown("""
    #### 11. Bitcoin
    Examine long-term logarithmic valuation channels for digital assets. Stress-test historical cycle tops/bottoms, power-law regression curves, and digital scarcity dynamics.
    """)
    st.page_link("pages/11_Bitcoin.py", label="Open Bitcoin Model", icon="🌈")

with col_p3_2:
    st.markdown("""
    #### 8. Building A Portfolio
    Architect balanced growth and income structures. Combine broad-market core holdings with income-generating distribution engines and model dividend reinvestment scenarios.
    """)
    st.page_link("pages/8_Building_A_Portfolio.py", label="Open Portfolio Builder", icon="📊")

    st.markdown("""
    #### 10. Jordi Visser AI Nexus
    Analyze the AI velocity shift, compressed corporate terminal values, power grid bottlenecks, tokenization, and dynamic capital reallocation strategies.
    """)
    st.page_link("pages/10_Jordi_Visser_AI_Nexus.py", label="Open Jordi Visser AI Nexus", icon="⚡")

st.markdown("---")

# ==============================================================================
# QUICK JUMP DIRECTORY
# ==============================================================================
st.header("🗺️ Quick Jump Directory")
st.caption("Direct access to all 11 modules in numerical order:")

col_dir1, col_dir2 = st.columns(2)

with col_dir1:
    st.page_link("pages/1_Financial_Literacy_Test.py", label="1. Financial Literacy Test", icon="🧠")
    st.page_link("pages/2_Budgeting_101.py", label="2. Budgeting 101", icon="💡")
    st.page_link("pages/3_Financial_Decoder.py", label="3. Financial Decoder", icon="🎟️")
    st.page_link("pages/4_Why_Stocks.py", label="4. Why Stocks?", icon="📈")
    st.page_link("pages/5_Opening_Your_First_Brokerage.py", label="5. Opening Your First Brokerage", icon="🏛️")
    st.page_link("pages/6_Random_Backtest.py", label="6. Random Backtest", icon="🎲")

with col_dir2:
    st.page_link("pages/7_Reverse_Screener.py", label="7. Reverse Screener", icon="🔍")
    st.page_link("pages/8_Building_A_Portfolio.py", label="8. Building A Portfolio", icon="📊")
    st.page_link("pages/9_Paper_Trading_Lab.py", label="9. Paper Trading Lab", icon="🧪")
    st.page_link("pages/10_Jordi_Visser_AI_Nexus.py", label="10. Jordi Visser AI Nexus", icon="⚡")
    st.page_link("pages/11_Bitcoin.py", label="11. Bitcoin Model", icon="🌈")

st.markdown("---")
st.caption("Tip: You can use this central hub page or click any item directly from the left sidebar navigation menu.")