from src.google_calendar.events import create_event

if __name__ == "__main__":
    summary = "Hello World"
    start_time = "2024-09-20T23:30:00"
    end_time = "2024-09-21T00:30:00"
    time_zone = "Europe/London"
    create_event(summary, start_time, end_time, time_zone)
