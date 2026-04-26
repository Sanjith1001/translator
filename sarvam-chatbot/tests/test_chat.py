import unittest
from types import SimpleNamespace
from unittest.mock import patch

from src.chat import chat


class TestChat(unittest.TestCase):
    @patch("src.chat.detect_language", return_value="hi-IN")
    @patch("src.chat.client")
    def test_chat_returns_reply_and_updates_history(self, mock_client, _mock_detect):
        mock_response = SimpleNamespace(
            choices=[SimpleNamespace(message=SimpleNamespace(content="नमस्ते!"))]
        )
        mock_client.chat.completions.return_value = mock_response

        history = []
        reply, detected, updated_history = chat("Hello", history=history)

        self.assertEqual(reply, "नमस्ते!")
        self.assertEqual(detected, "hi-IN")
        self.assertEqual(len(updated_history), 2)
        self.assertEqual(updated_history[0]["role"], "user")
        self.assertEqual(updated_history[1]["role"], "assistant")


if __name__ == "__main__":
    unittest.main()
