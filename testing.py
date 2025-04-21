import pandas as pd
import shutil
import os

# Path to your Excel file
# excel_path = r"C:\Users\mvska\Downloads\archive\EuroSAT\test.xlsx"

# Output folder for test images
output_dir = r"C:\Users\mvska\Downloads\mp1\data\test_images"
os.makedirs(output_dir, exist_ok=True)

# Read Excel
csv_path = 'C:\\Users\\mvska\\Downloads\\mp1\\data\\test_cleaned.csv'
df = pd.read_csv(csv_path)


# Adjust based on the actual column name
if 'Filename' in df.columns:
    image_paths = df['Filename']
else:
    image_paths = df.iloc[:, 0]  # fallback to first column

# Source folder where test images currently are (assumed from your Excel info)
source_dir = r"C:\Users\mvska\Downloads\mp1\data\train_images"

# Copy images
for img_name in image_paths:
    src_path = os.path.join(source_dir, img_name)
    dst_path = os.path.join(output_dir, os.path.basename(img_name))

    try:
        shutil.copy(src_path, dst_path)
        print(f"Copied: {img_name}")
    except FileNotFoundError:
        print(f"❌ Not Found: {img_name}")
