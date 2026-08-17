## Exercice 3 : Tribu co-dénombrable \quad $\bigstar\bigstar\star\star\star$


\textbf{Énoncé :}
Soit $X$ un ensemble non dénombrable. Montrer que $\mathcal{F} = \{A \subset X \mid A \text{ est dénombrable ou } A^c \text{ est dénombrable}\}$ est une tribu sur $X$.

\textbf{Correction exhaustive pas-à-pas :}
1. L'ensemble vide $\emptyset$ est fini (donc dénombrable), donc $\emptyset \in \mathcal{F}$, et son complémentaire $X \in \mathcal{F}$.
2. Stabilité par complémentaire : Si $A \in \mathcal{F}$, alors par définition, soit $A$ est dénombrable (donc le complémentaire de $A^c$ est dénombrable, d'où $A^c \in \mathcal{F}$), soit $A^c$ est dénombrable (donc $A^c \in \mathcal{F}$).
3. Stabilité par union dénombrable : Soit $(A_n)_{n \in \mathbb{N}}$ une suite d'éléments de $\mathcal{F}$.
   - Cas 1 : Pour tout $n$, $A_n$ est dénombrable. Une réunion dénombrable d'ensembles dénombrables est dénombrable, donc $\bigcup A_n$ est dénombrable, d'où $\bigcup A_n \in \mathcal{F}$.
   - Cas 2 : Il existe au moins un entier $k$ tel que $A_k^c$ est dénombrable.
     Alors $(\bigcup A_n)^c = \bigcap A_n^c \subset A_k^c$.
     Puisque $A_k^c$ est dénombrable, tout sous-ensemble de $A_k^c$ est dénombrable.
     Donc $(\bigcup A_n)^c$ est dénombrable, ce qui implique $\bigcup A_n \in \mathcal{F}$.
4. Conclusion : $\mathcal{F}$ est bien une tribu.
