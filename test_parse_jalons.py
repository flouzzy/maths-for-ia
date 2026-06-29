import unittest
import re

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

def parse_jalons(text_content):
    lines = text_content.strip().split('\n')

    current_year = ""
    current_trimester = ""
    trimester_context = ""

    jalons = []

    jalon_pattern = re.compile(r'(Jalon[s]? [\d à]+) : (.+)')

    for line in lines:
        line = line.strip()
        if line.startswith("Année"):
            current_year = line
        elif line.startswith("Trimestre"):
            current_trimester = line
            trimester_context = ""
        elif line.startswith("Jalon ") or line.startswith("Jalons "):
            match = jalon_pattern.match(line)
            if match:
                j_id = match.group(1)
                desc = match.group(2)
                jalons.append({
                    'id': j_id,
                    'desc': desc,
                })
        elif line:
            if current_trimester and not line.startswith("Jalon"):
                trimester_context += line + " "

    return jalons

class TestParseJalons(unittest.TestCase):
    def test_parse(self):
        jalons = parse_jalons(text)
        self.assertEqual(len(jalons), 3)

if __name__ == '__main__':
    unittest.main()
