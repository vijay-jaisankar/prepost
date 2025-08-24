"""Streamlit app to host the functionalities of PrePost."""

import os
# Set system path
import sys

import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from api.aimlapi_utils import AIMLAPIClient
from api.ollamaapi_utils import OllamaClient
from api.openai_utils import OpenAIClient

st.title("Image Uploader and Viewer")

uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    st.write("Image successfully uploaded and displayed!")
else:
    st.write("Please upload an image file.")
