import streamlit as st

st.set_page_config(
    page_title="Catbelly Financial Compass",
    page_icon="🧭",
    layout="wide"
)

# --- HEADER ---
st.title("🧭 Catbelly Financial Compass")
st.markdown("Welcome to the **Catbelly Financial Compass**! This interactive curriculum guides you step-by-step from foundational financial literacy and budgeting to advanced valuation, portfolio engineering, and paper trading.")

st.markdown("---")

# ==============================================================================
# PHASE 1: FOUNDATIONS & FINANCIAL LITERACY
# ==============================================================================
st.header("🌱 Phase 1: Foundations & Financial Literacy")
st.caption("Establish baseline financial literacy, set spending guidelines, and demystify financial vocabulary.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Financial Literacy Test")
    st.markdown("Assess your baseline financial knowledge through interactive questions covering fundamental investing principles, compounding, risk management, and key financial concepts.")
    st.page_link("pages/1_Financial_Literacy_Test.py", label="Take Literacy Test", icon="📝")

    st.subheader("3. Financial Decoder")
    st.markdown("Demystify complex balance sheet terms, financial metrics, and evaluate multi-vehicle compounding engines against consumer inflation and M2 currency debasement hurdles.")
    st.page_link("pages/3_Financial_Decoder.py", label="Open Financial Decoder", icon="📖")

with col2:
    st.subheader("2. Budgeting 101")
    st.markdown("Establish structural budgeting rules, track monthly cash inflows vs. outflows, optimize discretionary spending, and direct persistent free cash flow toward investment vehicles.")
    st.page_link("pages/2_Budgeting_101.py", label="Open Budgeting Tool", icon="💡")

    st.subheader("4. What are ETFs?")
    st.markdown("Your comprehensive guide to understanding exchange traded funds, examining structural cost advantages, exploring popular asset categories, and utilizing live search tools.")
    st.page_link("pages/4_What_are_ETFs.py", label="Open ETF Guide", icon="📊")

st.markdown("---")

# ==============================================================================
# PHASE 2: EQUITY PRINCIPLES & BACKTESTING
# ==============================================================================
st.header("📈 Phase 2: Equity Principles & Backtesting")
st.caption("Understand why stock ownership builds real wealth, open accounts, and run historical market simulations.")

col3, col4 = st.columns(2)

with col3:
    st.subheader("5. Why Stocks?")
    st.markdown("Explore the historical case for equities, inflation hedging, purchasing power protection, and why ownership in cash-flowing businesses remains a premier engine for long-term wealth creation.")
    st.page_link("pages/5_Why_Stocks.py", label="Explore Equity Principles", icon="📈")

    st.subheader("6. Random Backtest")
    st.markdown("Run Monte Carlo simulations and historical asset backtests to stress test portfolio returns across randomized market environments, drawdowns, and volatility cycles.")
    st.page_link("pages/6_Random_Backtest.py", label="Run Backtests", icon="🎲")

with col4:
    st.subheader("7. Opening Your First Brokerage")
    st.markdown("A practical walkthrough for setting up a taxable brokerage, Roth IRA, or traditional retirement account, including execution types, account choices, and transfer protocols.")
    st.page_link("pages/7_Opening_Your_First_Brokerage.py", label="Read Brokerage Guide", icon="🏛️")

st.markdown("---")

# ==============================================================================
# PHASE 3: ADVANCED ANALYSIS & IMPLEMENTATION
# ==============================================================================
st.header("🔬 Phase 3: Advanced Analysis & Implementation")
st.caption("Evaluate company fundamentals, engineer multi-asset portfolios, analyze macroeconomic shifts, and model digital asset valuation.")

col5, col6 = st.columns(2)

with col5:
    st.subheader("8. Reverse Screener")
    st.markdown("Type in any ticker to evaluate quality metrics against target benchmarks (ROIC, ROE, Margins, PEG), check the 200-week moving average, run 2-stage DCF fair value estimates, and view analyst consensus targets.")
    st.page_link("pages/8_Reverse_Screener.py", label="Open Reverse Screener", icon="🔍")

    st.subheader("10. Paper Trading Lab")
    st.markdown("Practice trade execution with real-time price lookups. Track target allocations, maintain a simulated portfolio, and visualize holdings across your allocation pyramid.")
    st.page_link("pages/10_Paper_Trading_Lab.py", label="Open Paper Trading Lab", icon="📋")

    st.subheader("12. Bitcoin, Ethereum & Solana")
    st.markdown("Examine long-term valuation channels for digital assets, layer-1 institutional settlement, and AI agent tokenization models.")
    st.page_link("pages/12_Bitcoin_Ethereum_Solana.py", label="Open Crypto & Layer-1 Model", icon="🪙")

    st.subheader("14. Sample Portfolios")
    st.markdown("Explore pre-built professional allocation models designed for different risk tolerances, time horizons, and wealth building objectives.")
    st.page_link("pages/14_Sample_Portfolios.py", label="Open Sample Portfolios", icon="📊")

with col6:
    st.subheader("9. Building A Portfolio")
    st.markdown("Architect balanced growth and income structures. Combine broad market core holdings with income-generating distribution engines and model dividend reinvestment scenarios.")
    st.page_link("pages/9_Building_A_Portfolio.py", label="Open Portfolio Builder", icon="💼")

    st.subheader("11. Jordi Visser AI Nexus")
    st.markdown("Analyze the AI velocity shift, compressed corporate terminal values, power grid bottlenecks, tokenization, and dynamic capital reallocation strategies.")
    st.page_link("pages/11_Jordi_Visser_AI_Nexus.py", label="Open Jordi Visser AI Nexus", icon="⚡")

    st.subheader("13. Peer Comparison")
    st.markdown("Benchmark individual stocks directly against their industry competitors across valuation multiples, growth metrics, and balance sheet strength.")
    st.page_link("pages/13_Peer_Comparison.py", label="Open Peer Comparison", icon="⚖️")

    st.subheader("15. Google Trends Tracker")
    st.markdown("Track macro search momentum, retail attention spikes, and narrative shifts across custom timelines.")
    st.page_link("pages/15_Google_Trends_Tracker.py", label="Open Google Trends Tracker", icon="📈")

st.markdown("---")

# ==============================================================================
# QUICK JUMP DIRECTORY
# ==============================================================================
st.markdown("### 📖 Quick Jump Directory")
st.markdown("Direct access to all 15 modules in numerical order:")

qc1, qc2 = st.columns(2)
with qc1:
    st.markdown("""
    * 1. [Financial Literacy Test](//@page=1_Financial_Literacy_Test)
    * 2. [Budgeting 101](//@page=2_Budgeting_101)
    * 3. [Financial Decoder](//@page=3_Financial_Decoder)
    * 4. [What are ETFs?](//@page=4_What_are_ETFs)
    * 5. [Why Stocks?](//@page=5_Why_Stocks)
    * 6. [Random Backtest](//@page=6_Random_Backtest)
    * 7. [Opening Your First Brokerage](//@page=7_Opening_Your_First_Brokerage)
    * 8. [Reverse Screener](//@page=8_Reverse_Screener)
    """)
with qc2:
    st.markdown("""
    * 9. [Building A Portfolio](//@page=9_Building_A_Portfolio)
    * 10. [Paper Trading Lab](//@page=10_Paper_Trading_Lab)
    * 11. [Jordi Visser AI Nexus](//@page=11_Jordi_Visser_AI_Nexus)
    * 12. [Bitcoin, Ethereum & Solana](//@page=12_Bitcoin_Ethereum_Solana)
    * 13. [Peer Comparison](//@page=13_Peer_Comparison)
    * 14. [Sample Portfolios](//@page=14_Sample_Portfolios)
    * 15. [Google Trends Tracker](//@page=15_Google_Trends_Tracker)
    """)