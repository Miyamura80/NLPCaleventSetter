import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from global_config import global_config


def get_calendar_service():
    scopes = ["https://www.googleapis.com/auth/calendar"]

    # Check if we're running in a CI environment
    is_ci = os.getenv("GITHUB_ACTIONS") == "true"

    if is_ci:
        # Use environment variables for credentials in CI
        creds = Credentials.from_authorized_user_info(
            info={
                "client_id": os.environ.get("GOOGLE_CLIENT_ID"),
                "client_secret": os.environ.get("GOOGLE_CLIENT_SECRET"),
                "refresh_token": os.environ.get("GOOGLE_REFRESH_TOKEN"),
            },
            scopes=scopes,
        )
    else:
        # Use credentials file for local development
        credentials_file = global_config.google_calendar.credentials_file
        flow = InstalledAppFlow.from_client_secrets_file(credentials_file, scopes)
        creds = flow.run_local_server(port=0)

    service = build("calendar", "v3", credentials=creds)
    return service
