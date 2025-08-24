"""Utility functions to use the OpenAI API"""

import os

# Load env variables
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(dotenv_path="../.env")


class OpenAIClient:
    """Base class to represent an OpenAI API Client"""

    def __init__(self):
        """Initialise instance variables"""
        self.api_key = os.environ.get("OPENAI_API_KEY")
        self.model_name = os.environ.get("OPENAI_MODEL_NAME")
        self.openai_client = OpenAI(api_key=self.api_key)

    def get_model_response(self, text_prompt, base64_image=None, max_tokens=256):
        """Get model response for a text prompt and (optionally) an image"""
        # Process text prompt
        content = [{"type": "input_text", "text": text_prompt}]

        # Process input image if supplied by the user
        if base64_image is not None:
            content.append(
                {
                    "type": "input_image",
                    "image_url": f"data:image/jpeg;base64,{base64_image}",
                }
            )

        # Send request
        response = self.openai_client.responses.create(
            model=self.model_name,
            input=[
                {
                    "role": "user",
                    "content": content,
                }
            ],
            max_output_tokens=max_tokens,
        )

        # Extract model response
        model_response = response.output_text
        return model_response
