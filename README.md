# 🏡 California Housing Price Prediction

A complete end-to-end Machine Learning project that predicts housing prices across California using the California Housing Dataset.  
This project includes data preprocessing, feature engineering, model training using Random Forest, model serialization with Pickle, and a Streamlit web application for interactive predictions.

---

## 🚀 Features

- 📊 **Exploratory Data Analysis (EDA)**
- 🔧 **Data Cleaning & Preprocessing**
- 🏗️ **Feature Engineering**
- 🌲 **Random Forest Regression Model**
- 💾 **Model Saving with Pickle**
- 🖥️ **Streamlit App for Real-Time Predictions**
- 📈 **80%+ R² Score**

---

## 📁 Project Structure

.
├── app.py # Streamlit web app
├── California.ipynb # Jupyter Notebook (training pipeline)
├── model.pkl # Saved Random Forest model
├── requirements.txt # Project dependencies
└── README.md # Documentation

---

## 🧠 Model Overview

- **Algorithm:** Random Forest Regressor  
- **Reason for Selection:**  
  Robust to outliers, handles non-linear patterns, minimal preprocessing required.
- **Evaluation Metric:** R² Score  
- **Achieved Score:** ~0.80

---

## 🔬 Data Preprocessing & Feature Engineering

### Applied Techniques:
- Handling missing values  
- Log transformation on skewed features  
- One-hot encoding of categorical variables  
- Adding engineered features:
  - `bedroom_ratio = total_bedrooms / total_rooms`
  - `household_rooms = total_rooms / households`

### Encoding:
`ocean_proximity` was transformed using **pandas.get_dummies()** with consistent columns for train & test.

---

## 🧪 How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Atharva-GH/California-House-Prediction.git
cd California-House-Prediction 
```
### 2️⃣ Install the dependencies
```
pip install -r requirements.txt
```
### 3️⃣ Run the Streamlit app
```
streamlit run app.py
```
<img width="1919" height="897" alt="image" src="https://github.com/user-attachments/assets/afa152f2-e861-4cb4-aac0-fd65f97b3a50" />
<img width="1904" height="895" alt="image" src="https://github.com/user-attachments/assets/14e626ed-1b60-4af4-8e2b-0eb65787c338" />


