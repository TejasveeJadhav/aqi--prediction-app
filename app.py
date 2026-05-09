import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("Model/catboost_aqi.pkl")

# App Title
st.title("Real-Time Air Quality Index Prediction System")

st.write("Enter pollutant values to predict AQI")

# User Inputs
pm25 = st.number_input("PM2.5")
pm10 = st.number_input("PM10")
no2 = st.number_input("NO2")
so2 = st.number_input("SO2")
co = st.number_input("CO")
o3 = st.number_input("O3")
nh3 = st.number_input("NH3")

# Prediction Button
if st.button("Predict AQI"):

    input_data = np.array([[pm25, pm10, no2, so2, co, o3, nh3]])

    prediction = model.predict(input_data)

    aqi = prediction[0]

    st.success(f"Predicted AQI: {aqi:.2f}")

    # AQI Category
    if aqi <= 50:
        st.info("Air Quality: Good")

    elif aqi <= 100:
        st.info("Air Quality: Satisfactory")

    elif aqi <= 200:
        st.warning("Air Quality: Moderate")

    elif aqi <= 300:
        st.warning("Air Quality: Poor")

    elif aqi <= 400:
        st.error("Air Quality: Very Poor")

    else:
        st.error("Air Quality: Severe")
        
