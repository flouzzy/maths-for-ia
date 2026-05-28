import os
import re

text = """
Année 1 : le socle des fondations et l'analyse réelle
Trimestre 1 : logique, ensembles et algèbre linéaire de base
L'objectif est de réapprendre la langue mathématique et de passer des tableaux de nombres à l'abstraction vectorielle.
Jalon 1 : Logique formelle, connecteurs, tables de vérité et calcul des propositions.
Jalon 2 : Méthodes de raisonnement (implication, contraposée, l'absurde, analyse-synthèse).
Jalon 3 : Quantification ($\\forall, \\exists$), ordre des quantificateurs et négation de propositions complexes.
Jalon 4 : Théorie des ensembles (ZFC), opérations sur les ensembles, ensembles des parties $\\mathcal{P}(E)$.
Jalon 5 : Applications, injections, surjections, bijections et composition de fonctions.
Jalon 6 : Relations d'équivalence, relations d'ordre, ensembles quotients et structures de base (groupes, anneaux, corps).
Jalon 7 : Espaces vectoriels abstraits, familles libres, familles génératrices et bases en dimension finie.
Jalon 8 : Applications linéaires, noyau ($\\ker$), image ($\\text{Im}$) et démonstration du théorème du rang.
Jalon 9 : Calcul matriciel, opérations, inversibilité et représentations des applications linéaires.
Jalon 10 : Changements de base, matrices de passage et matrices par blocs.
Jalon 11 : Formes linéaires, hyperplans, espace dual et orthogonalité en dimension finie.
Jalon 12 : Livrable IA T1 : Conception théorique d'un moteur de recherche sémantique par similarité cosinus (dualité et géométrie des espaces de plongement) et résolution d'un problème d'algèbre de l'X.
Trimestre 2 : analyse réelle, suites et séries de fonctions
Ce bloc demande du temps pour maîtriser la rigueur des limites et des approximations.
Jalon 13 : Structure de $\\mathbb{R}$, axiome de la borne supérieure et propriété d'Archimède.
Jalon 14 : Suites réelles et complexes, définitions rigoureuses des limites ($\\epsilon, N$) et critères de convergence.
Jalon 15 : Sous-suites, valeurs d'adhérence et preuve par séparation du théorème de Bolzano-Weierstrass.
Jalon 16 : Séries numériques à termes positifs, critères de comparaison, de d'Alembert et de Cauchy.
Jalon 17 : Séries absolument convergentes, semi-convergentes et produit de Cauchy de deux séries.
Jalon 18 : Continuité des fonctions d'une variable réelle, théorème des valeurs intermédiaires et compacité locale.
Jalon 19 : Dérivabilité, théorème de Rolle, théorème des accroissements finis et prolongement de la dérivée.
Jalon 20 : Dérivées successives, formules de Taylor-Lagrange, Taylor-Young et développements limités.
Jalon 21 : Suites de fonctions, étude de la convergence simple et de la convergence uniforme.
Jalon 22 : Séries de fonctions, convergence normale, théorèmes d'interversion limite-intégrale et limite-dérivée.
Jalon 23 : Séries entières, calcul du rayon de convergence (règle de d'Alembert-Cauchy) et propriétés de la somme.
Jalon 24 : Livrable IA T2 : Analyse mathématique des critères de convergence d'une régression polynomiale et résolution d'un problème d'analyse de l'ENS sur les interversions de limites.
Trimestre 3 : réduction des endomorphismes et espaces préhilbertiens
Ici, vous posez les bases géométriques nécessaires pour comprendre la structure des données.
Jalon 25 : Formes bilinéaires, formes sesquilinieaires, produit scalaire et inégalité de Cauchy-Schwarz.
Jalon 26 : Espaces euclidiens, orthogonalité, théorème de la projection orthogonale et algorithme de Gram-Schmidt.
Jalon 27 : Endomorphismes symétriques, adjoint d'un opérateur et matrices orthogonales.
Jalon 28 : Polynômes d'endomorphismes, idéaux annulateurs et démonstration du théorème de Cayley-Hamilton.
Jalon 29 : Éléments propres, polynôme caractéristique, sous-espaces propres et critères de diagonalisabilité.
Jalon 30 : Trigonalisation d'endomorphismes et décomposition de Dunford.
Jalon 31 : Introduction à la réduction de Jordan et structure des nilpotents.
Jalon 32 : Preuve complète du théorème spectral pour les endomorphismes symétriques.
Jalon 33 : Formes quadratiques, réduction de Gauss, base orthogonale et loi d'inertie de Sylvester.
Jalon 34 : Topologie élémentaire des espaces vectoriels normés (normes, équivalence des normes en dimension finie).
Jalon 35 : Caractérisation séquentielle des ouverts, des fermés et des compacts (Heine-Borel).
Jalon 36 : Livrable IA T3 : Écriture des équations de la décomposition en valeurs singulières (SVD) et application mathématique à la compression d'une matrice de pixels d'image.
Trimestre 4 : calcul différentiel et intégration de Riemann
Ce bloc reconstruit le calcul à plusieurs variables, moteur de l'apprentissage profond.
Jalon 37 : Intégrale de Riemann sur un segment, fonctions en escalier et propriétés de l'intégrale.
Jalon 38 : Théorème fondamental de l'analyse, primitives et techniques d'intégration (IPP, changement de variable).
Jalon 39 : Intégrales généralisées sur un intervalle quelconque et critères de convergence.
Jalon 40 : Intégrales dépendant d'un paramètre, théorèmes de continuité et de dérivation sous le signe $\\int$.
Jalon 41 : Équations différentielles linéaires du premier ordre et méthode de variation de la constante.
Jalon 42 : Équations différentielles linéaires du second ordre à coefficients constants.
Jalon 43 : Systèmes différentiels linéaires d'ordre 1 et calcul de l'exponentielle de matrice.
Jalon 44 : Fonctions de plusieurs variables, limites, continuité et topologie de $\\mathbb{R}^n$.
Jalon 45 : Différentiabilité, différentielle totale, dérivées partielles et gradient.
Jalon 46 : Matrice jacobienne, théorème de dérivation des fonctions composées (Chain Rule généralisée).
Jalon 47 : Dérivées partielles d'ordre deux, matrice hessienne et lemme de Schwarz.
Jalon 48 : Livrable IA T4 : Formalisation mathématique complète de la rétropropagation (Backpropagation) d'un réseau de neurones profond sous forme de produits de matrices jacobiennes.
Année 2 : l'abstraction topologique et la théorie de la mesure
Trimestre 5 : topologie générale et espaces métriques
Le premier grand saut dans l'abstraction pure. Prenez le temps de digérer chaque jalon.
Jalon 49 : Espaces topologiques généraux, définition par les ouverts, les fermés et les voisinages.
Jalon 50 : Opérateurs topologiques : intérieur, adhérence, frontière et ensembles denses.
Jalon 51 : Espaces métriques, topologie induite par une distance et distances équivalentes.
Jalon 52 : Applications continues entre espaces topologiques et définition fine des homéomorphismes.
Jalon 53 : Axiomes de séparation (notamment les espaces de Hausdorff).
Jalon 54 : Compacité générale (propriété de Borel-Lebesgue) et démonstration du théorème de Tychonoff pour les produits finis.
Jalon 55 : Connexité, connexité par arcs et étude des composantes connexes.
Jalon 56 : Espaces métriques complets, suites de Cauchy et théorème de prolongement des applications continues.
Jalon 57 : Théorème du point fixe de Banach (contractions) et application à l'existence locale des solutions d'EDP.
Jalon 58 : Théorème de Baire (les espaces de l'impossible) et applications aux fonctions continues nulle part dérivables.
Jalon 59 : Topologie des espaces de fonctions, convergence compacte et théorème d'Arzelà-Ascoli.
Jalon 60 : Livrable IA T5 : Preuve du théorème d'approximation universelle des réseaux de neurones (utilisation de la topologie de la convergence uniforme sur les compacts).
Trimestre 6 : théorie de la mesure et intégration de Lebesgue
Vous apprenez ici à mesurer des espaces de données complexes où l'intégration classique échoue.
Jalon 61 : Insuffisances de l'intégrale de Riemann, paradoxe de la fonction de Dirichlet.
Jalon 62 : Algèbres, $\\sigma$-algèbres (tribus), tribus engendrées et tribu de Borel sur $\\mathbb{R}$.
Jalon 63 : Définition axiomatique d'une mesure, mesures finies, $\\sigma$-finies et propriétés de continuité monotone.
Jalon 64 : Construction pas à pas de la mesure de Lebesgue sur $\\mathbb{R}$ via la mesure extérieure.
Jalon 65 : Fonctions mesurables, opérations élémentaires et approximation par des fonctions étagées.
Jalon 66 : Construction de l'intégrale de Lebesgue pour les fonctions mesurables positives.
Jalon 67 : Démonstration du théorème de convergence monotone (Beppo-Levi).
Jalon 68 : Lemme de Fatou et définition de l'intégrale pour les fonctions de signe quelconque (fonctions intégrables).
Jalon 69 : Démonstration complète du théorème de convergence dominée de Lebesgue.
Jalon 70 : Espaces mesurés produits, tribu produit et construction de la mesure produit.
Jalon 71 : Théorèmes de Fubini-Tonelli (fonctions positives) et de Fubini (fonctions intégrables).
Jalon 72 : Livrable IA T6 : Formalisation de la divergence de Kullback-Leibler entre deux distributions de probabilités continues complexes.
Trimestre 7 : espaces $L^p$ et analyse de Fourier
Ce bloc unifie vos compétences en télécommunications et la rigueur de la dimension infinie.
Jalon 73 : Définition des espaces $\\mathcal{L}^p$ et passage à l'espace quotient $L^p$ (égalité presque partout).
Jalon 74 : Inégalités fondamentales de l'analyse fonctionnelle : Hölder et Minkowski.
Jalon 75 : Preuve de la complétude des espaces $L^p$ (Théorème de Riesz-Fischer) : structure de Banach.
Jalon 76 : Propriétés géométriques de l'espace de Hilbert $L^2$, produit scalaire et identité du parallélogramme.
Jalon 77 : Densité des fonctions simples, des fonctions continues à support compact et des fonctions lisses dans $L^p$.
Jalon 78 : Séries de Fourier, calcul des coefficients, convergence ponctuelle (théorème de Dirichlet).
Jalon 79 : Convergence en moyenne quadratique des séries de Fourier et identité de Parseval.
Jalon 80 : Transformée de Fourier dans $L^1$, propriétés algébriques, Riemann-Lebesgue et produit de convolution.
Jalon 81 : Transformée de Fourier dans $L^2$, prolongement par densité et théorème d'isométrie de Plancherel.
Jalon 82 : Introduction à la théorie des distributions de Schwartz, espace des fonctions tests $\\mathcal{D}(\\mathbb{R})$.
Jalon 83 : Dérivation au sens des distributions, distribution de Dirac et introduction aux espaces de Sobolev $H^1(\\mathbb{R})$.
Jalon 84 : Livrable IA T7 : Création d'un module d'analyse spectrale pour l'extraction de caractéristiques audio à partir de la transformée de Fourier dans $L^2$.
Trimestre 8 : probabilités axiomatiques et statistiques fondamentales
Le cadre formel indispensable pour théoriser la gestion de l'incertitude.
Jalon 85 : Axiomes de Kolmogorov, espace de probabilité $(\\Omega, \\mathcal{F}, \\mathbb{P})$ comme un espace mesuré de masse 1.
Jalon 86 : Variables aléatoires vues comme des applications mesurables, loi d'une variable et mesure de probabilité image.
Jalon 87 : Intégration des variables aléatoires, espérance, variance et moments d'ordre supérieur.
Jalon 88 : Indépendance d'événements, de tribus et de variables aléatoires.
Jalon 89 : Lemmes de Borel-Cantelli (lois du tout ou rien) et applications aux comportements asymptotiques.
Jalon 90 : Les modes de convergence : presque sûre, en probabilité, dans $L^p$ et en loi (convergence étroite des mesures).
Jalon 91 : Inégalités de concentration : Markov, Chebyshev, Bienaymé, Chernoff et lemme de Hoeffding.
Jalon 92 : Démonstration rigoureuse de la loi forte des grands nombres.
Jalon 93 : Fonctions caractéristiques (transformée de Fourier de la loi) et théorème de continuité de Lévy.
Jalon 94 : Démonstration du théorème central limite (TCL) via les développements limités des fonctions caractéristiques.
Jalon 95 : Vecteurs gaussiens, loi normale multidimensionnelle, matrice de covariance et conditionnement gaussien.
Jalon 96 : Livrable IA T8 : Démonstration rigoureuse de la convergence de la fonction de perte Cross-Entropy vers l'information théorique de Shannon lors de l'entraînement des modèles de langage.
Année 3 : le niveau master (analyse fonctionnelle, géométrie et apprentissage)
Trimestre 9 : analyse fonctionnelle et théorie spectrale
Vous étudiez ici les espaces de dimension infinie où les fonctions deviennent de simples points.
Jalon 97 : Espaces de Banach, opérateurs linéaires continus entre Banach et topologie induite par la norme d'opérateur.
Jalon 98 : Théorème de Hahn-Banach (forme analytique), prolongement des formes linéaires sous-linéaires.
Jalon 99 : Théorème de Hahn-Banach (formes géométriques), séparation des ensembles convexes par des hyperplans.
Jalon 100 : Démonstration du théorème de Banach-Steinhaus (principe de la borne uniforme).
Jalon 101 : Théorème de l'application ouverte et théorème du graphe fermé.
Jalon 102 : Topologies faibles et faibles-*, compacité de la boule unité duale (Théorème de Banach-Alaoglu).
Jalon 103 : Espaces de Hilbert généraux, théorème de projection sur un convexe fermé et dualité de Riesz.
Jalon 104 : Bases hilbertiennes (systèmes orthonormés complets) et séparabilité des espaces de Hilbert.
Jalon 105 : Opérateurs adjoints, opérateurs compacts et propriétés de régularisation.
Jalon 106 : Théorème spectral pour les opérateurs compacts autoadjoints (décomposition en base hilbertienne d'éléments propres).
Jalon 107 : Introduction à la théorie des opérateurs non bornés et résolvante.
Jalon 108 : Livrable IA T9 : Modélisation de l'opérateur d'Attention de la structure Transformer sous forme d'opérateur intégral borné sur un espace hilbertien.
Trimestre 10 : géométrie différentielle et calcul des variations
L'étude des espaces courbes, base mathématique des architectures de réseaux sur graphes.
Jalon 109 : Topologie des sous-variétés de $\\mathbb{R}^n$, définition par des cartes locales, des paramétrages ou des équations.
Jalon 110 : Variétés différentielles abstraites, atlas, fonctions de transition (structures lisses).
Jalon 111 : Applications différentiables entre variétés, espace tangent en un point (dérivations) et fibré tangent $TM$.
Jalon 112 : Champs de vecteurs, flots locaux, courbes intégrales et crochet de Lie.
Jalon 113 : Tenseurs, formes différentielles, produit extérieur $\\wedge$ et calcul de la dérivée extérieure $d$.
Jalon 114 : Orientation des variétés et intégration des formes différentielles à support compact.
Jalon 115 : Démonstration du théorème de Stokes généralisé ($\\int_{\\partial M} \\omega = \\int_M d\\omega$).
Jalon 116 : Variétés riemanniennes, tenseur métrique, longueur des courbes et équations des géodésiques.
Jalon 117 : Calcul des variations, fonctionnelles, dérivation au sens de Gâteaux et équations d'Euler-Lagrange.
Jalon 118 : Conditions d'optimalité du second ordre pour les fonctionnelles et introduction aux multiplicateurs de Lagrange de dimension infinie.
Jalon 119 : Connexions avec les groupes de Lie, algèbres de Lie et symétries spatiales.
Jalon 120 : Livrable IA T10 : Formalisation mathématique des contraintes d'invariance par translation et rotation dans le cadre du Geometric Deep Learning (Graph Neural Networks).
Trimestre 11 : optimisation convexe avancée et méthodes à noyaux
Vous démontez ici les mécanismes physiques fine-tunant les grands modèles.
Jalon 121 : Ensembles convexes, fonctions convexes, épigraphe et propriétés de continuité des fonctions convexes.
Jalon 122 : Notion de sous-gradient, sous-différentiel $\\partial f(x)$ et optimisation de fonctions non lisses.
Jalon 123 : Problèmes d'optimisation sous contraintes, lagrangien et dualité de Lagrange (problème dual).
Jalon 124 : Conditions de Karush-Kuhn-Tucker (KKT) pour l'optimalité globale sous contraintes de qualification (Slater).
Jalon 125 : Opérateurs proximaux, théorème de Moreau-Yosida et algorithmes de descente de gradient proximale (ISTA/FISTA).
Jalon 126 : Noyaux définis positifs, théorème de Mercer et construction des espaces de Hilbert à noyau reproduisant (RKHS).
Jalon 127 : Démonstration du théorème du représentant dans les RKHS (réduction d'un problème d'optimisation infini à la dimension finie).
Jalon 128 : Flots de gradient (Gradient Flows) : interprétation continue de la descente de gradient comme courbe de plus grande pente dans l'espace des mesures.
Jalon 129 : Optimisation stochastique, algorithme de Robbins-Monro et critères de convergence presque sûre de la descente de gradient stochastique (SGD).
Jalon 130 : Régularisation implicite de la descente de gradient dans les modèles sur-paramétrés.
Jalon 131 : Algorithmes d'optimisation de second ordre en grande dimension (quasi-Newton, L-BFGS).
Jalon 132 : Livrable IA T11 : Codage complet en Python pur d'un solveur de point proximal sous contraintes KKT strictes pour l'élagage théorique (pruning) de réseaux profonds.
Trimestre 12 : théorie de l'apprentissage statistique
Le sommet du cursus : prouver mathématiquement qu'une machine est capable de généraliser.
Jalon 133 : Modèle PAC (Probably Approximately Correct), risque empirique vs risque réel.
Jalon 134 : Complexité des classes de fonctions, processus empiriques et inégalités de concentration maximales.
Jalon 135 : Complexité de Rademacher, symétrisation et bornes de généralisation basées sur Rademacher.
Jalon 136 : Théorie de Vapnik-Chervonenkis, fonction de croissance, dimension VC d'un espace d'hypothèses et lemme de Sauer.
Jalon 137 : Preuve des bornes de généralisation universelles de Vapnik via la dimension VC.
Jalon 138 : Inégalités de concentration avancées, inégalité de McDiarmid (différences bornées) et entropie de concentration.
Jalon 139 : Notion de stabilité algorithmique (Bousquet-Elisseeff) et son lien direct avec la capacité de généralisation.
Jalon 140 : Classifieur de Bayes optimal, fonctions de perte de substitution (Surrogate losses) et consistance de la minimisation du risque empirique.
Jalon 141 : Théorèmes de Glivenko-Cantelli généralisés pour les classes de fonctions VC.
Jalon 142 : Processus de décision de Markov (MDP) sur des espaces d'états continus, opérateurs de contraction de Bellman.
Jalon 143 : Théorie spectrale des graphes, laplacien combinatoire, laplacien normalisé et étude des coupures optimales (Min-Cut).
Jalon 144 : Le phénomène de double descente : analyse de la rupture de la théorie statistique classique (compromis biais-variance) dans le régime sur-paramétré.
Jalons 145 à 152 : Rédaction d'un article de recherche théorique de synthèse analysant les garanties de généralisation PAC d'une couche d'attention multi-têtes.
Jalons 153 à 156 : Synthèse finale, structuration de vos notes Obsidian en un graphe de connaissances unifié, et tournage de la série de vidéos YouTube clôturant le cycle d'études.
"""

TITLE_SPLIT_PATTERN = re.compile(r'[,(:]')

def extract_short_title(text):
    # Take part before first comma, parentheses, colon (if inside), or end
    # "Logique formelle, connecteurs" -> "Logique formelle"
    # "Quantification (\\forall, \\exists)" -> "Quantification"
    match = TITLE_SPLIT_PATTERN.split(text, 1)
    title = match[0].strip()
    return title

def parse_jalons(text_content):
    lines = text_content.strip().split('\n')

    current_year = ""
    current_trimester = ""
    trimester_context = ""

    jalons = []

    # Pre-compile regex for jalons
    jalon_pattern = re.compile(r'(Jalon[s]? [\d à]+) : (.+)')

    # First pass: collect all jalons
    for line in lines:
        line = line.strip()
        if line.startswith("Année"):
            current_year = line
        elif line.startswith("Trimestre"):
            current_trimester = line
            trimester_context = ""
        elif line.startswith("Jalon ") or line.startswith("Jalons "):
            # Parse jalon number and title
            match = jalon_pattern.match(line)
            if match:
                j_id = match.group(1)
                desc = match.group(2)
                
                short_title = extract_short_title(desc)
                if "Livrable IA" in short_title:
                    short_title = "Livrable IA"

                filename = f"{j_id} ({short_title}).md"
                filename = re.sub(r'[\\/*?:"<>|$]', '-', filename) # added $ to sanitize
                filename = filename.replace('--', '-') # avoid double dashes
                jalons.append({
                    'id': j_id,
                    'desc': desc,
                    'full_line': line,
                    'year': current_year,
                    'trimester': current_trimester,
                    'context': trimester_context,
                    'filename': filename
                })
        elif line:
            if current_trimester and not line.startswith("Jalon"):
                trimester_context += line + " "

    all_jalon_titles = [j['filename'] for j in jalons]
    return jalons, all_jalon_titles

def generate_links(jalon, jalons_list, index):
    links = []
    if index > 0:
        prev_j = jalons_list[index - 1]
        links.append(f"**Précédent** : [[{prev_j['filename'].replace('.md', '')}]]")
    if index < len(jalons_list) - 1:
        next_j = jalons_list[index + 1]
        links.append(f"**Suivant** : [[{next_j['filename'].replace('.md', '')}]]")
    return " | ".join(links)

# Special linking for Jalon 108
def get_custom_content(j_id):
    if "108" in j_id:
        # User requested specific links
        return "Notions liées : [[Jalon 76 (Propriétés géométriques de l'espace de Hilbert L^2)]] et [[Jalon 105 (Opérateurs adjoints)]]."
    return ""

def generate_concept_links(desc):
    links = []
    desc_lower = desc.lower()
    # Simple keyword matching to demonstrate interlinking
    if "hilbert" in desc_lower and "108" not in desc:
        links.append("[[Jalon 76 (Propriétés géométriques de l'espace de Hilbert L^2)]]")
    if "mesure" in desc_lower and not ("63" in desc or "64" in desc):
        links.append("[[Jalon 63 (Définition axiomatique d'une mesure)]]")
    if "topologi" in desc_lower and "49" not in desc:
        links.append("[[Jalon 49 (Espaces topologiques généraux)]]")
    if "vectoriel" in desc_lower and "7" not in desc:
        links.append("[[Jalon 7 (Espaces vectoriels abstraits)]]")
    
    if links:
        return "\\n**Concepts liés** : " + ", ".join(links) + "\\n"
    return ""

if __name__ == '__main__':
    jalons, all_jalon_titles = parse_jalons(text)

    cwd = os.getcwd()
    created_dirs = set()
    for i, jalon in enumerate(jalons):
        # Create a folder for the jalon
        folder_name = jalon['filename'].replace('.md', '')
        folder_path = os.path.join(cwd, folder_name)
        if folder_path not in created_dirs:
            os.makedirs(folder_path, exist_ok=True)
            created_dirs.add(folder_path)
        
        filepath = os.path.join(folder_path, jalon['filename'])
        
        content = f"# {jalon['id']}\n\n"
        content += f"**{jalon['year']}** > **{jalon['trimester']}**\n\n"
        
        if jalon['context'].strip():
            content += f"> *{jalon['context'].strip()}*\n\n"

        content += f"## Description\n{jalon['desc']}\n\n"

        # Custom links (Jalon 108 etc)
        custom_content = get_custom_content(jalon['id'])
        if custom_content:
            content += custom_content + "\n\n"

        # Automatic concept links
        content += generate_concept_links(jalon['desc'])

        content += "---\n"
        content += generate_links(jalon, jalons, i) + "\n"

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    print(f"Created {len(jalons)} notes in their respective folders in {cwd}")
