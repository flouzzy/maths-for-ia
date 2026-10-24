# Exercice 7 : $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé

Soit $X$ un espace de Banach. Un sous-espace vectoriel $M \subset X$ est dense dans $X$ si et seulement si, pour toute forme linéaire continue $f \in X'$, $f \equiv 0$ sur $M \implies f = 0$ sur $X$.
Démontrer ce résultat (connu sous le nom de critère de densité par orthogonalité) à l'aide du théorème de Hahn-Banach.

## Correction

**Sens $\implies$ (Direct et élémentaire)**
Supposons $M$ dense dans $X$. Soit $f \in X'$ continue telle que $f_{|M} = 0$.
Soit $x \in X$. Comme $M$ est dense, il existe une suite $(x_n)$ dans $M$ telle que $x_n \to x$.
Par continuité de $f$, $f(x) = f(\lim x_n) = \lim f(x_n) = \lim 0 = 0$.
Donc $f = 0$ sur $X$.

**Sens $\impliedby$ (Hahn-Banach géométrique)**
Supposons que la seule forme s'annulant sur $M$ est la forme nulle. Procédons par contraposée : supposons que $M$ n'est pas dense, donc $\overline{M} \neq X$.
Alors il existe $x_0 \in X \setminus \overline{M}$.
$\overline{M}$ est un sous-espace vectoriel fermé, donc un convexe fermé.
$\{x_0\}$ est un singleton compact, convexe et disjoint de $\overline{M}$.
Par Hahn-Banach (forme stricte), il existe $f \in X'$ continue et $\alpha \in \mathbb{R}$ tels que $\forall m \in \overline{M}, f(m) < \alpha < f(x_0)$.
Puisque $M$ est un sous-espace vectoriel, $f(M)$ est un sous-espace de $\mathbb{R}$. S'il était non nul, il vaudrait $\mathbb{R}$ tout entier, ce qui contredirait $f(M) < \alpha$.
Donc $f(M) = \{0\}$, c'est-à-dire $f_{|M} = 0$.
Mais $f(x_0) > \alpha \ge 0$, donc $f \neq 0$ sur $X$.
Par contraposée, le critère est prouvé. $\blacksquare$
