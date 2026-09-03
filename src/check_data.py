import pandas as pd

df = pd.read_csv(r"C:\Users\ADMIN\U2UInnovate-Project-15\data\raw\RTA Dataset.csv")

print("First 5 rows:")
print(df.head())

print("\nColumns:")
print(df.columns.tolist())

print("\nDataset Information:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())
