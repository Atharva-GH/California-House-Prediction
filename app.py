import streamlit as st
import numpy as np
import pickle

# -------------------------------
# Load your trained model
# -------------------------------
model = pickle.load(open("random_forest_model.pkl", "rb"))

# -------------------------------
# Average values of all features
# (Replace these with real means)
# -------------------------------
avg_values = {
    "longitude": -119.57,
    "latitude": 35.63,
    "housing_median_age": 28.6,
    "total_rooms": 2622.0,
    "total_bedrooms": 535.0,
    "population": 1425.0,
    "households": 499.0,
    "median_income": 3.87,
    "bedroom_ratio": 0.21,
    "household_rooms": 5.2
}

ocean_categories = ['<1H OCEAN', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN']


# -------------------------------
# Streamlit UI
# -------------------------------
st.title("California Housing Price Predictor")

st.write("Modify the values below or keep the **default average values**.")


# Numerical inputs with default averages
inputs = {}
for feature, avg in avg_values.items():
    inputs[feature] = st.number_input(
        feature.replace("_", " ").title(),
        value=float(avg)
    )

# Ocean proximity dropdown
ocean_input = st.selectbox("Ocean Proximity", ocean_categories)

# One-hot encoding manual mapping (model expects these)
for cat in ocean_categories:
    inputs[cat] = 1 if cat == ocean_input else 0


# Convert to array
values = np.array(list(inputs.values())).reshape(1, -1)


# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict Price"):
    prediction = model.predict(values)[0]
    st.success(f"Predicted House Price: **${prediction:,.2f}**")
