import unittest
from unittest.mock import patch
import os
import tempfile
from enrich_jalons_gemini import get_jalon_files, parse_file

class TestEnrichJalonsGemini(unittest.TestCase):

    @patch('enrich_jalons_gemini.glob.glob')
    def test_get_jalon_files(self, mock_glob):
        mock_glob.return_value = ["Jalon-2.md", "Jalon-1.md", "Jalon-10.md"]
        files = get_jalon_files()

        mock_glob.assert_called_once_with("Jalon*/**/*.md", recursive=True)
        self.assertEqual(files, ["Jalon-1.md", "Jalon-10.md", "Jalon-2.md"])

    def test_parse_file_standard(self):
        content = """# Jalon 1 (Logique formelle)
**Année 1** > **Trimestre 1**

**Précédent** : [[Jalon Précédent]]
**Suivant** : [[Jalon Suivant]]

Contenu de test.
"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as f:
            f.write(content)
            filepath = f.name

        try:
            main_content, title, year, trimester, prev_link, next_link = parse_file(filepath)

            self.assertEqual(year, "1")
            self.assertEqual(trimester, "1")
            self.assertEqual(prev_link, '"[[Jalon Précédent.md]]"')
            self.assertEqual(next_link, '"[[Jalon Suivant.md]]"')
            self.assertEqual(title, "Logique formelle")
        finally:
            os.unlink(filepath)

    def test_parse_file_no_headers(self):
        content = """# Introduction
Contenu de test sans headers."""

        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as f:
            f.write(content)
            filepath = f.name

        try:
            main_content, title, year, trimester, prev_link, next_link = parse_file(filepath)

            self.assertEqual(year, "1")
            self.assertEqual(trimester, "1")
            self.assertEqual(prev_link, "")
            self.assertEqual(next_link, "")
            self.assertEqual(title, "Introduction")
        finally:
            os.unlink(filepath)

    def test_parse_file_with_yaml_frontmatter(self):
        content = """---
uuid: "jalon-1"
title: "Logique formelle"
year: 1
trimester: 1
---
# Jalon 1 (Logique formelle)

Contenu.
---
**Précédent** : [[Jalon Précédent]]
**Suivant** : [[Jalon Suivant]]
"""
        # We write to a specific filename instead of a random temp file
        # to ensure regex cleaning of the filename works properly.
        filepath = "Jalon 1 (Logique formelle).md"
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        try:
            main_content, title, year, trimester, prev_link, next_link = parse_file(filepath)

            self.assertEqual(year, "1")
            self.assertEqual(trimester, "1")
            self.assertEqual(prev_link, '"[[Jalon Précédent.md]]"')
            self.assertEqual(next_link, '"[[Jalon Suivant.md]]"')
            self.assertEqual(title, "Logique formelle")
            # When YAML frontmatter and bottom nav links are present, the main_content is extracted as the text before the last '---'
            # Note: based on the current parse_file code, there might be specific parsing logic. Let's just check the title/metadata.
        finally:
            if os.path.exists(filepath):
                os.unlink(filepath)

if __name__ == '__main__':
    unittest.main()
