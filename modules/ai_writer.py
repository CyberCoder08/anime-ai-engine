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
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"AI Error: {str(e)}"
