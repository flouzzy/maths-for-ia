# Jalon 8 : Applications Linéaires, Noyau, Image et Théorème du Rang

Au cœur de l'algèbre linéaire, les applications linéaires représentent le langage naturel pour décrire les transformations qui préservent la structure des espaces vectoriels. Ce jalon est dédié à une compréhension approfondie de ces applications, de leurs propriétés fondamentales et des sous-espaces qui leur sont intrinsèquement liés : le noyau et l'image.

Une application linéaire, au-delà d'une simple fonction, est une transformation qui respecte l'addition des vecteurs et la multiplication par un scalaire. Elles sont les briques essentielles pour l'étude des endomorphismes, des isomorphismes et de la diagonalisation.

Le **noyau** (noté `ker f` ou `N(f)`) d'une application linéaire `f` est le sous-espace vectoriel de l'espace de départ constitué de tous les vecteurs que `f` transforme en le vecteur nul de l'espace d'arrivée. Il mesure, en quelque sorte, la "perte d'information" ou la "dégénérescence" de l'application : si le noyau est réduit au vecteur nul (ne contient que le vecteur nul), l'application est injective.

L'**image** (notée `Im f` ou `R(f)`) est le sous-espace vectoriel de l'espace d'arrivée composé de tous les vecteurs qui sont l'image d'au moins un vecteur de l'espace de départ. Elle représente l'ensemble des vecteurs que l'application peut "atteindre". Si l'image coïncide avec l'espace d'arrivée, l'application est surjective.

Le point culminant de cette exploration est le **Théorème du Rang**. Ce théorème fondamental établit une relation cruciale entre la dimension de l'espace de départ, la dimension du noyau (appelée *nullité*), et la dimension de l'image (appelée *rang*). Il s'énonce :

`dim(E) = dim(ker f) + dim(Im f)`

où `E` est l'espace de départ de l'application linéaire `f`. Plus qu'une simple formule, c'est un outil conceptuel puissant qui révèle une symétrie et une conservation de l'information dimensionnelle sous l'action d'une transformation linéaire. Il est la clé pour caractériser la bijectivité et pour comprendre les limitations et les capacités des applications linéaires. Ce jalon vous guidera à travers la compréhension et la manipulation de ces concepts, essentiels pour l'analyse des structures vectorielles et de leurs transformations.

---

## Exercices

Ce dossier contient les exercices suivants, couvrant les aspects théoriques et pratiques des applications linéaires, du noyau, de l'image et du théorème du rang.

*   [Exo-01] Vérification de la Linéarité - Difficulté: ★☆☆☆☆
*   [Exo-02] Détermination du Noyau et de l'Image pour des Applications Simples - Difficulté: ★★☆☆☆
*   [Exo-03] Calcul de Bases et de Dimensions du Noyau et de l'Image - Difficulté: ★★☆☆☆
*   [Exo-04] Application Directe du Théorème du Rang - Difficulté: ★★☆☆☆
*   [Exo-05] Injectivité, Surjectivité et Bijectivité via Noyau et Image - Difficulté: ★★★☆☆
*   [Exo-06] Représentation Matricielle et ses Liens avec Noyau/Image - Difficulté: ★★★☆☆
*   [Exo-07] Applications Linéaires sur des Espaces de Polynômes ou de Matrices - Difficulté: ★★★☆☆
*   [Exo-08] Démonstration de Propriétés du Noyau et de l'Image - Difficulté: ★★★★☆
*   [Exo-09] Théorème du Rang et Composition d'Applications Linéaires - Difficulté: ★★★★☆
*   [Exo-10] Problème de Synthèse : Analyse Complète d'une Application Linéaire - Difficulté: ★★★★★

---

## Travaux Pratiques (TPs)

Les TPs visent à approfondir la compréhension et la manipulation des concepts abordés, souvent avec une dimension de recherche ou d'exploration.

*   [TP-01] Exploration Géométrique des Transformations Linéaires en 2D et 3D
*   [TP-02] Algorithmes de Calcul de Bases du Noyau et de l'Image (numérique ou symbolique)
*   [TP-03] Démonstration Formelle et Variantes du Théorème du Rang
*   [TP-04] Étude des Isomorphismes et des Applications Linéaires Inversibles
*   [TP-05] Analyse d'Applications Linéaires Paramétrées et leurs Implications sur le Rang
