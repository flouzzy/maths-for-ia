---
uuid: exo-05
title: Exercice 5 - Spectre du Graphe Complet
---

# Exercice 5 : Spectre du Graphe Complet

**Énoncé :**
Soit $K_n$ le graphe complet à $n$ sommets.
1. Écrire la matrice d'adjacence $A$ de $K_n$ et calculer ses valeurs propres.
2. En déduire la matrice laplacienne $L$ de $K_n$ et déterminer son spectre (l'ensemble de ses valeurs propres) ainsi que les multiplicités de chaque valeur propre. Ne faire aucune ellipse.

**Correction Détaillée :**

*   *Analyse de l'énoncé :* Dans un graphe complet, chaque sommet est relié à tous les autres. Il y a $n$ sommets, donc le degré de chaque sommet est $n-1$.
*   *Résolution pas-à-pas :*

**Partie 1 : Matrice d'adjacence $A$**
1. La matrice d'adjacence $A$ de $K_n$ est de taille $n \times n$. Comme chaque sommet est relié à tous les autres sauf à lui-même, tous les éléments hors diagonale valent $1$ et la diagonale vaut $0$.
   On peut l'écrire sous la forme :
   $$A = J - I_n$$
   où $J$ est la matrice dont tous les coefficients valent $1$, et $I_n$ est la matrice identité de taille $n$.

2. Calculons les valeurs propres de $J$. Le rang de $J$ est 1 (toutes les lignes sont identiques). Ainsi, $0$ est valeur propre de multiplicité géométrique au moins $n-1$. Comme $J$ est symétrique réelle, elle est diagonalisable, et la multiplicité algébrique de $0$ est $n-1$.
   La trace de $J$ vaut $n$ (somme des éléments diagonaux). La somme des valeurs propres est égale à la trace, donc l'autre valeur propre $\lambda$ vérifie $0 \times (n-1) + \lambda = n$, d'où $\lambda = n$.
   Le spectre de $J$ est donc $\{0 (\times n-1), n (\times 1)\}$.

3. Soit $x$ un vecteur propre de $J$ pour la valeur propre $\lambda_J$.
   On a $A x = (J - I_n) x = J x - x = \lambda_J x - x = (\lambda_J - 1) x$.
   Les valeurs propres de $A$ sont donc les valeurs propres de $J$ diminuées de $1$.
   Pour $\lambda_J = 0$, on obtient $\lambda_A = -1$ avec multiplicité $n-1$.
   Pour $\lambda_J = n$, on obtient $\lambda_A = n - 1$ avec multiplicité $1$.
   Le spectre de $A$ est donc $\{-1 (\times n-1), n-1 (\times 1)\}$.

**Partie 2 : Matrice laplacienne $L$**
1. Par définition, $L = D - A$, où $D$ est la matrice des degrés.
   Pour $K_n$, le degré de chaque sommet est $d = n - 1$. Ainsi, $D = (n-1)I_n$.
   On a donc $L = (n-1)I_n - A$.

2. Soit $x$ un vecteur propre de $A$ pour la valeur propre $\lambda_A$.
   $L x = ((n-1)I_n - A) x = (n-1)x - A x = (n-1)x - \lambda_A x = (n-1 - \lambda_A) x$.
   Les valeurs propres de $L$ sont de la forme $\lambda_L = n - 1 - \lambda_A$.

3. Calculons le spectre de $L$ à partir de celui de $A$ :
   - Pour la valeur propre $\lambda_A = -1$ (multiplicité $n-1$) :
     $\lambda_L = n - 1 - (-1) = n$. Donc la valeur propre $n$ a pour multiplicité $n-1$.
   - Pour la valeur propre $\lambda_A = n-1$ (multiplicité $1$) :
     $\lambda_L = n - 1 - (n - 1) = 0$. Donc la valeur propre $0$ a pour multiplicité $1$.

4. Le spectre du laplacien $L$ du graphe complet $K_n$ est donc constitué de la valeur propre $0$ (multiplicité $1$) et de la valeur propre $n$ (multiplicité $n-1$).
