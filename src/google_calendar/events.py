from .service import get_calendar_service
from datetime import datetime
from termcolor import colored


def create_event(
    service, summary, start_time, end_time, time_zone, location=None, email_invites=None
):
    event = {
        "summary": summary,
        "start": {
            "dateTime": start_time.isoformat(),
            "timeZone": time_zone,
        },
        "end": {
            "dateTime": end_time.isoformat(),
            "timeZone": time_zone,
        },
    }

    if location:
        event["location"] = location

    if email_invites:
        event["attendees"] = [{"email": email} for email in email_invites]

    calendar_id = "primary"
    event = (
        service.events()
        .insert(calendarId=calendar_id, body=event, sendUpdates="all")
        .execute()
    )
    print(
        f'Event created: \n{colored(event.get("htmlLink"), "green", attrs=["underline"])}'
    )
    return event
