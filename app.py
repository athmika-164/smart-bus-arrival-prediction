import streamlit as st
import pandas as pd

st.title("🚌 Smart Bus Arrival Prediction System")

data = pd.read_csv("bus_data.csv")

bus = st.selectbox("Select Bus", data["Bus Name"].unique())

result = data[data["Bus Name"] == bus].iloc[0]

st.write("### Bus Details")
st.write("Bus Name:", result["Bus Name"])
st.write("Starting Point:", result["Starting Point"])
st.write("Destination:", result["Destination"])
st.write("Start Time:", result["Start Time"])
st.write("Estimated Arrival:", result["Estimated Arrival"])

if result["Status"] == "Available":
    st.success("Bus is coming")
else:
    st.warning("Bus is not currently available")