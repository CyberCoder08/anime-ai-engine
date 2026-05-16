import json
import os
import config

DATA_DIR = os.path.join(config.BASE_DIR, "data")
DATA_FILE = os.path.join(DATA_DIR, "posts.json")

def _ensure_file_exists():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump([], f)

def load_posts():
    _ensure_file_exists()
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_post(title, link, caption):
    posts = load_posts()
    
    new_post = {
        "title": title,
        "link": link,
        "caption": caption
    }
    
    posts.append(new_post)
    
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=4)

def is_duplicate(title):
    posts = load_posts()
    for post in posts:
        if post.get("title") == title:
            return True
    return False
