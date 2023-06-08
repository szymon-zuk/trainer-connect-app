from decouple import config
from google.oauth2 import service_account
import googleapiclient.discovery
from datetime import datetime
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
    service = googleapiclient.discovery.build("calendar", "v3", credentials=credentials)

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
