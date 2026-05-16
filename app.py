from flask import Flask, render_template, jsonify, send_from_directory
import os
import config
from engine.pipeline import process_news
from modules.storage import load_posts

# Ensure cloud environment has necessary directories
os.makedirs(os.path.join(config.BASE_DIR, 'data'), exist_ok=True)
os.makedirs(os.path.join(config.BASE_DIR, 'output', 'images'), exist_ok=True)
os.makedirs(os.path.join(config.BASE_DIR, 'assets'), exist_ok=True)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_engine():
    try:
        process_news()
        return jsonify({"status": "success", "message": "Engine ran successfully."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/posts')
def get_posts():
    try:
        posts = load_posts()
        return jsonify(posts)
    except Exception as e:
        return jsonify([])

@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory(os.path.join(config.BASE_DIR, 'output', 'images'), filename)

@app.route('/status')
def status():
    return jsonify({
        "status": "online",
        "version": "1.0",
        "environment": "production"
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
