import pandas as pd

# Load test set
test_path = "C:/Users/mvska/Downloads/mp1/data/test.csv"
test_df = pd.read_csv(test_path)

# Fix label casing
test_df['ClassName'] = test_df['ClassName'].str.strip().str.title()

# Confirm fix


# Save cleaned version (overwrite or new file)
test_df.to_csv("C:/Users/mvska/Downloads/mp1/data/test_cleaned.csv", index=False)
print("classes done")