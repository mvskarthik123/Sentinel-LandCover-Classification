import pandas as pd

test_df = pd.read_csv("C:/Users/mvska/Downloads/mp1/data/test.csv")
print(test_df['ClassName'].unique())