# app.py
import streamlit as st
import numpy as np
import joblib
import pandas as pd

st.set_page_config(page_title="House Price Predictor", layout="centered")
st.title("🏠 House Price Prediction App")

# Load trained model
model = joblib.load('./models/ridge_model_selected_features.joblib')

# Define input fields
st.header("Enter House Details")

def user_input():
    numeric_inputs = {}
    numeric_features = [
        'OverallQual', 'GrLivArea', 'GarageCars', 'GarageArea',
        'TotalBsmtSF', '1stFlrSF', 'FullBath', 'TotRmsAbvGrd',
        'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'Fireplaces',
        'BsmtFinSF1', 'LotArea', 'WoodDeckSF', 'OpenPorchSF',
        'HalfBath', '2ndFlrSF', 'ScreenPorch', 'PoolArea'
    ]

    for feature in numeric_features:
        numeric_inputs[feature] = st.number_input(f"{feature}", min_value=0, value=1000, step=10, key=feature)

    # Categorical features
    neighborhood = st.selectbox("Neighborhood", ['NAmes', 'CollgCr', 'OldTown', 'Edwards', 'Somerst'], key='Neighborhood')
    exter_qual = st.selectbox("ExterQual", ['TA', 'Gd', 'Ex', 'Fa'], key='ExterQual')
    kitchen_qual = st.selectbox("KitchenQual", ['TA', 'Gd', 'Ex', 'Fa'], key='KitchenQual')

    # Combine into one dict
    all_inputs = numeric_inputs
    all_inputs['Neighborhood'] = neighborhood
    all_inputs['ExterQual'] = exter_qual
    all_inputs['KitchenQual'] = kitchen_qual

    return pd.DataFrame([all_inputs])

input_df = user_input()

if st.button("Predict Price", key="predict_button"):
    try:
        log_price = model.predict(input_df)[0]
        predicted_price = np.expm1(log_price)  # inverse of log1p
        st.success(f"💰 Predicted House Price: ${predicted_price:,.2f}")
    except Exception as e:
        st.error(f"Error: {e}")
