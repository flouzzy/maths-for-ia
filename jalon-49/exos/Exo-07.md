# Exercice 7 : Topologie induite \quad $\bigstar\bigstar\bigstar\star\star$

\textbf{Énoncé :}
Soit $(X, \mathcal{T})$ un espace topologique et $A \subset X$. On définit $\mathcal{T}_A = \{O \cap A \mid O \in \mathcal{T}\}$. Montrer que $\mathcal{T}_A$ est une topologie sur $A$ (topologie induite ou topologie trace).

\textbf{Correction exhaustive :}
Vérifions les axiomes pour $\mathcal{T}_A$ sur l'ensemble $A$ :
1. $\emptyset \in \mathcal{T}$, et $\emptyset \cap A = \emptyset$, donc $\emptyset \in \mathcal{T}_A$.
   $X \in \mathcal{T}$, et $X \cap A = A$, donc $A \in \mathcal{T}_A$.
2. Soit $(U_i)_{i \in I}$ une famille d'éléments de $\mathcal{T}_A$. Pour chaque $i$, il existe $O_i \in \mathcal{T}$ tel que $U_i = O_i \cap A$.
   La réunion est $\bigcup_{i \in I} U_i = \bigcup_{i \in I} (O_i \cap A) = \left( \bigcup_{i \in I} O_i \right) \cap A$.
   Comme $\mathcal{T}$ est une topologie, $\bigcup_{i \in I} O_i \in \mathcal{T}$, donc l'intersection avec $A$ appartient à $\mathcal{T}_A$.
3. Soient $U_1, \dots, U_n \in \mathcal{T}_A$. Il existe $O_1, \dots, O_n \in \mathcal{T}$ tels que $U_k = O_k \cap A$.
   L'intersection finie est $\bigcap_{k=1}^n U_k = \bigcap_{k=1}^n (O_k \cap A) = \left( \bigcap_{k=1}^n O_k \right) \cap A$.
   Comme $\mathcal{T}$ est stable par intersection finie, $\bigcap_{k=1}^n O_k \in \mathcal{T}$, donc $\bigcap_{k=1}^n U_k \in \mathcal{T}_A$.
Conclusion : $\mathcal{T}_A$ est bien une topologie sur $A$.
