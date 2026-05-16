import google.generativeai as genai
import config

# Configure Gemini with the API key
genai.configure(api_key=config.GEMINI_API_KEY)

def generate_anime_caption(title, summary):
    print(f"🤖 Generating AI caption for: {title}...")
    
    prompt = f"""
    Rewrite the following anime news into an engaging viral Instagram caption.
    Requirements:
    - Start with a "🚨 BREAKING" or "🔥 JUST IN" style hook
    - Use an emotional, hyped-up anime fandom tone
    - Keep it short, scroll-stopping, and punchy
    - Create high excitement and urgency
    - End with 5-7 strong relevant anime hashtags (including #anime and #animenews).
    
    News Title: {title}
    News Summary: {summary}
    """
    
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Error generating caption: {e}"
