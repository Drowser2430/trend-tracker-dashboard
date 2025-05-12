import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random

# Load CSV files
df = pd.read_csv("trend_phase_summary.csv")  # Trend phase summary
raw_data = pd.read_csv("tiktok_trend_tracker_sample.csv")  # Original data

# Ensure Category column exists
if "Category" not in raw_data.columns:
    raw_data["Category"] = "Uncategorized"

# Branding Banner / Header
st.markdown("""
    <style>
    .title-banner {
        background-color: #111827;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        color: white;
    }
    .title-banner h2 {
        margin: 0;
        font-size: 2rem;
    }
    .title-banner p {
        margin: 0.5rem 0 0;
        font-size: 1rem;
        opacity: 0.8;
    }
    </style>
    <div class='title-banner'>
        <h2>✨ TikTok Trend Assistant ✨</h2>
        <p>Curated hooks, hashtags, and content flow by category – powered by AI</p>
    </div>
""", unsafe_allow_html=True)

# Simulated login section
with st.container():
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        username = st.text_input("TikTok Username")
    with col2:
        password = st.text_input("Password", type="password")

    logged_in = username and password
    if not logged_in:
        st.warning("Enter your TikTok username and password to continue.")
        st.stop()
    else:
        st.success(f"Welcome, @{username}!")

# Simulated user analytics
st.markdown("---")
st.subheader("📊 Your TikTok Analytics (Simulated)")
hashtag_list = raw_data["Hashtag"].unique().tolist()
user_analytics = {
    "Follower Count": f"{random.randint(2, 500)}K",
    "Avg Views per Video": f"{random.randint(1000, 30000)}",
    "Engagement Rate": f"{round(random.uniform(1.5, 12.0), 2)}%",
    "Top Performing Video": f"'{random.choice(hashtag_list) if hashtag_list else '#trending'}' with {random.randint(10000, 300000)} views"
}
for metric, value in user_analytics.items():
    st.metric(label=metric, value=value)

# Step-through interface
st.markdown("---")
st.subheader("1. Choose Your Category")
tiktok_categories = [
    "Dance", "Comedy / Skits", "Music / Singing / Covers", "Beauty / Makeup / Skincare",
    "Fashion / Outfits / Styling", "Fitness / Health / Gym", "Food / Recipes / Cooking",
    "Lifestyle / Vlogs / Routines", "DIY / Crafts", "Education / How-To / Tips",
    "Tech / AI / Gadgets", "Business / Finance / Side Hustles", "Motivation / Self-Improvement",
    "Pets / Animals", "Travel / Adventure", "Parenting / Family", "Gaming / Stream Highlights",
    "Books / Reading / Writing", "Cleaning / Organizing / Hacks", "Storytime / Personal Experience"
]
category_choice = st.selectbox("Select a TikTok category", options=tiktok_categories)
custom_category = st.text_input("Or enter a custom category")
selected_category = custom_category if custom_category else category_choice
category_data = raw_data[raw_data['Category'].str.contains(selected_category, case=False, na=False)]

st.markdown("---")
st.subheader("2. Get AI-Powered Hashtags & Hooks")

if not category_data.empty:
    hashtags = category_data["Hashtag"].unique().tolist()
    st.markdown("**Suggested Hashtags:**")
    st.write(random.sample(hashtags, min(5, len(hashtags))))
else:
    st.info("No data found for this category. Showing sample hashtags.")
    sample_hashtags = ["#fyp", "#trendingnow", "#viralvideo", "#tiktoktrend", "#2025vibes"]
    st.write(sample_hashtags)

st.markdown("**AI-Generated Hook:**")
st.success(random.choice([
    "You won't believe what happened when I tried this...",
    "This might be the smartest thing I’ve done in 2025.",
    "Here's what no one tells you about [insert topic]...",
    "This trend changed my entire content strategy.",
    "3 reasons this works better than anything else I've tried."
]))

st.markdown("**Script Starter:**")
st.code(random.choice([
    "I didn’t expect this to work, but then this happened…",
    "Here’s what I learned after trying [trend] for 7 days straight.",
    "So I found this trend and thought, why not?",
    "Let’s break down why this blew up on TikTok...",
    "I was today years old when I realized this hack."
]))

st.markdown("---")
st.subheader("3. View Trend Phase Summary")
st.dataframe(df[df['Hashtag'].isin(category_data['Hashtag'].unique())])

st.caption("Built with Streamlit · Created by Darius Rowser")
