# Exercice 7 : Identité de polarisation pour les opérateurs auto-adjoints $\bigstar\bigstar\bigstar\bigstar\star$
## Énoncé
Soit $H$ un espace de Hilbert complexe. Soit $T \in \mathcal{L}(H)$ un opérateur auto-adjoint, c'est-à-dire tel que $T^* = T$.
1. Montrer que pour tout $x \in H$, le scalaire $\langle Tx, x \rangle$ est réel.
2. Soit $A \in \mathcal{L}(H)$ un opérateur quelconque. On suppose que pour tout $x \in H$, $\langle Ax, x \rangle = 0$. En développant $\langle A(x+y), x+y \rangle$ et $\langle A(x+iy), x+iy \rangle$, démontrer rigoureusement que $A = 0$ (l'opérateur nul).
3. Déduire de ce qui précède que si $T \in \mathcal{L}(H)$ est un opérateur tel que $\langle Tx, x \rangle$ est réel pour tout $x \in H$, alors $T$ est auto-adjoint. (Ce résultat est spécifiquement vrai pour les Hilbert complexes).

## Correction
1. Soit $x \in H$. Calculons le conjugué du scalaire $c = \langle Tx, x \rangle$ :
$$ \overline{\langle Tx, x \rangle} = \langle x, Tx \rangle $$
Par définition de l'adjoint :
$$ = \langle T^*x, x \rangle $$
Puisque l'opérateur $T$ est supposé auto-adjoint ($T^* = T$), nous avons :
$$ = \langle Tx, x \rangle $$
Ainsi, le scalaire est égal à son propre conjugué complexe ($\overline{c} = c$), ce qui prouve que $\langle Tx, x \rangle \in \mathbb{R}$ pour tout $x \in H$.

2. Hypothèse : $\forall x \in H, \langle Ax, x \rangle = 0$.
Soient $x, y \in H$. Évaluons cette propriété sur le vecteur $x+y$ :
$$ 0 = \langle A(x+y), x+y \rangle = \langle Ax + Ay, x+y \rangle $$
En développant par bilinéarité (ou plus précisément sesquilinéarité) :
$$ = \langle Ax, x \rangle + \langle Ax, y \rangle + \langle Ay, x \rangle + \langle Ay, y \rangle $$
Par hypothèse sur les vecteurs $x$ et $y$, le premier et le dernier terme sont nuls :
$$ = 0 + \langle Ax, y \rangle + \langle Ay, x \rangle + 0 $$
Nous obtenons la relation (1) : $\langle Ax, y \rangle + \langle Ay, x \rangle = 0$.

Maintenant, évaluons la propriété sur le vecteur $x + iy$ :
$$ 0 = \langle A(x+iy), x+iy \rangle = \langle Ax + iAy, x+iy \rangle $$
$$ = \langle Ax, x \rangle + \langle Ax, iy \rangle + \langle iAy, x \rangle + \langle iAy, iy \rangle $$
Rappelons que le scalaire sort du deuxième argument avec un conjugué (anti-linéarité à droite) : $\langle u, cv \rangle = \overline{c} \langle u, v \rangle$, donc $\langle Ax, iy \rangle = -i \langle Ax, y \rangle$.
Le scalaire sort du premier argument linéairement : $\langle cu, v \rangle = c \langle u, v \rangle$, donc $\langle iAy, x \rangle = i \langle Ay, x \rangle$.
Le dernier terme donne $\langle iAy, iy \rangle = i(-i) \langle Ay, y \rangle = \langle Ay, y \rangle = 0$.
En remplaçant :
$$ 0 = 0 - i\langle Ax, y \rangle + i\langle Ay, x \rangle + 0 $$
En divisant par $i$ (ou en multipliant par $-i$), on obtient la relation (2) : $-\langle Ax, y \rangle + \langle Ay, x \rangle = 0$.
En additionnant l'équation (1) et l'équation (2), nous avons :
$$ 2 \langle Ay, x \rangle = 0 \implies \langle Ay, x \rangle = 0 $$
Cette relation est vraie pour tous vecteurs $x, y \in H$. En fixant un vecteur $y$ quelconque, son image $Ay$ est orthogonale à tout vecteur $x \in H$. La seule possibilité est que $Ay = 0$.
Puisque $Ay = 0$ pour tout $y$, l'opérateur $A$ est l'opérateur nul, soit $A = 0$.

3. Supposons que $\langle Tx, x \rangle \in \mathbb{R}$ pour tout $x$.
Cela signifie que pour tout $x$, le scalaire est égal à son conjugué :
$$ \langle Tx, x \rangle = \overline{\langle Tx, x \rangle} = \langle x, Tx \rangle $$
En utilisant la définition de l'adjoint sur le terme de droite :
$$ \langle Tx, x \rangle = \langle T^*x, x \rangle $$
Par linéarité à gauche du produit scalaire, nous pouvons soustraire les deux termes :
$$ \langle Tx, x \rangle - \langle T^*x, x \rangle = 0 $$
$$ \langle (T - T^*)x, x \rangle = 0 $$
Posons l'opérateur $A = T - T^*$. Nous avons montré que $\forall x \in H, \langle Ax, x \rangle = 0$.
D'après le résultat rigoureusement démontré à la question 2, cela implique immédiatement que $A = 0$, et par conséquent :
$$ T - T^* = 0 \implies T = T^* $$
L'opérateur $T$ est donc bien auto-adjoint.
