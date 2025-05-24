import streamlit as st
import requests
from PIL import Image
import io

st.set_page_config(page_title="Fake Currency Detector", layout="centered")
st.title("🧾 Fake Currency Detector")
st.markdown("Upload an image of Indian currency to check if it's **real or fake**.")

uploaded_file = st.file_uploader("📷 Upload Currency Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("🔍 Predict"):
        with st.spinner("Analyzing..."):
            files = {"file": uploaded_file.getvalue()}
            try:
                # Replace this with your actual deployed API endpoint
                response = requests.post("http://localhost:8000/predict", files=files)
                result = response.json()

                prediction = result.get("prediction", "Unknown")
                confidence = result.get("confidence", 0)

                st.success(f"Prediction: **{prediction}** ({confidence * 100:.1f}% confidence)")
            except Exception as e:
                st.error("Failed to get a prediction.")
                st.exception(e)
