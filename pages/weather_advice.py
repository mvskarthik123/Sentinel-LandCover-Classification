import streamlit as st
import random

# Mock weather data for various regions
region_weather_data = {
    "Punjab": {"temperature": 24.5, "rainfall": 80, "humidity": 60},
    "Tamil Nadu": {"temperature": 34.2, "rainfall": 120, "humidity": 70},
    "Rajasthan": {"temperature": 38.0, "rainfall": 40, "humidity": 25},
    "Kerala": {"temperature": 28.3, "rainfall": 220, "humidity": 85},
    "Maharashtra": {"temperature": 30.0, "rainfall": 150, "humidity": 55},
    "Uttar Pradesh": {"temperature": 26.7, "rainfall": 100, "humidity": 65},
    "West Bengal": {"temperature": 31.1, "rainfall": 170, "humidity": 78},
}

# Crop suggestions based on temperature and rainfall
def suggest_crops(temp, rainfall):
    if temp > 35 and rainfall < 50:
        return ["Sorghum", "Millets", "Pigeon Pea"]
    elif 25 <= temp <= 35 and 100 <= rainfall <= 200:
        return ["Rice", "Sugarcane", "Jute"]
    elif temp < 25 and rainfall < 100:
        return ["Wheat", "Barley", "Chickpea"]
    else:
        return ["Maize", "Cotton", "Groundnut"]

# Main app
def app():
    st.title("🌦️ Weather-based Crop Advisory")

    st.write("Select your region to view weather and crop recommendations:")

    region = st.selectbox("Choose your region", list(region_weather_data.keys()))

    if region:
        weather = region_weather_data[region]
        st.subheader(f"📍 Weather in {region}")

        st.write(f"**Temperature:** {weather['temperature']} °C")
        st.write(f"**Rainfall:** {weather['rainfall']} mm")
        st.write(f"**Humidity:** {weather['humidity']} %")

        crops = suggest_crops(weather['temperature'], weather['rainfall'])

        st.success("🌱 Recommended Crops:")
        for crop in crops:
            st.markdown(f"- {crop}")
