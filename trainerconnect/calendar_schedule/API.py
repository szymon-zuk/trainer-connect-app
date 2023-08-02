from decouple import config
from google.oauth2 import service_account
from googleapiclient.discovery import build
import os


if os.environ.get('GITHUB_WORKFLOW'):
    CAL_ID = "test cal_id"
else:
    CAL_ID = config("CAL_ID")

SCOPES = ["https://www.googleapis.com/auth/calendar"]
SERVICE_ACCOUNT_FILE = "./google-credentials.json"


def create_event(title, start, end, location, event_description):
    """Connecting to calendar using google-credentials.json"""

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    service = build("calendar", "v3", credentials=credentials)

    """Creating a new event"""

    timezone = "Europe/Warsaw"
    new_event = {
        "summary": title,
        "location": location,
        "description": event_description,
        "start": {
            "dateTime": start.strftime("%Y-%m-%dT%H:%M:%S"),
            "timeZone": timezone
        },
        "end": {
            "dateTime": end.strftime("%Y-%m-%dT%H:%M:%S"),
            "timeZone": timezone
        },
    }
    service.events().insert(calendarId=CAL_ID, body=new_event).execute()
    print('Event created: %s' % (new_event.get('htmlLink')))


def get_event_id():
    """Gets the id of last event from the table"""
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    service = build("calendar", "v3", credentials=credentials)
    result = service.events().list(calendarId=CAL_ID).execute()
    table_size = len(result['items'])
    event_id = result['items'][table_size - 1]['id']
    return event_id


def edit_event(title, start, end, location, event_description, event_id):
    """Connection same as in create_event"""

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    service = build("calendar", "v3", credentials=credentials)

    """Editing an event"""
    timezone = "Europe/Warsaw"
    edit_event = {
        "summary": title,
        "location": location,
        "description": event_description,
        "start": {
            "dateTime": start.strftime("%Y-%m-%dT%H:%M:%S"),
            "timeZone": timezone
        },
        "end": {
            "dateTime": end.strftime("%Y-%m-%dT%H:%M:%S"),
            "timeZone": timezone
        },
    }
    service.events().update(calendarId=CAL_ID, eventId=event_id, body=edit_event).execute()
    print('Event edited: %s' % (edit_event.get('htmlLink')))
