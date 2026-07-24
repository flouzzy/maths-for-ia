# Exercice 2 : ★

**Énoncé :**
Stabilité par réunion des ouverts.

**Correction (Zéro Ellipse) :**
Soient $(U_i)_{i \in I}$ une famille quelconque d'ouverts de $E$. Montrons que $U = \bigcup_{i \in I} U_i$ est un ouvert.

Soit $(x_n)_{n \in \mathbb{N}}$ une suite de $E$ convergeant vers $x \in U$.
Puisque $x \in \bigcup_{i \in I} U_i$, il existe au moins un indice $i_0 \in I$ tel que $x \in U_{i_0}$.
Comme $U_{i_0}$ est un ouvert, et que $(x_n)_{n \in \mathbb{N}}$ converge vers $x \in U_{i_0}$, par caractérisation séquentielle, il existe un rang $N \in \mathbb{N}$ tel que pour tout $n \ge N$, $x_n \in U_{i_0}$.
Or, $U_{i_0} \subset \bigcup_{i \in I} U_i = U$.
Donc pour tout $n \ge N$, $x_n \in U$.
Ceci démontre, par caractérisation séquentielle, que l'union quelconque d'ouverts est un ouvert. $\blacksquare$
