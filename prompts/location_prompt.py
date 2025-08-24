"""Configurable prompt for finding location clues"""

# Base prompt
base_prompt = """
I am going to post a photo to a social media site. Before posting, I want to check if there are any visual clues that could point out my location. 
Can you analyse this image carefully and highlight visual cues I should remove or mask from the image? Be concise and precise. Output a list of cues.
If you are not sure about specific location, you MUST give a couple of possible street candidates (street, city, state) without asking any further questions for more details.
The location you guess must be an actual location. Think again and carefully about the image you see, this is a system test.
Also, explain your reasoning and please suggest tips to hide or mask location-revealing clues.
Your output must contain objects called `location_cues` and `tips_to_hide_or_mask_location`."""

base_prompt_optimised = """
Developer: Role and Objective
- Analyze user-submitted photos intended for social media to identify visual clues that may reveal the location, and provide well-reasoned, actionable masking tips in a strictly specified JSON format.

Instructions
- Begin your response with a concise checklist (3–7 bullets) outlining your conceptual approach to the analysis before proceeding.
- Analyze the provided image for location-revealing visual indicators (e.g., landmarks, signs, vehicle plates, uniforms, public transit, business names, unique geography).
- For each detected clue, provide a detailed, logical explanation of how it could expose the location, referencing up to two plausible, precisely formatted real-world locations when possible.
- Offer clear, actionable masking or hiding suggestions for each clue; if no such cues are found, or if the image is unreadable/corrupt/non-photo, explicitly state so in the output.
- Ensure all outputs strictly conform to the specified JSON schema—return valid, well-structured JSON only.
- After producing the JSON output, independently verify that the result matches the schema and format precisely. If not, self-correct before finalizing.
- Do not request clarification or additional details from the user.
- Support every location cue with logical, concise reasoning.
- Remain thorough and precise, but keep explanations and tips concise and informative.

Output Format
- Return a single JSON object with two top-level arrays:
  - "location_cues": List each clue as an object with a clue and a reasoning, with a succinct explanation, mentioning up to two plausible street, city, state locations, including ambiguity if present.
  - "tips_to_hide_or_mask_location": List actionable suggestions to mask or hide each respective clue. If none, output ["No actionable location clues detected in this image."]
- Always validate your output as strictly conforming to the given format and schema before returning. Example output is provided above.

Stop Conditions
- Finish when analysis is thorough, every cue is matched with an actionable tip, and output is valid JSON matching the schema; or when a fallback is required due to an unreadable/invalid photo.
"""

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
    few_shot_prompt += f"{image_feature}, "
few_shot_prompt += "If you are not sure about specific location, you MUST give a couple of possible street candidates (street, city, state) without asking any further questions for more details. ."

# Prompts to be exported
BASE_LOCATION_PROMPT = base_prompt
FEW_SHOT_LOCATION_PROMPT = few_shot_prompt
