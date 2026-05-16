import time
import schedule
from engine.pipeline import process_news

def run_job():
    print("\n" + "="*50)
    print("🚀 Running Anime AI Engine Scheduled Job")
    print("="*50)
    process_news()

def start_scheduler():
    # Run once immediately
    run_job()
    
    # Then schedule every hour
    schedule.every(1).hours.do(run_job)
    
    print("\n⏰ Scheduler started. Waiting for next run... (Press Ctrl+C to stop)")
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    start_scheduler()
