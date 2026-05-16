def analyze_trend(title):
    title_lower = title.lower()
    
    # High-impact keywords
    viral_keywords = [
        "season", "trailer", "announcement", "confirmed", 
        "release date", "movie", "adaptation", "returns",
        "cast", "visual", "opening", "ending"
    ]
    
    score = 0
    for keyword in viral_keywords:
        if keyword in title_lower:
            score += 1
            
    # Priority logic
    if score >= 2:
        priority = "HIGH"
    elif score == 1:
        priority = "MEDIUM"
    else:
        priority = "LOW"
        
    return score, priority
