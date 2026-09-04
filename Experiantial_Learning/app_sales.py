import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------------
# Page Config
# ------------------------------------------------
st.set_page_config(page_title="Retail Sales Dashboard", layout="wide")

st.title("🛒 Retail Sales Dashboard")
st.write("Analyze daily retail sales data and visualize product performance.")

# ------------------------------------------------
# Load Data
# ------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("D:\\CODES\\Data Science\\DATA\\sales - sales (1).csv")
    df["Date"] = pd.to_datetime(df["Date"])
    return df

df = load_data()

# ------------------------------------------------
# 1. Load and Preview Dataset
# ------------------------------------------------
st.header("1. Dataset Preview")
st.dataframe(df.head(10))
st.caption(f"Dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")

# ------------------------------------------------
# 2. Summary Statistics (Mean & Median of Daily Revenue)
# ------------------------------------------------
st.header("2. Summary Statistics of Daily Revenue")

col1, col2 = st.columns(2)
col1.metric("Mean Daily Revenue", f"₹{df['Revenue'].mean():.2f}")
col2.metric("Median Daily Revenue", f"₹{df['Revenue'].median():.2f}")

# ------------------------------------------------
# 3. Total Units Sold and Revenue by Product Category
# ------------------------------------------------
st.header("3. Total Units Sold & Revenue by Product Category")

category_summary = df.groupby("ProductCategory").agg(
    Total_Units_Sold=("UnitsSold", "sum"),
    Total_Revenue=("Revenue", "sum")
).reset_index()

st.dataframe(category_summary)

# ------------------------------------------------
# 4. Line Chart: Daily Revenue Trend
# ------------------------------------------------
st.header("4. Daily Revenue Trend Over Time")

daily_revenue = df.groupby("Date")["Revenue"].sum().reset_index()

fig1, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(daily_revenue["Date"], daily_revenue["Revenue"], color="teal", marker="o", markersize=3)
ax1.set_xlabel("Date")
ax1.set_ylabel("Revenue")
ax1.set_title("Daily Revenue Trend")
plt.xticks(rotation=45)
st.pyplot(fig1)

# ------------------------------------------------
# 5. Bar Chart: Total Revenue by Product Category
# ------------------------------------------------
st.header("5. Total Revenue by Product Category")

fig2, ax2 = plt.subplots(figsize=(8, 4))
ax2.bar(category_summary["ProductCategory"], category_summary["Total_Revenue"], color="orange")
ax2.set_xlabel("Product Category")
ax2.set_ylabel("Total Revenue")
ax2.set_title("Total Revenue Comparison Across Product Categories")
st.pyplot(fig2)

# ------------------------------------------------
# Footer
# ------------------------------------------------
st.markdown("---")
st.caption("Retail Sales Dashboard | Streamlit WebApp | PRN: 125M1H031")
