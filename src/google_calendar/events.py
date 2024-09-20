from .service import get_calendar_service

def create_event(summary, start_time, end_time, time_zone='UTC', calendar_id='primary'):
    service = get_calendar_service()

    event = {
        'summary': summary,
        'start': {
            'dateTime': start_time,
            'timeZone': time_zone,
        },
        'end': {
            'dateTime': end_time,
            'timeZone': time_zone,
        },
    }

    event = service.events().insert(calendarId=calendar_id, body=event, sendUpdates='all').execute()
    print(f'Event created: {event.get("htmlLink")}')