"""Streamlit app to host the functionalities of PrePost."""

import os
# Set system path
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import base64

import streamlit as st
from openai import RateLimitError

from api.aimlapi_utils import AIMLAPIClient
from api.ollamaapi_utils import OllamaClient
from api.openai_utils import OpenAIClient
from prompts.caption_prompt import (IMAGE_CAPTIONS_RAW_PROMPT,
                                    IMAGE_TOPIC_DESCRIPTOR_PROMPT)
from prompts.location_prompt import (BASE_LOCATION_PROMPT,
                                     FEW_SHOT_LOCATION_PROMPT)

# Set up Clients
aiml_api_client = AIMLAPIClient()
ollama_api_client = OllamaClient()
openai_api_client = OpenAIClient()

# Background image
st.image("../static/prepost_logo.png")
st.markdown(
    "# PrePost: Explore tips to shield your post from attackers, and exciting captions for your post!"
)

uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Get base64 encoded image
    file_bytes = uploaded_file.read()
    base64_encoded = base64.b64encode(file_bytes).decode("utf-8")
    st.image(file_bytes, caption="Uploaded Image", use_container_width=True)

    # Step 1: Get location information
    try:
        location_information = openai_api_client.get_model_response(
            text_prompt=FEW_SHOT_LOCATION_PROMPT, base64_image=base64_encoded
        )
        print(location_information)
    except RateLimitError as e:
        print(f"Rate limit exceeded: {e}")

    location_information = dict(
        eval(
            ollama_api_client.get_model_response(
                text_prompt=FEW_SHOT_LOCATION_PROMPT, base64_image=base64_encoded
            )
        )
    )

    if "location_cues" in location_information:
        st.markdown("## Location cues identified in the image")
        for clue in location_information["location_cues"]:
            st.markdown(f"- {clue}")

    if "tips_to_hide_or_mask_location" in location_information:
        st.markdown("## Suggestions before posting")
        for tip in location_information["tips_to_hide_or_mask_location"]:
            st.markdown(f"- {tip}")

    # Step 2: Get topic information
    topic_information = ollama_api_client.get_model_response(
        text_prompt=IMAGE_TOPIC_DESCRIPTOR_PROMPT, base64_image=base64_encoded
    )

    # Step 3: Get captions
    captions_prompt_annotated = f"{IMAGE_CAPTIONS_RAW_PROMPT}: {topic_information}"
    try:
        captions_information = aiml_api_client.get_model_response(
            text_prompt=captions_prompt_annotated
        )
    except Exception as e:
        print(f"Rate limit exceeded: {e}")
        captions_information = ollama_api_client.get_model_response(
            text_prompt=captions_prompt_annotated
        )

    st.markdown("## Sample captions for your post!")
    st.text(dict(captions_information)["choices"][0]["message"]["content"])
