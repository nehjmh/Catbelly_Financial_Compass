import streamlit as st
import pandas as pd
import plotly.express as px
import yfinance as yf

st.set_page_config(page_title="Sample Portfolios - Catbelly Compass", layout="wide")

st.title("🐱 Catbelly Sample Portfolios (Live Tracker)")
st.caption("Educational model allocations ranging from Kitten to Tiger, starting at $10,000 on August 28, 2026.")

# Educational Disclaimer
st.warning(
    "**Educational Disclaimer:** These sample model portfolios are strictly for educational and conceptual tracking purposes. "
    "They do not constitute personalized financial advice or a recommendation to buy or sell any asset."
)

st.write("---")

# ---------------------------------------------------------
# FIXED BASELINE CONSTANTS (August 28, 2026 Locked Baseline)
# Starting Base: $10,000 per model tier
# ---------------------------------------------------------

BASELINE_PORTFOLIOS = {
    "🐱 Kitten (Ultra-Short Liquidity)": {
        "description": "Ultra-short liquidity & high-yield capital preservation without traditional bond duration risk.",
        "holdings": {
            "PULS": {"shares": 160.93, "target_pct": 80, "freq": "Monthly"},
            "STRC": {"shares": 10.27,  "target_pct": 10, "freq": "Semi-Monthly (2x/mo)"},
            "SATA": {"shares": 10.03,  "target_pct": 10, "freq": "Daily (Every Trading Day)"}
        }
    },
    "😼 Bobcat (Conservative Growth)": {
        "description": "Conservative yield blend introducing broad S&P 500 core equity exposure alongside short-duration cash equivalents.",
        "holdings": {
            "PULS": {"shares": 100.58, "target_pct": 50, "freq": "Monthly"},
            "SPLG": {"shares": 37.50,  "target_pct": 30, "freq": "Quarterly"},
            "STRC": {"shares": 10.27,  "target_pct": 10, "freq": "Semi-Monthly (2x/mo)"},
            "SATA": {"shares": 10.03,  "target_pct": 10, "freq": "Daily (Every Trading Day)"}
        }
    },
    "🐆 Cougar (Balanced Core)": {
        "description": "Balanced equity/yield core: 60% broad market equity (S&P 500 & Nasdaq 100) paired with 40% ultra-short income ballast.",
        "holdings": {
            "PULS": {"shares": 60.35, "target_pct": 30, "freq": "Monthly"},
            "SPLG": {"shares": 37.50, "target_pct": 30, "freq": "Quarterly"},
            "QQQM": {"shares": 10.17, "target_pct": 30, "freq": "Quarterly"},
            "STRC": {"shares": 5.14,  "target_pct": 5,  "freq": "Semi-Monthly (2x/mo)"},
            "SATA": {"shares": 5.01,  "target_pct": 5,  "freq": "Daily (Every Trading Day)"}
        }
    },
    "🦁 Lion (Aggressive Core Growth)": {
        "description": "Growth-tilted tier anchoring 80% in index equity cores (QQQM, SPLG, SMH) with a 20% high-frequency income component.",
        "holdings": {
            "QQQM": {"shares": 13.56, "target_pct": 40, "freq": "Quarterly"},
            "SPLG": {"shares": 37.50, "target_pct": 30, "freq": "Quarterly"},
            "SATA": {"shares": 20.05, "target_pct": 20, "freq": "Daily (Every Trading Day)"},
            "SMH":  {"shares": 1.81,  "target_pct": 10, "freq": "Quarterly"}
        }
    },
    "🐅 Tiger (Maximum Tech & Growth)": {
        "description": "High-beta concentrated growth tier taking on maximum equity exposure across tech ETFs, option income, and high-conviction growth stocks.",
        "holdings": {
            "FTEC": {"shares": 17.45, "target_pct": 50, "freq": "Quarterly"},
            "CHPY": {"shares": 30.32, "target_pct": 20, "freq": "Weekly"},
            "TSLA": {"shares": 2.87,  "target_pct": 10, "freq": "None (Capital Appreciation)"},
            "NVDA": {"shares": 4.60,  "target_pct": 10, "freq": "Quarterly"},
            "LLY":  {"shares": 0.85,  "target_pct": 10, "freq": "Quarterly"}
        }
    }
}

# Collect all unique tickers needed
all_tickers = sorted(list({ticker for tier in BASELINE_PORTFOLIOS.values() for ticker in tier["holdings"]}))

# Fetch Live Prices via yfinance
@st.cache_data(ttl=300)
def get_live_prices(ticker_list):
    prices = {}
    for ticker in ticker_list:
        try:
            data = yf.Ticker(ticker)
            price = data.fast_info.get("lastPrice") or data.history(period="1d")["Close"].iloc[-1]
            prices[ticker] = round(price, 2)
        except Exception:
            prices[ticker] = 0.0
    return prices

with st.spinner("Fetching live prices..."):
    live_prices = get_live_prices(all_tickers)

# Dropdown Selection for Tier
selected_tier_name = st.selectbox("Select Feline Risk Spectrum Tier:", list(BASELINE_PORTFOLIOS.keys()))
tier_info = BASELINE_PORTFOLIOS[selected_tier_name]

# Build DataFrame for Display
table_data = []
total_live_val = 0.0

for ticker, data in tier_info["holdings"].items():
    shares = data["shares"]
    target_pct = data["target_pct"]
    freq = data["freq"]
    current_price = live_prices.get(ticker, 0.0)
    current_val = shares * current_price
    total_live_val += current_val
    
    table_data.append({
        "Ticker": ticker,
        "Target Weight (%)": f"{target_pct}%",
        "Distribution Schedule": freq,
        "Locked Shares": f"{shares:,.2f}",
        "Current Price": f"${current_price:,.2f}",
        "Current Value": current_val
    })

df = pd.DataFrame(table_data)

# Display Summary Metrics
total_gain_loss = total_live_val - 10000.0
pct_gain_loss = (total_gain_loss / 10000.0) * 100

st.write("---")
m_col1, m_col2, m_col3 = st.columns(3)
m_col1.metric("Initial Capital (Aug 28, 2026)", "$10,000.00")
m_col2.metric("Current Portfolio Value", f"${total_live_val:,.2f}")
m_col3.metric("Total Return", f"{pct_gain_loss:+.2f}%", delta=f"${total_gain_loss:+,.2f}")

col_left, col_right = st.columns([1.3, 1])

with col_left:
    st.subheader(selected_tier_name)
    st.write(tier_info["description"])
    
    # Render holdings table with Distribution Schedule column
    df_display = df.copy()
    df_display["Current Value"] = df_display["Current Value"].apply(lambda x: f"${x:,.2f}")
    st.dataframe(df_display, hide_index=True, use_container_width=True)

with col_right:
    # Donut Chart Visualization
    fig = px.pie(
        df,
        values="Current Value",
        names="Ticker",
        title=f"Live Allocation Breakdown ({selected_tier_name.split(' ')[0]})",
        hole=0.4
    )
    fig.update_traces(textinfo="percent+label")
    st.plotly_chart(fig, use_container_width=True)