import datetime
import re
from typing import Any, Dict, List
import yaml

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

    def run(self, content: str) -> None:
        response = self.process_txt_llm(content)
        assert response is not None

        extracted_dict = self.extract_event_yaml(response.content)

        # Assertion
        mandatory_fields = ["summary", "start_time", "end_time", "time_zone"]
        for field in mandatory_fields:
            assert field in extracted_dict, AssertionError(f"{field} not in LLM output")

        create_event(
            service=self.service,  # Pass the service
            summary=extracted_dict["summary"],
            start_time=extracted_dict["start_time"],
            end_time=extracted_dict["end_time"],
            time_zone=extracted_dict["time_zone"],
            location=extracted_dict.get("location"),  # Make this optional
            email_invites=extracted_dict.get("emailInvites"),  # Make this optional
        )
        return None

    def extract_event_yaml(self, content: str) -> Dict[str, Any]:

        pattern = r"```yaml(.*?)```"
        matches = re.findall(pattern, content, re.DOTALL)
        yaml_content = matches[0].strip() if matches else ""

        try:
            parsed_dict = yaml.safe_load(yaml_content)
            return parsed_dict
        except yaml.YAMLError as e:
            print(f"Error parsing YAML: {e}")
            return {}

    def process_txt_llm(self, text):
        system_prompt = load_prompt("src/txt2event/system_prompts/txt2event.txt")

        today_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        messages = [
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": f"Today datetime: {today_date}\n\n{text}",
            },
        ]
        response = self.llm.invoke(messages)
        return response
