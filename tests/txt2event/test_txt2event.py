import unittest

from tests.test_class import TestCaseClass, ci_test
from global_config import global_config

from src.txt2event import Text2Event


class TestTxt2Event(TestCaseClass):
    def setUp(self) -> None:
        super().setUp()
        print(self.config)
        # Add any setup code here
        self.txt2event = Text2Event(self.config)

    @ci_test
    def test_extract_event_yaml(self):
        test_str = """Plan:
1) 

Code:
```yaml

```"""

    @ci_test
    def test_process_text(self):
        test_str = "What is the capital of France?"
        response = self.txt2event.process_text(test_str)
        print(response)
        self.assertIsNotNone(response)


if __name__ == "__main__":
    unittest.main()
