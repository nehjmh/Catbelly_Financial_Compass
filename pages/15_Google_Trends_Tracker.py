import streamlit as st
import pandas as pd
from pytrends.request import TrendReq
import datetime

st.set_page_config(page_title="Macro Sentiment Tracker - Catbelly Compass", layout="wide")

st.title("📊 Macro Sentiment & Google Trends Tracker")
st.caption("Measure public interest, narrative momentum, and retail attention shifts across monetary and hard-asset keywords.")

# Initialize PyTrends (cached to avoid repeated API hits)
@st.cache_resource
def get_pytrends():
    return TrendReq(hl='en-US', tz=360)

pytrends = get_pytrends()

# Sidebar Controls for Search Setup
st.sidebar.header("Search Parameters")

theme_preset = st.sidebar.selectbox(
    "Select Curated Macro Basket:",
    [
        "Custom Entry",
        "Hard Assets (Bitcoin vs Gold vs Scarcity)",
        "Fiat Stress (Debasement vs Inflation vs Money Printer)",
        "Tech & AI Narrative (AI Bubble vs Productivity vs Compute)",
        "AI Disruption & Terminal Value (Jordi Visser Theme)",
        "Energy & Infrastructure Bottlenecks",
        "Structural Labor & Productivity Shift"
    ]
)

# Handle preset keyword lists
if theme_preset == "Hard Assets (Bitcoin vs Gold vs Scarcity)":
    default_keywords = ["Bitcoin", "Gold price", "Scarcity", "Hard assets"]
elif theme_preset == "Fiat Stress (Debasement vs Inflation vs Money Printer)":
    default_keywords = ["Currency debasement", "Money printer", "Inflation rate", "De-dollarization"]
elif theme_preset == "Tech & AI Narrative (AI Bubble vs Productivity vs Compute)":
    default_keywords = ["AI bubble", "Artificial intelligence", "Data center", "Power grid"]
elif theme_preset == "AI Disruption & Terminal Value (Jordi Visser Theme)":
    default_keywords = ["Terminal value", "AI replacement", "White collar jobs", "SaaS multiples"]
elif theme_preset == "Energy & Infrastructure Bottlenecks":
    default_keywords = ["Data center power", "Grid capacity", "Nuclear energy", "Transformer shortage"]
elif theme_preset == "Structural Labor & Productivity Shift":
    default_keywords = ["AI productivity", "Labor shortage", "Automation", "Agentic AI"]
else:
    default_keywords = ["Bitcoin", "Inflation"]

# Keyword inputs
user_keywords = st.sidebar.text_input(
    "Enter keywords (comma-separated, max 5):",
    value=", ".join(default_keywords)
)

kw_list = [kw.strip() for kw in user_keywords.split(",") if kw.strip()][:5]

timeframe_option = st.sidebar.selectbox(
    "Timeframe:",
    ["today 3-m", "today 6-m", "today 12-m", "today 5-y", "all"],
    format_func=lambda x: (
        "Past 3 Months" if x == "today 3-m" else
        ("Past 6 Months" if x == "today 6-m" else
         ("Past 12 Months" if x == "today 12-m" else
          ("Past 5 Years" if x == "today 5-y" else "All History (2004-Present)")))
    )
)

geo_option = st.sidebar.selectbox("Geographic Region:", ["", "US", "GB", "CA", "AU"], format_func=lambda x: "Global (Worldwide)" if x == "" else x)

if st.sidebar.button("Fetch Trend Data"):
    if not kw_list:
        st.warning("Please enter at least one valid keyword.")
    else:
        with st.spinner(f"Querying Google Trends for: {', '.join(kw_list)}..."):
            try:
                pytrends.build_payload(kw_list, cat=0, timeframe=timeframe_option, geo=geo_option, gprop='')
                df = pytrends.interest_over_time()
                
                if not df.empty:
                    if 'isPartial' in df.columns:
                        df = df.drop(columns=['isPartial'])
                        
                    st.success("Trend data successfully retrieved!")
                    
                    # Main Chart
                    st.subheader("📈 Search Interest Over Time (Scaled 0-100)")
                    st.line_chart(df)
                    
                    # Progression / Digression Momentum Summary
                    st.write("---")
                    st.subheader("🔍 Momentum & Directional Shift")
                    st.caption("Comparing recent search volume against historical average to evaluate progression or digression.")
                    
                    cols = st.columns(len(kw_list))
                    for i, kw in enumerate(kw_list):
                        if kw in df.columns:
                            recent_val = df[kw].iloc[-1]
                            avg_val = df[kw].mean()
                            change_pct = ((recent_val - avg_val) / avg_val) * 100 if avg_val > 0 else 0
                            
                            with cols[i]:
                                status = "📈 Accelerating (Progression)" if change_pct >= 0 else "📉 Cooling (Digression)"
                                st.metric(
                                    label=kw,
                                    value=f"{recent_val} / 100",
                                    delta=f"{change_pct:+.1f}% vs Avg",
                                    help=status
                                )
                    
                    # Raw Data View
                    with st.expander("View Raw Historical Data Table"):
                        st.dataframe(df, use_container_width=True)
                        
                else:
                    st.warning("No data returned for these keywords. Try broadening terms or changing the timeframe.")
            except Exception as e:
                st.error(f"An error occurred while fetching data from Google Trends: {e}")
                st.info("Note: Google Trends occasionally rate-limits automated requests if queried too rapidly. If this happens, wait a minute and try again.")
else:
    st.info("👈 Use the sidebar to configure your keywords and timeframe, then click **Fetch Trend Data** to launch the analysis.")