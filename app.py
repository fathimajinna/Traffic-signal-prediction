import streamlit as st
import joblib
model = joblib.load("traffic_model.pkl")
encoders = joblib.load("label_encoders.pkl")
st.set_page_config(page_title="Smart Traffic Predictor", page_icon="🚦")
st.title("🚦 Smart Traffic Signal Predictor")
st.subheader("Let ML reduce traffic jams ✨")
hour = st.slider("⏰ Hour of Day (24hr)", 0, 23, 8)
date = st.slider("📆 Date of the Month", 1, 31, 15)
day = st.selectbox("📅 Day of the Week", encoders['day'].classes_)
cars = st.number_input("🚗 Number of Cars", 0)
bikes = st.number_input("🏍️ Number of Bikes", 0)
buses = st.number_input("🚌 Number of Buses", 0)
trucks = st.number_input("🚚 Number of Trucks", 0)

if st.button("🔮 Predict Traffic"):
    day_encoded = encoders['day'].transform([day])[0]
    features = [[hour, date, day_encoded, cars, bikes, buses, trucks]]
    pred = model.predict(features)
    traffic_status = encoders['situation'].inverse_transform(pred)[0]

    
    green_time = {
        'Low': 20,
        'Moderate': 40,
        'High': 60
    }.get(traffic_status, 45)

    st.success(f"🟢 Predicted Traffic: **{traffic_status}**")
    st.info(f"⏱️ Suggested Green Signal Duration: **{green_time} seconds**")

