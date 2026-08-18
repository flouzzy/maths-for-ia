## Exercice 2 : Tribu engendrée par un sous-ensemble \quad $\bigstar\bigstar\star\star\star$


\textbf{Énoncé :}
Déterminer explicitement la tribu $\sigma(\{A\})$ engendrée par une partie $A \subset X$.

\textbf{Correction exhaustive pas-à-pas :}
1. Une tribu contenant $A$ doit contenir $A$.
2. Par stabilité au complémentaire, elle doit contenir $A^c = X \setminus A$.
3. Elle doit contenir l'ensemble vide $\emptyset$ et l'espace entier $X$.
4. Posons $\mathcal{T} = \{\emptyset, A, A^c, X\}$.
5. Vérifions que $\mathcal{T}$ est une tribu :
   - $X \in \mathcal{T}$.
   - Stabilité par complémentaire : $A^c \in \mathcal{T}, (A^c)^c = A \in \mathcal{T}, \emptyset^c = X \in \mathcal{T}, X^c = \emptyset \in \mathcal{T}$.
   - Stabilité par union : $A \cup A^c = X$, $A \cup \emptyset = A$, etc. Toutes les unions possibles d'éléments de $\mathcal{T}$ restent dans $\mathcal{T}$.
6. $\mathcal{T}$ est donc une tribu contenant $A$. C'est manifestement la plus petite, car toute tribu contenant $A$ doit contenir ces quatre éléments.
7. Ainsi, $\sigma(\{A\}) = \{\emptyset, A, A^c, X\}$.
