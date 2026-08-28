import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Budgeting 101 & Cash Flow", page_icon="💵", layout="wide")

st.title("💵 Budgeting 101: The 50/30/20 Framework")
st.markdown("Build your monthly spending plan and align your cash flow with real financial goals.")

# --- SIDEBAR: INCOME & EXPENSE INPUTS ---
st.sidebar.header("1. Monthly Take-Home Pay")
monthly_income = st.sidebar.number_input("After-Tax Monthly Income ($)", min_value=500, max_value=50000, value=4000, step=100)

st.sidebar.header("2. Monthly Expenses Breakdown")

# Needs Input
st.sidebar.subheader("Essential Needs (50% Target)")
housing = st.sidebar.number_input("Rent / Mortgage ($)", value=1200, step=50)
utilities = st.sidebar.number_input("Utilities & Internet ($)", value=150, step=25)
groceries = st.sidebar.number_input("Groceries ($)", value=400, step=25)
transport = st.sidebar.number_input("Car Payment / Gas / Transit ($)", value=350, step=25)

# Wants Input
st.sidebar.subheader("Wants & Lifestyle (30% Target)")
dining_out = st.sidebar.number_input("Dining Out & Entertainment ($)", value=300, step=25)
subscriptions = st.sidebar.number_input("Streaming & Subscriptions ($)", value=50, step=10)
shopping = st.sidebar.number_input("Personal Shopping & Hobbies ($)", value=200, step=25)

# Savings & Debt Input
st.sidebar.subheader("Savings & Future (20% Target)")
emergency_fund = st.sidebar.number_input("Emergency Savings ($)", value=300, step=25)
investments = st.sidebar.number_input("Roth IRA / Brokerage ($)", value=400, step=25)
extra_debt = st.sidebar.number_input("Extra Debt Paydown ($)", value=100, step=25)

# --- CALCULATIONS ---
total_needs = housing + utilities + groceries + transport
total_wants = dining_out + subscriptions + shopping
total_savings = emergency_fund + investments + extra_debt
total_spent = total_needs + total_wants + total_savings
unallocated = monthly_income - total_spent

# Targets based on 50/30/20
target_needs = monthly_income * 0.50
target_wants = monthly_income * 0.30
target_savings = monthly_income * 0.20

# --- OVERVIEW METRICS ---
st.subheader("Monthly Breakdown vs. 50/30/20 Targets")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Needs (Target: 50%)", 
        value=f"${total_needs:,.0f}", 
        delta=f"{(total_needs/monthly_income)*100:.1f}% of Income"
    )
    st.caption(f"Target: **${target_needs:,.0f}**")

with col2:
    st.metric(
        label="Wants (Target: 30%)", 
        value=f"${total_wants:,.0f}", 
        delta=f"{(total_wants/monthly_income)*100:.1f}% of Income"
    )
    st.caption(f"Target: **${target_wants:,.0f}**")

with col3:
    st.metric(
        label="Savings (Target: 20%)", 
        value=f"${total_savings:,.0f}", 
        delta=f"{(total_savings/monthly_income)*100:.1f}% of Income"
    )
    st.caption(f"Target: **${target_savings:,.0f}**")

with col4:
    if unallocated >= 0:
        st.metric("Unallocated Cash", f"${unallocated:,.0f}", delta="Surplus 🟢")
        st.caption("Ready to deploy into savings!")
    else:
        st.metric("Unallocated Cash", f"${unallocated:,.0f}", delta="Deficit 🔴", delta_color="inverse")
        st.caption("Over budget! Trim wants or needs.")

st.markdown("---")

# --- VISUALIZATIONS ---
c_chart1, c_chart2 = st.columns(2)

with c_chart1:
    st.markdown("#### Category Breakdown")
    cat_df = pd.DataFrame({
        "Category": ["Needs (50%)", "Wants (30%)", "Savings (20%)"],
        "Amount": [total_needs, total_wants, total_savings]
    })
    fig_pie = px.pie(cat_df, values="Amount", names="Category", color="Category",
                     color_discrete_map={"Needs (50%)":"#636EFA", "Wants (30%)":"#EF553B", "Savings (20%)":"#00CC96"},
                     hole=0.4)
    st.plotly_chart(fig_pie, use_container_width=True)

with c_chart2:
    st.markdown("#### Spent vs. Ideal Benchmark")
    bench_df = pd.DataFrame({
        "Category": ["Needs", "Needs", "Wants", "Wants", "Savings", "Savings"],
        "Type": ["Actual", "Target", "Actual", "Target", "Actual", "Target"],
        "Amount": [total_needs, target_needs, total_wants, target_wants, total_savings, target_savings]
    })
    fig_bar = px.bar(bench_df, x="Category", y="Amount", color="Type", barmode="group")
    st.plotly_chart(fig_bar, use_container_width=True)

st.markdown("---")

# --- EDUCATIONAL TIPS SECTION ---
st.subheader("💡 Key Rules of Thumb for 20-Somethings")

col_t1, col_t2, col_t3 = st.columns(3)

with col_t1:
    st.markdown("""
    **1. Pay Yourself First**  
    Treat savings like a non-negotiable bill. Set up an automatic transfer on payday directly to your High-Yield Savings Account (HYSA) or Roth IRA before you spend a dime on lifestyle.
    """)

with col_t2:
    emergency_target = total_needs * 3
    st.markdown(f"""
    **2. Build the 3-Month Cushion**  
    Before investing aggressively in single stocks, keep 3 to 6 months of basic **Needs** (${emergency_target:,.0f}) in a liquid cash instrument yielding 4%+ (like SPAXX or PULS).
    """)

with col_t3:
    st.markdown("""
    **3. Beware of Subscription Creep**  
    Small recurring monthly fees feel invisible, but 5 neglected $15 subscriptions equal $900/year—cash that could be clearing the inflation hurdle in an index fund.
    """)