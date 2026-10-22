# Exercice 10 : Théorème de Riesz (compacité de la boule)
$\bigstar$\bigstar$\bigstar$\bigstar$\bigstar$

**Énoncé :**
Soit $E$ un espace vectoriel normé dont la boule unité fermée $B$ est compacte. En utilisant le fait qu'il existe un $\epsilon$-réseau fini, prouver que la dimension de $E$ est finie.

**Correction Détaillée :**
1. Supposons la dimension infinie. On construit une suite $(x_n)$ dans $B$ telle que $\|x_n - x_m\| \ge 1/2$ pour tout $n \neq m$ (lemme de Riesz).
2. On choisit $x_1$ de norme 1. Soit $F_1 = \text{Vect}(x_1)$. Il existe $x_2$ de norme 1 tel que $d(x_2, F_1) \ge 1/2$.
3. On itère pour obtenir la suite. Cette suite n'admet aucune sous-suite de Cauchy car les distances mutuelles sont $\ge 1/2$.
4. Cela contredit la compacité séquentielle de $B$. Donc la dimension doit être finie.
