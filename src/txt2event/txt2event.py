import datetime
import re
from typing import Any, Dict, List
import yaml
from termcolor import colored

from deps.ChatRouter.utils import ChatRouter, load_prompt
from global_config.global_config import global_config
from src.google_calendar.events import create_event
from src.google_calendar.service import get_calendar_service


class Text2Event:

    def __init__(
        self,
        config_dict: Dict[str, Any],
    ):
        self.session_id = config_dict.get("session_id")
        if not self.session_id:
            raise ValueError("session_id is required in the config_dict")

        self.llm = ChatRouter(
            config_dict=config_dict,
            session_path_postfix="/txt2event",
        )
        self.service = get_calendar_service()  # Initialize the service

    def run(self, content: str) -> bool:
        try:
            response = self.process_txt_llm(content)
            if response is None:
                return False

            extracted_dict = self.extract_event_yaml(response.content)

            # Assertion
            mandatory_fields = ["summary", "start_time", "end_time", "time_zone"]
            for field in mandatory_fields:
                if field not in extracted_dict:
                    print(f"Error: {field} not in LLM output")
                    return False

            event = create_event(
                service=self.service,  # Pass the service
                summary=extracted_dict["summary"],
                start_time=extracted_dict["start_time"],
                end_time=extracted_dict["end_time"],
                time_zone=extracted_dict["time_zone"],
                location=extracted_dict.get("location"),  # Make this optional
                email_invites=extracted_dict.get("emailInvites"),  # Make this optional
            )

            return event is not None

        except Exception as e:
            print(f"Error occurred: {str(e)}")
            return False

    def extract_event_yaml(self, content: str) -> Dict[str, Any]:

        pattern = r"```yaml(.*?)```"
        matches = re.findall(pattern, content, re.DOTALL)
        yaml_content = matches[0].strip() if matches else ""

        print(colored(yaml_content, "blue"))

        try:
            parsed_dict = yaml.safe_load(yaml_content)
            return parsed_dict
        except yaml.YAMLError as e:
            print(f"Error parsing YAML: {e}")
            return {}

    def process_txt_llm(self, text):
        system_prompt = load_prompt("src/txt2event/system_prompts/txt2event.txt")

        now = datetime.datetime.now()
        today_date = now.strftime("%Y-%m-%d %H:%M:%S")
        # This is needed, because the LLM is not aware of the current day of the week
        day_of_week = now.strftime("%A")

        messages = [
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": f"Today datetime: {today_date}\n\nDay of the week: {day_of_week}\n\n{text}",
            },
        ]
        response = self.llm.invoke(messages)
        return response
