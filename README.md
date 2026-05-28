# Business Sales Intelligence Dashboard with Machine Learning Forecasting

An end-to-end Data Science and Business Intelligence project focused on sales analysis, forecasting, and interactive dashboard development using Python, Scikit-Learn, Pandas, and Streamlit with interactive filtering and KPI analysis.

---

# Project Overview

This project was designed to simulate a realistic business analytics workflow starting from raw sales data and ending with a deployed interactive dashboard.

The system combines:

* Data Cleaning & Preprocessing
* Exploratory Data Analysis (EDA)
* Business KPI Analysis
* Machine Learning Forecasting
* Interactive Dashboard Development
* GitHub Integration & Cloud Deployment

The main objective was not only to predict future sales, but also to transform raw business data into meaningful insights and an interactive decision-support system.

---

# Features

* Interactive business dashboard
* Sales forecasting using Machine Learning
* KPI cards for business monitoring
* Dynamic filtering by category, region, and segment
* Profit and sales analysis
* Trend visualization
* Product performance insights
* Business recommendation system
* Feature importance visualization
* Cloud deployment using Streamlit

---

# Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Streamlit
* Joblib
* Google Colab
* VS Code
* GitHub

---

# Project Pipeline

```text
Data Collection
↓
Data Cleaning
↓
Exploratory Data Analysis
↓
Machine Learning Model Development
↓
Interactive Dashboard Development
↓
Deployment
```

---

# Dataset Information

The dataset used in this project was obtained from Kaggle and contains Superstore business sales data.

Key business-related columns include:

* Sales
* Profit
* Quantity
* Discount
* Category
* Sub-Category
* Region
* Segment
* Ship Mode
* Order Date

An earlier dataset was initially tested but later replaced because it lacked important columns such as `profit` and `quantity`, which limited the business analysis quality and reduced the realism of the forecasting system.

---

# Notebooks & Project Structure

```text
01_data_cleaning.ipynb
02_eda_analysis.ipynb
03_sales_prediction_model.ipynb
04_streamlit_ui_SalesPrediction.py
cleaned_superstore_sales.csv
feature_importance.csv
requirements.txt
README.md
```

### Notebook 01 — Data Cleaning

* Missing value handling
* Date formatting
* Duplicate analysis
* Feature engineering
* Business data preprocessing

### Notebook 02 — Exploratory Data Analysis

* Sales trend analysis
* Profit analysis
* Regional insights
* Category performance
* Discount impact visualization

### Notebook 03 — Machine Learning Model

* Random Forest Regressor
* Feature engineering
* Model evaluation
* Sales forecasting
* Feature importance extraction

### Notebook 04 — Streamlit Dashboard

* Interactive UI
* KPI visualization
* Business filtering
* Prediction simulator
* Dashboard deployment

---

# Machine Learning Model

The project uses a Random Forest Regressor for sales prediction.

Features used include:

* Profit
* Quantity
* Discount
* Category
* Sub-Category
* Region
* Segment
* Ship Mode
* Year
* Month

Evaluation metrics:

* MAE
* RMSE
* R² Score

The machine learning pipeline evolved from a simple time-based forecasting approach into a more advanced business-oriented prediction system using multiple business variables.

---

# Dashboard Features

The Streamlit dashboard includes:

* Executive KPI cards
* Sales & profit trends
* Category and regional analysis
* Top-performing products
* Interactive filters
* Machine learning prediction simulator
* Business recommendations
* Feature importance analysis

---

# Dashboard Preview

(Add dashboard screenshots here)

Example:

```md
![Dashboard Screenshot](screenshots/dashboard.png)
```

---

# Local Development

The dashboard was developed and tested locally using VS Code and Streamlit.

Run locally using:

```bash
streamlit run 04_streamlit_ui_SalesPrediction.py
```

---

# Deployment

The project was deployed using:

* GitHub
* Streamlit Community Cloud

This transformed the project into a publicly accessible interactive business intelligence web application.

Live Dashboard:
(Add Streamlit deployment link here)

---

# Challenges Faced

Some of the main challenges encountered during development included:

* Missing business-related dataset columns
* Handling meaningful duplicate sales records
* Machine learning redesign decisions
* Streamlit installation and environment issues
* Python PATH configuration problems
* GitHub file size limitations
* Model compression and deployment optimization
* Package dependency conflicts
* Streamlit deployment debugging

These challenges contributed significantly to the final system design and technical learning process.

---

# Future Improvements

Potential future improvements include:

* Real-time database integration
* Advanced forecasting models
* Customer segmentation
* Power BI integration
* Cloud database connectivity
* Real-time analytics
* API integration
* Authentication system

---

# Full Technical Report

A detailed technical report explaining:

* project architecture
* data cleaning workflow
* EDA process
* machine learning development
* debugging journey
* deployment process
* business insights

can be viewed here:

(Add Gamma report link here)

---

# Final Outcome

This project successfully demonstrates a complete end-to-end Data Science workflow combining:

* Data preprocessing
* Business analytics
* Machine Learning forecasting
* Interactive dashboard development
* Cloud deployment

The final result is a business-oriented analytics platform capable of transforming raw sales data into interactive insights and predictive business intelligence.

---

# Author

Liyan AlTahrawi

Data Science & Artificial Intelligence Student
