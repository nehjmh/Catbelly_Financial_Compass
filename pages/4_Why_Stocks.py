import streamlit as st
import pandas as pd

st.set_page_config(page_title="Why Stocks?", page_icon="📈", layout="wide")

st.title("📈 Why Stocks? (Understanding Equity & Real Value)")
st.markdown(
    "Before diving into stock picks or screeners, it helps to understand what you are actually buying, "
    "why the market grows over time, how companies build wealth, and what historical data reveals about market cycles."
)

st.markdown("---")

# --- INTERACTIVE TABS ---
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🧩 1. What is a Stock?",
    "🚀 2. Why Markets Rise",
    "🏢 3. How Companies Grow",
    "📊 4. Valuations & P/E",
    "🏢 5. Public Real Estate",
    "📜 6. Historical Data & Odds"
])

# ==========================================
# TAB 1: WHAT YOU ARE ACTUALLY BUYING
# ==========================================
with tab1:
    st.subheader("What are you actually doing when you buy a stock?")
    st.markdown(
        "Buying a share of stock isn't buying a digital lottery ticket or a casino chip. "
        "It is purchasing **genuine, legal co-ownership** in a real-world business enterprise."
    )
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.info("### 🤝 Fractional Ownership")
        st.markdown(
            "When you own 1 share of a public company, you own a proportional claim on:\n"
            "* **Physical & Digital Assets:** Buildings, factories, inventory, patents, and hardware.\n"
            "* **Net Profits:** Every dollar of cash flow left over after paying wages, debt, and operational costs.\n"
            "* **Future Expansion:** The compounded value of everything the company builds tomorrow."
        )

    with col_b:
        st.success("### ⚖️ Owner vs. Lender")
        st.markdown(
            "It helps to contrast stocks with traditional cash accounts or bonds:\n"
            "* **Savings / Bonds (Lender):** You loan cash to a bank or entity for a fixed interest rate. Your upside is capped at that interest rate.\n"
            "* **Stocks (Owner):** You own a piece of the engine itself. As the business grows its earnings, your upside has no artificial ceiling."
        )

    with st.expander("💡 Real-World Analogy: The Local Bakery"):
        st.markdown(
            "Imagine a neighborhood bakery worth $100,000 that earns $20,000 in net profit every year.\n\n"
            "If the owner divides the business into **1,000 equal shares** ($100 per share) and you buy **10 shares** ($1,000):\n"
            "* You literally own **1% of the bakery**.\n"
            "* You are entitled to **1% of the annual profits** ($200/year), whether paid out as cash or reinvested into new ovens to expand!"
        )

# ==========================================
# TAB 2: WHY THE STOCK MARKET GOES UP
# ==========================================
with tab2:
    st.subheader("Why does the overall stock market go up over time?")
    st.markdown(
        "Over multi-decade spans, stock market indices like the S&P 500 don't rise because of luck or speculation—they rise because of fundamental economic forces."
    )
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("### 📈 Productivity & Innovation")
        st.write(
            "Human ingenuity constantly improves efficiency. Better software, automation, and logistics allow companies to generate more output per hour of work, increasing net profit potential."
        )

    with c2:
        st.markdown("### 💰 Earnings Growth")
        st.write(
            "As global populations grow and consumer demand expands, public corporations sell more goods and services. Stock prices ultimately track corporate profit expansion over time."
        )

    with c3:
        st.markdown("### 🛡️ Built-in Inflation Protection")
        st.write(
            "When raw material costs and inflation rise, great businesses raise their consumer prices to protect margins. As revenue increases with inflation, corporate asset values adjust upward."
        )

# ==========================================
# TAB 3: HOW COMPANIES GROW (AND FAIL)
# ==========================================
with tab3:
    st.subheader("Why do some companies compound wealth while others shrink?")
    st.markdown(
        "Not all businesses are created equal. Investors develop strong beliefs about which companies will succeed based on how management handles capital and competition."
    )
    
    comparison_df = pd.DataFrame([
        {
            "Driver": "Capital Reinvestment",
            "Why Great Companies Grow": "Reinvesting profits into high-return projects (R&D, new locations, better tech) that compound future earnings.",
            "Why Struggling Companies Fail": "Wasting excess cash on bad acquisitions or low-return legacy projects."
        },
        {
            "Driver": "Competitive Moat",
            "Why Great Companies Grow": "Building strong pricing power, patents, or network effects so competitors cannot steal market share.",
            "Why Struggling Companies Fail": "Selling commodity products with zero pricing power, forcing them to cut prices to survive."
        },
        {
            "Driver": "Adaptability & Innovation",
            "Why Great Companies Grow": "Pivoting smoothly to new technology shifts (e.g., streaming, modern cloud hardware, online retail).",
            "Why Struggling Companies Fail": "Clinging to outdated business models until industry shifts make them obsolete."
        }
    ])
    
    st.table(comparison_df)

# ==========================================
# TAB 4: VALUATIONS & P/E RATIOS
# ==========================================
with tab4:
    st.subheader("Why do different sectors have totally different P/E ratios?")
    st.markdown(
        "The **Price-to-Earnings (P/E) ratio** tells you how many dollars investors are willing to pay today for every **$1.00 of annual net profit** a company earns."
    )
    
    st.markdown("### Comparing Two Real-World Sectors:")
    
    col_pe1, col_pe2 = st.columns(2)
    
    with col_pe1:
        st.warning("### ⚡ High Growth Tickers (e.g., Tech / Semi)")
        st.markdown(
            "**Typical P/E:** 25x – 40x+\n\n"
            "**Why investors pay more:** Investors expect earnings to double or triple over the coming years. "
            "They are paying a premium price today because they anticipate much larger profit checks tomorrow."
        )

    with col_pe2:
        st.info("### 🥤 Stable Income Tickers (e.g., Utilities / Staples)")
        st.markdown(
            "**Typical P/E:** 12x – 20x\n\n"
            "**Why investors pay less:** These companies are highly predictable and pay steady cash dividends, "
            "but their annual growth is slow. Investors pay a lower multiple because future profit growth is modest."
        )

# ==========================================
# TAB 5: PUBLIC REAL ESTATE (REITs)
# ==========================================
with tab5:
    st.subheader("Did you know you can own Real Estate on public exchanges?")
    st.markdown(
        "Many people believe real estate and stocks are completely separate asset classes. "
        "In reality, you can invest in real estate directly through publicly traded companies called **REITs (Real Estate Investment Trusts)**."
    )
    
    st.markdown("---")
    
    r_col1, r_col2 = st.columns(2)
    
    with r_col1:
        st.success("### 🏢 What is a REIT?")
        st.markdown(
            "A REIT is a company that owns, operates, or finances income-producing real estate. "
            "By buying shares in a REIT, you instantly own a slice of:\n"
            "* **Commercial Property:** Apartment complexes, shopping centers, and medical buildings.\n"
            "* **Modern Infrastructure:** Data centers, cell towers, and logistics warehouses."
        )

    with r_col2:
        st.info("### 💵 The 90% Dividend Advantage")
        st.markdown(
            "By law, REITs must pay out at least **90% of their taxable income** directly back to shareholders as cash distributions.\n\n"
            "This gives regular investors all the income benefits of being a landlord—**without dealing with mortgage applications, property management, or maintenance headaches!**"
        )

# ==========================================
# TAB 6: HISTORICAL DATA & ODDS
# ==========================================
with tab6:
    st.subheader("📜 What Does History Teach Us About Market Probability?")
    st.markdown(
        "Short-term stock movements are noisy and unpredictable, but over longer horizons, "
        "the market's upward bias creates compelling odds for patient investors."
    )
    
    st.markdown("---")
    
    # METRICS ROW
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric(label="Average Bull Market Length", value="~2.7 to 5 Years", delta="Average Gain: +180% to +400%")
    with m2:
        st.metric(label="Average Bear Market Length", value="~9 to 15 Months", delta="-35% Average Drop", delta_color="inverse")
    with m3:
        st.metric(label="Probability of Profit (20-Yr Horizon)", value="100%", delta="Historically Zero Loss Spans")

    st.markdown("### 🎲 The Time Horizon Game: Odds of a Positive Return")
    st.markdown(
        "If you zoom in on daily moves, the stock market looks almost like a coin toss. "
        "However, as you lengthen your holding period, the underlying growth of business earnings takes over."
    )

    odds_data = pd.DataFrame([
        {"Timeframe": "1 Day", "Historically Up": "54%", "Historically Down": "46%", "Market Character": "Coin Flip / Noise"},
        {"Timeframe": "Any 10-Day Period", "Historically Up": "~59%", "Historically Down": "~41%", "Market Character": "Slight Structural Edge"},
        {"Timeframe": "1 Month", "Historically Up": "63%", "Historically Down": "37%", "Market Character": "Short-Term Trend"},
        {"Timeframe": "1 Year", "Historically Up": "73%", "Historically Down": "27%", "Market Character": "Earnings Dominance Starts"},
        {"Timeframe": "5 Years", "Historically Up": "88%", "Historically Down": "12%", "Market Character": "Strong Growth Edge"},
        {"Timeframe": "10 Years", "Historically Up": "95%", "Historically Down": "5%", "Market Character": "High Probability Wealth Building"},
        {"Timeframe": "20 Years", "Historically Up": "100%", "Historically Down": "0%", "Market Character": "Historical Certainty of Profit"}
    ])
    st.table(odds_data)

    st.markdown("---")
    
    col_h1, col_h2 = st.columns(2)
    
    with col_h1:
        st.success("### 🐂 Bull vs. 🐻 Bear Markets")
        st.markdown(
            "* **Bear Markets Are Short & Sharp:** Historically, bear markets (declines of 20%+) last about **9 to 15 months** on average.\n"
            "* **Bull Markets Are Long & Generous:** Expansion cycles last significantly longer—averaging **3 to 5+ years**—and capture far more total gain than bear markets destroy.\n"
            "* **Time Spent Up:** Across 90+ years of modern market history, stocks have spent roughly **78% of all time in expansion/bull market mode**."
        )

    with col_h2:
        st.warning("### ⚠️ The Cost of Missing the Best Days")
        st.markdown(
            "* **Clustered Volatility:** The stock market's best single trading days almost always occur during bear markets or the early weeks of a recovery.\n"
            "* **Missing top performance:** Over 30-year periods, missing just the **10 best trading days** can cut an investor's overall total returns by nearly **50%**.\n"
            "* **Takeaway:** Trying to jump in and out of the market to avoid downturns usually results in missing the explosive recovery days that build real wealth."
        )