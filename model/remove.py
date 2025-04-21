import pandas as pd

# Load original test CSV
df = pd.read_csv('data/test_cleaned.csv')

# Filter out rows with unwanted classes
df = df[~df['ClassName'].isin(['Highway', 'Industrial'])]

# Save the cleaned version
df.to_csv('data/test_cleaned_8class.csv', index=False)
