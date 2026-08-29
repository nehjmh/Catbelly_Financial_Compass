import streamlit as st
import pandas as pd
import yfinance as yf

st.set_page_config(page_title="What are ETFs? - Catbelly Compass", layout="wide")

st.title("📖 What are ETFs? (Exchange-Traded Funds)")
st.caption("Your comprehensive guide to understanding, evaluating, and exploring Exchange-Traded Funds.")

# Navigation Tabs for Structure
tab_overview, tab_popular, tab_search = st.tabs(["📚 Educational Overview", "🌟 Popular ETF Categories", "🔍 Live ETF Search Workbench"])

with tab_overview:
    st.subheader("What is an ETF?")
    st.write(
        "An **Exchange-Traded Fund (ETF)** is a pooled investment security that operates much like a mutual fund "
        "but trades on a stock exchange like an individual stock. ETFs can hold hundreds or thousands of stocks, "
        "bonds, commodities, or derivatives, allowing investors to gain instant diversification with a single transaction."
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🏛️ History & Evolution")
        st.write(
            "The modern ETF era began in **1993** with the launch of the SPDR S&P 500 ETF Trust (**SPY**), "
            "created by State Street Global Advisors. Initially designed to give institutional investors a flexible way "
            "to trade the entire S&P 500 index, ETFs quickly gained traction among individual investors due to their intraday liquidity "
            "and low structural costs."
        )
        
        st.markdown("### 📈 Growth & Market Scope")
        st.write(
            "Over the past three decades, the ETF market has exploded from a single product into a multi-trillion-dollar global industry. "
            "Today's scope spans far beyond simple index tracking, encompassing sector funds, international markets, fixed income, "
            "commodities, leveraged strategies, and complex options-based income distribution funds."
        )

    with col2:
        st.markdown("### 💡 Why ETFs Make Investing Easier")
        st.markdown("""
        * **Instant Diversification:** Buying one share of an S&P 500 ETF instantly spreads your risk across 500 top U.S. corporations.
        * **Intraday Liquidity:** Unlike mutual funds that only price once at market close, ETFs can be bought and sold at any time during market hours.
        * **Transparency:** Most ETFs publish their exact daily holdings transparently, so you always know what you own.
        * **Minimums & Access:** With fractional shares, you can build a diversified portfolio with just a few dollars.
        """)
        
        st.markdown("### 💰 The Cost Advantage")
        st.write(
            "ETFs are renowned for their low **Expense Ratios** (often ranging from 0.03% to 0.75% annually). "
            "Because most traditional index ETFs are passively managed, they avoid the heavy research and high turnover costs "
            "associated with actively managed mutual funds, leaving more of the compounding returns in your pocket."
        )

    st.write("---")
    st.markdown("### 🌐 External ETF Research Resources")
    st.write(
        "To dive deeper into fund fundamentals, expense comparisons, and screener tools, explore these popular independent research platforms:"
    )
    
    r_col1, r_col2 = st.columns(2)
    with r_col1:
        st.markdown("""
        * **[ETF.com](https://www.etf.com)** – Comprehensive fund analysis, news, analytics, and category breakdowns.
        * **[ETF Database (ETFdb.com)](https://etfdb.com)** – Robust ETF screener, category comparisons, and tax efficiency tools.
        """)
    with r_col2:
        st.markdown("""
        * **[Morningstar](https://www.morningstar.com)** – Industry-standard ratings, risk analytics, and portfolio overlap tools.
        * **[Yahoo Finance](https://finance.yahoo.com)** – Real-time quotes, historical performance charts, and underlying holdings data.
        """)

with tab_popular:
    st.subheader("Popular ETFs by Category")
    st.caption("Curated lists of widely-tracked funds across core market segments.")
    
    category = st.selectbox(
        "Select ETF Category to View:",
        ["Broad Market Indexes", "Sectors & Industries", "High Income / Options-Based", "Thematic & Growth"]
    )
    
    if category == "Broad Market Indexes":
        pop_data = pd.DataFrame({
            "Ticker": ["SPY", "SPLG", "QQQM", "VT", "IWM"],
            "Name": ["SPDR S&P 500 ETF Trust", "SPDR Portfolio S&P 500 ETF", "Invesco Nasdaq 100 ETF", "Vanguard Total World Stock ETF", "iShares Russell 2000 ETF"],
            "Focus": ["S&P 500 Index", "Low-Cost S&P 500 Core", "Nasdaq-100 Tech Focus", "Global Equities", "U.S. Small Cap"],
            "Expense Ratio": ["0.0945%", "0.02%", "0.15%", "0.07%", "0.19%"]
        })
    elif category == "Sectors & Industries":
        pop_data = pd.DataFrame({
            "Ticker": ["FTEC", "SMH", "XLF", "XLE", "XLV"],
            "Name": ["Fidelity MSCI Information Tech Index ETF", "VanEck Semiconductor ETF", "Financial Select Sector SPDR Fund", "Energy Select Sector SPDR Fund", "Health Care Select Sector SPDR Fund"],
            "Focus": ["Information Technology", "Semiconductors & Chips", "Banking & Financials", "Oil, Gas & Energy", "Healthcare & Pharma"],
            "Expense Ratio": ["0.084%", "0.35%", "0.09%", "0.09%", "0.09%"]
        })
    elif category == "High Income / Options-Based":
        pop_data = pd.DataFrame({
            "Ticker": ["SPYI", "QQQI", "CHPY", "PULS", "STRC"],
            "Name": ["Neos S&P 500 High Income ETF", "Neos Nasdaq-100 High Income ETF", "Roundhill S&P 500 0DTE Covered Call", "Pimco Enhanced Low Duration Active ETF", "Strive Ultra Short Income ETF"],
            "Focus": ["S&P 500 Covered Call Income", "Nasdaq 100 Covered Call Income", "Semiconductor Option Income", "Ultra-Short Liquidity / Monthly", "Short Duration Income / Semi-Monthly"],
            "Expense Ratio": ["0.68%", "0.68%", "0.95%", "0.55%", "0.30%"]
        })
    else:  # Thematic & Growth
        pop_data = pd.DataFrame({
            "Ticker": ["ARKK", "XAR", "BOTZ", "ICLN", "PAVE"],
            "Name": ["ARK Innovation ETF", "SPDR S&P Aerospace & Defense ETF", "Global X Robotics & Artificial Intelligence ETF", "iShares Global Clean Energy ETF", "Global X U.S. Infrastructure Development ETF"],
            "Focus": ["Disruptive Growth Tech", "Aerospace & Defense", "AI & Robotics", "Clean Energy", "Infrastructure"],
            "Expense Ratio": ["0.75%", "0.35%", "0.68%", "0.40%", "0.47%"]
        })

    st.dataframe(pop_data, hide_index=True, use_container_width=True)

with tab_search:
    st.subheader("🔍 ETF Search & Natural Language Finder")
    st.caption("Type a ticker symbol (e.g., `SPY`) OR ask a question in plain English (e.g., *'what's an etf for big banks'*, *'Are there ETFs for China?'*, or *'What ETFs have Qualcomm?'*).")
    
    query = st.text_input("Search ETFs or describe what you want:", value="what's an etf for big banks").strip()
    
    if query:
        # Broad & Inclusive Natural Language Keyword Map
        nl_mappings = {
            # Banking & Financials
            "bank": [("XLF", "Financial Select Sector SPDR Fund"), ("KBE", "SPDR S&P Bank ETF"), ("KRE", "SPDR S&P Regional Banking ETF")],
            "financial": [("XLF", "Financial Select Sector SPDR Fund"), ("VFH", "Vanguard Financials ETF")],
            "wall street": [("XLF", "Financial Select Sector SPDR Fund")],
            
            # International & Country-Specific
            "china": [("MCHI", "iShares MSCI China ETF"), ("FXI", "iShares China Large-Cap ETF"), ("KWEB", "KraneShares CSI China Internet ETF")],
            "chinese": [("MCHI", "iShares MSCI China ETF"), ("FXI", "iShares China Large-Cap ETF"), ("KWEB", "KraneShares CSI China Internet ETF")],
            "emerging": [("VWO", "Vanguard FTSE Emerging Markets ETF"), ("EEM", "iShares MSCI Emerging Markets ETF")],
            "international": [("VXUS", "Vanguard Total International Stock ETF"), ("EFA", "iShares MSCI EAFE ETF")],
            
            # Specific Stocks & Companies
            "qualcomm": [("SMH", "VanEck Semiconductor ETF"), ("SOXX", "iShares Semiconductor ETF"), ("QQQM", "Invesco Nasdaq 100 ETF"), ("FTEC", "Fidelity MSCI Information Tech ETF")],
            "qcom": [("SMH", "VanEck Semiconductor ETF"), ("SOXX", "iShares Semiconductor ETF"), ("QQQM", "Invesco Nasdaq 100 ETF")],
            "coca": [("XLP", "Consumer Staples Select Sector SPDR Fund"), ("VDC", "Vanguard Consumer Staples ETF"), ("NOBL", "ProShares S&P 500 Dividend Aristocrats ETF"), ("SCHD", "Schwab U.S. Dividend Equity ETF")],
            "cola": [("XLP", "Consumer Staples Select Sector SPDR Fund"), ("VDC", "Vanguard Consumer Staples ETF"), ("NOBL", "ProShares S&P 500 Dividend Aristocrats ETF")],
            "ko": [("XLP", "Consumer Staples Select Sector SPDR Fund"), ("VDC", "Vanguard Consumer Staples ETF"), ("NOBL", "ProShares S&P 500 Dividend Aristocrats ETF")],
            "pepsi": [("XLP", "Consumer Staples Select Sector SPDR Fund"), ("VDC", "Vanguard Consumer Staples ETF")],
            "pep": [("XLP", "Consumer Staples Select Sector SPDR Fund"), ("VDC", "Vanguard Consumer Staples ETF")],
            "nvidia": [("SMH", "VanEck Semiconductor ETF"), ("QQQM", "Invesco Nasdaq 100 ETF"), ("FTEC", "Fidelity MSCI Information Tech ETF")],
            "nvda": [("SMH", "VanEck Semiconductor ETF"), ("QQQM", "Invesco Nasdaq 100 ETF"), ("FTEC", "Fidelity MSCI Information Tech ETF")],
            "apple": [("QQQM", "Invesco Nasdaq 100 ETF"), ("FTEC", "Fidelity MSCI Information Tech ETF"), ("SPY", "SPDR S&P 500 ETF Trust")],
            "aapl": [("QQQM", "Invesco Nasdaq 100 ETF"), ("FTEC", "Fidelity MSCI Information Tech ETF")],
            "tesla": [("QQQM", "Invesco Nasdaq 100 ETF"), ("ARKK", "ARK Innovation ETF"), ("XLY", "Consumer Discretionary Select Sector SPDR Fund")],
            "tsla": [("QQQM", "Invesco Nasdaq 100 ETF"), ("ARKK", "ARK Innovation ETF")],
            "microsoft": [("QQQM", "Invesco Nasdaq 100 ETF"), ("FTEC", "Fidelity MSCI Information Tech ETF")],
            "msft": [("QQQM", "Invesco Nasdaq 100 ETF"), ("FTEC", "Fidelity MSCI Information Tech ETF")],
            
            # Sectors & Themes
            "consumer": [("XLP", "Consumer Staples Select Sector SPDR Fund"), ("XLY", "Consumer Discretionary Select Sector SPDR Fund"), ("VDC", "Vanguard Consumer Staples ETF")],
            "staple": [("XLP", "Consumer Staples Select Sector SPDR Fund"), ("VDC", "Vanguard Consumer Staples ETF")],
            "beverage": [("XLP", "Consumer Staples Select Sector SPDR Fund")],
            
            # Dow Jones / Indexes
            "dow": [("DIA", "SPDR Dow Jones Industrial Average ETF Trust")],
            "jones": [("DIA", "SPDR Dow Jones Industrial Average ETF Trust")],
            "s&p": [("SPY", "SPDR S&P 500 ETF Trust"), ("VOO", "Vanguard S&P 500 ETF")],
            "nasdaq": [("QQQ", "Invesco QQQ Trust"), ("QQQM", "Invesco Nasdaq 100 ETF")],
            "russell": [("IWM", "iShares Russell 2000 ETF")],
            
            # Commodities & Metals
            "metal": [("GLD", "SPDR Gold Shares"), ("SLV", "iShares Silver Trust"), ("GDX", "VanEck Gold Miners ETF")],
            "gold": [("GLD", "SPDR Gold Shares"), ("IAU", "iShares Gold Trust"), ("GDX", "VanEck Gold Miners ETF")],
            "silver": [("SLV", "iShares Silver Trust"), ("SIVR", "Aberdeen Physical Silver Shares ETF")],
            
            # Sectors & Industries
            "chip": [("SMH", "VanEck Semiconductor ETF"), ("SOXX", "iShares Semiconductor ETF")],
            "semiconductor": [("SMH", "VanEck Semiconductor ETF"), ("SOXX", "iShares Semiconductor ETF")],
            "tech": [("QQQM", "Invesco Nasdaq 100 ETF"), ("FTEC", "Fidelity MSCI Information Tech ETF"), ("VGT", "Vanguard Information Technology ETF")],
            "energy": [("XLE", "Energy Select Sector SPDR Fund"), ("VDE", "Vanguard Energy ETF")],
            "healthcare": [("XLV", "Health Care Select Sector SPDR Fund")],
            "real estate": [("VNQ", "Vanguard Real Estate ETF"), ("XLRE", "Real Estate Select Sector SPDR Fund")],
            
            # Income & Dividends
            "dividend": [("SCHD", "Schwab U.S. Dividend Equity ETF"), ("VYM", "Vanguard High Dividend Yield ETF"), ("NOBL", "ProShares S&P 500 Dividend Aristocrats ETF")],
            "income": [("SPYI", "Neos S&P 500 High Income ETF"), ("QQQI", "Invesco Nasdaq-100 High Income ETF"), ("JEPI", "JPMorgan Equity Premium Income ETF")],
            
            "small cap": [("IWM", "iShares Russell 2000 ETF"), ("VB", "Vanguard Small-Cap ETF")],
            "crypto": [("IBIT", "iShares Bitcoin Trust"), ("ETHA", "iShares Ethereum Trust")]
        }
        
        lower_query = query.lower()
        matched_tickers = []
        
        # Scan sentence for any matching keywords
        for keyword, items in nl_mappings.items():
            if keyword in lower_query:
                for t, n in items:
                    if (t, n) not in matched_tickers:
                        matched_tickers.append((t, n))
                        
        if matched_tickers:
            st.markdown(f"🎯 **Found {len(matched_tickers)} matching recommendations based on your description:**")
            
            results = []
            for t, desc in matched_tickers:
                try:
                    tk = yf.Ticker(t)
                    info = tk.info
                    price = info.get("regularMarketPrice") or info.get("previousClose", 0.0)
                    er = info.get("expenseRatio", None)
                    results.append({
                        "Ticker": t,
                        "Fund Name": desc,
                        "Current Price": f"${price:,.2f}" if price else "N/A",
                        "Expense Ratio": f"{er * 100:.2f}%" if er else "N/A"
                    })
                except Exception:
                    results.append({"Ticker": t, "Fund Name": desc, "Current Price": "N/A", "Expense Ratio": "N/A"})
                    
            st.dataframe(pd.DataFrame(results), hide_index=True, use_container_width=True)
            
        elif len(query.split()) == 1 and len(query) <= 5:
            # Direct Ticker Lookup fallback
            search_ticker = query.upper().strip()
            try:
                with st.spinner(f"Fetching details for ticker `{search_ticker}`..."):
                    etf = yf.Ticker(search_ticker)
                    info = etf.info
                    
                    name = info.get("longName") or info.get("shortName", search_ticker)
                    price = info.get("regularMarketPrice") or info.get("previousClose", 0.0)
                    category_desc = info.get("category", "Exchange Traded Fund")
                    summary = info.get("longBusinessSummary", "No descriptive summary available for this ticker.")
                    expense_ratio = info.get("expenseRatio", None)
                    div_yield = info.get("dividendYield", None)
                    
                    m1, m2, m3, m4 = st.columns(4)
                    m1.metric("Fund Name", name)
                    m2.metric("Current Price", f"${price:,.2f}" if price else "N/A")
                    m3.metric("Expense Ratio", f"{expense_ratio * 100:.2f}%" if expense_ratio else "N/A")
                    m4.metric("Dividend Yield", f"{div_yield * 100:.2f}%" if div_yield else "N/A")
                    
                    st.write("---")
                    st.markdown(f"**Asset Category / Focus:** {category_desc}")
                    st.markdown("### Fund Summary")
                    st.write(summary)
                    
            except Exception:
                st.warning(f"Could not retrieve details for ticker `{search_ticker}`. Please check the symbol.")
        else:
            st.warning(f"We couldn't match any specific categories or stocks for your sentence (`{query}`). Try including keywords like **'bank'**, **'china'**, **'Qualcomm'**, **'Nvidia'**, or **'dividend'**, or enter a direct ticker symbol like `XLF` or `SPY`.")