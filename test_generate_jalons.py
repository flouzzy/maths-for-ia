import unittest
from generate_jalons import (
    extract_short_title,
    parse_jalons,
    get_custom_content,
    generate_concept_links,
    generate_links
)

class TestGenerateJalons(unittest.TestCase):

    def test_extract_short_title(self):
        # comma
        self.assertEqual(extract_short_title("Logique formelle, connecteurs"), "Logique formelle")
        # parentheses
        self.assertEqual(extract_short_title("Quantification (\\forall, \\exists)"), "Quantification")
        # colon
        self.assertEqual(extract_short_title("Jalon 1 : Logique"), "Jalon 1")
        # no split characters
        self.assertEqual(extract_short_title("Simple Title"), "Simple Title")
        # multiple characters
        self.assertEqual(extract_short_title("First, Second (Third) : Fourth"), "First")

    def test_get_custom_content(self):
        # id with 108
        self.assertIn("Jalon 76", get_custom_content("Jalon 108"))
        self.assertIn("Jalon 105", get_custom_content("Jalon 108"))
        # id without 108
        self.assertEqual(get_custom_content("Jalon 107"), "")
        self.assertEqual(get_custom_content("Jalon 1"), "")

    def test_generate_concept_links(self):
        # hilbert
        links = generate_concept_links("This is about hilbert spaces")
        self.assertIn("Jalon 76", links)
        self.assertNotIn("Jalon 49", links)

        # hilbert with 108 (exclusion)
        links = generate_concept_links("This is about hilbert spaces in 108")
        self.assertNotIn("Jalon 76", links)

        # mesure
        links = generate_concept_links("Something related to mesure")
        self.assertIn("Jalon 63", links)

        # mesure with 63 or 64 (exclusion)
        links = generate_concept_links("Something related to mesure in 63")
        self.assertNotIn("Jalon 63", links)
        links = generate_concept_links("Something related to mesure in 64")
        self.assertNotIn("Jalon 63", links)

        # topologie
        links = generate_concept_links("Discussion on topologie")
        self.assertIn("Jalon 49", links)

        # topologie with 49 (exclusion)
        links = generate_concept_links("Discussion on topologie in 49")
        self.assertNotIn("Jalon 49", links)

        # vectoriel
        links = generate_concept_links("Espace vectoriel")
        self.assertIn("Jalon 7", links)

        # vectoriel with 7 (exclusion)
        links = generate_concept_links("Espace vectoriel 7")
        self.assertNotIn("Jalon 7", links)

        # Multiple matches
        links = generate_concept_links("hilbert and topologie")
        self.assertIn("Jalon 76", links)
        self.assertIn("Jalon 49", links)

        # No match
        links = generate_concept_links("Nothing related to concepts")
        self.assertEqual(links, "")

    def test_generate_links(self):
        jalons_list = [
            {"filename": "Jalon 1 (First).md"},
            {"filename": "Jalon 2 (Second).md"},
            {"filename": "Jalon 3 (Third).md"}
        ]

        # First item (index 0) - should only have "Suivant"
        links = generate_links(jalons_list[0], jalons_list, 0)
        self.assertNotIn("Précédent", links)
        self.assertIn("Suivant", links)
        self.assertIn("Jalon 2 (Second)", links)

        # Middle item (index 1) - should have both "Précédent" and "Suivant"
        links = generate_links(jalons_list[1], jalons_list, 1)
        self.assertIn("Précédent", links)
        self.assertIn("Jalon 1 (First)", links)
        self.assertIn("Suivant", links)
        self.assertIn("Jalon 3 (Third)", links)

        # Last item (index 2) - should only have "Précédent"
        links = generate_links(jalons_list[2], jalons_list, 2)
        self.assertIn("Précédent", links)
        self.assertIn("Jalon 2 (Second)", links)
        self.assertNotIn("Suivant", links)

        # Single item list
        single_list = [{"filename": "Jalon 1 (Only).md"}]
        links = generate_links(single_list[0], single_list, 0)
        self.assertEqual(links, "")

    def test_parse_jalons(self):
        sample_text = """
Année 1 : test
Trimestre 1 : test
Jalon 1 : First Jalon
Jalon 2 : Second Jalon
Jalons 3 à 4 : Multiple
"""
        jalons, all_jalon_titles = parse_jalons(sample_text)
        self.assertEqual(len(jalons), 3)
        self.assertEqual(jalons[0]["id"], "Jalon 1")
        self.assertEqual(jalons[0]["desc"], "First Jalon")
        self.assertEqual(jalons[0]["year"], "Année 1 : test")
        self.assertEqual(jalons[0]["trimester"], "Trimestre 1 : test")

        self.assertEqual(jalons[1]["id"], "Jalon 2")
        self.assertEqual(jalons[2]["id"], "Jalons 3 à 4")

        self.assertIn("Jalon 1", all_jalon_titles)
        self.assertIn("Jalon 2", all_jalon_titles)
        self.assertIn("Jalons 3 à 4", all_jalon_titles)


if __name__ == "__main__":
    unittest.main()
