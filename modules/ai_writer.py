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
    fallback_caption = "🔥 Big anime update just dropped! Fans are already discussing this everywhere. Stay tuned for more anime news. #anime #otaku #animenews"

    try:
        time.sleep(10)
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        error_msg = str(e)
        if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
            print(f"Rate limit exceeded (429). Waiting 15 seconds to retry...")
            time.sleep(15)
            try:
                time.sleep(10)
                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=prompt
                )
                return response.text
            except Exception as retry_e:
                return fallback_caption
        
        return fallback_caption
