## Exercice 5 : Tribu trace \quad $\bigstar\bigstar\bigstar\star\star$


\textbf{Énoncé :}
Soit $(X, \mathcal{F})$ un espace mesurable et $Y \subset X$ un sous-ensemble (pas nécessairement dans $\mathcal{F}$). Démontrer que $\mathcal{F}_Y = \{A \cap Y \mid A \in \mathcal{F}\}$ est une tribu sur $Y$, appelée tribu trace.

\textbf{Correction exhaustive pas-à-pas :}
1. L'ensemble entier pour $Y$ est $Y$. Or $X \in \mathcal{F}$ et $X \cap Y = Y$, donc $Y \in \mathcal{F}_Y$.
2. Stabilité par complémentaire relatif : Soit $B \in \mathcal{F}_Y$. Il existe $A \in \mathcal{F}$ tel que $B = A \cap Y$.
   Le complémentaire de $B$ dans $Y$ est $Y \setminus B = Y \setminus (A \cap Y) = Y \setminus A = (X \setminus A) \cap Y$.
   Puisque $\mathcal{F}$ est une tribu, $X \setminus A \in \mathcal{F}$. Donc $(X \setminus A) \cap Y \in \mathcal{F}_Y$.
3. Stabilité par union dénombrable : Soit $(B_n)_{n \in \mathbb{N}}$ une suite dans $\mathcal{F}_Y$. Pour tout $n$, il existe $A_n \in \mathcal{F}$ tel que $B_n = A_n \cap Y$.
   $\bigcup_{n \in \mathbb{N}} B_n = \bigcup_{n \in \mathbb{N}} (A_n \cap Y) = \left( \bigcup_{n \in \mathbb{N}} A_n \right) \cap Y$.
   Puisque $\mathcal{F}$ est une tribu, $\bigcup A_n \in \mathcal{F}$. Ainsi, l'union des $B_n$ appartient à $\mathcal{F}_Y$.
4. $\mathcal{F}_Y$ est bien une tribu sur $Y$.
