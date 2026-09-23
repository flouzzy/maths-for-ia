# Exercice 5 : Espace $L^2$ (★★★☆☆)

**Énoncé :**
Dans $L^2([0, 1])$, soit $V$ le sous-espace vectoriel des polynômes de degré inférieur ou égal à 1, i.e., $V = \text{Vect}(1, x)$.
Trouver la projection orthogonale de la fonction $f(x) = x^2$ sur le sous-espace $V$.

**Correction Détaillée :**
*Analyse de l'énoncé :* La projection $p$ est de la forme $ax + b$. La différence $f - p$ doit être orthogonale à $V$, donc orthogonale à $1$ et à $x$.

*Résolution pas-à-pas :*
On cherche $p(x) = ax + b$ tel que pour tout $g \in V$, $\langle f - p, g \rangle = 0$.
Il suffit de vérifier l'orthogonalité pour la base de $V$ :
1. $\langle f - p, 1 \rangle = 0$
2. $\langle f - p, x \rangle = 0$

Équation 1 :
$$ \int_0^1 (x^2 - (ax + b)) dx = 0 \implies \left[ \frac{x^3}{3} - a\frac{x^2}{2} - bx \right]_0^1 = 0 \implies \frac{1}{3} - \frac{a}{2} - b = 0 $$
Soit $3a + 6b = 2$.

Équation 2 :
$$ \int_0^1 x(x^2 - (ax + b)) dx = 0 \implies \int_0^1 (x^3 - ax^2 - bx) dx = 0 $$
$$ \left[ \frac{x^4}{4} - a\frac{x^3}{3} - b\frac{x^2}{2} \right]_0^1 = 0 \implies \frac{1}{4} - \frac{a}{3} - \frac{b}{2} = 0 $$
Soit $4a + 6b = 3$.

On a donc un système :
$4a + 6b = 3$
$3a + 6b = 2$

En soustrayant, $a = 1$.
En remplaçant, $3(1) + 6b = 2 \implies 6b = -1 \implies b = -1/6$.

La projection orthogonale est donc $p(x) = x - 1/6$.
