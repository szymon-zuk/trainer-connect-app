from apiclient.discovery import build
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from datetime import datetime


class GoogleCalendar:
    def send_to_API(
        title,
        start_time,
        end_time,
        host_email,
        guest_email,
        location,
        event_description,
    ):
        credentials = pickle.load(open("token.pkl", "rb"))
        service = build("calendar", "v3", credentials=credentials)
        result = service.calendarList().list().execute()
        calendar_id = result["items"][0]["id"]

        start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
        end_time = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
        timezone = "Europe/Warsaw"

        event = {
            "summary": title,
            "location": location,
            "description": event_description,
            "start": {
                "dateTime": start_time1.strftime("%Y-%m-%dT%H:%M:%S"),
                "timeZone": timezone,
            },
            "end": {
                "dateTime": end_time1.strftime("%Y-%m-%dT%H:%M:%S"),
                "timeZone": timezone,
            },
            "attendees": [
                {"email": host_email},
                {"email": guest_email},
            ],
            "reminders": {
                "useDefault": False,
                "overrides": [
                    {"method": "email", "minutes": 24 * 60},
                    {"method": "popup", "minutes": 10},
                ],
            },
        }
        service.events().insert(calendarId=calendar_id, body=event).execute()

    def get_event_id():
        """This function return google calendar event id as string - last value from table"""
        credentials = pickle.load(open("token.pkl", "rb"))
        service = build("calendar", "v3", credentials=credentials)
        result = service.calendarList().list().execute()
        calendar_id = result["items"][0]["id"]
        result = (
            service.events().list(calendarId=calendar_id, maxResults=2400).execute()
        )
        table_size = len(result["items"])
        event_id = result["items"][table_size - 1]["id"]
        return event_id
