import os
import pandas as pd

# ---------------------------------------
# 1. File paths
# ---------------------------------------

INPUT_PATH = "../data/raw/RTA Dataset.csv"
OUTPUT_DIR = "../data/processed"
OUTPUT_PATH = "../data/processed/processed_accidents.csv"

# Create processed folder if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ---------------------------------------
# 2. Load dataset
# ---------------------------------------

print("Loading dataset...")

df = pd.read_csv(INPUT_PATH)

print("Dataset loaded successfully!")

print("\nOriginal dataset shape:")
print(df.shape)


# ---------------------------------------
# 3. Remove unnecessary spaces
# ---------------------------------------

df.columns = df.columns.str.strip()

print("\nColumn names:")
print(df.columns.tolist())


# ---------------------------------------
# 4. Remove duplicate rows
# ---------------------------------------

duplicate_count = df.duplicated().sum()

print("\nDuplicate rows:", duplicate_count)

df = df.drop_duplicates()

print("Shape after removing duplicates:")
print(df.shape)


# ---------------------------------------
# 5. Check missing values
# ---------------------------------------

print("\nMissing values before cleaning:")

print(df.isnull().sum())


# ---------------------------------------
# 6. Replace '?' with missing value
# ---------------------------------------

df = df.replace("?", pd.NA)


# ---------------------------------------
# 7. Handle categorical missing values
# ---------------------------------------

categorical_columns = df.select_dtypes(
    include=["object"]
).columns

for column in categorical_columns:

    if df[column].isnull().sum() > 0:

        mode_value = df[column].mode()

        if len(mode_value) > 0:

            df[column] = df[column].fillna(
                mode_value[0]
            )


# ---------------------------------------
# 8. Handle numerical missing values
# ---------------------------------------

numerical_columns = df.select_dtypes(
    include=["int64", "float64"]
).columns

for column in numerical_columns:

    if df[column].isnull().sum() > 0:

        df[column] = df[column].fillna(
            df[column].median()
        )


# ---------------------------------------
# 9. Convert Date column
# ---------------------------------------

if "Time" in df.columns:

    df["Time"] = pd.to_datetime(
        df["Time"],
        format="%H:%M:%S",
        errors="coerce"
    )

    df["Hour"] = df["Time"].dt.hour


# ---------------------------------------
# 10. Create time-based features
# ---------------------------------------

if "Hour" in df.columns:

    def get_time_period(hour):

        if pd.isna(hour):
            return "Unknown"

        if hour < 6:
            return "Night"

        elif hour < 12:
            return "Morning"

        elif hour < 18:
            return "Afternoon"

        else:
            return "Evening"

    df["Time_Period"] = df["Hour"].apply(
        get_time_period
    )


# ---------------------------------------
# 11. Convert Day_of_week
# ---------------------------------------

if "Day_of_week" in df.columns:

    df["Is_Weekend"] = df["Day_of_week"].isin(
        ["Saturday", "Sunday"]
    ).astype(int)


# ---------------------------------------
# 12. Convert numeric columns
# ---------------------------------------

numeric_columns_to_convert = [
    "Number_of_vehicles_involved",
    "Number_of_casualties"
]

for column in numeric_columns_to_convert:

    if column in df.columns:

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

        df[column] = df[column].fillna(
            df[column].median()
        )


# ---------------------------------------
# 13. Check Accident Severity
# ---------------------------------------

if "Accident_severity" in df.columns:

    print("\nAccident Severity Distribution:")

    print(
        df["Accident_severity"].value_counts()
    )


# ---------------------------------------
# 14. Final missing value check
# ---------------------------------------

print("\nMissing values after cleaning:")

print(df.isnull().sum())


# ---------------------------------------
# 15. Save processed dataset
# ---------------------------------------

df.to_csv(
    OUTPUT_PATH,
    index=False
)

print("\nProcessed dataset saved successfully!")

print("File location:")

print(OUTPUT_PATH)

print("\nFinal dataset shape:")

print(df.shape)