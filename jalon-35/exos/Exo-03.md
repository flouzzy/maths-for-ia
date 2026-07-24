# Exercice 3 : ★★

**Énoncé :**
Stabilité par intersection finie des ouverts.

**Correction (Zéro Ellipse) :**
Soit $p \in \mathbb{N}^*$ et $U_1, \dots, U_p$ des ouverts de $E$. Montrons que $U = \bigcap_{k=1}^p U_k$ est un ouvert.

Soit $(x_n)_{n \in \mathbb{N}}$ une suite de $E$ convergeant vers $x \in U$.
Puisque $x \in \bigcap_{k=1}^p U_k$, pour tout $k \in \{1, \dots, p\}$, $x \in U_k$.
Pour chaque ouvert $U_k$, puisque $x_n \to x \in U_k$, il existe un rang $N_k \in \mathbb{N}$ tel que pour tout $n \ge N_k$, $x_n \in U_k$.
Posons $N = \max(N_1, \dots, N_p)$. (Ce maximum existe car l'intersection est finie).
Soit $n \ge N$. Alors $n \ge N_k$ pour tout $k \in \{1, \dots, p\}$.
Donc, pour tout $k \in \{1, \dots, p\}$, $x_n \in U_k$.
Cela signifie exactement que $x_n \in \bigcap_{k=1}^p U_k = U$.
Ainsi, il existe un rang à partir duquel tous les termes de la suite sont dans l'intersection. L'intersection finie d'ouverts est ouverte. $\blacksquare$
