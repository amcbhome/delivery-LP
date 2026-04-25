import streamlit as st
import numpy as np
import pandas as pd
from scipy.optimize import linprog

st.set_page_config(page_title="Logistics Optimizer", layout="centered")

st.title("🚚 Delivery Route Optimizer")
st.markdown("Developed by [amcbhome](https://github.com/amcbhome)")

# --- SIDEBAR INPUTS ---
st.sidebar.header("Global Parameters")
cost_per_mile = st.sidebar.number_input("Cost per unit/mile (£)", value=5.0, step=0.5)

st.sidebar.header("Depot Supply")
s1 = st.sidebar.number_input("Depot 1 Supply", value=2500)
s2 = st.sidebar.number_input("Depot 2 Supply", value=3100)
s3 = st.sidebar.number_input("Depot 3 Supply", value=1250)

st.sidebar.header("Store Capacity")
c1 = st.sidebar.number_input("Store 1 Capacity", value=2000)
c2 = st.sidebar.number_input("Store 2 Capacity", value=3000)
c3 = st.sidebar.number_input("Store 3 Capacity", value=2000)

# --- CONSTANTS ---
distances = np.array([
    [22, 33, 40],
    [27, 30, 22],
    [36, 20, 25],
])

supply_fixed = [s1, s2, s3]
store_caps = [c1, c2, c3]

# --- OPTIMIZATION LOGIC ---
c = (distances * cost_per_mile).flatten()

# Constraints: Supply (Equality)
A_eq = np.zeros((3, 9))
for i in range(3):
    A_eq[i, 3*i : 3*i+3] = 1

# Constraints: Capacity (Upper Bound)
A_ub = np.zeros((3, 9))
for j in range(3):
    for i in range(3):
        A_ub[j, 3*i + j] = 1

if st.button("Run Optimization Engine"):
    if sum(supply_fixed) > sum(store_caps):
        st.error(f"❌ Infeasible: Total Supply ({sum(supply_fixed)}) exceeds Total Capacity ({sum(store_caps)})!")
    else:
        res = linprog(c=c, A_ub=A_ub, b_ub=store_caps, A_eq=A_eq, b_eq=supply_fixed, method="highs")

        if res.success:
            st.success(f"### Optimal Total Cost: £{res.fun:,.2f}")
            
            # 1. Format Matrix (Trimmed to 0 decimal places)
            optimal_x = res.x.reshape(3, 3).astype(int)
            df_matrix = pd.DataFrame(
                optimal_x, 
                index=["Depot 1", "Depot 2", "Depot 3"], 
                columns=["Store 1", "Store 2", "Store 3"]
            )
            
            st.subheader("Optimal Shipping Schedule (Units)")
            st.table(df_matrix)

            # 2. Format Slack Analysis (Trimmed to 0 decimal places)
            st.subheader("Capacity Utilization & Slack")
            delivered = optimal_x.sum(axis=0)
            slack = np.array(store_caps) - delivered
            
            df_slack = pd.DataFrame({
                "Capacity": store_caps,
                "Actual Delivered": delivered,
                "Remaining Slack": slack
            }, index=["Store 1", "Store 2", "Store 3"])
            
            # Displaying as a clean table instead of a chart
            st.table(df_slack)
            
        else:
            st.error("Optimization failed. The constraints provided do not allow for a valid solution.")
