import unittest
from unittest.mock import patch, MagicMock
import enrich_jalons_gemini

class TestEnrichJalonsGemini(unittest.TestCase):
    @patch('enrich_jalons_gemini.client')
    @patch('enrich_jalons_gemini.time.sleep')
    def test_generate_enriched_content_retry_on_resource_exhausted(self, mock_sleep, mock_client):
        # Mock client to raise an exception indicating RESOURCE_EXHAUSTED then succeed
        mock_client.models.generate_content.side_effect = [
            Exception("RESOURCE_EXHAUSTED: quota exceeded"),
            MagicMock(text="Enriched content")
        ]

        result = enrich_jalons_gemini.generate_enriched_content(
            "Test Title", "Original content", "Jalon 1.md", "1", "1", "", ""
        )

        # Check that sleep was called
        mock_sleep.assert_called_once_with(60)

        # Check that it eventually succeeded and returned the text
        self.assertEqual(result, "Enriched content")

        # Check that client was called twice
        self.assertEqual(mock_client.models.generate_content.call_count, 2)

    @patch('enrich_jalons_gemini.client')
    @patch('enrich_jalons_gemini.time.sleep')
    def test_generate_enriched_content_immediate_failure_on_generic_error(self, mock_sleep, mock_client):
        # Mock client to raise a generic exception
        mock_client.models.generate_content.side_effect = Exception("Some generic error")

        result = enrich_jalons_gemini.generate_enriched_content(
            "Test Title", "Original content", "Jalon 1.md", "1", "1", "", ""
        )

        # Check that sleep was NOT called
        mock_sleep.assert_not_called()

        # Check that it failed and returned None
        self.assertIsNone(result)

        # Check that client was called only once
        self.assertEqual(mock_client.models.generate_content.call_count, 1)

    @patch('enrich_jalons_gemini.client')
    @patch('enrich_jalons_gemini.time.sleep')
    def test_generate_enriched_content_fails_after_max_retries(self, mock_sleep, mock_client):
        # Mock client to always raise RESOURCE_EXHAUSTED
        mock_client.models.generate_content.side_effect = Exception("RESOURCE_EXHAUSTED")

        result = enrich_jalons_gemini.generate_enriched_content(
            "Test Title", "Original content", "Jalon 1.md", "1", "1", "", ""
        )

        # Check that sleep was called 10 times
        self.assertEqual(mock_sleep.call_count, 10)

        # Check that it failed and returned None
        self.assertIsNone(result)

        # Check that client was called 10 times
        self.assertEqual(mock_client.models.generate_content.call_count, 10)

if __name__ == '__main__':
    unittest.main()
