"""Configurable prompts for the image captioning pipeline"""

# Descriptor prompt
descriptor_prompt = """I am going to post this image to Social media. What main topics or objects are covered in this image? Be brief and suggest 3 to 5 concepts or topics that can then be used to generate captions. Make sure to output ONLY 3 to 5 words for topics. Don't share your reasoning. Ensure to adhere to a 5 word limit. Output your answer with commas for example 'Car, BMW, Fast car, Germany, Logo'"""

# Captioning base prompt
captioning_base_prompt = """Create 3 sample captions for a Social media post. The prompts should be exciting and lively and should perform well for likes and comments. Be as creative as you like. The image is about the following points, read it carefully and ensure the captions you generate feature only these input points and stick to the topics. Here are the points:"""

# Prompts to be exported
IMAGE_TOPIC_DESCRIPTOR_PROMPT = descriptor_prompt
IMAGE_CAPTIONS_RAW_PROMPT = captioning_base_prompt
