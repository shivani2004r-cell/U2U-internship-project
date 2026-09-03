import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

DATA_PATH = "../data/raw/road_accidents.csv"
OUTPUT_DIR = "../reports/figures"

os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv(r"C:\Users\ADMIN\U2UInnovate-Project-15\data\raw\RTA Dataset.csv")

print("Dataset Shape:", df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())
target_column = "Accident_severity"

print("\nAccident Severity Distribution:")
print(df[target_column].value_counts())