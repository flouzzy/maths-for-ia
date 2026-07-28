---
uuid: "jalon-27-exo-08"
title: "Exercice 08 : Matrice de passage entre bases orthonormées"
---
# Exercice 08 : Racine carrée symétrique définie positive

**Difficulté :** ★★★★☆

## Énoncé

Soit $S$ un endomorphisme symétrique défini positif (toutes ses valeurs propres sont strictement positives). Montrer qu'il existe un unique endomorphisme symétrique défini positif $R$ tel que $R^2 = S$.

## Démonstration sans ellipse

**Existence :**
D'après le théorème spectral, il existe une base orthonormée $(e_1, \dots, e_n)$ de vecteurs propres de $S$ avec les valeurs propres associées $\lambda_1, \dots, \lambda_n$. Comme $S$ est défini positif, $\lambda_i > 0$ pour tout $i$.
On définit l'endomorphisme $R$ par $R(e_i) = \sqrt{\lambda_i} e_i$ pour tout $i$.
Par construction, $R$ est diagonalisable dans la base orthonormée $(e_1, \dots, e_n)$ avec des valeurs propres $\sqrt{\lambda_i} > 0$. Donc $R$ est symétrique et défini positif.
De plus, $R^2(e_i) = R(\sqrt{\lambda_i} e_i) = \sqrt{\lambda_i} R(e_i) = (\sqrt{\lambda_i})^2 e_i = \lambda_i e_i = S(e_i)$.
Les endomorphismes $R^2$ et $S$ coïncident sur une base, ils sont donc égaux : $R^2 = S$.

**Unicité :**
Soit $R'$ un autre endomorphisme symétrique défini positif tel que $(R')^2 = S$.
Comme $R'$ et $S$ commutent ($R' \circ S = R' \circ (R')^2 = (R')^3 = (R')^2 \circ R' = S \circ R'$), $R'$ conserve les sous-espaces propres de $S$.
Soit $E_\lambda$ le sous-espace propre de $S$ pour la valeur propre $\lambda$.
La restriction $r'$ de $R'$ à $E_\lambda$ est symétrique définie positive et vérifie $(r')^2 = \lambda \operatorname{Id}$.
Les valeurs propres de $r'$ doivent être racines de $X^2 - \lambda$. Comme $r'$ est défini positif, sa seule valeur propre possible est $\sqrt{\lambda}$.
Puisque $r'$ est symétrique avec une unique valeur propre $\sqrt{\lambda}$, $r'$ est obligatoirement l'homothétie de rapport $\sqrt{\lambda}$ sur $E_\lambda$.
Ainsi, $R'$ agit exactement comme $R$ sur chaque sous-espace propre de $S$.
Comme $E$ est somme directe orthogonale de ces sous-espaces, $R' = R$. L'unicité est prouvée. $\blacksquare$
