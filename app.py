import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV files
df = pd.read_csv("trend_phase_summary.csv")  # Trend phase summary
raw_data = pd.read_csv("tiktok_trend_tracker_sample.csv")  # Original data

# Ensure Category column exists
if "Category" not in raw_data.columns:
    raw_data["Category"] = "Uncategorized"

# Branding Banner / Header
st.markdown("""
    <div style='background-color:#000000;padding:10px 20px;border-radius:10px'>
        <h2 style='color:white;text-align:center;'>✨ Welcome to TikTok Trend Assistant ✨</h2>
        <p style='color:white;text-align:center;'>Minimal tools. Maximum results.</p>
    </div>
""", unsafe_allow_html=True)

st.write("Choose what you need: hashtag generator, hook generator, or TikTok Shop insights.")

# Simulated login section
with st.sidebar:
    st.header("👤 TikTok Login")
    username = st.text_input("TikTok Username:")
    password = st.text_input("Password:", type="password")
    logged_in = username and password
    if logged_in:
        st.success(f"Welcome, @{username}!")
    else:
        st.warning("Please enter your TikTok username and password to access features.")

# Feature selection
feature = st.radio("What would you like to generate?", ["Hashtag Generator", "Hook Generator", "TikTok Shop Insights"])

if feature == "TikTok Shop Insights":
    st.info("This feature is coming soon.")

elif logged_in:
    # TikTok categories
    tiktok_categories = [
        "Dance", "Comedy / Skits", "Music / Singing / Covers", "Beauty / Makeup / Skincare",
        "Fashion / Outfits / Styling", "Fitness / Health / Gym", "Food / Recipes / Cooking",
        "Lifestyle / Vlogs / Routines", "DIY / Crafts", "Education / How-To / Tips",
        "Tech / AI / Gadgets", "Business / Finance / Side Hustles", "Motivation / Self-Improvement",
        "Pets / Animals", "Travel / Adventure", "Parenting / Family", "Gaming / Stream Highlights",
        "Books / Reading / Writing", "Cleaning / Organizing / Hacks", "Storytime / Personal Experience"
    ]

    category_choice = st.selectbox("Choose a TikTok category:", options=tiktok_categories)
    custom_category = st.text_input("Or enter a custom category:")
    selected_category = custom_category if custom_category else category_choice
    category_data = raw_data[raw_data['Category'].str.contains(selected_category, case=False, na=False)]

    if feature == "Hashtag Generator":
        st.subheader("📈 Trending Hashtags")
        trending_hashtags = category_data["Hashtag"].unique()
        st.write(trending_hashtags if len(trending_hashtags) else "No hashtags found for this category.")

    elif feature == "Hook Generator":
        st.subheader("🎯 Content Suggestions")
        st.markdown(f"**Category Selected:** {selected_category}")
        st.markdown("**Suggested Hook:** \"What happens when you try this for 3 days straight?\" 🧠")
        st.markdown("**Script Starter:** \"I didn't think this would work... but then it went viral. Here's what I did:\" ✨")

    st.subheader("\U0001F4CA Trend Phase Summary")
    st.dataframe(df[df['Hashtag'].isin(category_data['Hashtag'].unique())])

st.caption("Built with Streamlit · Created by Darius Rowser")

 
