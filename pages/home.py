import streamlit as st
from PIL import Image
import torch
import torchvision.transforms as transforms
from model.dispatcher import MODEL_DISPATCHER
import json

# Map model output index to class name
idx_to_class = [
    "AnnualCrop",
    "Forest",
    "HerbaceousVegetation",
    "Pasture",
    "PermanentCrop",
    "Residential",
    "River",
    "SeaLake"
]

# Load crop info JSON
with open("data/info.json", "r") as f:
    crop_info = json.load(f)

# Preprocessing pipeline
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

@st.cache_resource
def load_model():
    model = MODEL_DISPATCHER['resnet50'](pretrained=False)
    model.load_state_dict(torch.load('model/checkpoints/checkpoint.pt', map_location=torch.device('cpu')))
    model.eval()
    return model

def predict_image(image, model):
    image_tensor = transform(image).unsqueeze(0)
    with torch.no_grad():
        output = model(image_tensor)
        pred = torch.argmax(output, dim=1).item()
    return pred

# --- MAIN APP LOGIC ---
def app():
    st.title("🌍 Land Cover Classifier + Crop Suggestion")
    st.write("Upload a satellite image to classify land type and receive intelligent vegetation advice.")

    file = st.file_uploader("Choose a satellite image...", type=["jpg", "jpeg", "png"])

    if file:
        image = Image.open(file).convert("RGB")
        st.image(image, caption="Uploaded Image", use_container_width=True)

        model = load_model()
        pred_idx = predict_image(image, model)

        if 0 <= pred_idx < len(idx_to_class):
            pred_class = idx_to_class[pred_idx]
            st.success(f"🌱 Predicted Land Type: **{pred_class}**")

            if pred_class in crop_info:
                data = crop_info[pred_class]
                st.info(f"🌾 Recommendation: {data['recommendation']}")

                with st.expander("📅 Crop Calendar & Climate Needs"):
                    for crop in data['calendar']:
                        st.markdown(f"**{crop}**")
                        st.markdown(f"🗓️ {data['calendar'][crop]}")
                        st.markdown(f"🌡️ {data['climate'][crop]}")
                        st.markdown("---")

                report = f"""--- Crop Report ---
Predicted Land Type: {pred_class}
Recommendation: {data['recommendation']}

Crop Calendar:
{chr(10).join([f"{c}: {data['calendar'][c]}" for c in data['calendar']])}

Climate Info:
{chr(10).join([f"{c}: {data['climate'][c]}" for c in data['climate']])}
"""
                st.download_button("📥 Download Crop Plan", report, file_name="crop_plan.txt")
            else:
                st.error(f"No data available for predicted class: {pred_class}")
        else:
            st.error("❌ Invalid prediction index. Please check model outputs.")
