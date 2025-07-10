import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the saved Random Forest model
model = joblib.load('./models/random_forest_model.joblib')

# Title
st.title("🚢 Titanic Survival Predictor")

st.markdown("Enter passenger information to predict survival.")

# User Input Form
pclass = st.selectbox("Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)", [1, 2, 3])
sex = st.radio("Sex", ['male', 'female'])
age = st.slider("Age", 0, 80, 25)
sibsp = st.number_input("Number of Siblings/Spouses aboard", 0, 8, 0)
parch = st.number_input("Number of Parents/Children aboard", 0, 6, 0)
fare = st.number_input("Fare Paid", 0.0, 600.0, 32.0)
embarked = st.selectbox("Port of Embarkation", ['S', 'C', 'Q'])

# Feature Engineering
sex_encoded = 0 if sex == 'male' else 1
family_size = sibsp + parch + 1
is_alone = 1 if family_size == 1 else 0
embarked_Q = 1 if embarked == 'Q' else 0
embarked_S = 1 if embarked == 'S' else 0

# Prediction button
if st.button("Predict Survival"):
    input_data = pd.DataFrame([[
        pclass, sex_encoded, age, sibsp, parch, fare,
        embarked_Q, embarked_S, family_size, is_alone
    ]], columns=[
        'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare',
        'embarked_Q', 'embarked_S', 'family_size', 'is_alone'
    ])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("🎉 This passenger would have **SURVIVED**.")
    else:
        st.error("❌ This passenger would have **NOT SURVIVED**.")
