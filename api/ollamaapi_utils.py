"""Utility functions to use the Ollama API"""

import os

import requests
# Load env variables
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")


class OllamaClient:
    """Base class to represent an Ollama API Client"""

    def __init__(self):
        """Initialise instance variables"""
        base_api_url = os.environ.get("OLLAMA_BASE_API_URL")
        # Remove trailing /
        if base_api_url[-1] == "/":
            base_api_url = base_api_url[:-1]
        self.api_url = f"{base_api_url}/api/generate"
        self.model_name = os.environ.get("OLLAMA_MODEL_NAME")

        # Pull model
        pull_response = requests.post(
            url=f"{base_api_url}/api/pull",
            json={"model": self.model_name, "stream": False},
        )
        print(f"Model pull status: {pull_response.text}")

    def get_model_response(self, text_prompt, base64_image=None):
        """Get model response for a text prompt and (optionally) an image input"""
        # Process text prompt
        payload = {
            "model": self.model_name,
            "prompt": text_prompt,
            "format": "json",
            "stream": False,
        }
        # Process input image if supplied by the user
        if base64_image is not None:
            payload["images"] = [str(base64_image)]

        # Send request
        response = requests.post(url=self.api_url, json=payload)

        # Extract model response
        api_response = response.json()

        return api_response["response"]
