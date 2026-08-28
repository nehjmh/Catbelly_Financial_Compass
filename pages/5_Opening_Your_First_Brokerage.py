import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Opening Your First Brokerage Account",
    page_icon="🚪",
    layout="wide"
)

st.title("🚪 Opening Your First Brokerage Account")
st.markdown(
    "Taking the step from a traditional bank to an investment brokerage can feel intimidating, "
    "but the process is simpler than most people expect. Here is exactly what to expect when opening "
    "and using your first account."
)

st.markdown("---")

# --- NAVIGATION TABS ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📋 1. What You Need to Sign Up",
    "🏢 2. Major Brokerages Compared",
    "📂 3. Account Types Explained",
    "🧩 4. Fractional Shares & Minimums",
    "🛒 5. What Buying a Stock Looks Like"
])

# ==========================================
# TAB 1: SIGNUP PROCESS & REQUIREMENTS
# ==========================================
with tab1:
    st.subheader("How Hard Is It to Open an Account?")
    st.markdown(
        "Opening a brokerage account online typically takes **10 to 15 minutes**—similar to opening "
        "a new checking account or applying for a credit card."
    )
    
    col_req1, col_req2 = st.columns(2)
    
    with col_req1:
        st.info("### 📝 What Information You Will Need")
        st.markdown(
            "* **Personal Details:** Full legal name, date of birth, home address, and phone number.\n"
            "* **Social Security Number (SSN) / ITIN:** Required by law for tax reporting and identity verification.\n"
            "* **Employment Details:** Employer name and industry (standard regulatory check).\n"
            "* **Linked Bank Account:** Routing and checking account numbers for initial funding."
        )

    with col_req2:
        st.success("### 🔒 What to Expect After Hitting Submit")
        st.markdown(
            "* **Instant Identity Verification:** Most applications are approved automatically in real-time.\n"
            "* **Tax Forms (W-9):** You will digitally sign standard tax agreement forms.\n"
            "* **Funding Transfer:** Bank ACH transfers usually take 1–3 business days to clear, though many brokerages offer **instant trading credit** for small initial deposits."
        )

    with st.expander("💡 Why do brokerages ask for my SSN and employer?"):
        st.markdown(
            "Brokerages are regulated by FINRA and the SEC. Federal law requires identity verification "
            "to prevent money laundering, verify tax filings, and ensure employees of financial firms "
            "comply with insider trading rules."
        )

# ==========================================
# TAB 2: BROKERAGE COMPARISON
# ==========================================
with tab2:
    st.subheader("Choosing Where to Open Your Account")
    st.markdown(
        "Modern major brokerages offer **$0 stock and ETF trading commissions**. "
        "However, they differ in features, cash yields, tier structures, and **margin borrowing rates**."
    )
    
    broker_df = pd.DataFrame([
        {
            "Brokerage": "Interactive Brokers (IBKR)",
            "Account Minimum": "$0",
            "Fractional Shares": "Yes ($1 minimums)",
            "Cash Yield": "High (~4.8% on uninvested cash >$10k)",
            "Margin Rates": "Lowest (Benchmark + 0.75% to 1.5%)",
            "Best Known For": "Pro traders, global market access, lowest margin rates, two plan tiers (IBKR Lite vs. Pro)."
        },
        {
            "Brokerage": "Fidelity Investments",
            "Account Minimum": "$0",
            "Fractional Shares": "Yes (Dollar-based, 7,000+ stocks/ETFs)",
            "Cash Yield": "High (~SPAXX Auto-Sweep)",
            "Margin Rates": "Standard / High (~11% - 13%+ Tiered)",
            "Best Known For": "Exceptional customer service, zero-expense index funds, all-in-one platform."
        },
        {
            "Brokerage": "Charles Schwab",
            "Account Minimum": "$0",
            "Fractional Shares": "Yes ('Stock Slices' for S&P 500)",
            "Cash Yield": "Low (Standard Bank Yield)",
            "Margin Rates": "Standard / High (~11% - 13%+ Tiered)",
            "Best Known For": "Excellent research tools, checking account integration, global travel debit card."
        },
        {
            "Brokerage": "Vanguard",
            "Account Minimum": "$0",
            "Fractional Shares": "Yes (Vanguard ETFs & select stocks)",
            "Cash Yield": "High (VMFXX Money Market)",
            "Margin Rates": "Standard (~11% - 13%+ Tiered)",
            "Best Known For": "Investor-owned structure, pioneer of low-cost index investing."
        },
        {
            "Brokerage": "Robinhood",
            "Account Minimum": "$0",
            "Fractional Shares": "Yes ($1 minimums)",
            "Cash Yield": "High with Gold (~5.0%) / Standard without",
            "Margin Rates": "Low with Gold (~6.0% - 6.5%)",
            "Best Known For": "Mobile-first interface, streamlined app experience for beginners."
        }
    ])
    
    st.table(broker_df)

    st.warning("### 🔍 Understanding IBKR's Tier Structure & Margin Rates")
    col_m1, col_m2 = st.columns(2)
    
    with col_m1:
        st.markdown(
            "**Interactive Brokers Tiers (Lite vs. Pro):**\n"
            "* **IBKR Lite:** Designed for retail investors—offers $0 commission stock/ETF trades and an easy-to-use desktop/mobile app.\n"
            "* **IBKR Pro:** Designed for active investors—uses volume-based pricing, direct market routing, and provides the absolute lowest margin borrowing rates in the industry."
        )
        
    with col_m2:
        st.markdown(
            "**What is Margin Interest?**\n"
            "* **Margin** is money you borrow from your brokerage using your portfolio as collateral.\n"
            "* **Traditional Brokers (Fidelity/Schwab):** Charge higher retail margin interest rates (~11%-13%+).\n"
            "* **Interactive Brokers:** Passes through institutional benchmark rates, making borrowing significantly cheaper for investors utilizing leverage or liquidity lines."
        )

# ==========================================
# TAB 3: ACCOUNT TYPES
# ==========================================
with tab3:
    st.subheader("Which Type of Account Should You Open?")
    st.markdown(
        "When you click 'Open Account', the brokerage will ask you to select an **account structure**. "
        "Here are the primary options:"
    )
    
    col_acct1, col_acct2 = st.columns(2)
    
    with col_acct1:
        st.markdown("### 🏦 Taxable Individual Brokerage Account")
        st.markdown(
            "* **Purpose:** General investing and liquid money growth.\n"
            "* **Flexibility:** Withdraw your cash or sell shares anytime without age penalties.\n"
            "* **Taxes:** Dividends and capital gains are subject to annual taxes in the year realized.\n"
            "* **Contribution Limits:** None."
        )

    with col_acct2:
        st.markdown("### 🛡️ Roth IRA (Tax-Advantaged Retirement)")
        st.markdown(
            "* **Purpose:** Long-term retirement building.\n"
            "* **Flexibility:** Designed for age 59½+, though direct contributions can be withdrawn tax-free anytime.\n"
            "* **Taxes:** Contributions are made after-tax; growth and retirement withdrawals are **100% tax-free**.\n"
            "* **Contribution Limits:** Annual maximums apply (e.g., $7,000/year for 2024–2026)."
        )

# ==========================================
# TAB 4: FRACTIONAL SHARES & MINIMUMS
# ==========================================
with tab4:
    st.subheader("How Much Money Do You Need to Start?")
    st.markdown(
        "A common misconception is that you need thousands of dollars to start investing. "
        "With **fractional shares**, you can invest with as little as **$1 to $5**."
    )
    
    col_f1, col_f2 = st.columns(2)
    
    with col_f1:
        st.warning("### ❌ Old School Way (Whole Shares Only)")
        st.markdown(
            "If a share of Microsoft or an S&P 500 ETF cost $400, you had to save up a full $400 "
            "before buying a single share."
        )

    with col_f2:
        st.success("### 🟢 Modern Way (Dollar-Based Investing)")
        st.markdown(
            "You decide how many dollars you want to invest (e.g., $25). "
            "If the stock costs $400 per share, the brokerage gives you **0.0625 shares**."
        )
        
    st.info(
        "💡 **Key Benefit:** Fractional shares allow you to set up automatic recurring investments "
        "(e.g., $50 every payday) directly into broad-market index ETFs regardless of the stock's share price."
    )

# ==========================================
# TAB 5: WHAT BUYING A STOCK LOOKS LIKE
# ==========================================
with tab5:
    st.subheader("What You Will See When Placing an Order")
    st.markdown(
        "When you log into your brokerage app to place a trade, you will fill out a simple order form. "
        "Here is an interactive preview of the main fields:"
    )
    
    st.markdown("---")
    
    # ORDER PREVIEW SIMULATION
    col_ord1, col_ord2 = st.columns(2)
    
    with col_ord1:
        st.markdown("### 📝 Interactive Order Preview")
        
        symbol = st.text_input("Ticker Symbol", value="VOO").upper()
        order_action = st.selectbox("Action", ["Buy", "Sell"])
        order_type = st.selectbox("Order Type", ["Market Order", "Limit Order"])
        amount_type = st.radio("Order Amount", ["Dollars ($)", "Shares (#)"])
        
        if amount_type == "Dollars ($)":
            order_val = st.number_input("Amount to Invest ($)", value=100.0, step=10.0)
        else:
            order_val = st.number_input("Number of Shares", value=1.0, step=0.1)

    with col_ord2:
        st.markdown("### 🔍 Field Explanations")
        
        if order_type == "Market Order":
            st.success(
                "**Market Order (Recommended for Beginners):** "
                "Executes immediately at the current available market price. Simple and fast."
            )
        else:
            st.warning(
                "**Limit Order:** "
                "Sets a specific maximum price you are willing to pay. The order will only execute "
                "if the stock price drops to or below your target."
            )
            
        st.markdown(
            f"**Action Summary:** You are submitting an order to **{order_action}** "
            f"**{order_val} {amount_type.lower()}** of **{symbol}** using a **{order_type}** during market hours."
        )