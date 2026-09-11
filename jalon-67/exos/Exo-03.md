# Exercice 3 : Croissance presque partout

**Difficulté :** $\bigstar$$\bigstar$$\star$$\star$$\star$

## Énoncé
Soit $f_n = \mathbf{1}_{[0, 1]} + \frac{1}{n} \mathbf{1}_{\mathbb{Q} \cap [0, 1]}$. Montrer que bien que la suite soit décroissante partout, on peut utiliser Beppo-Levi sur une suite modifiée presque partout.

## Correction Détaillée
1. La suite est décroissante, Beppo-Levi ne s'applique pas directement. Cependant, sur $[0, 1] \setminus \mathbb{Q}$ (de mesure de Lebesgue 1), $f_n(x) = 1$. Donc $f_n = 1$ presque partout.
2. On peut prendre $g_n = \mathbf{1}_{[0, 1]}$ constante (donc croissante au sens large) égale presque partout à $f_n$.
