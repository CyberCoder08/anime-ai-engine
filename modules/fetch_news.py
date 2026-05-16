import feedparser

def get_latest_news():
    sources = [
        "https://www.animenewsnetwork.com/news/rss.xml",
        "https://myanimelist.net/rss/news.xml"
    ]
    
    news_list = []
    
    for rss_url in sources:
        print(f"📡 Fetching news from {rss_url}...")
        feed = feedparser.parse(rss_url)
        
        # Get top 2-3 news entries from each source
        for entry in feed.entries[:3]:
            # Clean up the summary (it might have HTML tags, but we'll leave it simple for now)
            summary = entry.get("summary", "No summary available.")
            
            news_item = {
                "title": entry.title,
                "summary": summary,
                "link": entry.link
            }
            news_list.append(news_item)
            
    return news_list
