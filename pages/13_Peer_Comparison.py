import streamlit as st
import pandas as pd
import yfinance as yf
import numpy as np
import requests

st.set_page_config(page_title="Peer & Best-in-Class Comparator - Catbelly Compass", layout="wide")

st.title("⚖️ Best-in-Class Peer Comparator")
st.caption("Evaluate any ticker's fundamentals, leverage, valuation, and multi-year performance against direct industry peers.")

# Helper function to generate a browser-spoofed session for yfinance
def get_custom_session():
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    })
    return session

# User Input
target_ticker = st.text_input("Enter Ticker Symbol to Analyze:", value="CB").upper().strip()

if target_ticker:
    # 1. Specific Ticker Overrides
    peer_groups = {
        "KO": ["KO", "PEP", "KDP", "MNST"],
        "PEP": ["PEP", "KO", "KDP", "MNST"],
        "NVDA": ["NVDA", "AMD", "AVGO", "INTC", "QCOM"],
        "AAPL": ["AAPL", "MSFT", "GOOGL", "META"],
        "MSFT": ["MSFT", "AAPL", "GOOGL", "AMZN"],
        "TSLA": ["TSLA", "RIVN", "F", "GM", "TM"],
        "JNJ": ["JNJ", "PFE", "LLY", "ABBV"],
        "O": ["O", "NNN", "VICI", "SPG"],
        "CB": ["CB", "PGR", "TRV", "ALL"]
    }
    
    # 2. Sector-Based Default Fallbacks
    sector_defaults = {
        "Financial Services": ["JPM", "BAC", "WFC", "GS"],
        "Technology": ["AAPL", "MSFT", "NVDA", "GOOGL"],
        "Healthcare": ["JNJ", "UNH", "PFE", "LLY"],
        "Consumer Cyclical": ["AMZN", "TSLA", "HD", "MCD"],
        "Consumer Defensive": ["WMT", "PG", "KO", "PEP"],
        "Energy": ["XOM", "CVX", "COP", "SLB"],
        "Industrials": ["UPS", "HON", "CAT", "GE"],
        "Utilities": ["NEE", "DUK", "SO", "AEP"],
        "Real Estate": ["O", "PLD", "AMT", "SPG"],
        "Basic Materials": ["LIN", "APD", "FCX", "NEM"],
        "Communication Services": ["GOOGL", "META", "NFLX", "DIS"]
    }

    if target_ticker in peer_groups:
        peers = peer_groups[target_ticker]
    else:
        try:
            # Pass custom session to avoid cloud blocks on sector lookup
            target_info = yf.Ticker(target_ticker, session=get_custom_session()).info
            sector = target_info.get("sector", "")
            sector_peers = sector_defaults.get(sector, ["SPY", "QQQ"])
            peers = [target_ticker] + [p for p in sector_peers if p != target_ticker][:4]
        except Exception:
            peers = [target_ticker, "SPY", "QQQ"]

    st.subheader(f"Comparing {target_ticker} against Peer Group: {', '.join(peers)}")
    
    @st.cache_data(ttl=600)
    def fetch_comprehensive_data(ticker_list):
        data_rows = []
        session = get_custom_session()
        
        for t in ticker_list:
            stock = None
            # Try standard Ticker first (ideal for localhost)
            try:
                stock = yf.Ticker(t)
                info = stock.info
                # Quick validation to ensure info isn't empty/blocked
                if not info or "regularMarketPrice" not in info and "currentPrice" not in info and "shortName" not in info:
                    raise ValueError("Blocked or empty info dictionary")
            except Exception:
                # Fallback: Retry with the custom session headers (ideal for Streamlit Cloud)
                try:
                    stock = yf.Ticker(t, session=session)
                    info = stock.info
                except Exception:
                    continue

            try:
                if not info:
                    continue
                    
                # Fix Dividend Yield scaling
                raw_yield = info.get("dividendYield", 0) or 0
                div_yield = raw_yield if raw_yield > 1.0 else raw_yield * 100.0
                
                # Extract Debt to Equity
                de_raw = info.get("debtToEquity", None)
                de_ratio = round(de_raw, 1) if de_raw is not None else None

                # Extract PEG ratio
                peg_ratio = info.get("pegRatio", None)
                peg_ratio = round(peg_ratio, 2) if peg_ratio else None

                # Fetch history (try standard first, fallback to session if needed)
                try:
                    hist = stock.history(period="max")
                except Exception:
                    hist = yf.Ticker(t, session=session).history(period="max")

                ret_1yr, ret_3yr, ret_5yr = 0.0, 0.0, 0.0
                
                if not hist.empty:
                    current_price = hist["Close"].iloc[-1]
                    
                    if len(hist) >= 252:
                        p_1yr = hist["Close"].iloc[-252]
                        ret_1yr = ((current_price - p_1yr) / p_1yr) * 100
                        
                    if len(hist) >= 756:
                        p_3yr = hist["Close"].iloc[-756]
                        ret_3yr = (((current_price / p_3yr) ** (1/3)) - 1) * 100
                        
                    if len(hist) >= 1260:
                        p_5yr = hist["Close"].iloc[-1260]
                        ret_5yr = (((current_price / p_5yr) ** (1/5)) - 1) * 100

                data_rows.append({
                    "Ticker": t,
                    "Name": info.get("shortName", t),
                    "Market Cap ($B)": round(info.get("marketCap", 0) / 1e9, 1),
                    "P/E Ratio": round(info.get("trailingPE", 0), 1) if info.get("trailingPE") else None,
                    "PEG Ratio": peg_ratio,
                    "Debt/Equity": de_ratio,
                    "Div Yield (%)": round(div_yield, 2),
                    "Net Margin (%)": round(info.get("profitMargins", 0) * 100, 1) if info.get("profitMargins") else 0.0,
                    "ROE (%)": round(info.get("returnOnEquity", 0) * 100, 1) if info.get("returnOnEquity") else 0.0,
                    "1-Yr Return (%)": round(ret_1yr, 1),
                    "3-Yr Ann. (%)": round(ret_3yr, 1),
                    "5-Yr Ann. (%)": round(ret_5yr, 1),
                })
            except Exception:
                continue
        return pd.DataFrame(data_rows)

    with st.spinner(f"Fetching fundamentals & performance for {target_ticker} and peers..."):
        df_peers = fetch_comprehensive_data(peers)
        
    if not df_peers.empty:
        # Best-in-Class Scoring with PEG, Debt-to-Equity, and return weighting
        def calculate_score(row):
            if row["Net Margin (%)"] < 0 or row["ROE (%)"] < 0:
                return -9999
            
            score = (
                (row["Net Margin (%)"] * 2.0) + 
                (row["ROE (%)"] * 2.0) + 
                (row["3-Yr Ann. (%)"] * 1.5) + 
                (row["5-Yr Ann. (%)"] * 1.0) + 
                (row["1-Yr Return (%)"] * 0.5)
            )
            
            peg = row["PEG Ratio"]
            if peg is not None and 0 < peg < 3.0:
                score += (3.0 - peg) * 10.0
                
            de = row["Debt/Equity"]
            if de is not None and de > 300:
                score -= 30.0
                
            return score

        df_peers["Score"] = df_peers.apply(calculate_score, axis=1)
        
        # Sort dataframe from best score to worst score
        df_peers = df_peers.sort_values(by="Score", ascending=False).reset_index(drop=True)
        
        best_ticker = df_peers.loc[0]["Ticker"]
        best_name = df_peers.loc[0]["Name"]
        
        display_df = df_peers.drop(columns=["Score"])
        
        # Define Styling Function to highlight the best performer in each numeric column
        def highlight_max_min(s):
            is_min_cols = ["P/E Ratio", "PEG Ratio", "Debt/Equity"]
            if s.name in ["Ticker", "Name"]:
                return [''] * len(s)
            
            valid_s = s.dropna()
            if valid_s.empty:
                return [''] * len(s)
                
            if s.name in is_min_cols:
                best_val = valid_s[valid_s > 0].min() if not valid_s[valid_s > 0].empty else valid_s.min()
            else:
                best_val = valid_s.max()
                
            return ['background-color: rgba(40, 167, 69, 0.25); font-weight: bold;' if v == best_val and pd.notnull(v) else '' for v in s]

        # Apply clean formatting strings alongside the green highlighting
        format_dict = {
            "Market Cap ($B)": "{:,.1f}",
            "P/E Ratio": "{:.1f}",
            "PEG Ratio": "{:.2f}",
            "Debt/Equity": "{:.1f}",
            "Div Yield (%)": "{:.2f}%",
            "Net Margin (%)": "{:.1f}%",
            "ROE (%)": "{:.1f}%",
            "1-Yr Return (%)": "{:+.1f}%",
            "3-Yr Ann. (%)": "{:+.1f}%",
            "5-Yr Ann. (%)": "{:+.1f}%",
        }

        styled_df = display_df.style.apply(highlight_max_min).format(format_dict, na_rep="-")

        # Display Sorted and Color-Coded Table
        st.dataframe(styled_df, hide_index=True, use_container_width=True)
        
        # Best in Class Callout Box
        st.success(f"🏆 **Best-in-Class Winner for this Group:** **{best_ticker} ({best_name})** takes the top spot based on profitability, valuation growth (PEG), balance sheet health (Debt/Equity), and multi-year performance.")
        
        if best_ticker == target_ticker:
            st.markdown(f"✅ **Verdict:** Yes! **{target_ticker}** is currently demonstrating **Best-in-Class** metrics among its peer group.")
        else:
            st.markdown(f"⚠️ **Verdict:** **{target_ticker}** is competitive, but **{best_ticker}** currently leads the peer group across key financial efficiencies.")
    else:
      st.warning("Could not retrieve data for this ticker group. Please check the symbol.")