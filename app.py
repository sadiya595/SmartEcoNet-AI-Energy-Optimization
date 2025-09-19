import streamlit as st
import joblib
import numpy as np


# Load model
model = joblib.load('final_energy_model.pkl')


st.title('AI/ML Appliance Usage Predictor & Energy Optimization')


# Exact features in correct order
all_feature_names = [
    'lights', 'T1', 'RH_1', 'T2', 'RH_2', 'T3', 'RH_3', 'T4', 
    'RH_4', 'T5', 'RH_5', 'T6', 'RH_6', 'T7', 'RH_7', 'T8', 
    'RH_8', 'T9', 'RH_9', 'T_out', 'Press_mm_hg', 'RH_out', 
    'Windspeed', 'Visibility', 'Tdewpoint', 'rv1', 'rv2', 
    'hour', 'dayofweek'
]


# Top features to ask user for input (based on your feature importance)
top_features = ['hour', 'T3', 'RH_3', 'lights', 'Press_mm_hg', 'RH_out', 'Windspeed']


# Default values for the features (median/mean from dataset)
default_values = {
    'lights': 0, 'T1': 21.5, 'RH_1': 40.0, 'T2': 21.0, 'RH_2': 40.0, 'T3': 21.0, 'RH_3': 40.0,
    'T4': 21.0, 'RH_4': 40.0, 'T5': 21.0, 'RH_5': 40.0, 'T6': 21.0, 'RH_6': 40.0, 'T7': 21.0,
    'RH_7': 40.0, 'T8': 21.0, 'RH_8': 40.0, 'T9': 21.0, 'RH_9': 40.0, 'T_out': 21.0,
    'Press_mm_hg': 750.0, 'RH_out': 50.0, 'Windspeed': 4.0, 'Visibility': 45.0, 'Tdewpoint': 10.0,
    'rv1': 13.0, 'rv2': 13.0, 'hour': 12.0, 'dayofweek': 3
}


# Descriptions for tooltips
feature_descriptions = {
    "hour": "Current hour of the day (0-23), affects energy usage patterns",
    "T3": "Temperature reading from sensor 3 inside the house (°C)",
    "RH_3": "Relative humidity % from sensor 3 inside the house",
    "lights": "Current energy usage or state of lights in the home",
    "Press_mm_hg": "Atmospheric pressure outside in millimeters of mercury",
    "RH_out": "Outdoor relative humidity %",
    "Windspeed": "Outdoor wind speed (affects heating/cooling demand)"
}

st.subheader("Enter values for key features influencing energy usage:")


# Collect user inputs only for top features with tooltips
user_inputs = {}
for f in top_features:
    user_inputs[f] = st.number_input(
        label=f"Input {f}",
        value=float(default_values[f]),
        help=feature_descriptions.get(f, "")
    )


# Build full input list in correct order for prediction
model_input = []
for f in all_feature_names:
    if f in user_inputs:
        model_input.append(user_inputs[f])
    else:
        model_input.append(default_values[f])


if st.button('Predict'):
    input_array = np.array(model_input).reshape(1, -1)
    prediction = model.predict(input_array)[0]

    st.success(f'Predicted Appliance Energy Usage: {prediction:.2f} Wh')

    # Energy optimization advice
    if prediction > 120:
        st.warning("High predicted energy usage! Consider reducing appliance use during peak hours and optimizing indoor conditions.")
    elif prediction < 70:
        st.info("Energy usage is efficient. Good sustainable practices!")
    else:
        st.info("Moderate energy usage. There is some room for optimization.")

    # Simple visualization of expected usage trend by hour
    hours = list(range(24))
    usage_trend = [prediction * (0.5 + 0.5 * np.sin((h / 24) * 2 * np.pi)) for h in hours]
    st.line_chart(data=usage_trend, height=250, width=700)
