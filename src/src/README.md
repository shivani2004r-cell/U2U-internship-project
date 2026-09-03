# 💻 Source Code

This folder contains the Python source code used for data analysis, preprocessing, feature engineering, machine learning, prediction, and the Streamlit web application.

## 📁 Files

| File                     | Purpose                                                                  |
| ------------------------ | ------------------------------------------------------------------------ |
| `check_data.py`          | Checks the dataset structure, columns, data types, and basic information |
| `data_analysis.py`       | Performs exploratory data analysis and generates visualizations          |
| `feature_engineering.py` | Prepares and transforms features for machine learning                    |
| `train_model.py`         | Trains and evaluates the machine learning model                          |
| `predict.py`             | Uses the trained model to predict accident severity                      |
| `app.py`                 | Runs the interactive Streamlit web application                           |

## 🔄 Source Code Workflow

```text
road_accidents.csv
        ↓
check_data.py
        ↓
data_analysis.py
        ↓
feature_engineering.py
        ↓
train_model.py
        ↓
predict.py
        ↓
app.py
```

## 📌 File Descriptions

### 1. `check_data.py`

This script is used to inspect the dataset.

It checks:

* Number of rows and columns
* Column names
* Data types
* Missing values
* Basic statistical information
* Sample records

### 2. `data_analysis.py`

This script performs Exploratory Data Analysis (EDA).

It analyzes factors such as:

* Accident severity
* Weather conditions
* Road conditions
* Vehicle conditions
* Other accident-related features

It also generates graphs and charts for understanding the dataset.

### 3. `feature_engineering.py`

This script prepares the dataset for machine learning.

It performs tasks such as:

* Selecting useful features
* Encoding categorical variables
* Handling missing values
* Transforming data
* Preparing input features and target variable

### 4. `train_model.py`

This script trains and evaluates the machine learning model.

Main steps include:

* Loading processed data
* Splitting data into training and testing sets
* Training the model
* Evaluating model performance
* Comparing model results

### 5. `predict.py`

This script uses the trained machine learning model to predict accident severity for new input data.

### 6. `app.py`

This file contains the Streamlit application.

The application provides an interactive interface where users can enter accident-related information and receive a predicted accident severity.

## ▶️ Running the Source Code

From the project root:

```bash
cd src
```

Then run the required Python file:

```bash
python check_data.py
```

For the Streamlit application:

```bash
streamlit run app.py
```

## 🛠️ Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* Streamlit

