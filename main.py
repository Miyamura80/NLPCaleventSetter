import tkinter as tk
from tkinter import scrolledtext
from src.txt2event import Text2Event
from global_config import global_config
from human_id import generate_id
from termcolor import colored


def get_multiline_input():
    def on_submit():
        nonlocal user_input
        user_input = text_area.get("1.0", tk.END).strip()
        root.quit()

    root = tk.Tk()
    root.title("Event Description")

    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack()

    label = tk.Label(frame, text="Enter your event description:")
    label.pack()

    text_area = scrolledtext.ScrolledText(frame, width=50, height=10)
    text_area.pack()

    submit_button = tk.Button(frame, text="Submit", command=on_submit)
    submit_button.pack()

    user_input = ""
    root.mainloop()
    root.destroy()

    return user_input


def main():
    print(colored("Welcome to the Natural Language Calendar Event Booker!", "blue"))

    description = get_multiline_input()

    if not description:
        print(colored("No input provided. Exiting.", "red"))
        return

    config = global_config.__dict__
    config["session_id"] = generate_id()
    config["session_name"] = "Natural Language Calendar Booker"
    config["session_path"] = "/clitool"

    txt2event = Text2Event(config)
    success = txt2event.run(description)

    if success:
        print(colored("Event booked successfully!", "green"))
    else:
        print(colored("Failed to book the event.", "red"))


if __name__ == "__main__":
    main()
