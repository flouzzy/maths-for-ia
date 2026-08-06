# Exercice 5 : Intersection de topologies \quad $\bigstar\bigstar\star\star\star$

\textbf{Énoncé :}
Soient $\mathcal{T}_1$ et $\mathcal{T}_2$ deux topologies sur un ensemble $X$. Montrer que leur intersection $\mathcal{T}_1 \cap \mathcal{T}_2$ est encore une topologie sur $X$.

\textbf{Correction exhaustive :}
Vérifions les axiomes pour $\mathcal{T} = \mathcal{T}_1 \cap \mathcal{T}_2$.
1. $\emptyset \in \mathcal{T}_1$ et $\emptyset \in \mathcal{T}_2$, donc $\emptyset \in \mathcal{T}$. De même, $X \in \mathcal{T}_1$ et $X \in \mathcal{T}_2$, donc $X \in \mathcal{T}$.
2. Soit $(O_i)_{i \in I}$ une famille d'éléments de $\mathcal{T}$. Pour tout $i$, $O_i \in \mathcal{T}_1$ et $O_i \in \mathcal{T}_2$. Comme $\mathcal{T}_1$ est une topologie, $\bigcup_{i \in I} O_i \in \mathcal{T}_1$. De même pour $\mathcal{T}_2$. Donc $\bigcup_{i \in I} O_i \in \mathcal{T}_1 \cap \mathcal{T}_2 = \mathcal{T}$.
3. Soient $U, V \in \mathcal{T}$. Alors $U, V \in \mathcal{T}_1$ et $U, V \in \mathcal{T}_2$. Par stabilité de $\mathcal{T}_1$ et $\mathcal{T}_2$ par intersections finies, $U \cap V \in \mathcal{T}_1$ et $U \cap V \in \mathcal{T}_2$. Donc $U \cap V \in \mathcal{T}$.
Conclusion : L'intersection de topologies est une topologie.
