# import os
# import pandas as pd
# from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
# import matplotlib.pyplot as plt

# # Paths
# TRAIN_DIR = r"C:\Users\mvska\Downloads\mp1\data\train_images"
# PRED_PATH = "predictionsfinal.csv"

# # 1. Build Ground Truth Table from train_images
# gt_data = []
# for class_name in os.listdir(TRAIN_DIR):
#     class_folder = os.path.join(TRAIN_DIR, class_name)
#     if os.path.isdir(class_folder):
#         for fname in os.listdir(class_folder):
#             if fname.endswith(".jpg"):
#                 gt_data.append((fname, class_name))

# ground_truth_df = pd.DataFrame(gt_data, columns=["image_id", "true_class"])

# # 2. Load Predictions
# pred_df = pd.read_csv(PRED_PATH)
# pred_df["image_id"] = pred_df["image_id"].apply(lambda x: os.path.basename(x))  # strip path

# # 3. Merge and Compare
# merged = pd.merge(pred_df, ground_truth_df, on="image_id", how="inner")

# # 4. Evaluation Metrics
# y_true = merged["true_class"]
# y_pred = merged["class"]

# print("📊 Classification Report:")
# print(classification_report(y_true, y_pred))

# # 5. Confusion Matrix
# cm = confusion_matrix(y_true, y_pred, labels=sorted(y_true.unique()))
# disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=sorted(y_true.unique()))
# disp.plot(xticks_rotation=45, cmap='viridis')
# plt.title("Confusion Matrix")
# plt.tight_layout()
# plt.show()
import os
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import seaborn as sns

# Paths
TRAIN_DIR = r"C:\Users\mvska\Downloads\mp1\data\train_images"
PRED_PATH = "predictionsfinal.csv"

# 1. Build Ground Truth Table from train_images
gt_data = []
for class_name in os.listdir(TRAIN_DIR):
    class_folder = os.path.join(TRAIN_DIR, class_name)
    if os.path.isdir(class_folder):
        for fname in os.listdir(class_folder):
            if fname.endswith(".jpg"):
                gt_data.append((fname, class_name))

ground_truth_df = pd.DataFrame(gt_data, columns=["image_id", "true_class"])

# 🧠 Class distribution check
train_labels = [label for _, label in gt_data]
plt.figure(figsize=(10, 6))
sns.countplot(y=train_labels, order=pd.Series(train_labels).value_counts().index)
plt.title("Training Data Class Distribution")
plt.xlabel("Count")
plt.ylabel("Class")
plt.tight_layout()
plt.show()

# 2. Load Predictions
pred_df = pd.read_csv(PRED_PATH)
pred_df["image_id"] = pred_df["image_id"].apply(lambda x: os.path.basename(x))  # strip path

# 3. Merge and Compare
merged = pd.merge(pred_df, ground_truth_df, on="image_id", how="inner")

# 4. Evaluation Metrics
y_true = merged["true_class"]
y_pred = merged["class"]

print("📊 Classification Report:")
print(classification_report(y_true, y_pred))

# 5. Confusion Matrix
cm = confusion_matrix(y_true, y_pred, labels=sorted(y_true.unique()))
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=sorted(y_true.unique()))
disp.plot(xticks_rotation=45, cmap='viridis')
plt.title("Confusion Matrix")
plt.tight_layout()
plt.show()


