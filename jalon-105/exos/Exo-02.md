# Exercice 2 : Propriété multiplicative de l'adjoint $\bigstar\star\star\star\star$
## Énoncé
Soient $H$ un espace de Hilbert, et $S, T \in \mathcal{L}(H)$ deux opérateurs linéaires continus.
Démontrer rigoureusement que $(ST)^* = T^* S^*$.

## Correction
Soient $x, y \in H$. Par définition de l'opérateur adjoint, nous avons pour tout opérateur linéaire $A$ et tout couple de vecteurs $(u, v)$ : $\langle Au, v \rangle = \langle u, A^*v \rangle$.
Appliquons cela à l'opérateur composé $ST$.
1. Partons du membre de gauche de l'égalité définissant $(ST)^*$ :
$$ \langle (ST)x, y \rangle = \langle S(Tx), y \rangle $$
2. Appliquons la définition de l'adjoint de $S$ en considérant $Tx$ comme le vecteur d'entrée $u$ :
$$ \langle S(Tx), y \rangle = \langle Tx, S^*y \rangle $$
3. Appliquons maintenant la définition de l'adjoint de $T$, en considérant $x$ comme le vecteur $u$ et $S^*y$ comme le vecteur $v$ :
$$ \langle Tx, S^*y \rangle = \langle x, T^*(S^*y) \rangle $$
$$ = \langle x, (T^*S^*)y \rangle $$
4. En rassemblant l'ensemble de la chaîne d'égalités, nous obtenons pour tout $x, y \in H$ :
$$ \langle (ST)x, y \rangle = \langle x, (T^*S^*)y \rangle $$
Par définition de l'unicité de l'opérateur adjoint (qui stipule que si $\langle Ax, y \rangle = \langle x, By \rangle$ pour tout $x,y$, alors $A^* = B$), on conclut immédiatement que :
$$ (ST)^* = T^* S^* $$
