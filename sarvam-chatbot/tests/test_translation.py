import unittest
from types import SimpleNamespace
from unittest.mock import patch

from src.translation import translate_colloquial, translate_formal, translate_text


class TestTranslation(unittest.TestCase):
    @patch("src.translation.client")
    def test_translate_text(self, mock_client):
        mock_client.text.translate.return_value = SimpleNamespace(translated_text="வணக்கம்")

        translated = translate_text("hello", target_language="ta-IN", source_language="en-IN")
        self.assertEqual(translated, "வணக்கம்")

    @patch("src.translation.client")
    def test_translate_styles(self, mock_client):
        mock_client.text.translate.return_value = SimpleNamespace(translated_text="नमस्ते")

        self.assertEqual(translate_formal("hello", "hi-IN"), "नमस्ते")
        self.assertEqual(translate_colloquial("hello", "hi-IN"), "नमस्ते")


if __name__ == "__main__":
    unittest.main()
