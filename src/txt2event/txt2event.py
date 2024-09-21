from typing import Any, Dict, List
from deps.ChatRouter.utils import ChatRouter
from global_config.global_config import global_config

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

    def process_text(self, text):
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": text},
        ]
        response = self.llm.invoke(messages)
        return response
