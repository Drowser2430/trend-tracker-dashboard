
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV files
df = pd.read_csv("trend_phase_summary.csv")  # Trend phase summary
raw_data = pd.read_csv("tiktok_trend_tracker_sample.csv")  # Original data

# Add a placeholder 'Category' column if not already present
if 'Category' not in raw_data.columns:
    raw_data['Category'] = ['Dance'] * 14 + ['AI'] * 14 + ['Cleaning'] * 14

# App title
st.title("\U0001F4C8 TikTok Trend Tracker Dashboard")
st.write("Search for a category to discover trending hashtags, viral hooks, and suggested scripts based on data from previous high-performing videos.")

# Filter by Category
st.sidebar.header("🔍 Filter by Category")
selected_category = st.sidebar.selectbox("Choose a category to explore:", raw_data['Category'].unique())
category_data = raw_data[raw_data['Category'] == selected_category]

# Hashtag Search
st.subheader("Trend Growth Over Time")
search_input = st.text_input("Search for a hashtag in this category (e.g. #dancechallenge):")
filtered_tags = category_data[category_data["Hashtag"].str.contains(search_input, case=False)]["Hashtag"].unique()

if len(filtered_tags) == 0:
    st.warning("No matching hashtags found.")
else:
    selected_tags = st.multiselect(
        "Select matching hashtags to compare:",
        options=filtered_tags,
        default=filtered_tags
    )

    for tag in selected_tags:
        subset = category_data[category_data["Hashtag"] == tag]
        st.line_chart(subset.set_index("Date")["Views"])

# Summary table
st.subheader("\U0001F4CA Trend Phase Summary")
st.dataframe(df[df['Hashtag'].isin(category_data['Hashtag'].unique())])

st.caption("Built with Streamlit · Created by Darius Rowser")
