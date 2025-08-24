"""Streamlit app to host the functionalities of PrePost."""

import os
# Set system path
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import base64

import streamlit as st

from api.aimlapi_utils import AIMLAPIClient
from api.ollamaapi_utils import OllamaClient
from api.openai_utils import OpenAIClient
from prompts.caption_prompt import (IMAGE_CAPTIONS_RAW_PROMPT,
                                    IMAGE_TOPIC_DESCRIPTOR_PROMPT)
from prompts.location_prompt import (BASE_LOCATION_PROMPT,
                                     FEW_SHOT_LOCATION_PROMPT)

st.title("Image Uploader and Viewer")
st.text_area(BASE_LOCATION_PROMPT)
st.text_area(FEW_SHOT_LOCATION_PROMPT)
st.text_area(IMAGE_TOPIC_DESCRIPTOR_PROMPT)
st.text_area(IMAGE_CAPTIONS_RAW_PROMPT)

uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Get base64 encoded image
    file_bytes = uploaded_file.read()
    base64_encoded = base64.b64encode(file_bytes).decode("utf-8")
    st.text_area("Base64 Encoded Image", base64_encoded, height=200)
    st.image(file_bytes, caption="Uploaded Image", use_column_width=True)
