from google import genai
import config

client = genai.Client(api_key=config.GEMINI_API_KEY)

def generate_anime_caption(title, summary):
    print(f"Generating AI caption for: {title}")

    prompt = f"""
Rewrite this anime news into a viral Instagram caption.

Rules:
- exciting anime fandom tone
- Gen-Z style
- emotional hype
- include emojis
- include hashtags

Title:
{title}

Summary:
{summary}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"AI Error: {e}"
