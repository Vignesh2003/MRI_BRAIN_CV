import streamlit as st
import requests
from PIL import Image

st.title("Brain MRI Metastasis Segmentation")

uploaded_file = st.file_uploader("Choose a brain MRI image...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded MRI Image", use_column_width=True)
    
    # Send the image to the backend API for segmentation
    with open(uploaded_file.name, "rb") as file:
        response = requests.post("http://127.0.0.1:8000/predict/", files={"file": file})
        result = response.json()

    st.write("Metastasis Segmentation Result:", result['result'])
