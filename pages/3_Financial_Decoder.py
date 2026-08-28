import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_page_config(
    page_title="3. Financial Decoder",
    page_icon="🎟️",
    layout="wide"
)

st.title("🎟️ Module 3: Financial Decoder")
st.markdown("Demystify essential financial vocabulary, model currency debasement hurdles, and compare compounding vehicles against real-world inflation.")

st.markdown("---")

# Setup Tabs
tab1, tab2, tab3 = st.tabs([
    "📖 Terms Decoder", 
    "⏳ Yield and Purchasing Power Protection", 
    "📊 Hurdle Rate Simulator"
])

# ==============================================================================
# TAB 1: TERMS DECODER
# ==============================================================================
with tab1:
    st.subheader("📖 Terms Decoder & Financial Glossary")
    st.caption("A structured dictionary of key financial concepts, ranging from everyday investing basics to advanced valuation metrics.")

    # --------------------------------------------------------------------------
    # CATEGORY 1: FOUNDATIONAL INVESTING & SAVINGS BASICS
    # --------------------------------------------------------------------------
    st.markdown("### 🌱 1. Foundational Concepts")
    
    with st.expander("🔹 Inflation & Purchasing Power"):
        st.write("**Definition:** Inflation is the gradual increase in prices over time. Purchasing power is the actual amount of goods or services one unit of money can buy.")
        st.write("**Why It Matters:** If your cash earns 2% in bank interest while inflation runs at 4%, you are losing 2% of your actual buying power every year.")

    with st.expander("🔹 Compound Interest / Compounding"):
        st.write("**Definition:** Earning interest on top of the interest you've already earned, creating an accelerating growth curve over time.")
        st.write("**Why It Matters:** Compounding turns small, consistent investments into substantial long-term wealth because time multiplies exponential growth.")

    with st.expander("🔹 Dividends & Yield"):
        st.write("**Definition:** A dividend is a cash payment made by a corporation to its shareholders out of its profits. Dividend yield is the annual dividend payout divided by the current stock price (expressed as a percentage).")
        st.write("**Why It Matters:** Dividends provide regular income without requiring you to sell your underlying shares.")

    with st.expander("🔹 Stocks vs. Bonds"):
        st.write("**Definition:** A stock represents equity (fractional ownership) in a business. A bond is an IOU (debt) where you lend money to a government or corporation in exchange for fixed interest payments.")
        st.write("**Why It Matters:** Stocks offer higher long-term growth and inflation protection, while bonds offer lower-risk fixed nominal payouts.")

    with st.expander("🔹 Asset Allocation & Diversification"):
        st.write("**Definition:** Asset allocation is how you split your money among different categories (stocks, bonds, real estate, cash). Diversification is spreading capital across multiple investments to reduce risk.")
        st.write("**Why It Matters:** Don't put all your eggs in one basket. Proper allocation protects your portfolio if one asset class drops.")

    # --------------------------------------------------------------------------
    # CATEGORY 2: CORPORATE METRICS & VALUATION
    # --------------------------------------------------------------------------
    st.markdown("### 🔍 2. Valuation & Quality Metrics")

    with st.expander("🔸 ROIC (Return on Invested Capital)"):
        st.write("**Definition:** Measures how efficiently a business converts capital (debt and equity) into net operating profits.")
        st.write("**Why It Matters:** High-ROIC companies possess strong economic moats, allowing them to reinvest cash at elevated return rates and raise prices during inflationary periods.")

    with st.expander("🔸 P/E Ratio (Price-to-Earnings) & PEG Ratio"):
        st.write("**Definition:** P/E compares a stock's market price to its annual per-share earnings. The PEG ratio divides the P/E by the expected earnings growth rate.")
        st.write("**Why It Matters:** A P/E shows how expensive a stock is relative to current profits, while PEG accounts for future growth speed (a PEG below 1.0 often signals good value).")

    with st.expander("🔸 2-Stage DCF (Discounted Cash Flow)"):
        st.write("**Definition:** A valuation formula that projects a company's free cash flow for several years into the future (Stage 1), estimates a perpetual steady state (Stage 2), and discounts those cash flows back to present-day dollars.")
        st.write("**Why It Matters:** It estimates the true intrinsic fair value of a company, telling you if a stock is cheap or overpriced relative to its future earnings.")

    with st.expander("🔸 Terminal Value"):
        st.write("**Definition:** The estimated total value of a company's cash flows beyond a specific forecast horizon (typically 5 to 10 years out).")
        st.write("**Why It Matters:** In traditional models, terminal value accounts for 60%–80% of a stock's calculated value. AI disruption can shrink these multi-decade terminal expectations rapidly.")

    # --------------------------------------------------------------------------
    # CATEGORY 3: MACROECONOMICS & ADVANCED ENGINES
    # --------------------------------------------------------------------------
    st.markdown("### ⚡ 3. Macroeconomics & Income Engines")

    with st.expander("🔺 M2 Money Supply"):
        st.write("**Definition:** The total measure of currency circulating in the economy, including physical cash, checking accounts, savings deposits, and money market funds.")
        st.write("**Why It Matters:** Rapid expansion of M2 increases the overall units of money, setting the true baseline hurdle rate needed to prevent currency debasement from eroding your wealth.")

    with st.expander("🔺 Debasement Hurdle Rate"):
        st.write("**Definition:** The benchmark return (~10%) required to beat official consumer inflation (CPI), money supply growth (M2), and asset price increases combined.")
        st.write("**Why It Matters:** Returns below this hurdle lead to a hidden, steady loss of actual purchasing power over time.")

    with st.expander("🔺 Option Volatility Harvest"):
        st.write("**Definition:** Generating cash distribution yield by writing (selling) call options or cash-secured put options against index holdings (used by ETFs like SPYI, QQQI, and STRC).")
        st.write("**Why It Matters:** Converts market volatility into immediate monthly income streams to clear high hurdle rates without liquidating core shares.")


# ==============================================================================
# TAB 2: YIELD & PURCHASING POWER PROTECTION
# ==============================================================================
with tab2:
    st.subheader("⏳ Yield & Purchasing Power Protection")
    st.markdown("""
    To preserve wealth over long time horizons, portfolios must clear the **10% Real Debasement Hurdle**—a combined measure of official CPI inflation, currency supply expansion (M2 growth), and asset-price inflation.
    """)
    
    st.markdown("---")
    
    # Key Summary Metrics
    st.markdown("### 🎯 Real Return Benchmark vs. 10% Hurdle")
    m_col1, m_col2, m_col3, m_col4 = st.columns(4)
    
    with m_col1:
        st.metric("Traditional Savings / HYSAs", "4.5%", "-5.5% Real Decay", delta_color="inverse")
    with m_col2:
        st.metric("10-Year US Treasury", "4.2%", "-5.8% Real Decay", delta_color="inverse")
    with m_col3:
        st.metric("S&P 500 Historical Core", "10.2%", "+0.2% Net Protection", delta_color="normal")
    with m_col4:
        st.metric("High-Yield Equity/Income", "12.5%+", "+2.5% Net Surplus", delta_color="normal")

    st.markdown("---")
    
    # Comparative Matrix
    st.markdown("### 🛡️ Purchasing Power Protection Across Asset Classes")
    
    comparison_data = [
        {
            "Asset Class": "Cash & Savings Accounts",
            "Nominal Yield (Est.)": "0.5% - 4.5%",
            "10% Hurdle Gap": "❌ -5.5% to -9.5%",
            "Purchasing Power Trajectory": "Severe Guaranteed Loss",
            "Equity Advantage / Moat Mechanism": "None. Fixed nominal value decays constantly against expanding money supply."
        },
        {
            "Asset Class": "Fixed Income / Bonds (AGG, BND)",
            "Nominal Yield (Est.)": "4.0% - 5.5%",
            "10% Hurdle Gap": "❌ -4.5% to -6.0%",
            "Purchasing Power Trajectory": "Moderate Net Decay",
            "Equity Advantage / Moat Mechanism": "Capped upside. Coupons are nominal and cannot adjust upward with inflation."
        },
        {
            "Asset Class": "Broad Market Equities (SPY, QQQ)",
            "Nominal Yield (Est.)": "10.0% - 12.0%",
            "10% Hurdle Gap": "✅ +0.0% to +2.0%",
            "Purchasing Power Trajectory": "Full Protection & Growth",
            "Equity Advantage / Moat Mechanism": "Companies pass rising costs to consumers; underlying earnings & revenues expand with inflation."
        },
        {
            "Asset Class": "High-Yield Option Engines (SPYI, QQQI, STRC)",
            "Nominal Yield (Est.)": "11.0% - 14.0%",
            "10% Hurdle Gap": "✅ +1.0% to +4.0%",
            "Purchasing Power Trajectory": "High Cash Flow Surplus",
            "Equity Advantage / Moat Mechanism": "Option volatility premiums monetized into monthly cash flow to immediately exceed the 10% bar."
        }
    ]
    
    st.table(pd.DataFrame(comparison_data))
    
    st.info("""
    💡 **Core Economic Reality:** Fixed nominal yields (savings accounts, CDs, standard bonds) lock in negative real returns once the full 10% debasement hurdle is applied. Stock market structures act as a dynamic hedge because corporate earnings and cash-distribution engines naturally scale alongside nominal economic expansion.
    """)

# ==============================================================================
# TAB 3: HURDLE RATE SIMULATOR
# ==============================================================================
with tab3:
    st.subheader("📊 Interactive Hurdle Rate Simulator")
    st.caption("Model how initial capital grows or degrades when pitted against inflation and currency debasement over time.")
    
    col_sim_left, col_sim_right = st.columns([1, 2])
    
    with col_sim_left:
        st.markdown("#### ⚙️ Simulation Controls")
        initial_inv = st.number_input("Initial Investment ($)", value=100000, step=10000)
        years = st.slider("Time Horizon (Years)", min_value=1, max_value=30, value=15)
        
        hurdle_rate = st.slider("Debasement Hurdle Rate (%)", min_value=1.0, max_value=15.0, value=10.0, step=0.5) / 100.0
        asset_return = st.slider("Asset Nominal Return (%)", min_value=0.0, max_value=20.0, value=12.0, step=0.5) / 100.0

    with col_sim_right:
        timeline = np.arange(0, years + 1)
        
        # Calculations
        nominal_values = initial_inv * ((1 + asset_return) ** timeline)
        hurdle_baseline = initial_inv * ((1 + hurdle_rate) ** timeline)
        real_purchasing_power = nominal_values / ((1 + hurdle_rate) ** timeline)
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=timeline, y=nominal_values,
            mode='lines+markers', name='Nominal Portfolio Value',
            line=dict(color='#2E7D32', width=3)
        ))
        
        fig.add_trace(go.Scatter(
            x=timeline, y=hurdle_baseline,
            mode='lines', name='10% Hurdle Baseline',
            line=dict(color='#D32F2F', width=2, dash='dash')
        ))
        
        fig.add_trace(go.Scatter(
            x=timeline, y=real_purchasing_power,
            mode='lines', name='Real Purchasing Power',
            line=dict(color='#0288D1', width=3)
        ))
        
        fig.update_layout(
            title="Nominal Growth vs. Debasement Hurdle vs. Real Purchasing Power",
            xaxis_title="Years",
            yaxis_title="Value ($)",
            hovermode="x unified",
            height=420,
            margin=dict(l=20, r=20, t=50, b=20)
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
    net_real_diff = real_purchasing_power[-1] - initial_inv
    if net_real_diff >= 0:
        st.success(f"✅ **Outcome:** At an asset yield of {asset_return*100:.1f}%, your investment clears the {hurdle_rate*100:.1f}% hurdle. Real purchasing power grows by **+${net_real_diff:,.2f}** over {years} years.")
    else:
        st.error(f"❌ **Outcome:** At an asset yield of {asset_return*100:.1f}%, your investment fails to clear the {hurdle_rate*100:.1f}% hurdle. Real purchasing power shrinks by **-${abs(net_real_diff):,.2f}** over {years} years.")