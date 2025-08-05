import base64
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import os

def get_gmail_service():

    creds = Credentials(
        None,
        refresh_token=os.getenv("GMAIL_REFRESH_TOKEN"),
        token_uri="https://oauth2.googleapis.com/token",
        client_id=os.getenv("GMAIL_CLIENT_ID"),
        client_secret=os.getenv("GMAIL_CLIENT_SECRET")
    )
    return build('gmail', 'v1', credentials=creds)

def fetch_latest_emails(max_results=3):
    service = get_gmail_service()
    results = service.users().messages().list(userId='me', labelIds=['INBOX'], maxResults=max_results).execute()
    messages = results.get('messages', [])
    
    email_texts = []
    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        snippet = msg_data.get('snippet', '')
        if 'data' in msg_data['payload']['body']:
            data = msg_data['payload']['body']['data']
            decoded = base64.urlsafe_b64decode(data).decode('utf-8')
            email_texts.append(decoded)
        else:
            email_texts.append(snippet)
    return email_texts
