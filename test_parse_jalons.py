import unittest
import re
from generate_jalons import parse_jalons

text = r"""
Année 1 : le socle des fondations
Trimestre 1 : logique
L'objectif est de réapprendre la langue.
Jalon 1 : Logique formelle, connecteurs.
Trimestre 2 : analyse réelle, suites et séries de fonctions
Ce bloc demande du temps pour maîtriser la rigueur des limites et des approximations.
Jalon 13 : Structure de $\mathbb{R}$, axiome de la borne supérieure et propriété d'Archimède.
Trimestre 10 : géométrie différentielle et calcul des variations
L'étude des espaces courbes, base mathématique des architectures de réseaux sur graphes.
Jalon 109 : Topologie des sous-variétés de $\mathbb{R}^n$, définition par des cartes locales, des paramétrages ou des équations.
"""

class TestParseJalons(unittest.TestCase):
    def test_parse(self):
        jalons = parse_jalons(text)
        self.assertEqual(len(jalons), 3)

if __name__ == '__main__':
    unittest.main()
