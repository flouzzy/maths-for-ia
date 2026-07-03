---
uuid: "exo-11-09"
title: "Exercice 9: Base anté-duale"
---
# Exercice 9: Base anté-duale (Difficulté $\star \star \star \star$)

## Énoncé
Soit $E = \mathbb{R}^3$. On donne la famille de formes linéaires $\mathcal{C}^* = (\phi_1, \phi_2, \phi_3)$ définies par :
$\phi_1(x, y, z) = x + y$, $\phi_2(x, y, z) = y + z$, $\phi_3(x, y, z) = x + z$.
Montrer que c'est une base de $E^*$ et trouver la base primale associée $\mathcal{C} = (e_1, e_2, e_3)$ telle que $\mathcal{C}^*$ en soit la base duale.

## Correction détaillée

1. **Vérification du caractère libre :**
   La matrice représentative des formes coordonnées par rapport à la base canonique duale est :
   $M = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix}$
   Calculons le déterminant par développement selon la première ligne :
   $\det(M) = 1(1 \times 1 - 1 \times 0) - 1(0 \times 1 - 1 \times 1) + 0 = 1 - (-1) = 2 \neq 0$.
   La famille est libre de cardinal 3, c'est une base de $E^*$.

2. **Recherche de la base primale :**
   Nous cherchons les vecteurs $e_i = (x_i, y_i, z_i)$ tels que $\phi_j(e_i) = \delta_{i,j}$.
   Pour $e_1 = (x_1, y_1, z_1)$ :
   - $\phi_1(e_1) = x_1 + y_1 = 1$
   - $\phi_2(e_1) = y_1 + z_1 = 0 \implies z_1 = -y_1$
   - $\phi_3(e_1) = x_1 + z_1 = 0 \implies x_1 = -z_1 = y_1$
   En remplaçant $x_1$ et $y_1$ dans la première : $y_1 + y_1 = 1 \implies y_1 = \frac{1}{2}$.
   Donc $x_1 = \frac{1}{2}$ et $z_1 = -\frac{1}{2}$. Le vecteur est $e_1 = (\frac{1}{2}, \frac{1}{2}, -\frac{1}{2})$.

3. **Calcul de $e_2$ et $e_3$ de façon identique :**
   - Pour $e_2$ : $\phi_1(e_2) = 0 \implies y = -x$, $\phi_2(e_2) = 1 \implies y + z = 1$, $\phi_3(e_2) = 0 \implies x = -z$.
     D'où $y = z = \frac{1}{2}$ et $x = -\frac{1}{2}$. $e_2 = (-\frac{1}{2}, \frac{1}{2}, \frac{1}{2})$.
   - Pour $e_3$ : $\phi_1(e_3) = 0 \implies y = -x$, $\phi_2(e_3) = 0 \implies z = -y$, $\phi_3(e_3) = 1 \implies x + z = 1$.
     D'où $x = z = \frac{1}{2}$ et $y = -\frac{1}{2}$. $e_3 = (\frac{1}{2}, -\frac{1}{2}, \frac{1}{2})$.

**Conclusion :**
La base anté-duale est explicite.
