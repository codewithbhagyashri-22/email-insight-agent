from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import datetime
import os
from dateutil import parser 

def get_calendar_service():
    
    creds = Credentials(
        None,
        refresh_token=os.getenv("GMAIL_REFRESH_TOKEN"),
        token_uri="https://oauth2.googleapis.com/token",
        client_id=os.getenv("GMAIL_CLIENT_ID"),
        client_secret=os.getenv("GMAIL_CLIENT_SECRET")
    )
    
    return build('calendar', 'v3', credentials=creds)

def add_task_to_calendar(title, due_time_str):
    service = get_calendar_service()

    try:
        due = parser.parse(due_time_str, fuzzy=True)
        start = due.isoformat()
        end = (due + datetime.timedelta(minutes=30)).isoformat()
    except Exception as e:
        print("⛔ Failed to parse date:", e)
        start = end = datetime.datetime.utcnow().isoformat() + "Z"

    event = {
        'summary': title,
        'start': {'dateTime': start, 'timeZone': 'Asia/Kolkata'},
        'end': {'dateTime': end, 'timeZone': 'Asia/Kolkata'}
    }

    print("✅ Event to be created:", event)
    service.events().insert(calendarId=os.getenv("GOOGLE_CALENDAR_ID"), body=event).execute()
    print("✅ Event created Successfully")
