import streamlit as st
import requests
st.set_page_config(page_title="Digital-Twin Demo", layout="wide")

st.title("Digital-Twin Recovery Companion — Demo")
st.markdown("""This demo shows a local simulation using the backend's /ml/simulate endpoint.
Make sure the FastAPI app is running at http://127.0.0.1:8000""")

patient_id = st.number_input("Patient ID", min_value=1, value=1)
extra_minutes = st.slider("Extra balance minutes per day (scenario)", min_value=0, max_value=30, value=5)
if st.button("Run Simulation"):
    payload = {"patient_id": patient_id, "scenario": {"extra_minutes_balance": extra_minutes}}
    try:
        res = requests.post("http://127.0.0.1:8000/ml/simulate", json=payload, timeout=5)
        st.json(res.json())
    except Exception as e:
        st.error("Failed to call API: " + str(e))
