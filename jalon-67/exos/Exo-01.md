# Exercice 1 : Continuité croissante de la mesure

**Difficulté :** $\star$

**Énoncé :**
Montrer que si $A_n$ est une suite croissante de mesurables, $\mu(\cup_n A_n) = \lim_n \mu(A_n)$ en utilisant le théorème de Beppo Levi.

**Correction :**
Soit $f_n = \mathbb{I}_{A_n}$. Puisque $A_n \subset A_{n+1}$, $f_n \leq f_{n+1}$. De plus, pour $x \in X$, $f_n(x) \to \mathbb{I}_{A}(x)$ où $A = \cup A_n$. Par Beppo Levi, $\int \mathbb{I}_{A} d\mu = \lim \int \mathbb{I}_{A_n} d\mu$. Or $\int \mathbb{I}_{A} d\mu = \mu(A)$ et $\int \mathbb{I}_{A_n} d\mu = \mu(A_n)$. D'où le résultat. $\blacksquare$
