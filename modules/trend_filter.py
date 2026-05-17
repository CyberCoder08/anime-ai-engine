def analyze_trend(title):
    title_lower = title.lower()

    viral_keywords = [
        "season",
        "trailer",
        "announcement",
        "confirmed",
        "release date",
        "movie",
        "adaptation",
        "returns",
        "cast",
        "visual",
        "opening",
        "ending",
        "anime",
        "new"
    ]

    score = 0

    for keyword in viral_keywords:
        if keyword in title_lower:
            score += 1

    # Relaxed logic:
    # Anything with at least 1 keyword becomes HIGH
    if score >= 1:
        priority = "HIGH"
    else:
        priority = "LOW"

    return score, priority
