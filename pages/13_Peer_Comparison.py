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
