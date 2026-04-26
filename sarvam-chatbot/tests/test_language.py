import unittest
from types import SimpleNamespace
from unittest.mock import patch

from src.language import detect_language


class TestLanguage(unittest.TestCase):
    @patch("src.language.client")
    def test_detect_language_returns_bcp47(self, mock_client):
        mock_client.text.identify_language.return_value = SimpleNamespace(language_code="ta-IN")

        code = detect_language("vanakkam")
        self.assertEqual(code, "ta-IN")


if __name__ == "__main__":
    unittest.main()
