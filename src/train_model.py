import pandas as pd
import joblib
import os
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ---------------------------------------
# 1. Paths
# ---------------------------------------

DATA_PATH = r"C:\Users\ADMIN\U2UInnovate-Project-15\data\processed\processed_accidents.csv"
MODEL_DIR = "../models"

os.makedirs(MODEL_DIR, exist_ok=True)


# ---------------------------------------
# 2. Load processed dataset
# ---------------------------------------

print("Loading processed dataset...")

df = pd.read_csv(DATA_PATH)

print("Dataset loaded successfully!")
print("Dataset shape:", df.shape)


# ---------------------------------------
# 3. Target variable
# ---------------------------------------

TARGET = "Accident_severity"

features = [
    "Weather_conditions",
    "Road_surface_conditions",
    "Light_conditions",
    "Type_of_vehicle",
    "Number_of_vehicles_involved",
    "Number_of_casualties"
]

X = df[features]
y = df[TARGET]


# ---------------------------------------
# 4. Identify column types
# ---------------------------------------

categorical_features = X.select_dtypes(
    include=["object"]
).columns.tolist()

numerical_features = X.select_dtypes(
    include=["int64", "float64"]
).columns.tolist()

print("\nCategorical features:")
print(categorical_features)

print("\nNumerical features:")
print(numerical_features)


# ---------------------------------------
# 5. Preprocessing
# ---------------------------------------

categorical_transformer = Pipeline(
    steps=[
        (
            "imputer",
            SimpleImputer(
                strategy="most_frequent"
            )
        ),
        (
            "encoder",
            OneHotEncoder(
                handle_unknown="ignore"
            )
        )
    ]
)

numerical_transformer = Pipeline(
    steps=[
        (
            "imputer",
            SimpleImputer(
                strategy="median"
            )
        )
    ]
)


preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            categorical_transformer,
            categorical_features
        ),
        (
            "numerical",
            numerical_transformer,
            numerical_features
        )
    ]
)


# ---------------------------------------
# 6. Train-test split
# ---------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining records:", len(X_train))
print("Testing records:", len(X_test))


# ---------------------------------------
# 7. Create Random Forest model
# ---------------------------------------

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)


# ---------------------------------------
# 8. Create complete pipeline
# ---------------------------------------

pipeline = Pipeline(
    steps=[
        (
            "preprocessor",
            preprocessor
        ),
        (
            "model",
            model
        )
    ]
)


# ---------------------------------------
# 9. Train model
# ---------------------------------------

print("\nTraining model...")

pipeline.fit(
    X_train,
    y_train
)

print("Model training completed!")

print("\nMaking predictions...")

predictions = pipeline.predict(X_test)

print("Predictions completed!")

accuracy = accuracy_score(
    y_test,
    predictions
)

print("\nModel Accuracy:")
print(accuracy)

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        predictions
    )
)

print("\nConfusion Matrix:")

cm = confusion_matrix(
    y_test,
    predictions
)

print(cm)

plt.figure(figsize=(8, 6))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    xticklabels=pipeline.classes_,
    yticklabels=pipeline.classes_
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")

plt.tight_layout()

plt.savefig(
    "../reports/figures/confusion_matrix.png"
)

plt.show()

joblib.dump(
    pipeline,
    "../models/accident_model.pkl"
)

print("\nModel saved successfully!")

print(
    "Model location: ../models/accident_model.pkl"
)
# ---------------------------------------
# 10. Make predictions
# ---------------------------------------

predictions = pipeline.predict(
    X_test
)


# ---------------------------------------
# 11. Evaluate model
# ---------------------------------------

accuracy = accuracy_score(
    y_test,
    predictions
)

print("\nModel Accuracy:")
print(accuracy)

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        predictions
    )
)


# ---------------------------------------
# 12. Confusion Matrix
# ---------------------------------------

print("\nConfusion Matrix:")

print(
    confusion_matrix(
        y_test,
        predictions
    )
)


# ---------------------------------------
# 13. Save trained model
# ---------------------------------------

MODEL_PATH = "../models/accident_model.pkl"

joblib.dump(
    pipeline,
    MODEL_PATH
)

print("\nModel saved successfully!")

print(
    "Model location:",
    MODEL_PATH
)