# 🚀 Deployment

This folder contains the files required to install the project dependencies and run the application.

## 📁 Folder Structure

```text
deployment/
│
├── README.md
└── requirements.txt
```

## 📦 requirements.txt

The `requirements.txt` file contains the Python libraries required to run the project.

The main dependencies include:

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* Streamlit

## ⚙️ Installation

First, create a virtual environment from the project root:

```bash
python -m venv venv
```

Activate the virtual environment in Windows PowerShell:

```bash
.\venv\Scripts\Activate.ps1
```

Install the required packages:

```bash
pip install -r deployment/requirements.txt
```

## ▶️ Run the Application

Move to the source code folder:

```bash
cd src
```

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in a web browser.

## 🔄 Deployment Workflow

```text
Clone GitHub Repository
        ↓
Create Virtual Environment
        ↓
Install Dependencies
        ↓
Prepare Dataset
        ↓
Train Model
        ↓
Run Streamlit Application
        ↓
View Predictions
```

## 🛠️ Technologies

* Python
* Streamlit
* Scikit-learn
* Pandas
* NumPy
* Joblib

## 📌 Note

Make sure Python is installed on the system before installing the project dependencies.
