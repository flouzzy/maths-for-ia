import unittest
from generate_jalons import generate_concept_links, extract_short_title, parse_jalons

class TestExtractShortTitle(unittest.TestCase):

    def test_split_on_comma(self):
        self.assertEqual(extract_short_title("Logique formelle, connecteurs"), "Logique formelle")

    def test_split_on_parenthesis(self):
        self.assertEqual(extract_short_title("Quantification (\\forall, \\exists)"), "Quantification")

    def test_split_on_colon(self):
        self.assertEqual(extract_short_title("Titre: Sous-titre"), "Titre")

    def test_no_separator(self):
        self.assertEqual(extract_short_title("Titre simple sans separateur"), "Titre simple sans separateur")

    def test_strips_whitespace(self):
        self.assertEqual(extract_short_title("  Espaces vectoriels   , suite"), "Espaces vectoriels")

    def test_multiple_separators(self):
        # Should split on the FIRST separator
        self.assertEqual(extract_short_title("Titre, sous-titre (suite)"), "Titre")


class TestGenerateConceptLinks(unittest.TestCase):

    def test_no_match(self):
        self.assertEqual(generate_concept_links("This is a random description."), "")

    def test_hilbert_match(self):
        result = generate_concept_links("This is about Hilbert spaces.")
        self.assertIn("[[Jalon 76 (Propriétés géométriques de l'espace de Hilbert L^2)]]", result)
        self.assertIn("**Concepts liés** :", result)

    def test_hilbert_exclude_108(self):
        result = generate_concept_links("This is about Hilbert spaces in jalon 108.")
        self.assertEqual(result, "")

    def test_mesure_match(self):
        result = generate_concept_links("Une mesure de probabilité.")
        self.assertIn("[[Jalon 63 (Définition axiomatique d'une mesure)]]", result)

    def test_mesure_exclude_63_64(self):
        result1 = generate_concept_links("Une mesure de probabilité in jalon 63.")
        self.assertEqual(result1, "")
        result2 = generate_concept_links("Une mesure de probabilité in jalon 64.")
        self.assertEqual(result2, "")

    def test_topologi_match(self):
        result = generate_concept_links("Une étude topologique.")
        self.assertIn("[[Jalon 49 (Espaces topologiques généraux)]]", result)

    def test_topologi_exclude_49(self):
        result = generate_concept_links("Une étude topologique in jalon 49.")
        self.assertEqual(result, "")

    def test_vectoriel_match(self):
        result = generate_concept_links("Espace vectoriel.")
        self.assertIn("[[Jalon 7 (Espaces vectoriels abstraits)]]", result)

    def test_vectoriel_exclude_7(self):
        result = generate_concept_links("Espace vectoriel in jalon 7.")
        self.assertEqual(result, "")

    def test_case_insensitivity(self):
        result = generate_concept_links("HILBERT MESURE TOPOLOGI VECTORIEL")
        self.assertIn("[[Jalon 76 (Propriétés géométriques de l'espace de Hilbert L^2)]]", result)
        self.assertIn("[[Jalon 63 (Définition axiomatique d'une mesure)]]", result)
        self.assertIn("[[Jalon 49 (Espaces topologiques généraux)]]", result)
        self.assertIn("[[Jalon 7 (Espaces vectoriels abstraits)]]", result)

    def test_multiple_matches(self):
        result = generate_concept_links("hilbert and mesure")
        expected = "\\n**Concepts liés** : [[Jalon 76 (Propriétés géométriques de l'espace de Hilbert L^2)]], [[Jalon 63 (Définition axiomatique d'une mesure)]]\\n"
        self.assertEqual(result, expected)

class TestParseJalons(unittest.TestCase):
    def test_basic_parsing(self):
        text = """
Année 1 : le socle des fondations
Trimestre 1 : logique
L'objectif est de réapprendre la langue.
Jalon 1 : Logique formelle, connecteurs.
"""
        jalons, titles = parse_jalons(text)
        self.assertEqual(len(jalons), 1)
        j = jalons[0]
        self.assertEqual(j['id'], "Jalon 1")
        self.assertEqual(j['year'], "Année 1 : le socle des fondations")
        self.assertEqual(j['trimester'], "Trimestre 1 : logique")
        self.assertEqual(j['context'].strip(), "L'objectif est de réapprendre la langue.")
        self.assertEqual(j['desc'], "Logique formelle, connecteurs.")
        self.assertEqual(j['filename'], "Jalon 1 (Logique formelle).md")
        self.assertEqual(titles, ["Jalon 1 (Logique formelle).md"])

    def test_livrable_ia_title(self):
        text = "Jalon 12 : Livrable IA T1 : Conception théorique d'un moteur de recherche"
        jalons, titles = parse_jalons(text)
        self.assertEqual(len(jalons), 1)
        self.assertEqual(jalons[0]['filename'], "Jalon 12 (Livrable IA).md")

    def test_filename_sanitization(self):
        # We need a string where extract_short_title keeps the problematic characters.
        # Since extract_short_title splits on `,`, `(`, and `:`, we shouldn't use them in the short title part.
        text = 'Jalon 2 : A \\ / * ? " < > | $ -- C'
        jalons, titles = parse_jalons(text)
        self.assertEqual(len(jalons), 1)
        # "A \ / * ? \" < > | $ -- C" -> "A - - - - - - - - - - C"
        self.assertEqual(jalons[0]['filename'], "Jalon 2 (A - - - - - - - - - - C).md")

    def test_multiple_jalons(self):
        text = "Jalons 145 à 152 : Synthèse"
        jalons, titles = parse_jalons(text)
        self.assertEqual(len(jalons), 1)
        self.assertEqual(jalons[0]['id'], "Jalons 145 à 152")
        self.assertEqual(jalons[0]['filename'], "Jalons 145 à 152 (Synthèse).md")

    def test_empty_input(self):
        jalons, titles = parse_jalons("")
        self.assertEqual(jalons, [])
        self.assertEqual(titles, [])


if __name__ == '__main__':
    unittest.main()
