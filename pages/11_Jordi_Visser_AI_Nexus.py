import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_page_config(
    page_title="10. Jordi Visser Macro & AI Nexus",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Page 10: The AI Macro Nexus & Disruption Framework")
st.caption("Strategic Insights & Market Philosophy from Macro Analyst Jordi Visser")

st.markdown("""
### *“Set it and Forget it is Dead” — Navigating the AI Velocity Shift*
Artificial Intelligence is drastically shortening corporate life cycles, driving hyper-disruption, and forcing a fundamental shift in portfolio strategy. Traditional long-term equity valuation models like DCF (Discounted Cash Flow) rely on terminal value assumptions that are collapsing under the weight of AI acceleration.
""")

st.markdown("---")

# ==============================================================================
# SECTION 1: CORE PILLARS OF VISSER'S THESIS
# ==============================================================================
st.header("🧠 1. Core Macro & Investment Pillars")

col1, col2 = st.columns(2)

with col1:
    st.subheader("⏳ The Death of Terminal Value & 'Set-it-and-Forget-it'")
    st.markdown("""
    * **Compressed Terminal Value:** Traditional stock valuation models assume companies generate cash flows 10 to 20 years into the future. AI capability acceleration means business models can be disrupted or rendered obsolete in 2 to 5 years.
    * **No More Passive Buy-and-Hold:** Holding legacy equity indices blindly exposes investors to hidden "value traps"—incumbents whose moats are eroding faster than balance sheets can adjust.
    * **Active Adaptability:** Portfolios require continuous monitoring of technological moats, capex efficiency, and real-time revenue velocity.
    """)

    st.subheader("🌐 Tokenization & Modern Financial Infrastructure")
    st.markdown("""
    * **On-Chain Settlement & Liquidity:** Tokenization of real-world assets (RWAs), equities, and monetary reserves is removing friction, enabling 24/7 global liquidity settlement.
    * **Digital Hard Assets:** As fiat software systems expand and debasement continues, digital assets (Bitcoin/Solana) and decentralized infrastructure become primary structural hedges.
    """)

with col2:
    st.subheader("🚀 AI Acceleration & Power/Compute Moats")
    st.markdown("""
    * **Energy & Compute Infrastructure:** The true winners of early-phase AI adoption are not just model builders, but the energy suppliers, natural gas pipelines, nuclear providers, and semiconductor memory manufacturers feeding the compute grid.
    * **Asymmetric Winner-Take-All Dynamics:** AI adoption curves are non-linear; companies leveraging proprietary data flywheel loops widen competitive moats exponentially.
    * **Software Friction to Zero:** Zero marginal cost of code creation means legacy SaaS models pricing per seat face intense margin pressure from open-source and agentic workflows.
    """)

st.markdown("---")

# ==============================================================================
# SECTION 2: INTERACTIVE SIMULATION - TERMINAL VALUE COMPRESSION MODEL
# ==============================================================================
st.header("📉 2. Terminal Value Compression & Valuation Model")
st.markdown("""
Explore how shrinking terminal value horizons impact theoretical equity valuations. 
Adjust the **AI Disruption Horizon** slider to see how AI velocity alters present values compared to traditional 20-year DCF assumptions.
""")

col_sim1, col_sim2 = st.columns([1, 2])

with col_sim1:
    st.subheader("Model Parameters")
    initial_fcf = st.number_input("Base Free Cash Flow ($M):", value=100.0, step=10.0)
    discount_rate = st.slider("Discount Rate (WACC %):", min_value=5.0, max_value=15.0, value=9.0, step=0.5) / 100
    base_growth = st.slider("Near-Term Growth Rate (%):", min_value=0.0, max_value=25.0, value=12.0, step=1.0) / 100
    half_life_years = st.slider("AI Disruption Horizon (Years):", min_value=3, max_value=20, value=7, step=1,
                                help="Number of years before AI disruption drastically degrades terminal cash flows.")

with col_sim2:
    years = np.arange(1, 21)
    
    # Traditional Cash Flow stream
    trad_cf = [initial_fcf * ((1 + base_growth) ** t) for t in range(20)]
    trad_pv = [cf / ((1 + discount_rate) ** (t + 1)) for t, cf in enumerate(trad_cf)]
    
    # AI Disrupted Cash Flow stream
    ai_cf = []
    for t in range(20):
        if t < half_life_years:
            cf = initial_fcf * ((1 + base_growth) ** t)
        else:
            decay_factor = 0.65 ** (t - half_life_years + 1)
            cf = initial_fcf * ((1 + base_growth) ** half_life_years) * decay_factor
        ai_cf.append(cf)
    
    ai_pv = [cf / ((1 + discount_rate) ** (t + 1)) for t, cf in enumerate(ai_cf)]

    total_trad_val = sum(trad_pv)
    total_ai_val = sum(ai_pv)
    pct_haircut = ((total_ai_val - total_trad_val) / total_trad_val) * 100

    fig_dcf = go.Figure()
    fig_dcf.add_trace(go.Bar(x=years, y=trad_pv, name="Traditional DCF (20-Yr Horizon)", marker_color="#3366CC", opacity=0.7))
    fig_dcf.add_trace(go.Bar(x=years, y=ai_pv, name="AI Disrupted DCF", marker_color="#FF4B4B", opacity=0.85))

    fig_dcf.update_layout(
        title=f"Present Value of Annual Cash Flows (Implied Valuation Haircut: {pct_haircut:.1f}%)",
        xaxis_title="Year",
        yaxis_title="Present Value ($M)",
        barmode="overlay",
        template="plotly_white",
        height=400,
        legend=dict(orientation="h", y=1.1, x=0)
    )
    
    st.plotly_chart(fig_dcf, use_container_width=True)

    m1, m2, m3 = st.columns(3)
    m1.metric("Legacy Model Value", f"${total_trad_val:,.1f}M")
    m2.metric("AI-Adjusted Model Value", f"${total_ai_val:,.1f}M")
    m3.metric("Terminal Value Loss", f"{pct_haircut:.1f}%", delta_color="inverse")

st.markdown("---")

# ==============================================================================
# SECTION 3: VISSER'S PORTFOLIO ALLOCATION MATRIX
# ==============================================================================
st.header("🧩 3. The AI Macro Portfolio Framework")
st.markdown("How to structure capital to capture upside velocity while insulating against terminal value erosion.")

framework_data = [
    {
        "Tier / Layer": "1. Compute & Energy Foundation",
        "Strategic Role": "Bottleneck Monopolies & Power",
        "Target Assets / Tickers": "Semiconductors (NVDA, TSM), Power & Gas Infrastructure, Memory (MU)",
        "Key Investment Thesis": "Provides physical infrastructure essential to keep AI models running regardless of which software applications win."
    },
    {
        "Tier / Layer": "2. High-Yield Income Engines",
        "Strategic Role": "Cash Flow Generation",
        "Target Assets / Tickers": "Option-Income & High-Yield ETFs (SPYI, QQQI, STRC, CHPY, WeeklyPay Set)",
        "Key Investment Thesis": "Harvests elevated market volatility to generate high cash flow payouts, enabling continuous dry-powder deployment."
    },
    {
        "Tier / Layer": "3. Sovereign & Digital Scarcity",
        "Strategic Role": "Fiscal Debasement & Tokenization",
        "Target Assets / Tickers": "Bitcoin (BTC / IBIT), Hard Assets, Solana / Tokenized Networks",
        "Key Investment Thesis": "Protects against accelerating central bank balance sheet expansion and monetary debasement as tech drives deflation."
    },
    {
        "Tier / Layer": "4. Legacy SaaS & At-Risk Incumbents",
        "Strategic Role": "Underweight / Avoidance",
        "Target Assets / Tickers": "Per-Seat SaaS Models, Low-Moat Outsourcing, Unhedged Real Estate",
        "Key Investment Thesis": "High vulnerability to zero-marginal-cost software tools and AI agent displacement."
    }
]

df_framework = pd.DataFrame(framework_data)

st.table(df_framework)

st.markdown("""
> **Key Takeaway:** In an era defined by AI acceleration and monetary expansion, active positioning requires balancing hard asset scarcity, physical compute bottlenecks, and continuous cash flow generation.
""")