import timeit

setup_uncached = r'''
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
lines = text.strip().split('\n')

def run_uncached():
    for line in lines:
        if "Trimestre" in line:
            match = re.search(r'\*\*Trimestre (\d+).*?\*\*', line)
            if match:
                current_trimester = f"Trimestre {match.group(1)} : " + re.search(r'\*\*Trimestre \d+\s*:\s*(.*?)\*\*', line).group(1)
        elif line.startswith("Jalon"):
            match = re.search(r'Jalon(s)?\s+([\d à]+).*?:\s*(.*)', line)
            if match:
                desc = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', match.group(3))
'''

setup_cached = r'''
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
lines = text.strip().split('\n')

trimestre_num_pattern = re.compile(r'\*\*Trimestre (\d+).*?\*\*')
trimestre_title_pattern = re.compile(r'\*\*Trimestre \d+\s*:\s*(.*?)\*\*')
jalon_detail_pattern = re.compile(r'Jalon(s)?\s+([\d à]+).*?:\s*(.*)')
md_link_pattern = re.compile(r'\[([^\]]+)\]\([^\)]+\)')

def run_cached():
    for line in lines:
        if "Trimestre" in line:
            match = trimestre_num_pattern.search(line)
            if match:
                current_trimester = f"Trimestre {match.group(1)} : " + trimestre_title_pattern.search(line).group(1)
        elif line.startswith("Jalon"):
            match = jalon_detail_pattern.search(line)
            if match:
                desc = md_link_pattern.sub(r'\1', match.group(3))
'''

stmt_uncached = "run_uncached()"
stmt_cached = "run_cached()"

time_uncached = timeit.timeit(stmt_uncached, setup=setup_uncached, number=100000)
time_cached = timeit.timeit(stmt_cached, setup=setup_cached, number=100000)

print(f"Uncached Time (100,000 runs): {time_uncached:.4f} seconds")
print(f"Cached Time (100,000 runs):   {time_cached:.4f} seconds")
print(f"Improvement: {(time_uncached - time_cached) / time_uncached * 100:.2f}%")
