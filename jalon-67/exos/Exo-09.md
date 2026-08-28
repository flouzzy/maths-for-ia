# Exercice 9 : Lien avec la mesure produit ★★★★★

**Énoncé :**
Démontrer que pour des fonctions mesurables positives étagées, l'intégrale double vérifie Beppo Levi.

**Correction :**
1. Soit $(f_n(x,y))$ une suite croissante de fonctions étagées positives sur $X \times Y$.
2. On s'intéresse à $I_n = \int_{X \times Y} f_n(x,y) d(\mu \otimes \nu)$.
3. Par définition de l'intégrale des fonctions étagées, c'est une somme finie de mesures de rectangles.
4. La croissance de la suite assure que $\lim I_n$ existe dans $[0, +\infty]$.
5. La limite de $f_n$ est mesurable positive $f(x,y)$. Par construction de l'intégrale de Lebesgue, $f$ est la limite d'une suite de fonctions étagées $s_m \le f$. Le supremum de $\int s_m$ est $\int f$. La correspondance stricte est assurée par Beppo Levi sur l'espace produit.
