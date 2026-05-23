import unittest
from generate_jalons import generate_concept_links

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

if __name__ == '__main__':
    unittest.main()
