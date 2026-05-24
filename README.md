# Jalons de Mathématiques pour l'Intelligence Artificielle

Ce dépôt contient un script permettant de générer automatiquement un ensemble de fiches de notes (au format Markdown) destinées à être utilisées comme coffre (*vault*) dans [Obsidian](https://obsidian.md/). Ce projet modélise un programme de mathématiques sur 3 ans, spécifiquement orienté vers les fondements théoriques de l'intelligence artificielle.

## Objectif du Projet

Le projet génère des "Jalons" d'apprentissage répartis sur trois années de cursus :
- **Année 1 : Le socle des fondations et l'analyse réelle** (Logique, algèbre linéaire, analyse réelle, réduction d'endomorphismes, etc.)
- **Année 2 : L'abstraction topologique et la théorie de la mesure** (Topologie générale, théorie de la mesure, intégration de Lebesgue, espaces $L^p$, probabilités axiomatiques, etc.)
- **Année 3 : Le niveau master (analyse fonctionnelle, géométrie et apprentissage)** (Analyse fonctionnelle, géométrie différentielle, optimisation convexe avancée, théorie de l'apprentissage statistique, etc.)

Ces notes sont structurées et interconnectées. Elles incluent des liens de navigation vers les jalons précédents et suivants, ainsi que des liens sémantiques automatiques entre les concepts mathématiques transversaux.

- **`Tableau de bord.md`** : Un index global interactif (sous forme de checklist) permettant de suivre votre progression à travers tout le cursus. Chaque jalon y est lié pour une navigation rapide.

## Fichiers Principaux

- **`generate_jalons.py`** : C'est le script principal du projet, écrit en Python. Il contient le texte source du programme complet, le découpe par années et trimestres, et génère pour chaque jalon un dossier dédié contenant la fiche principale (par exemple : `Jalon 1 (Logique formelle)/Jalon 1 (Logique formelle).md`). Cette structure permet d'organiser proprement chaque jalon en y ajoutant des ressources complémentaires (exercices, schémas, notes personnelles) sans encombrer la racine du dépôt.
- **`test_generate_jalons.py`** : Contient la suite de tests unitaires du projet, permettant de vérifier la logique de création de liens inter-concepts (`generate_concept_links`) définie dans le script principal.
- **`generate_jalons.ps1`, `generate_index.ps1`, `git-sync.ps1`** : Scripts utilitaires PowerShell prévus pour une utilisation sous environnement Windows ou via `pwsh` pour générer des index ou automatiser certaines tâches Git.

## Historique d'enrichissement IA

- **Jalon 1** : Logique formelle, connecteurs, tables de vérité et calcul des propositions. (Enrichi le 2026-05-24)
- **Jalon 2** : Méthodes de raisonnement (implication, contraposée, l'absurde, analyse-synthèse). (Enrichi le 2026-05-24)
- **Jalon 3** : Quantification ($\forall, \exists$), ordre des quantificateurs et négation de propositions complexes. (Enrichi le 2026-05-24)
- **Jalon 4** : Théorie des ensembles (ZFC), opérations sur les ensembles, ensembles des parties $\mathcal{P}(E)$. (Enrichi le 2026-05-24)
- **Jalon 5** : Applications, injections, surjections, bijections et composition de fonctions. (Enrichi le 2026-05-24)
- **Jalon 6** : Relations d'équivalence, relations d'ordre, ensembles quotients et structures de base (groupes, anneaux, corps). (Enrichi le 2026-05-24)
- **Jalon 7** : Espaces vectoriels abstraits, familles libres, familles génératrices et bases en dimension finie. (Enrichi le 2026-05-24)
- **Jalon 8** : Applications linéaires, noyau (ker), image (Im) et démonstration du théorème du rang. (Enrichi le 2026-05-24)
- **Jalon 9** : Calcul matriciel, opérations, inversibilité et représentations des applications linéaires. (Enrichi le 2026-05-24)
- **Jalon 10** : Changements de base, matrices de passage et matrices par blocs. (Enrichi le 2026-05-24)
- **Jalon 11** : Formes linéaires, hyperplans, espace dual et orthogonalité en dimension finie. (Enrichi le 2026-05-24)
- **Jalon 12** : Livrable IA T1 : Conception théorique d'un moteur de recherche sémantique par similarité cosinus (dualité et géométrie des espaces de plongement) et résolution d'un problème d'algèbre de l'X. (Enrichi le 2026-05-24)
- **Jalon 13** : Structure de $\mathbb{R}$, axiome de la borne supérieure et propriété d'Archimède. (Enrichi le 2026-05-24)
- **Jalon 14** : Suites réelles et complexes, définitions rigoureuses des limites ($\epsilon, N$) et critères de convergence. (Enrichi le 2026-05-24)
- **Jalon 15** : Sous-suites, valeurs d'adhérence et preuve par séparation du théorème de Bolzano-Weierstrass. (Enrichi le 2026-05-24)
- **Jalon 16** : Séries numériques à termes positifs, critères de comparaison, de d'Alembert et de Cauchy. (Enrichi le 2026-05-24)
- **Jalon 17** : Séries absolument convergentes, semi-convergentes et produit de Cauchy de deux séries. (Enrichi le 2026-05-24)
- **Jalon 18** : Continuité des fonctions d'une variable réelle, théorème des valeurs intermédiaires et compacité locale. (Enrichi le 2026-05-24)
- **Jalon 19** : Dérivabilité, théorème de Rolle, théorème des accroissements finis et prolongement de la dérivée. (Enrichi le 2026-05-24)
- **Jalon 20** : Dérivées successives, formules de Taylor-Lagrange, Taylor-Young et développements limités. (Enrichi le 2026-05-24)
- **Jalon 21** : Suites de fonctions, étude de la convergence simple et de la convergence uniforme. (Enrichi le 2026-05-24)
- **Jalon 22** : Séries de fonctions, convergence normale, théorèmes d'interversion limite-intégrale et limite-dérivée. (Enrichi le 2026-05-24)
- **Jalon 23** : Séries entières, calcul du rayon de convergence (règle de d'Alembert-Cauchy) et propriétés de la somme. (Enrichi le 2026-05-24)
- **Jalon 24** : Livrable IA T2 : Analyse mathématique des critères de convergence d'une régression polynomiale et résolution d'un problème d'analyse de l'ENS sur les interversions de limites. (Enrichi le 2026-05-24)
- **Jalon 25** : Formes bilinéaires, formes sesquilinieaires, produit scalaire et inégalité de Cauchy-Schwarz. (Enrichi le 2026-05-24)
- **Jalon 26** : Espaces euclidiens, orthogonalité, théorème de la projection orthogonale et algorithme de Gram-Schmidt. (Enrichi le 2026-05-24)
- **Jalon 27** : Endomorphismes symétriques, adjoint d'un opérateur et matrices orthogonales. (Enrichi le 2026-05-24)
- **Jalon 28** : Polynômes d'endomorphismes, idéaux annulateurs et théorème de Cayley-Hamilton. (Enrichi le 2026-05-24)
- **Jalon 29** : Éléments propres, polynôme caractéristique, sous-espaces propres et critères de diagonalisabilité. (Enrichi le 2026-05-24)
- **Jalon 30** : Trigonalisation d'endomorphismes et décomposition de Dunford. (Enrichi le 2026-05-24)
- **Jalon 31** : Introduction à la réduction de Jordan et structure des nilpotents. (Enrichi le 2026-05-24)
- **Jalon 32** : Preuve complète du théorème spectral pour les endomorphismes symétriques. (Enrichi le 2026-05-24)
- **Jalon 33** : Formes quadratiques, réduction de Gauss, base orthogonale et loi d'inertie de Sylvester. (Enrichi le 2026-05-24)
- **Jalon 34** : Topologie élémentaire des espaces vectoriels normés (normes, équivalence des normes en dimension finie). (Enrichi le 2026-05-24)
- **Jalon 35** : Caractérisation séquentielle des ouverts, des fermés et des compacts (Heine-Borel). (Enrichi le 2026-05-24)
- **Jalon 36** : Livrable IA T3 : Écriture des équations de la décomposition en valeurs singulières (SVD) et application mathématique à la compression d'une matrice de pixels d'image. (Enrichi le 2026-05-24)
- **Jalon 37** : Intégrale de Riemann sur un segment, fonctions en escalier et propriétés de l'intégrale. (Enrichi le 2026-05-24)
- **Jalon 38** : Théorème fondamental de l'analyse, primitives et techniques d'intégration (IPP, changement de variable). (Enrichi le 2026-05-24)
- **Jalon 39** : Intégrales généralisées sur un intervalle quelconque et critères de convergence. (Enrichi le 2026-05-24)
- **Jalon 40** : Intégrales dépendant d'un paramètre, théorèmes de continuité et de dérivation sous le signe $\int$. (Enrichi le 2026-05-24)
- **Jalon 41** : Équations différentielles linéaires du premier ordre et méthode de variation de la constante. (Enrichi le 2026-05-24)
- **Jalon 42** : Équations différentielles linéaires du second ordre à coefficients constants. (Enrichi le 2026-05-24)
- **Jalon 43** : Systèmes différentiels linéaires d'ordre 1 et calcul de l'exponentielle de matrice. (Enrichi le 2026-05-24)
- **Jalon 44** : Fonctions de plusieurs variables, limites, continuité et topologie de $\mathbb{R}^n$. (Enrichi le 2026-05-24)
- **Jalon 45** : Différentiabilité, différentielle totale, dérivées partielles et gradient. (Enrichi le 2026-05-24)
- **Jalon 46** : Matrice jacobienne, théorème de dérivation des fonctions composées (Chain Rule généralisée). (Enrichi le 2026-05-24)
- **Jalon 47** : Dérivées partielles d'ordre deux, matrice hessienne et lemme de Schwarz. (Enrichi le 2026-05-24)
- **Jalon 48** : Livrable IA T4 : Formalisation mathématique complète de la rétropropagation (Backpropagation) d'un réseau de neurones profond sous forme de produits de matrices jacobiennes. (Enrichi le 2026-05-24)
- **Jalon 49** : Espaces topologiques généraux, définition par les ouverts, les fermés et les voisinages. (Enrichi le 2026-05-24)
- **Jalon 50** : Opérateurs topologiques : intérieur, adhérence, frontière et ensembles denses. (Enrichi le 2026-05-24)
- **Jalon 51** : Espaces métriques, topologie induite par une distance et distances équivalentes. (Enrichi le 2026-05-24)
- **Jalon 52** : Applications continues entre espaces topologiques et définition fine des homéomorphismes. (Enrichi le 2026-05-24)
- **Jalon 53** : Axiomes de séparation (notamment les espaces de Hausdorff). (Enrichi le 2026-05-24)
- **Jalon 54** : Compacité générale (propriété de Borel-Lebesgue) et démonstration du théorème de Tychonoff pour les produits finis. (Enrichi le 2026-05-24)
- **Jalon 55** : Connexité, connexité par arcs et étude des composantes connexes. (Enrichi le 2026-05-24)
- **Jalon 56** : Espaces métriques complets, suites de Cauchy et théorème de prolongement des applications continues. (Enrichi le 2026-05-24)
- **Jalon 57** : Théorème du point fixe de Banach (contractions) et application à l'existence locale des solutions d'EDP. (Enrichi le 2026-05-24)
- **Jalon 58** : Théorème de Baire (les espaces de l'impossible) et applications aux fonctions continues nulle part dérivables. (Enrichi le 2026-05-24)
- **Jalon 59** : Topologie des espaces de fonctions, convergence compacte et théorème d'Arzelà-Ascoli. (Enrichi le 2026-05-24)
- **Jalon 60** : Livrable IA T5 : Preuve du théorème d'approximation universelle des réseaux de neurones (utilisation de la topologie de la convergence uniforme sur les compacts). (Enrichi le 2026-05-24)
- **Jalon 61** : Insuffisances de l'intégrale de Riemann et motivation pour la mesure de Lebesgue. (Enrichi le 2026-05-24)
- **Jalon 62** : Algèbres, tribus (sigma-algèbres) et classes monotones. (Enrichi le 2026-05-24)
- **Jalon 63** : Définition axiomatique d'une mesure, mesures de probabilité et propriétés de continuité monotone. (Enrichi le 2026-05-24)
- **Jalon 64** : Construction pas à pas de la mesure de Lebesgue sur $\mathbb{R}$ via la mesure extérieure. (Enrichi le 2026-05-24)
- **Jalon 65** : Fonctions mesurables, opérations sur les fonctions mesurables et fonctions simples. (Enrichi le 2026-05-24)
- **Jalon 66** : Construction de l'intégrale de Lebesgue pour les fonctions mesurables positives. (Enrichi le 2026-05-24)
- **Jalon 67** : Démonstration du théorème de convergence monotone (Beppo Levi). (Enrichi le 2026-05-24)
- **Jalon 68** : Lemme de Fatou et définition de l'intégrale pour les fonctions de signe quelconque. (Enrichi le 2026-05-24)
- **Jalon 69** : Démonstration complète du théorème de convergence dominée de Lebesgue. (Enrichi le 2026-05-24)
- **Jalon 70** : Espaces mesurés produits et construction de la mesure produit. (Enrichi le 2026-05-24)
- **Jalon 71** : Théorèmes de Fubini-Tonelli pour l'interversion des intégrales. (Enrichi le 2026-05-24)
- **Jalon 72** : Livrable IA T6 : Formalisation de la divergence de Kullback-Leibler entre deux distributions de probabilités continues complexes. (Enrichi le 2026-05-24)
- **Jalon 73** : Définition des espaces $\mathcal{L}^p$ et passage à l'espace quotient $L^p$. (Enrichi le 2026-05-24)
- **Jalon 74** : Inégalités fondamentales de l'analyse fonctionnelle : Hölder, Minkowski et Jensen. (Enrichi le 2026-05-24)
- **Jalon 75** : Preuve de la complétude des espaces $L^p$ (Théorème de Riesz-Fischer). (Enrichi le 2026-05-24)
- **Jalon 76** : Propriétés géométriques de l'espace de Hilbert $L^2$. (Enrichi le 2026-05-24)
- **Jalon 77** : Densité des fonctions simples et des fonctions continues dans $L^p$. (Enrichi le 2026-05-24)
- **Jalon 78** : Séries de Fourier : coefficients de Fourier et convergence dans $L^2$. (Enrichi le 2026-05-24)
- **Jalon 79** : Convergence en moyenne quadratique des séries de Fourier et identité de Parseval. (Enrichi le 2026-05-24)
- **Jalon 80** : Transformée de Fourier dans $L^1$, propriétés et théorème d'inversion. (Enrichi le 2026-05-24)
- **Jalon 81** : Transformée de Fourier dans $L^2$, isométrie de Plancherel. (Enrichi le 2026-05-24)
- **Jalon 82** : Introduction à la théorie des distributions de Schwartz. (Enrichi le 2026-05-24)
- **Jalon 83** : Dérivation au sens des distributions. (Enrichi le 2026-05-24)
- **Jalon 84** : Livrable IA T7 : Création d'un module d'analyse spectrale pour l'extraction de caractéristiques audio à partir de la transformée de Fourier dans $L^2$. (Enrichi le 2026-05-24)
- **Jalon 85** : Axiomes de Kolmogorov et espace de probabilité $(\Omega, \mathcal{F}, P)$. (Enrichi le 2026-05-24)
- **Jalon 86** : Variables aléatoires vues comme des applications mesurables. (Enrichi le 2026-05-24)
- **Jalon 87** : Intégration des variables aléatoires et définition de l'espérance mathématique. (Enrichi le 2026-05-24)
- **Jalon 88** : Indépendance d'événements, de tribus et de variables aléatoires. (Enrichi le 2026-05-24)
- **Jalon 89** : Lemmes de Borel-Cantelli et loi du zéro-un de Kolmogorov. (Enrichi le 2026-05-24)
- **Jalon 90** : Les modes de convergence : presque sûre, en probabilité, dans $L^p$ et en loi. (Enrichi le 2026-05-24)
- **Jalon 91** : Inégalités de concentration : Markov, Tchebychev et Chernoff. (Enrichi le 2026-05-24)
- **Jalon 92** : Démonstration rigoureuse de la loi forte des grands nombres. (Enrichi le 2026-05-24)
- **Jalon 93** : Fonctions caractéristiques : définition, propriétés et injectivité. (Enrichi le 2026-05-24)
- **Jalon 94** : Démonstration du théorème central limite. (Enrichi le 2026-05-24)
- **Jalon 95** : Vecteurs gaussiens, matrice de covariance et caractérisation par les combinaisons linéaires. (Enrichi le 2026-05-24)
- **Jalon 96** : Livrable IA T8 : Démonstration rigoureuse de la convergence de la fonction de perte Cross-Entropy vers l'information théorique de Shannon lors de l'entraînement des modèles de langage. (Enrichi le 2026-05-24)
- **Jalon 97** : Espaces de Banach, normes d'opérateurs et espace dual. (Enrichi le 2026-05-24)

## Comment Générer les Notes

Assurez-vous d'avoir Python 3 installé. Pour générer ou mettre à jour l'ensemble des notes Markdown, il vous suffit d'exécuter le script Python depuis la racine du dépôt :

```bash
python3 generate_jalons.py
```

Une fois la commande exécutée, le script créera de nombreux dossiers correspondant au cursus. Vous pouvez ensuite ouvrir le répertoire racine du projet directement dans Obsidian pour consulter et lier vos notes. Obsidian détectera automatiquement les fichiers Markdown à l'intérieur des dossiers.

## Comment Lancer les Tests

Le projet utilise le framework standard `unittest` de Python. Pour lancer les tests et s'assurer que le script de liens conceptuels fonctionne correctement sans introduire de régression, exécutez la commande suivante :

```bash
python3 -m unittest test_generate_jalons.py
```
