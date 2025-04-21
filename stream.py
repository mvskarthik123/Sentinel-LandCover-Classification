import streamlit as st

# 🚨 SET CONFIG FIRST!
st.set_page_config(page_title="Land Cover + Crop Recommender", layout="wide")

# Then import after setting config
from pages import home, know_vegetation, weather_advice

# Define your pages
pages = {
    "🏠 Home": home.app,
    "🌾 Know Your Vegetation": know_vegetation.app,
    "🌦️ Weather Advisory": weather_advice.app,
}

# Sidebar navigation
selected = st.sidebar.radio("Navigation", list(pages.keys()))
pages[selected]()
