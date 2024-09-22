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
    def test_run(self):
        test_str = """> Hardi:
Would Mon 4PM work?

> Eito Miyamura ♨️:
Sounds good! Whats your email?

> Eito Miyamura ♨️:
And what area of London will you be around?

> Hardi:
hardi@gatlingx.com
I am in Shordetich but on Mon I will be coming from Dulwitch by train so near Victoria could work or maybe start 5PM and do near Shorditch
"""
        self.txt2event.run(test_str)

    def test_process_txt_to_event(self):
        test_str = """> Hardi:
Would Mon 4PM work?

> Eito Miyamura ♨️:
Sounds good! Whats your email?

> Eito Miyamura ♨️:
And what area of London will you be around?

> Hardi:
hardi@gatlingx.com
I am in Shordetich but on Mon I will be coming from Dulwitch by train so near Victoria could work or maybe start 5PM and do near Shorditch
"""
        response = self.txt2event.process_txt_llm(test_str)
        print(response)
        self.assertIsNotNone(response)

        extracted_dict = self.txt2event.extract_event_yaml(response.content)
        print(extracted_dict)
        self.assertIsNotNone(extracted_dict)


if __name__ == "__main__":
    unittest.main()
