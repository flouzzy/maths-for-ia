# Jalon 10 : Changements de base, matrices de passage et matrices par blocs

## Présentation

Ce répertoire rassemble les ressources pratiques et théoriques associées au Jalon 10 du cursus "Mathématiques pour l'Intelligence Artificielle". Ce jalon est consacré à l'étude approfondie des changements de base dans les espaces vectoriels, à l'utilisation des matrices de passage, et à la manipulation des matrices par blocs. Ces concepts constituent le socle algébrique indispensable pour comprendre les transformations de représentations (Feature Engineering, espaces latents) au cœur de l'Intelligence Artificielle moderne.

## Exercices Théoriques (`exos/`)

Le sous-répertoire `exos/` propose une série de dix exercices, conçus selon une progression académique rigoureuse, visant à asseoir la maîtrise calculatoire et conceptuelle des notions abordées.

*   **`Exo-01.md` à `Exo-02.md` :** Manipulations directes des matrices de passage en petite dimension (calculs d'inverses, changements de coordonnées de vecteurs).
*   **`Exo-03.md` à `Exo-04.md` :** Formules de changement de base pour les endomorphismes, notions de matrices semblables et applications aux calculs de puissances de matrices.
*   **`Exo-05.md` à `Exo-06.md` :** Démonstrations théoriques sur les invariants de similitude (trace, déterminant) et premières manipulations d'endomorphismes particuliers (projecteurs, symétries) sous des bases adaptées.
*   **`Exo-07.md` à `Exo-08.md` :** Introduction aux matrices par blocs, opérations algébriques fondamentales (produit par blocs, inversion de matrices triangulaires supérieures par blocs).
*   **`Exo-09.md` à `Exo-10.md` :** Problèmes de synthèse complexes nécessitant l'articulation des changements de base continus et de la diagonalisation par blocs, préparant aux méthodes de réduction spectrale.

## Travaux Pratiques (`tp/`)

Le sous-répertoire `tp/` contient cinq travaux pratiques d'implémentation pure ("from scratch" en Python), visant à matérialiser les concepts algébriques par l'algorithmique, avec validation mathématique formelle.

*   **`TP-01.md` :** Implémentation de la structure de données matricielle et de l'algorithme d'inversion par pivot de Gauss.
*   **`TP-02.md` :** Algorithmique du changement de coordonnées d'un vecteur et validation de l'isomorphisme de représentation.
*   **`TP-03.md` :** Calcul de la matrice semblable d'un endomorphisme suite à un changement de base.
*   **`TP-04.md` :** Architecture algorithmique pour les opérations sur les matrices partitionnées par blocs.
*   **`TP-05.md` :** Application finale : utilisation d'un changement de base heuristique pour optimiser le calcul d'une transformation linéaire complexe sur un grand jeu de données.
