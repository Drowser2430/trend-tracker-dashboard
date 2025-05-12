
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV files
df = pd.read_csv("trend_phase_summary.csv")  # Trend phase summary
raw_data = pd.read_csv("tiktok_trend_tracker_sample.csv")  # Original data

# App title
st.title("📈 TikTok Trend Tracker Dashboard")
st.write("Track how TikTok hashtags rise, peak, and fade over time.")

# Trend line chart section
st.subheader("Trend Growth Over Time")
selected_tags = st.multiselect(
    "Select hashtags to compare",
    raw_data["Hashtag"].unique(),
    default=raw_data["Hashtag"].unique()
)

for tag in selected_tags:
    subset = raw_data[raw_data["Hashtag"] == tag]
    st.line_chart(subset.set_index("Date")["Views"])

# Summary table
st.subheader("📊 Trend Phase Summary")
st.dataframe(df)

st.caption("Built with Streamlit · Created by Darius Rowser")
