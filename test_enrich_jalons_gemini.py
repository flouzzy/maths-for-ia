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

    def test_extract_clean_title(self):
        # Case 1: Standard `# Jalon X : Title` format
        title = enrich_jalons_gemini.extract_clean_title("# Jalon 1 : Introduction à l'IA\nSome text", "Jalon 1.md")
        self.assertEqual(title, "Introduction à l'IA")

        # Case 2: Content with `# Jalon X (Title)` format
        title = enrich_jalons_gemini.extract_clean_title("# Jalon 1 (Introduction à l'IA)\nSome text", "Jalon 1.md")
        self.assertEqual(title, "Introduction à l'IA")

        # Case 3: Content missing H1 header, extract from filename with parens `Jalon X (Title).md`
        title = enrich_jalons_gemini.extract_clean_title("No title header here\nJust text", "Jalon 2 (Réseaux de neurones).md")
        self.assertEqual(title, "Réseaux de neurones")

        # Case 4: Content missing H1 header, falling back to clean filename `Jalon X.md` and empty text
        title = enrich_jalons_gemini.extract_clean_title("", "Jalon 3 (Deep Learning).md")
        self.assertEqual(title, "Deep Learning")

        # Case 5: "Jalons" plural and ranges like "Jalons X à Y : Title"
        title = enrich_jalons_gemini.extract_clean_title("# Jalons 4 à 5 : Optimisation\nText", "Jalons 4 à 5.md")
        self.assertEqual(title, "Optimisation")

        # Case 6: Stripping prefix completely where title is something else
        title = enrich_jalons_gemini.extract_clean_title("# Les arbres de décision\nText", "Jalon 6.md")
        self.assertEqual(title, "Les arbres de décision")

        # Case 7: Content missing H1 header, falling back to simple filename
        title = enrich_jalons_gemini.extract_clean_title("Just some content without title", "Jalon 7.md")
        self.assertEqual(title, "Jalon 7")

    def test_extract_main_content(self):
        # Case 1: Simple content without YAML or nav links
        content = "Just some plain text content.\nNo lines."
        self.assertEqual(enrich_jalons_gemini.extract_main_content(content), content)

        # Case 2: Content with YAML frontmatter but NO nav links at the end
        content_yaml = "---\nuuid: 123\n---\n# Jalon 1\nSome text here"
        # Since it has --- but no **Précédent** or **Suivant**, it should return the entire content
        self.assertEqual(enrich_jalons_gemini.extract_main_content(content_yaml), content_yaml)

        # Case 3: Content with frontmatter AND nav links (Précédent)
        content_nav_prev = "---\nuuid: 123\n---\n# Jalon 1\nMain text\n---\n**Précédent** : [[Jalon 0.md]]"
        expected_nav_prev = "---\nuuid: 123\n---\n# Jalon 1\nMain text"
        self.assertEqual(enrich_jalons_gemini.extract_main_content(content_nav_prev), expected_nav_prev)

        # Case 4: Content with frontmatter AND nav links (Suivant)
        content_nav_next = "---\nuuid: 123\n---\n# Jalon 1\nMain text\n---\n**Suivant** : [[Jalon 2.md]]"
        expected_nav_next = "---\nuuid: 123\n---\n# Jalon 1\nMain text"
        self.assertEqual(enrich_jalons_gemini.extract_main_content(content_nav_next), expected_nav_next)

        # Case 5: Content with frontmatter AND both nav links
        content_nav_both = "---\nuuid: 123\n---\n# Jalon 1\nMain text\n---\n**Précédent** : [[Jalon 0.md]]\n**Suivant** : [[Jalon 2.md]]"
        expected_nav_both = "---\nuuid: 123\n---\n# Jalon 1\nMain text"
        self.assertEqual(enrich_jalons_gemini.extract_main_content(content_nav_both), expected_nav_both)

if __name__ == '__main__':
    unittest.main()
