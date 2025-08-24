"""Utility functions to use the AIML API"""

import os

import requests
# Load env variables
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")


class AIMLAPIClient:
    """Base class to represent an AIML API Client"""

    def __init__(self):
        """Initialise instance variables"""
        self.api_key = os.environ.get("AIML_API_KEY")
        self.model_name = os.environ.get("AIML_MODEL_NAME")
        self.api_url = "https://api.aimlapi.com/v1/chat/completions"

    def get_model_response(self, text_prompt, max_tokens=256):
        """Get model response for a text prompt"""
        # Construct request headers
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }

        # Process text prompt
        content = [{"type": "text", "text": text_prompt}]

        # Construct request payload
        payload = {
            "model": self.model_name,
            "messages": [
                {
                    "role": "user",
                    "content": content,
                    "max_tokens": max_tokens,
                }
            ],
        }

        # Send request
        response = requests.post(url=self.api_url, headers=headers, json=payload)

        # Extract model response
        api_response = response.json()
        model_response = api_response["message"]["content"]

        return model_response
