import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------------
# Page Config
# ------------------------------------------------
st.set_page_config(page_title="Student Grades Explorer", layout="wide")

st.title("🎓 Student Grades Explorer")
st.write("Explore student performance data across different subjects and visualize their scores.")

# ------------------------------------------------
# Load Data
# ------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("grades.csv")
    return df

df = load_data()

# ------------------------------------------------
# 1. Load and Preview Dataset
# ------------------------------------------------
st.header("1. Dataset Preview")
st.dataframe(df.head(10))
st.caption(f"Dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")

# ------------------------------------------------
# 2. Select Subject from Dropdown
# ------------------------------------------------
st.header("2. Select a Subject")

subjects = sorted(df["Subject"].unique())
selected_subject = st.selectbox("Choose a subject:", subjects)

subject_df = df[df["Subject"] == selected_subject]

# ------------------------------------------------
# 3. Summary Statistics for Selected Subject (Final Scores)
# ------------------------------------------------
st.header(f"3. Summary Statistics for {selected_subject} (Final Scores)")

mean_final = subject_df["Final"].mean()
median_final = subject_df["Final"].median()
std_final = subject_df["Final"].std()

col1, col2, col3 = st.columns(3)
col1.metric("Mean", f"{mean_final:.2f}")
col2.metric("Median", f"{median_final:.2f}")
col3.metric("Std Deviation", f"{std_final:.2f}")

# ------------------------------------------------
# 4. Boxplot: Final Score Distribution Across Subjects
# ------------------------------------------------
st.header("4. Final Score Distribution Across All Subjects")

fig1, ax1 = plt.subplots(figsize=(8, 5))
sns.boxplot(x="Subject", y="Final", data=df, ax=ax1, palette="Set2")
ax1.set_title("Final Score Distribution by Subject")
ax1.set_xlabel("Subject")
ax1.set_ylabel("Final Score")
st.pyplot(fig1)

# ------------------------------------------------
# 5. Scatterplot: Test1 vs Final for Selected Subject
# ------------------------------------------------
st.header(f"5. Test1 vs Final Scores - {selected_subject}")

fig2, ax2 = plt.subplots(figsize=(8, 5))
sns.scatterplot(x="Test1", y="Final", data=subject_df, hue="Subject", ax=ax2, s=80)
ax2.set_title(f"Test1 vs Final Scores ({selected_subject})")
ax2.set_xlabel("Test1 Score")
ax2.set_ylabel("Final Score")
st.pyplot(fig2)

# ------------------------------------------------
# Footer
# ------------------------------------------------
st.markdown("---")
st.caption("Student Grades Explorer | Streamlit WebApp | PRN: 125M1H031")
