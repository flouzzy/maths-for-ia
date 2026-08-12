## Exercice 3 : Complétude et suites de Cauchy (Facile) \quad $\bigstar\bigstar\bigstar\star\star$

\textbf{Énoncé :}
Soit $X$ un espace métrique. Montrer que l'intersection d'une suite décroissante de fermés non vides dont le diamètre tend vers zéro est un singleton si $X$ est complet.
\textbf{Correction Détaillée :}
1. Soit $(F_n)$ une suite décroissante de fermés non vides tels que $\text{diam}(F_n) \to 0$.
2. Pour chaque $n$, choisissons $x_n \in F_n$.
3. Pour $p \geq q \geq N$, on a $x_p \in F_p \subset F_q$ et $x_q \in F_q$.
4. Donc $d(x_p, x_q) \leq \text{diam}(F_q)$.
5. Comme $\text{diam}(F_q) \to 0$, pour tout $\epsilon > 0$, il existe $N$ tel que pour $q \geq N$, $\text{diam}(F_q) < \epsilon$. Ainsi $d(x_p, x_q) < \epsilon$.
6. La suite $(x_n)$ est de Cauchy.
7. Comme $X$ est complet, $x_n$ converge vers un point $l$.
8. Pour tout $k$, les termes de la suite $x_n$ (pour $n \geq k$) appartiennent au fermé $F_k$. La limite $l$ appartient donc à $F_k$.
9. Ainsi $l \in \cap F_n$.
10. Unicité : s'il existe un autre point $y \in \cap F_n$, $d(l, y) \leq \text{diam}(F_n) \to 0$, donc $d(l, y) = 0 \implies l=y$. L'intersection est un singleton.
