from src.txt2event import Text2Event
from global_config import global_config
from human_id import generate_id
from termcolor import colored


def main():
    print("Welcome to the Natural Language Calendar Event Booker!")
    description = input("Please enter a natural language description of your event.")

    config = global_config.__dict__
    config["session_id"] = generate_id()
    config["session_name"] = "Natural Language Calendar Booker"
    config["session_path"] = "/clitool"
    print(config)

    txt2event = Text2Event(config)
    success = txt2event.run(description)

    if success:
        print(colored("Event booked successfully!", "green"))
    else:
        print(colored("Failed to book the event.", "red"))


if __name__ == "__main__":
    main()
