# Exercice 6 : Opérateur de décalage (Shift)
$\bigstar$\bigstar$\bigstar\star\star$

**Énoncé :**
Soit $E = \ell^2(\mathbb{N})$ et l'opérateur de décalage à droite $S(x_0, x_1, \dots) = (0, x_0, x_1, \dots)$. Calculer $\|S\|$, est-il surjectif ?

**Correction Détaillée :**
1. Pour tout $x \in \ell^2$, $\|S(x)\|^2 = 0^2 + x_0^2 + x_1^2 + \dots = \|x\|^2$.
2. Ainsi, $S$ est une isométrie, et sa norme est exactement $\|S\| = 1$.
3. L'opérateur n'est pas surjectif : la suite $(1, 0, 0, \dots)$ n'est pas dans l'image de $S$ car toute suite image a 0 en première coordonnée.
