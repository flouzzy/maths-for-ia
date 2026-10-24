# Exercice 10 : $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé

Démontrer que dans un espace de dimension infinie, la séparation stricte de deux convexes fermés disjoints n'est pas toujours possible (les deux ensembles étant non compacts).

## Correction

**Étape 1 : Contre-exemple dans $\ell^2$**
Considérons l'espace de Hilbert $E = \ell^2$.
Soit $e_n$ la base hilbertienne canonique (la suite avec un 1 à la position $n$ et 0 ailleurs).
Définissons les ensembles :
$A = \{ (x_n) \in \ell^2 \mid \forall n, x_n \ge 0, x_{2n} \ge 1 \}$
$B = \{ (x_n) \in \ell^2 \mid \forall n, x_n \ge 0, x_{2n+1} \ge 1, \sum_{k=1}^\infty x_{2k} x_{2k+1} \le \frac{1}{2} \}$

En réalité, un exemple plus classique de Dieudonné dans un Fréchet est utilisé, mais adaptons dans un Banach avec deux convexes fermés qui s'approchent asymptotiquement :
Soit $E = \ell^2(\mathbb{N})$.
Soit $A$ le plan vectoriel engendré par $u=(1, 1/2, 1/3, \dots)$ et des modifications locales.
Plus simplement, dans $c_0$ (suites tendant vers 0) :
$A = \{ x \in c_0 \mid x_{2n} = 0, n \ge 1 \}$
$B = \{ x \in c_0 \mid x_{2n-1} + n x_{2n} = 1 \}$
$A$ et $B$ sont des variétés affines fermées, donc convexes fermées.
L'intersection est vide car si $x \in A$, $x_{2n}=0$, donc pour $x \in B$ il faudrait $x_{2n-1} = 1$. Or $x \in c_0$ implique $x_k \to 0$, ce qui contredit $x_{2n-1}=1$. Donc $A \cap B = \emptyset$.
Cependant, la distance $d(A, B) = \inf ||a-b||_\infty = 0$ (en prenant $x_{2n}=1/n \to 0$ et $x_{2n-1}=0$).
Ainsi, ils ne peuvent être séparés *strictement* (car la marge $\epsilon$ serait nécessairement nulle). $\blacksquare$
