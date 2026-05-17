from google import genai
import os

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

def generate_anime_caption(topic):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"Write a short viral anime Instagram caption about: {topic}"
        )

        return response.text

    except Exception as e:
        return f"AI Error: {str(e)}"
