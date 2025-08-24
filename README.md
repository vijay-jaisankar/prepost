# PrePost: Plan before you post.

![Prepost Logo](./static/prepost_logo.png)

Explore tips to shield your post from attackers, and exciting captions for your post! We leverage state-of-the-art models like [GPT-5](https://aimlapi.com/models/gpt-5) to help you **plan before you post**.  

## Main Features
- Checks and flagging for possibly location-revealing clues in an uploaded image intended for Social media uploads
- Suggestions for cool and targeted captions for the corresponding social media posts.

## Set up
- First, populate API keys (and an Ollama server URL for local testing, if required) into `.env.example` and then run `cp .env.example .env`. For more details, please refer to the [AIML API Docs](https://docs.aimlapi.com/quickstart/setting-up?_gl=1*bcp25*_gcl_aw*R0NMLjE3NTYwNDMyMjcuQ2owS0NRanc4S3JGQmhEVUFSSXNBTXZJQXBZTWFLWGNrWWJjeWpaVW0tR3h5NC1QbUZ6STJHVHg0ekVDeWsyd0VfTlR3WFRELUxJQjIzRWFBcnlfRUFMd193Y0I.*_gcl_au*ODM1NzQ1MDE5LjE3NTU1MTAxODU.) and [OpenAI Docs](https://platform.openai.com/docs/guides/latest-model).
- Create a virtual environment and install the dependencies:
    ```bash
    virtualenv venv
    source venv/bin/activate
    pip install -r REQUIREMENTS.txt
    ```


## Launching the app
```bash
cd streamlit_app/
streamlit run app.py
```

---
Submitted to the Co-Creating with GPT-5 hackathon