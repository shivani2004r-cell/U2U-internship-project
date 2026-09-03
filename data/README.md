# 📊 Data

This folder contains the datasets used for the **Predictive Analytics for Road Accident Prevention** project.

## 📁 Folder Structure

```text
data/
│
├── README.md
│
├── raw/
│   └── road_accidents.csv
│
└── processed/
    └── processed_accidents.csv
```

## 📂 Raw Data

The `raw/` folder contains the original road accident dataset collected from the **Road Traffic Severity Classification** dataset.

### File

* `road_accidents.csv`

The raw dataset is kept unchanged and is used as the input for data cleaning and preprocessing.

## 📂 Processed Data

The `processed/` folder contains the cleaned and processed dataset generated during the data preprocessing stage.

### File

* `processed_accidents.csv`

The processed dataset is used for feature engineering and machine learning model training.

## 🔗 Dataset Source

The dataset was obtained from Kaggle:

**Road Traffic Severity Classification**

https://www.kaggle.com/datasets/avikumart/road-traffic-severity-classification

## 🔄 Data Processing Flow

```text
Raw Dataset
     ↓
Data Cleaning
     ↓
Missing Value Handling
     ↓
Data Transformation
     ↓
Processed Dataset
     ↓
Feature Engineering
     ↓
Machine Learning
```

## ⚠️ Note

The raw dataset should not be modified directly. Any cleaned or transformed version should be saved in the `processed/` folder.
