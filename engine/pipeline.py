from modules.fetch_news import get_latest_news
from modules.ai_writer import generate_anime_caption
from modules.storage import is_duplicate, save_post
from modules.poster_generator import create_poster
from modules.trend_filter import analyze_trend

def process_news():
    print("🔥 Anime AI Engine is processing...")
    
    print("\n--- FETCHING NEWS ---")
    news_items = get_latest_news()
    
    if not news_items:
        print("No news found.")
        return
        
    print("\n--- TREND FILTER & PROCESSING ---\n")
    
    for i, item in enumerate(news_items, 1):
        title = item['title']
        link = item['link']
        summary = item['summary']
        
        # 1. Trend Filter
        score, priority = analyze_trend(title)
        if priority != "HIGH":
            print(f"⛔ SKIPPED (Priority: {priority}, Score: {score}): {title}\n")
            continue
            
        # 2. Duplicate Check
        if is_duplicate(title):
            print(f"⛔ Skipping duplicate: {title}\n")
            continue
            
        try:
            print(f"🚀 TREND DETECTED: High priority news (Score: {score})")
            print(f"📰 Processing news: {title}")
            
            # 3. Generate Caption
            caption = generate_anime_caption(title, summary)
            print("🔥 AI VIRAL CAPTION GENERATED")
            print(f"{caption}\n")
            
            # 4. Save to Database
            from modules.storage import load_posts
            total_posts = len(load_posts()) + 1
            
            save_post(title, link, caption)
            print("💾 SAVED TO DATABASE")
            
            # 5. Create Poster
            img_path = create_poster(title, caption, total_posts)
            if img_path:
                print(f"🎨 POSTER CREATED: {img_path}\n")
            else:
                print(f"⚠️ Poster generation failed\n")
            
            print("-" * 50 + "\n")
        except Exception as e:
            print(f"⚠️ Failed to process news {i}: {e}\n")
            print("-" * 50 + "\n")
