import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------------
# Page Config
# ------------------------------------------------
st.set_page_config(page_title="Titanic Survival Analysis Dashboard", layout="wide")

st.title("🚢 Titanic Survival Analysis Dashboard")
st.write("Analyze survival trends from the Titanic dataset.")

# ------------------------------------------------
# Load & Clean Data
# ------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("D:\\CODES\\Data Science\\DATA\\titanic.csv")

    # Drop rows with missing values
    df = df.dropna()

    # Map numeric codes to labels
    df["Pclass_Label"] = df["Pclass"].map({1: "1st Class", 2: "2nd Class", 3: "3rd Class"})
    df["Survived_Label"] = df["Survived"].map({0: "Did Not Survive", 1: "Survived"})

    return df

df = load_data()

# ------------------------------------------------
# 1. Preview Dataset & Data Cleaning
# ------------------------------------------------
st.header("1. Dataset Preview (After Cleaning)")
st.dataframe(df.head(10))
st.caption(f"Dataset contains {df.shape[0]} rows after dropping missing values. "
           f"Pclass and Survived have been mapped to readable labels.")

# ------------------------------------------------
# 2. Survival Rates by Passenger Class and Gender
# ------------------------------------------------
st.header("2. Survival Rates by Passenger Class and Gender")

survival_by_class = (
    df.groupby("Pclass_Label")["Survived"].mean() * 100
).round(2).reset_index()
survival_by_class.columns = ["Passenger Class", "Survival Rate (%)"]

survival_by_gender = (
    df.groupby("Sex")["Survived"].mean() * 100
).round(2).reset_index()
survival_by_gender.columns = ["Gender", "Survival Rate (%)"]

survival_by_class_gender = (
    df.groupby(["Pclass_Label", "Sex"])["Survived"].mean() * 100
).round(2).reset_index()
survival_by_class_gender.columns = ["Passenger Class", "Gender", "Survival Rate (%)"]

col1, col2 = st.columns(2)
with col1:
    st.subheader("By Passenger Class")
    st.dataframe(survival_by_class)
with col2:
    st.subheader("By Gender")
    st.dataframe(survival_by_gender)

st.subheader("By Passenger Class & Gender (Combined)")
st.dataframe(survival_by_class_gender)

# ------------------------------------------------
# 3. Boxplot: Age Distribution by Survival Status
# ------------------------------------------------
st.header("3. Age Distribution by Survival Status")

fig1, ax1 = plt.subplots(figsize=(8, 5))
sns.boxplot(x="Survived_Label", y="Age", data=df, ax=ax1, palette="Set2")
ax1.set_title("Age Distribution by Survival Status")
ax1.set_xlabel("Survival Status")
ax1.set_ylabel("Age")
st.pyplot(fig1)

# ------------------------------------------------
# 4. Average Age for Survivors and Non-Survivors
# ------------------------------------------------
st.header("4. Average Age: Survivors vs Non-Survivors")

avg_age = df.groupby("Survived_Label")["Age"].mean().round(2)

col3, col4 = st.columns(2)
col3.metric("Avg Age - Survived", f"{avg_age.get('Survived', 0):.2f}")
col4.metric("Avg Age - Did Not Survive", f"{avg_age.get('Did Not Survive', 0):.2f}")

# ------------------------------------------------
# Footer
# ------------------------------------------------
st.markdown("---")
st.caption("Titanic Survival Analysis Dashboard | Streamlit WebApp | PRN: 125M1H031")
