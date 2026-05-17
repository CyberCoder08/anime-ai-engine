import time
from google import genai
import os

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

def generate_anime_caption(title, description=""):
    prompt = f"""
Write a short hype anime Instagram caption for this news.

Title:
{title}

Description:
{description}

Make it engaging, modern, short, energetic, and include emojis.
"""
    fallback_caption = "🔥 Big anime update just dropped! Stay tuned for more anime news. #anime #otaku #animenews"

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        error_msg = str(e)
        if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
            return fallback_caption
            
        time.sleep(3)
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )
            return response.text
        except Exception as retry_e:
            return fallback_caption
