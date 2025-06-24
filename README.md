🚦 Smart Traffic Signal Optimization using Machine Learning
A real-time intelligent system to predict and optimize green signal duration using traffic data, powered by ML models trained on real vehicle flow counts.
Built with 💻 Python, 🧠 scikit-learn, and ⚡ Streamlit.

📌 Problem Statement
Urban traffic congestion is a major challenge in modern cities. Traditional traffic lights operate on fixed timers, which leads to:

Longer wait times ⏱️

Fuel wastage ⛽

Traffic pile-ups 🚗🚛🚌

Goal:
Design an ML-based system that can learn from past traffic patterns and dynamically predict the optimal green signal duration, improving traffic flow efficiency in real-time.

💡 Features
⏰ Input time, day, vehicle counts (cars, bikes, buses, trucks)

🧠 Predicts traffic congestion level (low/moderate/high)

⏱️ Suggests green light duration using trained ML model

⚙️ Built with RandomForestRegressor to model smart signal timing

📊 Simple UI built with Streamlit

🎯 Optional real-time CCTV or satellite-based upgrades

📁 Folder Structure
bash
Copy
Edit
SmartTrafficProject/
├── Traffic.csv                # Input dataset
├── train_model.ipynb          # Notebook to preprocess + train model
├── traffic_model.pkl          # Saved trained model
├── label_encoders.pkl         # Encoded label mappings (Day)
├── app.py                     # Streamlit app for live predictions
├── requirements.txt           # All dependencies
└── README.md                  # This file
🧪 Dataset Info
Columns: Time, Date, Day, CarCount, BikeCount, BusCount, TruckCount, Traffic Situation

Added Column: GreenTime – ML label representing optimal green duration (20s–60s)

Format: .csv, preprocessed with pandas

✅ Dataset adapted from real-world Kaggle vehicle flow data
✅ Option to integrate with satellite/CCTV data using OpenCV + YOLO

🧠 Model Overview
Type: Regression

Algorithm: RandomForestRegressor

Features:

Hour of day

Date

Day of week (encoded)

Vehicle counts (cars, bikes, buses, trucks)

Label: Predicted GreenTime (in seconds)

