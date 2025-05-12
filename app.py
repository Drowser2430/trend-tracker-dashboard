import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV files
df = pd.read_csv("trend_phase_summary.csv")  # Trend phase summary
raw_data = pd.read_csv("tiktok_trend_tracker_sample.csv")  # Original data

# App title
st.title("\U0001F4C8 TikTok Trend Tracker Dashboard")
st.write("Search for a category to discover trending hashtags, viral hooks, and suggested scripts based on data from previous high-performing videos.")

# Simulated login section
with st.sidebar:
    st.header("👤 TikTok Login")
    username = st.text_input("Enter your TikTok username (simulated login):")
    if username:
        st.success(f"Welcome, @{username}!")

# TikTok official content categories
tiktok_categories = [
    "Dance", "Comedy / Skits", "Music / Singing / Covers", "Beauty / Makeup / Skincare",
    "Fashion / Outfits / Styling", "Fitness / Health / Gym", "Food / Recipes / Cooking",
    "Lifestyle / Vlogs / Routines", "DIY / Crafts", "Education / How-To / Tips",
    "Tech / AI / Gadgets", "Business / Finance / Side Hustles", "Motivation / Self-Improvement",
    "Pets / Animals", "Travel / Adventure", "Parenting / Family", "Gaming / Stream Highlights",
    "Books / Reading / Writing", "Cleaning / Organizing / Hacks", "Storytime / Personal Experience"
]

# Filter by Category with dropdown and custom input
st.sidebar.header("🔍 Filter by Category")
category_choice = st.sidebar.selectbox("Choose a TikTok category:", options=tiktok_categories)
custom_category = st.sidebar.text_input("Or enter a custom category:")
selected_category = custom_category if custom_category else category_choice
category_data = raw_data[raw_data['Category'].str.contains(selected_category, case=False, na=False)]

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

# Suggestions based on search
if username and selected_tags.any():
    st.subheader("🎯 Content Suggestions")
    st.markdown("**Next TikTok Idea:** Use the selected hashtag(s) in a 15-second video using trending audio in the \"{0}\" category.".format(selected_category))
    st.markdown("**Suggested Hook:** \"What happens when you try this for 3 days straight?\" 🧠")
    st.markdown("**Script Starter:** \"I didn't think this would work... but then it went viral. Here's what I did:\" ✨")

# Summary table
st.subheader("\U0001F4CA Trend Phase Summary")
st.dataframe(df[df['Hashtag'].isin(category_data['Hashtag'].unique())])

st.caption("Built with Streamlit · Created by Darius Rowser")



 
