from gmail_connector import fetch_latest_emails
from llm_agent import process_email
from calendar_sync import add_task_to_calendar
import os
from dotenv import load_dotenv

load_dotenv(override=True)

def main():
    emails = fetch_latest_emails()
    for email_text in emails:
        print("\n📥 New Email:\n", email_text[:200])
        result = process_email(email_text)
        print("📋 Summary:", result['summary'])
        for task in result['tasks']:
            print("📅 Syncing:", task)
            add_task_to_calendar(task['title'], task['due'])

if __name__ == "__main__":
    main()
