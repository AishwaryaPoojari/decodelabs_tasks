
import unittest
from chatbot import get_response


class TestDecodeBot(unittest.TestCase):

    def test_greeting(self):
        response = get_response("hello")
        self.assertIn("Hello", response)

    def test_greeting_case_insensitive(self):
        response = get_response("HELLO")
        self.assertIn("Hello", response)

    def test_artificial_intelligence(self):
        response = get_response("what is ai")
        self.assertIn("Artificial Intelligence", response)

    def test_machine_learning(self):
        response = get_response("what is machine learning")
        self.assertIn("Machine Learning", response)

    def test_python(self):
        response = get_response("what is python")
        self.assertIn("Python", response)

    def test_help_command(self):
        response = get_response("help")
        self.assertIn("available topics", response)

    def test_unknown_question(self):
        response = get_response("tell me something unknown")
        self.assertIn("don't understand", response)

    def test_whitespace_handling(self):
        response = get_response("  hello  ")
        self.assertIn("Hello", response)

    def test_thank_you(self):
        response = get_response("thank you")
        self.assertIn("You're welcome", response)


if __name__ == "__main__":
    unittest.main()
