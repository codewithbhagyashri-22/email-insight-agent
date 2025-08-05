#This code is used to get Refresh Token. Execute it one time only.

from google_auth_oauthlib.flow import InstalledAppFlow

# Gmail API scope
SCOPES = ['https://www.googleapis.com/auth/gmail.modify','https://www.googleapis.com/auth/calendar']

# Load credentials
flow = InstalledAppFlow.from_client_secrets_file(
    'client_secret.json', SCOPES)

# Run auth flow
creds = flow.run_local_server(port=0)

# Print the refresh token
print("Refresh Token:", creds.refresh_token)
print("Client ID:", creds.client_id)
print("Client Secret:", creds.client_secret)

# Copy Refresh Token from and add it in .env file 
