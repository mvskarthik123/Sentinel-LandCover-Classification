import streamlit as st
import json

with open("crop_data.json", "r") as f:
    crop_info = json.load(f)

def app():
    st.title("🌾 Know Your Vegetation")
    st.write("Learn about land types, what crops work well, and how to plan based on land cover.")

    for land_type, data in crop_info.items():
        with st.expander(f"🌍 {land_type}"):
            st.markdown(f"**🌱 Suitable for:** {data['recommendation']}")
            st.markdown("**📅 Crop Calendar:**")
            for crop, timing in data["calendar"].items():
                st.markdown(f"- {crop}: {timing}")
            st.markdown("**🌡️ Climate Info:**")
            for crop, climate in data["climate"].items():
                st.markdown(f"- {crop}: {climate}")
