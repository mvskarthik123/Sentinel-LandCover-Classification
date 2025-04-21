import torch
from torchvision import transforms
from PIL import Image
from model.dispatcher import MODEL_DISPATCHER

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'

# Load model using the dispatcher (same as in train.py)
model = MODEL_DISPATCHER['resnet50'](pretrained=False)  # pretrained=False since we only need architecture
model.load_state_dict(torch.load("model/checkpoints/checkpoint.pt", map_location=DEVICE))
model.to(DEVICE)
model.eval()

# Define class names
class_names = sorted([
    'AnnualCrop', 'Forest', 'HerbaceousVegetation', 'Highway', 'Industrial',
    'Pasture', 'PermanentCrop', 'Residential', 'River', 'SeaLake'
])

# Transformation (same as valid_transforms)
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

# Sample image path
img_path = r"C:\Users\mvska\Downloads\mp1\data\train_images\Forest\Forest_470.jpg"

# Replace with your actual test image path
img = Image.open(img_path).convert('RGB')
img = img.resize((224, 224))  # Resizing manually before ToTensor (as in train transforms)
img = transform(img).unsqueeze(0).to(DEVICE)

# Predict
with torch.no_grad():
    output = model(img)
    _, predicted = torch.max(output, 1)

print(f"Predicted Class: {class_names[predicted.item()]}")
