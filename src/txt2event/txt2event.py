from typing import Any, Dict, List
from deps.ChatRouter.utils import ChatRouter, load_prompt
from global_config.global_config import global_config
import datetime

import re


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

    def extract_event_yaml(self, content: str) -> List[str]:
        pattern = r"```yaml(.*?)```"
        matches = re.findall(pattern, content, re.DOTALL)
        return [match.strip() for match in matches]

    def process_txt_to_event(self, text):
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
