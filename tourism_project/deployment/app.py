
import streamlit as st
import pandas as pd
import joblib

# Load trained model
from huggingface_hub import hf_hub_download

model_path = hf_hub_download(
    repo_id="saiadityalingam3/wellness-tourism-model",
    filename="wellness_tourism_model.joblib"
)

model = joblib.load(model_path)

st.title("Wellness Tourism Package Prediction")

st.write("Enter the customer details below to predict whether the customer is likely to purchase the Wellness Tourism Package.")

# -------------------------------
# User Inputs
# -------------------------------

Age = st.number_input("Age", min_value=18, max_value=100, value=35)

TypeofContact = st.selectbox("Type of Contact", [0,1])

CityTier = st.selectbox("City Tier", [1,2,3])

DurationOfPitch = st.number_input("Duration Of Pitch", value=15.0)

Occupation = st.selectbox("Occupation", [0,1,2,3])

Gender = st.selectbox("Gender", [0,1,2])

NumberOfPersonVisiting = st.number_input("Number Of Person Visiting", value=2)

NumberOfFollowups = st.number_input("Number Of Followups", value=3)

ProductPitched = st.selectbox("Product Pitched",[0,1,2,3,4])

PreferredPropertyStar = st.number_input("Preferred Property Star",value=3)

MaritalStatus = st.selectbox("Marital Status",[0,1,2])

NumberOfTrips = st.number_input("Number Of Trips",value=3)

Passport = st.selectbox("Passport",[0,1])

PitchSatisfactionScore = st.slider("Pitch Satisfaction Score",1,5)

OwnCar = st.selectbox("Own Car",[0,1])

NumberOfChildrenVisiting = st.number_input("Number Of Children Visiting",value=0)

Designation = st.selectbox("Designation",[0,1,2,3,4])

MonthlyIncome = st.number_input("Monthly Income",value=30000.0)

# -------------------------------
# Prediction
# -------------------------------

if st.button("Predict"):

    input_df = pd.DataFrame([[
        Age,
        TypeofContact,
        CityTier,
        DurationOfPitch,
        Occupation,
        Gender,
        NumberOfPersonVisiting,
        NumberOfFollowups,
        ProductPitched,
        PreferredPropertyStar,
        MaritalStatus,
        NumberOfTrips,
        Passport,
        PitchSatisfactionScore,
        OwnCar,
        NumberOfChildrenVisiting,
        Designation,
        MonthlyIncome
    ]], columns=[
        'Age',
        'TypeofContact',
        'CityTier',
        'DurationOfPitch',
        'Occupation',
        'Gender',
        'NumberOfPersonVisiting',
        'NumberOfFollowups',
        'ProductPitched',
        'PreferredPropertyStar',
        'MaritalStatus',
        'NumberOfTrips',
        'Passport',
        'PitchSatisfactionScore',
        'OwnCar',
        'NumberOfChildrenVisiting',
        'Designation',
        'MonthlyIncome'
    ])

    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.success("The customer is likely to purchase the Wellness Tourism Package.")
    else:
        st.error("The customer is unlikely to purchase the Wellness Tourism Package.")
