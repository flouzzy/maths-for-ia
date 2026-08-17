## Exercice 8 : Image réciproque de tribu \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$


\textbf{Énoncé :}
Soit $f : X \to Y$ une application et $\mathcal{F}_Y$ une tribu sur $Y$. Montrer que l'ensemble $f^{-1}(\mathcal{F}_Y) = \{f^{-1}(B) \mid B \in \mathcal{F}_Y\}$ est une tribu sur $X$.

\textbf{Correction exhaustive pas-à-pas :}
1. L'espace complet : $Y \in \mathcal{F}_Y$. L'image réciproque est $f^{-1}(Y) = X$. Donc $X \in f^{-1}(\mathcal{F}_Y)$.
2. Stabilité par complémentaire : Soit $A \in f^{-1}(\mathcal{F}_Y)$. Il existe $B \in \mathcal{F}_Y$ tel que $A = f^{-1}(B)$.
   Le complémentaire est $X \setminus A = X \setminus f^{-1}(B) = f^{-1}(Y \setminus B)$.
   Puisque $\mathcal{F}_Y$ est une tribu, $Y \setminus B \in \mathcal{F}_Y$. Donc $X \setminus A \in f^{-1}(\mathcal{F}_Y)$.
3. Stabilité par union dénombrable : Soit $(A_n)_{n \in \mathbb{N}}$ une suite dans $f^{-1}(\mathcal{F}_Y)$. Il existe une suite $(B_n)$ dans $\mathcal{F}_Y$ telle que $A_n = f^{-1}(B_n)$.
   $\bigcup A_n = \bigcup f^{-1}(B_n) = f^{-1}(\bigcup B_n)$.
   Puisque $\mathcal{F}_Y$ est une tribu, $\bigcup B_n \in \mathcal{F}_Y$. Ainsi, $\bigcup A_n \in f^{-1}(\mathcal{F}_Y)$.
4. Conclusion : $f^{-1}(\mathcal{F}_Y)$ est bien une tribu sur $X$.
