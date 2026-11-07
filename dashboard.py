import streamlit as st
import pandas as pd
import os
import joblib

st.set_page_config(
    page_title="GasSense AI",
    page_icon="🏭",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: #101D2B;
    color: #F1F5F9;
}
[data-testid="stHeader"] {
    background: transparent;
}
.block-container {
    padding-top: 2rem;
    max-width: 1250px;
}
h1, h2, h3, p, label {
    color: #F1F5F9 !important;
}
[data-testid="stMetric"] {
    background: #203447;
    border: 1px solid #35485B;
    padding: 20px;
    border-radius: 14px;
}
[data-testid="stMetricLabel"] {
    color: #B9C9D7 !important;
}
[data-testid="stMetricValue"] {
    color: #56C9C0 !important;
}
div.stButton > button {
    background: #56C9C0;
    color: #101D2B;
    border: none;
    border-radius: 9px;
    font-weight: bold;
}
hr {
    border-color: #35485B;
}
</style>
""", unsafe_allow_html=True)

# Header
st.title("🏭 GasSense AI")
st.markdown("### SMART FACTORY GAS SAFETY MONITORING")

st.markdown("""
**Developed by**

Basmala Ahmed & Dai Khalid Ahmed

📧 Basmala.2324510@stemqena.moe.edu.eg

📧 dai.2324534@stemqena.moe.edu.eg

Grade 12 | Group 23319 | 2026/2027
---
""")

# Sidebar
with st.sidebar:
    st.title("🏭 GasSense AI")
    st.markdown("**Navigation**")
    st.markdown("📊 System Overview")
    st.markdown("🧠 AI Analysis")
    st.markdown("📈 Sensor Trends")
    st.divider()
    st.caption("Smart Industrial Safety System")

# Refresh
if st.button("🔄 Refresh Readings"):
    st.rerun()

st.header("System Overview")

FILE_NAME = "gas_data.csv"
features = ["gas_level", "temperature", "humidity"]

data = pd.DataFrame()

if os.path.exists(FILE_NAME) and os.path.getsize(FILE_NAME) > 0:
    try:
        data = pd.read_csv(FILE_NAME)
    except pd.errors.EmptyDataError:
        data = pd.DataFrame()

if data.empty:
    col1, col2, col3 = st.columns(3)
    col1.metric("Gas Level", "--")
    col2.metric("Temperature", "--")
    col3.metric("Humidity", "--")

    st.info("⏳ Waiting for real sensor readings...")

else:
    if all(col in data.columns for col in features):
        latest = data.iloc[-1]

        col1, col2, col3 = st.columns(3)
        col1.metric("Gas Level", latest["gas_level"])
        col2.metric("Temperature", latest["temperature"])
        col3.metric("Humidity", latest["humidity"])

        st.divider()
        st.header("AI Analysis")

        model_file = "best_gassense_model.pkl"

        if not os.path.exists(model_file):
            model_file = "gassense_model.pkl"

        if os.path.exists(model_file):
            try:
                model = joblib.load(model_file)
                reading = pd.DataFrame(
                    [[latest[col] for col in features]],
                    columns=features
                )
                prediction = model.predict(reading)[0]
                st.success(f"AI Predicted Status: {prediction}")
            except Exception:
                st.warning("Unable to generate AI prediction.")
        else:
            st.warning("AI model is not trained yet.")

        st.divider()
        st.header("Sensor Data Trends")
        st.line_chart(data[features].tail(20))

        st.header("Recent Readings")
        st.dataframe(data.tail(10), use_container_width=True)

    else:
        st.error("Dataset columns are incomplete.")

# Footer
st.divider()
st.markdown("""
<div style="text-align:center; padding:20px;">
    <h3 style="color:#56C9C0;">GasSense AI</h3>
    <p>Developed by Basmala Ahmed & Dai Khalid Ahmed</p>
    <p style="color:#AABBCB;">Grade 12 | Group 23319 | 2026/2027</p>
</div>
""", unsafe_allow_html=True)
