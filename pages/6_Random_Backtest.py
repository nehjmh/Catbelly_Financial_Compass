import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import datetime
import random
import itertools

st.set_page_config(
    page_title="Random Backtest Rumble",
    page_icon="🎲",
    layout="wide"
)

st.title("🎲 Random Backtest Rumble Engine")
st.markdown(
    "Pit tickers against each other across randomized time windows drawn from **1985 to the present**. "
    "Run 9-round multi-year match-ups, rapid **100-round single-day sprints**, or **All Durations**!"
)

st.markdown("---")

# --- SIDEBAR GLOBAL CONTROLS ---
st.sidebar.markdown("### 📅 Date Pool & Duration Setup")

MIN_DATE = datetime.date(1985, 1, 1)
MAX_DATE = datetime.date.today()

date_range = st.sidebar.date_input(
    "Allowable Date Pool:",
    value=(MIN_DATE, MAX_DATE),
    min_value=MIN_DATE,
    max_value=MAX_DATE
)

if isinstance(date_range, tuple) and len(date_range) == 2:
    pool_start, pool_end = date_range
else:
    pool_start, pool_end = MIN_DATE, MAX_DATE

# Duration Options including "All Durations"
DURATION_OPTIONS = {
    "All Durations": "ALL",
    "1-Day (100-Sample Sprint)": 0.00396, # ~1 day
    "3 Months": 0.25,
    "6 Months": 0.5,
    "9 Months": 0.75,
    "12 Months": 1.0,
    "2 Years": 2.0,
    "5 Years": 5.0
}

duration_label = st.sidebar.selectbox(
    "Fixed Round Duration:",
    options=list(DURATION_OPTIONS.keys()),
    index=0
)

duration_choice_yrs = DURATION_OPTIONS[duration_label]
is_1day_mode = (duration_label == "1-Day (100-Sample Sprint)")
is_all_mode = (duration_label == "All Durations")

# Set target rounds per duration tier
target_rounds = 100 if is_1day_mode else 9

initial_capital = st.sidebar.number_input("Starting Balance ($):", min_value=1000, value=10000, step=1000)

# --- HELPER FUNCTIONS ---
@st.cache_data(ttl=86400)
def get_effective_start_date(tickers, default_start):
    """Finds the youngest inception date among selected tickers to ensure data availability."""
    latest_inception = default_start
    for t in tickers:
        try:
            ticker_obj = yf.Ticker(t)
            hist = ticker_obj.history(period="max")
            if not hist.empty:
                first_date = hist.index[0].date()
                if first_date > latest_inception:
                    latest_inception = first_date
        except Exception:
            pass
    return latest_inception

@st.cache_data(ttl=3600)
def fetch_historical_prices(tickers, start_date, end_date):
    fetch_start = start_date - datetime.timedelta(days=10)
    df = yf.download(tickers, start=fetch_start, end=end_date, progress=False)["Close"]
    return df

def generate_single_duration_windows(min_date, max_date, fixed_duration_years, price_df, tickers, num_rounds):
    """Generates valid random windows for a specific duration setting."""
    windows = []
    
    # Fast path for 1-day random sampling
    if isinstance(fixed_duration_years, (int, float)) and fixed_duration_years < 0.01:
        daily_pct = price_df[tickers].pct_change().dropna()
        valid_dates = daily_pct.index.date
        
        if len(valid_dates) > 0:
            sample_size = min(num_rounds, len(valid_dates))
            sampled_dates = sorted(random.sample(list(valid_dates), sample_size))
            
            for idx, s_date in enumerate(sampled_dates, 1):
                windows.append({
                    "Round": f"Round {idx}",
                    "Duration": "1 Day",
                    "Start": s_date,
                    "End": s_date,
                    "IsSingleDay": True
                })
        return windows

    # Multi-day random window sampling
    days_in_window = int(fixed_duration_years * 365.25)
    dur_label = f"{int(round(fixed_duration_years * 12))} Mo" if fixed_duration_years < 1.0 else f"{int(fixed_duration_years)} Yr"
    
    attempts = 0
    round_idx = 1
    
    while len(windows) < num_rounds and attempts < (num_rounds * 20):
        attempts += 1
        latest_start = max_date - datetime.timedelta(days=days_in_window)
        if latest_start <= min_date:
            w_start = min_date
        else:
            days_between = (latest_start - min_date).days
            rand_days = random.randint(0, max(1, days_between))
            w_start = min_date + datetime.timedelta(days=rand_days)
            
        w_end = min(w_start + datetime.timedelta(days=days_in_window), max_date)
        
        w_df = price_df.loc[(price_df.index.date >= w_start) & (price_df.index.date <= w_end)]
        
        if len(w_df) >= 5 and not w_df[tickers].isna().any().any():
            windows.append({
                "Round": f"Round {round_idx}",
                "Duration": dur_label,
                "Start": w_start,
                "End": w_end,
                "IsSingleDay": False
            })
            round_idx += 1
            
    return windows

def generate_valid_windows(min_date, max_date, fixed_duration_years, price_df, tickers, num_rounds):
    """Master window generator supporting specific durations or 'All Durations'."""
    if fixed_duration_years == "ALL":
        all_windows = []
        sub_specs = [
            (0.00396, 100), # 1-Day Sprint (100 rounds)
            (0.25, 9),      # 3 Mo (9 rounds)
            (0.5, 9),       # 6 Mo (9 rounds)
            (0.75, 9),      # 9 Mo (9 rounds)
            (1.0, 9),       # 12 Mo (9 rounds)
            (2.0, 9),       # 2 Yr (9 rounds)
            (5.0, 9)        # 5 Yr (9 rounds)
        ]
        
        global_round_counter = 1
        for dur_yrs, r_count in sub_specs:
            res_wins = generate_single_duration_windows(min_date, max_date, dur_yrs, price_df, tickers, r_count)
            for w in res_wins:
                w["Round"] = f"Round {global_round_counter}"
                all_windows.append(w)
                global_round_counter += 1
        return all_windows
    else:
        return generate_single_duration_windows(min_date, max_date, fixed_duration_years, price_df, tickers, num_rounds)

# --- TABS INTERFACE ---
tab_head_to_head, tab_multi_rumble = st.tabs(["🥊 Head-to-Head Duel", "🏆 Multi-Ticker Factorial Tournament"])

# ==============================================================================
# TAB 1: HEAD-TO-HEAD DUEL
# ==============================================================================
with tab_head_to_head:
    st.markdown("### 🥊 1-on-1 Head-to-Head Matchup")
    col_asset_a, col_asset_b = st.columns(2)

    with col_asset_a:
        ticker_a = st.text_input("Contender A Ticker:", value="QQQ", key="t_a").strip().upper()
        
    with col_asset_b:
        ticker_b = st.text_input("Contender B Ticker:", value="SPY", key="t_b").strip().upper()

    if ticker_a and ticker_b:
        h2h_tickers = list(set([ticker_a, ticker_b]))
        effective_start = get_effective_start_date(h2h_tickers, pool_start)
        
        if effective_start > pool_start:
            st.caption(f"ℹ️ Date pool automatically adjusted to **{effective_start.strftime('%b %Y')}** based on inception date.")

        with st.spinner(f"Fetching market data for {ticker_a} vs {ticker_b}..."):
            h2h_data = fetch_historical_prices(h2h_tickers, effective_start, pool_end)

        if not h2h_data.empty and ticker_a in h2h_data.columns and ticker_b in h2h_data.columns:
            h2h_data = h2h_data.ffill().bfill()
            daily_returns = h2h_data.pct_change()

            if is_all_mode:
                btn_label = f"🎲 RUN ALL DURATIONS ({ticker_a} vs {ticker_b})"
            elif is_1day_mode:
                btn_label = f"🎲 RUN 100-DAY SPRINT ({ticker_a} vs {ticker_b})"
            else:
                btn_label = f"🎲 RUN HEAD-TO-HEAD DUEL ({target_rounds} Rounds)"

            # Force window regeneration when duration mode changes or button clicked
            if "h2h_windows" not in st.session_state or st.button(btn_label, use_container_width=True, key="btn_h2h"):
                st.session_state.h2h_windows = generate_valid_windows(
                    effective_start, pool_end, duration_choice_yrs, h2h_data, h2h_tickers, target_rounds
                )

            h2h_windows = st.session_state.h2h_windows

            results_h2h = []
            wins_a, wins_b, ties = 0, 0, 0

            for w in h2h_windows:
                if w.get("IsSingleDay", False):
                    day_dt = pd.Timestamp(w["Start"])
                    if day_dt in daily_returns.index:
                        ret_a = float(daily_returns.loc[day_dt, ticker_a]) * 100
                        ret_b = float(daily_returns.loc[day_dt, ticker_b]) * 100
                    else:
                        continue
                    tf_str = f"{w['Start'].strftime('%b %d, %Y')} (1 Day)"
                else:
                    w_df = h2h_data.loc[(h2h_data.index.date >= w["Start"]) & (h2h_data.index.date <= w["End"])]
                    if w_df.empty or len(w_df) < 2:
                        continue
                    ret_a = ((w_df[ticker_a].iloc[-1] - w_df[ticker_a].iloc[0]) / w_df[ticker_a].iloc[0]) * 100
                    ret_b = ((w_df[ticker_b].iloc[-1] - w_df[ticker_b].iloc[0]) / w_df[ticker_b].iloc[0]) * 100
                    tf_str = f"{w['Start'].strftime('%b %Y')} - {w['End'].strftime('%b %Y')} ({w['Duration']})"

                if ret_a > ret_b:
                    winner = ticker_a
                    wins_a += 1
                elif ret_b > ret_a:
                    winner = ticker_b
                    wins_b += 1
                else:
                    winner = "Tie"
                    ties += 1

                results_h2h.append({
                    "Round": w["Round"],
                    "Timeframe": tf_str,
                    f"{ticker_a} Return": ret_a,
                    f"{ticker_b} Return": ret_b,
                    "Round Winner": f"🏆 {winner}" if winner != "Tie" else "🤝 Tie"
                })

            df_h2h = pd.DataFrame(results_h2h)

            if not df_h2h.empty:
                st.markdown("---")
                score_col1, score_col2, score_col3 = st.columns(3)
                
                win_pct_a = (wins_a / len(df_h2h)) * 100
                win_pct_b = (wins_b / len(df_h2h)) * 100
                
                score_col1.metric(f"{ticker_a} Score", f"{wins_a} / {len(df_h2h)} Wins", delta=f"{win_pct_a:.1f}% Win Rate")
                score_col2.metric(f"{ticker_b} Score", f"{wins_b} / {len(df_h2h)} Wins", delta=f"{win_pct_b:.1f}% Win Rate")

                with score_col3:
                    verdict = f"🏆 **{ticker_a} Dominates!**" if wins_a > wins_b else f"🏆 **{ticker_b} Dominates!**" if wins_b > wins_a else "🤝 **Dead Heat Tie!**"
                    st.subheader(verdict)

                styled_df = df_h2h.style.format({f"{ticker_a} Return": "{:+.2f}%", f"{ticker_b} Return": "{:+.2f}%"})
                
                if is_1day_mode or is_all_mode:
                    st.dataframe(styled_df, use_container_width=True, hide_index=True, height=450)
                else:
                    st.dataframe(styled_df, use_container_width=True, hide_index=True)
        else:
            st.error("Could not fetch pricing data for selected tickers.")

# ==============================================================================
# TAB 2: MULTI-TICKER FACTORIAL TOURNAMENT
# ==============================================================================
with tab_multi_rumble:
    st.markdown("### 🏆 Round-Robin Multi-Ticker Tournament")
    st.write(
        "Enter tickers below to run round-robin tournaments across single-day or multi-year windows."
    )

    tickers_raw = st.text_input(
        "Enter Ticker Symbols (comma-separated):", 
        value="QQQ, SPY, SMH, IWY, SCHD",
        help="Example: QQQ, SPY, SMH, IWY, SCHD"
    )

    multi_tickers = [t.strip().upper() for t in tickers_raw.split(",") if t.strip()]
    unique_tickers = list(set(multi_tickers))

    pairs = list(itertools.combinations(unique_tickers, 2))
    st.caption(f"**Loaded Tickers ({len(unique_tickers)}):** {', '.join(unique_tickers)} | **Pairwise Duels:** {len(pairs)} match-ups")

    if len(unique_tickers) < 2:
        st.warning("Please enter at least 2 unique tickers to run a tournament.")
        st.stop()

    m_effective_start = get_effective_start_date(unique_tickers, pool_start)
    if m_effective_start > pool_start:
        st.caption(f"ℹ️ Tournament date pool automatically adjusted to **{m_effective_start.strftime('%b %Y')}** based on inception date.")

    with st.spinner("Downloading historical price matrix for all tickers..."):
        all_multi_data = fetch_historical_prices(unique_tickers, m_effective_start, pool_end)

    if not all_multi_data.empty:
        all_multi_data = all_multi_data.ffill().bfill()
        multi_daily_returns = all_multi_data.pct_change()

        btn_multi_label = "🎲 RUN TOURNAMENT (All Durations)" if is_all_mode else f"🎲 RUN TOURNAMENT ({target_rounds} Rounds per Pair)"

        if st.button(btn_multi_label, use_container_width=True, key="btn_multi"):
            st.session_state.multi_windows = generate_valid_windows(
                m_effective_start, pool_end, duration_choice_yrs, all_multi_data, unique_tickers, target_rounds
            )

        if "multi_windows" in st.session_state:
            multi_windows = st.session_state.multi_windows

            scores = {t: {"Wins": 0, "Losses": 0, "Ties": 0, "Total Rounds": 0, "Total Return Sum": 0.0} for t in unique_tickers}
            matchup_logs = []

            for t1, t2 in pairs:
                if t1 not in all_multi_data.columns or t2 not in all_multi_data.columns:
                    continue

                t1_wins, t2_wins = 0, 0
                
                for w in multi_windows:
                    if w.get("IsSingleDay", False):
                        day_dt = pd.Timestamp(w["Start"])
                        if day_dt in multi_daily_returns.index:
                            ret1 = float(multi_daily_returns.loc[day_dt, t1]) * 100
                            ret2 = float(multi_daily_returns.loc[day_dt, t2]) * 100
                        else:
                            continue
                    else:
                        w_df = all_multi_data.loc[(all_multi_data.index.date >= w["Start"]) & (all_multi_data.index.date <= w["End"])]
                        if w_df.empty or len(w_df) < 2:
                            continue
                        ret1 = ((w_df[t1].iloc[-1] - w_df[t1].iloc[0]) / w_df[t1].iloc[0]) * 100
                        ret2 = ((w_df[t2].iloc[-1] - w_df[t2].iloc[0]) / w_df[t2].iloc[0]) * 100

                    scores[t1]["Total Rounds"] += 1
                    scores[t2]["Total Rounds"] += 1
                    scores[t1]["Total Return Sum"] += ret1
                    scores[t2]["Total Return Sum"] += ret2

                    if ret1 > ret2:
                        scores[t1]["Wins"] += 1
                        scores[t2]["Losses"] += 1
                        t1_wins += 1
                    elif ret2 > ret1:
                        scores[t2]["Wins"] += 1
                        scores[t1]["Losses"] += 1
                        t2_wins += 1
                    else:
                        scores[t1]["Ties"] += 1
                        scores[t2]["Ties"] += 1

                matchup_logs.append({
                    "Matchup": f"{t1} vs {t2}",
                    f"{t1} Score": f"{t1_wins} Wins",
                    f"{t2} Score": f"{t2_wins} Wins",
                    "Winner": t1 if t1_wins > t2_wins else t2 if t2_wins > t1_wins else "Tie"
                })

            leaderboard = []
            for t, metrics in scores.items():
                tot = max(1, metrics["Total Rounds"])
                win_rate = (metrics["Wins"] / tot) * 100
                avg_ret = metrics["Total Return Sum"] / tot
                leaderboard.append({
                    "Ticker": t,
                    "Total Wins": metrics["Wins"],
                    "Total Losses": metrics["Losses"],
                    "Ties": metrics["Ties"],
                    "Win Rate (%)": win_rate,
                    "Avg Return (%)": avg_ret
                })

            df_leaderboard = pd.DataFrame(leaderboard).sort_values(by=["Win Rate (%)", "Avg Return (%)"], ascending=False).reset_index(drop=True)
            df_leaderboard.index = df_leaderboard.index + 1

            st.markdown("---")
            st.markdown("## 🥇 Final Tournament Placement Leaderboard")

            top_ticker = df_leaderboard.iloc[0]["Ticker"]
            top_rate = df_leaderboard.iloc[0]["Win Rate (%)"]
            st.success(f"🏆 **Grand Champion: {top_ticker}** (Achieved a **{top_rate:.1f}% Win Rate** across all pairwise duels!)")

            st.dataframe(
                df_leaderboard.style.format({
                    "Win Rate (%)": "{:.1f}%",
                    "Avg Return (%)": "{:+.2f}%"
                }),
                use_container_width=True
            )

            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("##### 🤝 Pairwise Matchup Log")
            st.dataframe(pd.DataFrame(matchup_logs), use_container_width=True, hide_index=True)