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
### Developed by

**Basmala Ahmed**  
📧 Basmala.2324510@stemqena.moe.edu.eg

**Dai Khaled Ahmed**  
📧 dai.2324534@stemqena.moe.edu.eg

Grade 12 | Group 23319 | 2026/2027
""")
if st.button("Refresh Readings"):
    st.rerun()

FILE_NAME = "gas_data.csv"

if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
    st.info("Waiting for real sensor readings...")

else:
    data = pd.read_csv(FILE_NAME)

    if data.empty:
        st.info("Waiting for real sensor readings...")

    else:
        features = ["gas_level", "temperature", "humidity"]

        if not all(col in data.columns for col in features):
            st.error("Dataset columns are incomplete.")

        else:
            latest = data.iloc[-1]

            col1, col2, col3 = st.columns(3)

            col1.metric("Gas Level", latest["gas_level"])
            col2.metric("Temperature", latest["temperature"])
            col3.metric("Humidity", latest["humidity"])

            st.subheader("AI Prediction")

            model_file = "best_gassense_model.pkl"

            if not os.path.exists(model_file):
                model_file = "gassense_model.pkl"

            if os.path.exists(model_file):
                model = joblib.load(model_file)

                reading = pd.DataFrame(
                    [[latest[col] for col in features]],
                    columns=features
                )

                prediction = model.predict(reading)[0]

                st.write("Predicted Status:", prediction)

            else:
                st.warning(
                    "AI model is not trained yet. "
                    "Waiting for real labeled data."
                )

    