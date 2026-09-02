# U2U-internship-project
# 🚗 Predictive Analytics for Road Accident Prevention

## 📌 Project Overview

**Predictive Analytics for Road Accident Prevention** is a Machine Learning project that analyzes historical road accident data to identify accident patterns and predict accident severity.

The system uses factors such as **weather conditions, road surface conditions, light conditions, vehicle type, number of vehicles involved, and number of casualties** to predict the possible severity of an accident.

## 🔗 Project Links

- **GitHub Repository:** [U2U-internship-project]((https://github.com/shivani2004r-cell/U2U-internship-project))
- **Source Code:** [View Source Code](YOUR_GITHUB_URL/tree/main/src)
- **Dataset:** [View Dataset](https://www.kaggle.com/datasets/avikumart/road-traffic-severity-classification?utm_source=chatgpt.com)

## 🎯 Objectives

The main objectives of this project are:

* 📊 Analyze historical road accident data.
* 🧹 Clean and preprocess the accident dataset.
* 🔧 Perform feature engineering to create useful predictive features.
* 🤖 Develop Machine Learning models for accident severity prediction.
* 📈 Evaluate and compare different Machine Learning models.
* 🚨 Predict accident severity based on given conditions.
* 🌐 Develop an interactive Streamlit application for prediction.

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Data Analysis

* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn

### Machine Learning

* Scikit-learn
* Random Forest
* Decision Tree
* Logistic Regression

### Model Management

* Joblib

### Web Application

* Streamlit

### Development Tools

* Visual Studio Code
* Git
* GitHub

---

## 📂 Project Structure

```text
U2U-internship-project/
│
├── README.md
│
├── data/
│   ├── README.md
│   ├── raw/
│   │   └── road_accidents.csv
│   │
│   └── processed/
│       └── processed_accidents.csv
│
├── src/
│   ├── README.md
│   ├── check_data.py
│   ├── data_analysis.py
│   ├── feature_engineering.py
│   ├── train_model.py
│   ├── predict.py
│   └── app.py
│
├── models/
│   └── accident_model.pkl
│
├── reports/
│   ├── README.md
│   ├── figures/
│   │   ├── accident_severity_distribution.png
│   │   ├── weather_vs_severity.png
│   │   └── confusion_matrix.png
│   │
│   └── final_report.pdf
│
├── deployment/
│   ├── README.md
│   └── requirements.txt
│
└── .gitignore
```

---

## 🔄 Project Workflow

```text
Historical Accident Data
          │
          ▼
    Data Collection
          │
          ▼
     Data Cleaning
          │
          ▼
 Exploratory Data Analysis
          │
          ▼
  Feature Engineering
          │
          ▼
 Data Preprocessing
          │
          ▼
 Machine Learning Models
          │
          ▼
   Model Evaluation
          │
          ▼
Severity Prediction
          │
          ▼
 Streamlit Web Application
```

---

# 📊 1. Data Collection

Historical road accident data is collected and stored in:

```text
data/raw/road_accidents.csv
```

The dataset contains information related to road accidents, including environmental, road, vehicle, and accident-related factors.

Important features may include:

* Weather conditions
* Road surface conditions
* Light conditions
* Type of vehicle
* Number of vehicles involved
* Number of casualties
* Accident severity

> **Note:** The exact columns depend on the dataset being used.

---

# 🧹 2. Data Cleaning

The collected dataset is cleaned before Machine Learning.

The cleaning process includes:

* Removing duplicate records.
* Identifying missing values.
* Handling missing categorical values.
* Handling missing numerical values.
* Checking data types.
* Removing unnecessary columns.
* Preparing the dataset for analysis and modeling.

The cleaned dataset is stored in:

```text
data/processed/processed_accidents.csv
```

---

# 📈 3. Exploratory Data Analysis

Exploratory Data Analysis (EDA) is performed to understand accident patterns and relationships between different factors.

The analysis focuses on:

### Accident Severity

The distribution of different accident severity levels is analyzed.

### Weather Conditions

The relationship between weather conditions and accident severity is studied.

### Road Conditions

Different road surface conditions are analyzed to identify their relationship with accident severity.

### Light Conditions

Daylight and night-time accident patterns are compared.

### Vehicle Information

Vehicle types and their relationship with accident severity are analyzed.

### Accident Characteristics

The number of vehicles involved and casualties are also studied.

Generated graphs are stored in:


reports/figures/

# 🔧 4. Feature Engineering

Feature engineering is used to transform raw data into useful features for Machine Learning.

Examples include:

* Extracting year from date.
* Extracting month from date.
* Extracting day of the week.
* Extracting accident hour.
* Creating weekend indicators.
* Encoding categorical variables.
* Selecting relevant predictive features.

These features help the Machine Learning model identify patterns in accident severity.

---

# 🤖 5. Machine Learning

The project uses classification algorithms to predict accident severity.

The following models can be evaluated:

### 1. Logistic Regression

A baseline classification algorithm used to establish an initial performance level.

### 2. Decision Tree

A tree-based model that makes predictions using a series of decision rules.

### 3. Random Forest

An ensemble Machine Learning algorithm that combines multiple decision trees to improve prediction performance.

The best-performing model is selected based on evaluation results.

---

# 📊 6. Model Evaluation

The trained models are evaluated using classification metrics such as:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

Example result format:

| Model               |      Accuracy |
| ------------------- | ------------: |
| Logistic Regression | Actual Result |
| Decision Tree       | Actual Result |
| Random Forest       | Actual Result |

> **Note:** The actual values should be added after training the models. Results should not be manually estimated.

---

# 🚨 7. Accident Severity Prediction

After training, the selected Machine Learning model can predict accident severity based on input conditions.

### Example Input

```text
Weather: Rainy
Road Condition: Wet
Light Condition: Night
Vehicle Type: Motorcycle
Vehicles Involved: 2
Casualties: 1
```

### Example Output


Predicted Accident Severity: High


The prediction depends on the trained model and the actual dataset.



# 🌐 8. Streamlit Web Application

The project includes an interactive web application built using **Streamlit**.

The application allows users to enter accident-related conditions and receive a predicted accident severity.

### Application Features

* Weather condition selection.
* Road condition selection.
* Light condition selection.
* Vehicle type selection.
* Number of vehicles input.
* Number of casualties input.
* Accident severity prediction.

---

# ▶️ 9. How to Run the Project

## Step 1: Clone the Repository

```bash
git clone <[(https://github.com/shivani2004r-cell/U2U-internship-project)]>
```

Move into the project directory:

```bash
cd U2U-internship-project
```

---

## Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

### Windows PowerShell

```bash
.\venv\Scripts\Activate.ps1
```

If activation is successful, the terminal will show:

```text
(venv)
```

---

## Step 3: Install Dependencies

```bash
pip install -r deployment/requirements.txt
```

---

## Step 4: Check the Dataset

Go to the source folder:

```bash
cd src
```

Run:

```bash
python check_data.py
```

This checks:

* Dataset columns
* Dataset size
* Data types
* Missing values
* Sample records

---

## Step 5: Perform Data Analysis

Run:

```bash
python data_analysis.py
```

This performs exploratory data analysis and generates graphs.

---

## Step 6: Perform Feature Engineering

Run:

```bash
python feature_engineering.py
```

The processed dataset will be generated in:

```text
data/processed/processed_accidents.csv
```

---

## Step 7: Train the Machine Learning Model

Run:

```bash
python train_model.py
```

The trained model will be saved in:

```text
models/accident_model.pkl
```

---

## Step 8: Test Prediction

Run:

```bash
python predict.py
```

The program will display the predicted accident severity.

---

## Step 9: Run Streamlit Application

From the `src` folder:

```bash
streamlit run app.py
```

The Streamlit application will open in your browser.

---

# 📁 Dataset

The project uses a historical road accident dataset for analysis and Machine Learning.

The dataset should be placed at:

```text
data/raw/road_accidents.csv
```

The target variable is:

```text
Accident_severity
```

The dataset may contain multiple accident severity classes depending on the source dataset.

---

# 📌 Expected Output

The project produces:

### Data Analysis

```text
Accident severity distribution
Weather vs accident severity
Road condition vs accident severity
Light condition vs accident severity
```

### Machine Learning

```text
Model accuracy
Precision
Recall
F1-score
Confusion matrix
```

### Prediction

```text
Predicted Accident Severity
```

### Web Application

```text
Interactive Streamlit prediction interface
```

---

# 💡 Key Benefits

* Helps identify accident severity patterns.
* Uses historical data for predictive analysis.
* Identifies important accident-related factors.
* Supports data-driven accident analysis.
* Provides an interactive prediction interface.
* Demonstrates practical application of Machine Learning.

---

# 🔮 Future Enhancements

The project can be improved by adding:

* 📍 Accident hotspot detection.
* 🗺️ Geographic accident visualization.
* 🌦️ Real-time weather data.
* 🚦 Real-time traffic information.
* 📱 Mobile application.
* 🔔 Real-time risk alerts.
* ☁️ Cloud deployment.
* 📊 Interactive dashboards.
* 🛰️ GPS-based accident risk prediction.
* 🤖 More advanced Machine Learning models.

---

# ⚠️ Limitations

* Prediction quality depends on the quality and coverage of the historical dataset.
* Historical patterns may not represent every current road situation.
* The model does not guarantee that an accident will occur.
* Predictions should be treated as analytical estimates.
* Real-time traffic, weather, and geographic information may not be included in the initial version.

---

# 👩‍💻 Project Information

**Project:** U2U Internship Project

**Title:** Predictive Analytics for Road Accident Prevention

**Domain:** Data Science & Machine Learning

**Programming Language:** Python

**Framework:** Streamlit

**Repository:** GitHub

---

# 📜 Conclusion

The **Predictive Analytics for Road Accident Prevention** project demonstrates how historical road accident data can be combined with Data Science and Machine Learning to analyze accident patterns and predict accident severity.

By combining **data analysis, feature engineering, Machine Learning, visualization, and an interactive Streamlit application**, the project provides a practical demonstration of predictive analytics for road accident severity classification.

---

## ⭐ Project Workflow Summary

```text
Collect Data
     ↓
Clean Data
     ↓
Analyze Data
     ↓
Engineer Features
     ↓
Train ML Models
     ↓
Evaluate Models
     ↓
Select Best Model
     ↓
Predict Accident Severity
     ↓
Streamlit Application
```

---

## 🙏 Acknowledgement

This project was developed as part of the **U2U Internship Project** to demonstrate practical skills in Data Science, Machine Learning, and predictive analytics.
