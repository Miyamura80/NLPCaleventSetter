from src.txt2event import Text2Event
from global_config import global_config
from human_id import generate_id

def get_multiline_input():
    print("Please enter a natural language description of your event.")
    print("Press Enter twice to finish your input:")
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    return "\n".join(lines)


def main():
    print("Welcome to the Natural Language Calendar Event Booker!")
    description = get_multiline_input()

    config = global_config.__dict__
    config["session_id"] = generate_id()
    config["session_name"] = "Natural Language Calendar Booker"
    config["session_path"] = "/clitool"

    txt2event = Text2Event(config)
    success = txt2event.run(description)

    if success:
        print("Event booked successfully!")
    else:
        print("Failed to book the event.")


if __name__ == "__main__":
    main()
