---
uuid: "jalon-127"
title: "Théorème du représentant dans les RKHS"
year: 3
trimester: 11
tags:
  - math/analyse
  - ia/theorie
prev: "[[Jalon 126 (Noyaux définis positifs et RKHS).md]]"
next: "[[Jalon 128 (Flots de gradient).md]]"
---

# Jalon 127 : Théorème du représentant dans les RKHS

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous soyez un compositeur et que vous ayez accès à une infinité d'instruments de musique (un espace de dimension infinie). On vous demande de composer la chanson qui ressemble le plus à une série de 10 enregistrements que l'on vous donne (vos données).
    - On pourrait croire que pour trouver la meilleure chanson, vous devez essayer toutes les combinaisons d'instruments possibles. C'est un travail infini !
    - Le **Théorème du Représentant** dit une chose incroyable : la meilleure chanson sera **toujours** une simple combinaison des 10 enregistrements que l'on vous a donnés. Vous n'avez pas besoin d'inventer de nouveaux sons ; les exemples eux-mêmes contiennent toute l'information nécessaire pour construire la solution optimale.
- **Le "Pourquoi on a inventé ça" :** Pour pouvoir coder. Un ordinateur ne peut pas chercher une solution dans un espace de dimension infinie. Ce théorème prouve que l'on peut ramener un problème de dimension infinie à un simple calcul sur $N$ nombres (les coefficients associés à chaque donnée). C'est ce qui rend les méthodes à noyaux (comme les SVM) utilisables en pratique.
- **Visualisation :** On a un immense espace (un Hilbert). La solution optimale est un vecteur. Ce vecteur est "poussé" par les données vers un petit sous-espace plat. On n'a plus qu'à chercher la solution dans ce petit espace.

## 2. Formalisation

Soit $\mathcal{X}$ un ensemble et $H$ un RKHS de fonctions de $\mathcal{X}$ vers $\mathbb{R}$, associé au noyau $K$. On dispose de $n$ données $(x_i, y_i) \in \mathcal{X} \times \mathbb{R}$.

### A. Le Problème d'Optimisation

On cherche à minimiser une fonctionnelle de la forme :
$$J(f) = L(f(x_1), \dots, f(x_n)) + \Omega(\|f\|_H^2)$$
où :
- $L : \mathbb{R}^n \to \mathbb{R}$ est une fonction de perte quelconque (ex: Moindres carrés).
- $\Omega : \mathbb{R}_+ \to \mathbb{R}$ est une fonction de régularisation **strictement croissante**.

### B. Énoncé du Théorème du Représentant

> **Théorème (Kimeldorf & Wahba) :**
> Toute fonction $f^* \in H$ minimisant la fonctionnelle $J$ admet une décomposition de la forme :
> $$f^*(\cdot) = \sum_{i=1}^n \alpha_i K(x_i, \cdot)$$
> où $\alpha_1, \dots, \alpha_n \in \mathbb{R}$ sont des coefficients scalaires.

## 3. Démonstrations

### Démonstration du Théorème

1. **Décomposition de l'espace :** Soit $S = \text{vect}(K(x_1, \cdot), \dots, K(x_n, \cdot))$ le sous-espace de $H$ engendré par les fonctions du noyau aux points de données. C'est un espace de dimension finie (au plus $n$).
2. **Projection :** Toute fonction $f \in H$ peut se décomposer de manière unique (Jalon 103) en :
   $f = f_{||} + f_\perp$ avec $f_{||} \in S$ et $f_\perp \in S^\perp$.
3. **Calcul des valeurs de f aux points de données :**
   Grâce à la propriété de reproduction (Jalon 126) :
   $f(x_i) = \langle f, K(x_i, \cdot) \rangle = \langle f_{||} + f_\perp, K(x_i, \cdot) \rangle$.
   Comme $K(x_i, \cdot) \in S$, alors $\langle f_\perp, K(x_i, \cdot) \rangle = 0$.
   Donc $f(x_i) = f_{||}(x_i)$. La partie perpendiculaire n'influence pas la perte $L$.
4. **Calcul de la norme :**
   Par le théorème de Pythagore (Jalon 76) :
   $\|f\|_H^2 = \|f_{||}\|_H^2 + \|f_\perp\|_H^2 \ge \|f_{||}\|_H^2$.
5. **Comparaison des scores :**
   $J(f) = L(f(x_1), \dots) + \Omega(\|f\|_H^2) \ge L(f_{||}(x_1), \dots) + \Omega(\|f_{||}\|_H^2) = J(f_{||})$.
   L'égalité n'est atteinte que si $\|f_\perp\|=0$ (car $\Omega$ est strictement croissante).
6. **Conclusion :** Le minimum est nécessairement atteint pour une fonction $f_{||}$ appartenant à $S$. Toute solution $f^*$ est donc une combinaison linéaire des $K(x_i, \cdot)$.

## 4. Exercices d'Application

### Exercice 1 : Kernel Ridge Regression
**Énoncé :** Transformer le problème de minimisation $\sum (f(x_i) - y_i)^2 + \lambda \|f\|_H^2$ en un problème matriciel sur $\alpha$.
**Correction Détaillée :**
1. On pose $f(x) = \sum \alpha_j K(x_j, x)$. Alors $f(x_i) = \sum \alpha_j K(x_j, x_i) = (\mathbf{K}\alpha)_i$.
2. $\|f\|_H^2 = \langle \sum \alpha_i K(x_i, \cdot), \sum \alpha_j K(x_j, \cdot) \rangle = \sum \sum \alpha_i \alpha_j K(x_i, x_j) = \alpha^T \mathbf{K} \alpha$.
3. Le problème devient : $\min_{\alpha} \|\mathbf{K}\alpha - y\|^2 + \lambda \alpha^T \mathbf{K} \alpha$.
**Résultat :** En dérivant par rapport à $\alpha$, on trouve $(\mathbf{K} + \lambda I)\alpha = y$, soit $\alpha = (\mathbf{K} + \lambda I)^{-1} y$. C'est une simple inversion de matrice $n \times n$.

### Exercice 2 : Niveau Avancé (Cas des SVM)
**Énoncé :** Pourquoi les SVM sont-ils dits "parcimonieux" malgré le théorème du représentant ?
**Correction Détaillée :**
Le théorème dit que $f$ est une somme sur tous les $n$ points. Mais pour les SVM, les conditions KKT (Jalon 124) imposent que de nombreux $\alpha_i$ soient nuls. La solution "représentée" n'utilise en fait que les points les plus importants (les vecteurs supports).

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** Ce théorème est le lien final entre l'**Analyse Fonctionnelle** et l'**Algorithme Informatique**. Il garantit que l'on peut apprendre dans des espaces de caractéristiques de dimension infinie avec un budget de calcul fini.
- **Example Concret :**
    - **Scikit-Learn (SVC) :** Quand vous utilisez `SVC(kernel='rbf')`, la bibliothèque résout exactement le problème de dimension $N$ décrit par ce théorème.
    - **Processus Gaussiens :** La prédiction d'un GP en un nouveau point $x$ est une combinaison linéaire des observations passées, où les poids sont donnés par le noyau. C'est l'application directe de la forme du représentant.
    - **Large-scale Learning :** Comme le problème dépend de $N$, si $N$ est immense (millions), l'inversion de $\mathbf{K}$ devient impossible. On utilise alors des approximations (Nyström method) qui consistent à choisir une "base" plus petite que les $N$ données tout en respectant l'esprit du théorème.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 126 (Noyaux définis positifs et RKHS).md]], [[Jalon 103 (Espaces de Hilbert généraux).md]]
- **Concepts Futurs dépendants :** [[Jalon 137 (Preuve des bornes de généralisation universelles de Vapnik via la dimension VC.).md]], [[Jalon 140 (Classifieur de Bayes optimal).md]]
