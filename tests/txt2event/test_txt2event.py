import unittest

from tests.test_class import TestCaseClass, ci_test
from global_config import global_config

from src.txt2event import Text2Event


class TestTxt2Event(TestCaseClass):
    def setUp(self) -> None:
        super().setUp()
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
    def test_process_txt_to_event(self):
        test_str = """> Hardi:
Would Wed 4PM work?

> Eito Miyamura ♨️:
Sounds good! Whats your email?

> Eito Miyamura ♨️:
And what area of London will you be around?

> Hardi:
hardi@gatlingx.com
I am in Shordetich but on Wed I will be coming from Dulwitch by train so near Victoria could work or maybe start 5PM and do near Shorditch
"""
        response = self.txt2event.process_txt_to_event(test_str)
        print(response)
        self.assertIsNotNone(response)


if __name__ == "__main__":
    unittest.main()
