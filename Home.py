import streamlit as st

st.set_page_config(
    page_title="Catbelly Financial Compass",
    page_icon="🧭",
    layout="wide"
)

st.title("🧭 Catbelly Financial Compass")
st.write("Welcome to the **Catbelly Financial Compass**! This interactive curriculum guides you step-by-step from foundational financial literacy and budgeting to advanced valuation, portfolio engineering, and paper trading.")

st.write("---")

# ==========================================
# PHASE 1: FOUNDATIONS & FINANCIAL LITERACY
# ==========================================
st.markdown("### 🌱 Phase 1: Foundations & Financial Literacy")
st.caption("Establish baseline financial knowledge, set spending guidelines, and demystify financial vocabulary.")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 1. Financial Literacy Test")
    st.write("Assess your baseline financial knowledge through interactive questions covering fundamental investing principles, compounding, risk management, and key financial concepts.")
    st.markdown("📖 [Take Literacy Test](Financial_Literacy_Test)")

    st.markdown("#### 3. Financial Decoder")
    st.write("Demystify complex balance sheet terms, financial metrics, and evaluate multi-vehicle compounding engines against consumer inflation and M2 currency debasement hurdles.")
    st.markdown("🧮 [Open Financial Decoder](Financial_Decoder)")

with col2:
    st.markdown("#### 2. Budgeting 101")
    st.write("Establish structural budgeting rules, track monthly cash inflows vs. outflows, optimize discretionary spending, and direct persistent free cash flow toward investment vehicles.")
    st.markdown("💡 [Open Budgeting Tool](Budgeting_101)")

    st.markdown("#### 4. What are ETFs?")
    st.write("Your comprehensive guide to understanding exchange-traded funds, examining structural cost advantages, exploring popular asset categories, and utilizing live search tools.")
    st.markdown("📘 [Open ETF Guide](What_are_ETFs)")

st.write("---")

# ==========================================
# PHASE 2: EQUITY PRINCIPLES & BACKTESTING
# ==========================================
st.markdown("### 📉 Phase 2: Equity Principles & Backtesting")
st.caption("Understand why stock ownership builds real wealth, open accounts, and run historical market simulations.")

col3, col4 = st.columns(2)

with col3:
    st.markdown("#### 5. Why Stocks?")
    st.write("Explore the historical case for equities, inflation hedging, purchasing power protection, and why ownership in cash-flowing businesses remains a premier engine for long-term wealth creation.")
    st.markdown("📈 [Explore Equity Principles](Why_Stocks)")

    st.markdown("#### 6. Random Backtest")
    st.write("Run Monte Carlo simulations and historical asset backtests to stress-test portfolio returns across randomized market environments, drawdowns, and volatility cycles.")
    st.markdown("📊 [Run Backtests](Random_Backtest)")

with col4:
    st.markdown("#### 7. Opening Your First Brokerage")
    st.write("A practical walkthrough for setting up a taxable brokerage, Roth IRA, or traditional retirement account, including execution types, account choices, and transfer protocols.")
    st.markdown("🏦 [Read Brokerage Guide](Opening_Your_First_Brokerage)")

st.write("---")

# ==========================================
# PHASE 3: ADVANCED ANALYSIS & IMPLEMENTATION
# ==========================================
st.markdown("### 🔬 Phase 3: Advanced Analysis & Implementation")
st.caption("Evaluate company fundamentals, engineer multi-asset portfolios, analyze macroeconomic shifts, and model digital asset valuation.")

col5, col6 = st.columns(2)

with col5:
    st.markdown("#### 8. Reverse Screener")
    st.write("Type in any ticker to evaluate quality metrics against target benchmarks (ROIC, ROE, Margins, PEG), check the 200-week moving average, run 2-stage DCF fair value estimates, and view analyst consensus targets.")
    st.markdown("🔍 [Open Reverse Screener](Reverse_Screener)")

    st.markdown("#### 10. Paper Trading Lab")
    st.write("Practice trade execution with real-time price lookups. Track target allocations, maintain a simulated portfolio, and visualize holdings across your allocation pyramid.")
    st.markdown("📝 [Open Paper Trading Lab](Paper_Trading_Lab)")

    st.markdown("#### 12. Bitcoin")
    st.write("Examine long-term logarithmic valuation channels for digital assets. Stress-test historical cycle tops/bottoms, power-law regression curves, and digital scarcity dynamics.")
    st.markdown("🪙 [Open Bitcoin Model](Bitcoin)")

    st.markdown("#### 14. Peer Comparison")
    st.write("Benchmark individual stocks directly against their industry competitors across valuation multiples, growth metrics, and balance sheet strength.")
    st.markdown("⚖️ [Open Peer Comparison](Peer_Comparison)")

with col6:
    st.markdown("#### 9. Building A Portfolio")
    st.write("Architect balanced growth and income structures. Combine broad-market core holdings with income-generating distribution engines and model dividend reinvestment scenarios.")
    st.markdown("💼 [Open Portfolio Builder](Building_A_Portfolio)")

    st.markdown("#### 11. Jordi Visser AI Nexus")
    st.write("Analyze the AI velocity shift, compressed corporate terminal values, power grid bottlenecks, tokenization, and dynamic capital reallocation strategies.")
    st.markdown("⚡ [Open Jordi Visser AI Nexus](Jordi_Visser_AI_Nexus)")

    st.markdown("#### 13. Sample Portfolios")
    st.write("Explore pre-built professional allocation models designed for different risk tolerances, time horizons, and wealth-building objectives.")
    st.markdown("📁 [Open Sample Portfolios](Sample_Portfolios)")

st.write("---")

# ==========================================
# QUICK JUMP DIRECTORY
# ==========================================
st.markdown("### 🗺️ Quick Jump Directory")
st.caption("Direct access to all 14 modules in numerical order:")

jump_col1, jump_col2 = st.columns(2)

with jump_col1:
    st.markdown("""
    * 1. [Financial Literacy Test](Financial_Literacy_Test)
    * 2. [Budgeting 101](Budgeting_101)
    * 3. [Financial Decoder](Financial_Decoder)
    * 4. [What are ETFs?](What_are_ETFs)
    * 5. [Why Stocks?](Why_Stocks)
    * 6. [Random Backtest](Random_Backtest)
    * 7. [Opening Your First Brokerage](Opening_Your_First_Brokerage)
    """)

with jump_col2:
    st.markdown("""
    * 8. [Reverse Screener](Reverse_Screener)
    * 9. [Building A Portfolio](Building_A_Portfolio)
    * 10. [Paper Trading Lab](Paper_Trading_Lab)
    * 11. [Jordi Visser AI Nexus](Jordi_Visser_AI_Nexus)
    * 12. [Bitcoin](Bitcoin)
    * 13. [Sample Portfolios](Sample_Portfolios)
    * 14. [Peer Comparison](Peer_Comparison)
    """)