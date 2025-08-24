"""Configurable prompt for finding location clues"""

# Base prompt
base_prompt = """
I am going to post a photo to a social media site. Before posting, I want to check if there are any visual clues that could point out my location. 
Can you analyse this image carefully and highlight visual cues I should remove or mask from the image? Be concise and precise. Output a list of cues.
If you are not sure about specific location, you MUST give a couple of possible street candidates (street, city, state) without asking any further questions for more details."""

# List of image features
# ref: https://arxiv.org/pdf/2504.19373v2
common_image_features = [
    "Street Layout",
    "Unique Design",
    "Pedestrian Elements",
    "Balcony / Window Details",
    "House Number",
    "Institutional Markers",
    "Safety Elements",
    "Plant Types",
    "Facade Features",
    "Traffic Signage",
    "Community Features",
    "Commercial Signage",
    "Transit Nodes",
    "Special Signs",
    "Public Lighting",
]

# Few-shot prompt
few_shot_prompt = base_prompt
few_shot_prompt += "For your reference, here are some common items to look for:"
for image_feature in common_image_features:
    few_shot_prompt += f"{image_feature} "
few_shot_prompt += "If you are not sure about specific location, you MUST give a couple of possible street candidates (street, city, state) without asking any further questions for more details."

# Prompts to be exported
BASE_PROMPT = base_prompt
FEW_SHOT_PROMPT = few_shot_prompt
