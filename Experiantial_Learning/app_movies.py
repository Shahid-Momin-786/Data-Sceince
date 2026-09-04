import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------------
# Page Config
# ------------------------------------------------
st.set_page_config(page_title="Movie Ratings Explorer", layout="wide")

st.title("🎬 Movie Ratings Explorer")
st.write("Explore and analyze movie ratings data based on selected genres.")

# ------------------------------------------------
# Load Data
# ------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("D:\\CODES\\Data Science\\DATA\\movies.csv")
    # Drop rows with missing values in key columns
    key_columns = ["Genre", "Year", "Rating", "Votes"]
    df = df.dropna(subset=key_columns)
    return df

df = load_data()

# ------------------------------------------------
# 1. Load and Preview Dataset
# ------------------------------------------------
st.header("1. Dataset Preview")
st.dataframe(df.head(10))
st.caption(f"Dataset contains {df.shape[0]} rows and {df.shape[1]} columns after dropping missing values.")

# ------------------------------------------------
# 2. Select Genre from Dropdown
# ------------------------------------------------
st.header("2. Select a Genre")

genres = sorted(df["Genre"].unique())
selected_genre = st.selectbox("Choose a genre:", genres)

genre_df = df[df["Genre"] == selected_genre]

# ------------------------------------------------
# 3. Summary Statistics for Selected Genre
# ------------------------------------------------
st.header(f"3. Summary Statistics for {selected_genre}")

avg_rating = genre_df["Rating"].mean()
avg_votes = genre_df["Votes"].mean()
median_year = genre_df["Year"].median()

col1, col2, col3 = st.columns(3)
col1.metric("Average Rating", f"{avg_rating:.2f}")
col2.metric("Average Votes", f"{avg_votes:.0f}")
col3.metric("Median Year of Release", f"{median_year:.0f}")

# ------------------------------------------------
# 4. Boxplot: Rating Distribution Across All Genres
# ------------------------------------------------
st.header("4. Rating Distribution Across All Genres")

fig1, ax1 = plt.subplots(figsize=(8, 5))
sns.boxplot(x="Genre", y="Rating", data=df, ax=ax1, palette="Set3")
ax1.set_title("Movie Rating Distribution by Genre")
ax1.set_xlabel("Genre")
ax1.set_ylabel("Rating")
st.pyplot(fig1)

# ------------------------------------------------
# 5. Scatterplot: Votes vs Rating for Selected Genre
# ------------------------------------------------
st.header(f"5. Votes vs Rating - {selected_genre}")

fig2, ax2 = plt.subplots(figsize=(8, 5))
scatter = ax2.scatter(
    genre_df["Votes"], genre_df["Rating"],
    s=genre_df["Votes"] / 20,      # vote count as marker size
    c=genre_df["Rating"],          # rating as color gradient
    cmap="viridis", alpha=0.7, edgecolors="black"
)
ax2.set_title(f"Votes vs Rating ({selected_genre})")
ax2.set_xlabel("Votes")
ax2.set_ylabel("Rating")
cbar = plt.colorbar(scatter, ax=ax2)
cbar.set_label("Rating")
st.pyplot(fig2)

# ------------------------------------------------
# Footer
# ------------------------------------------------
st.markdown("---")
st.caption("Movie Ratings Explorer | Streamlit WebApp | PRN: 125M1H031")
