## Exercice 10 : Lemme des classes monotones (Cas simplifé) \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$


\textbf{Énoncé :}
Une classe monotone $\mathcal{M}$ est stable par limites croissantes dénombrables et limites décroissantes dénombrables. Démontrer que si une algèbre $\mathcal{A}$ est une classe monotone, alors c'est une tribu.

\textbf{Correction exhaustive pas-à-pas :}
1. On sait que $\mathcal{A}$ est une algèbre : elle contient $X$, est stable par complémentaire et par union finie.
2. Pour montrer que c'est une tribu, il suffit de prouver la stabilité par union dénombrable.
3. Soit $(A_n)_{n \in \mathbb{N}}$ une suite d'éléments de $\mathcal{A}$.
4. Posons $B_N = \bigcup_{n=0}^N A_n$. Puisque $\mathcal{A}$ est une algèbre (stable par union finie), $B_N \in \mathcal{A}$ pour tout $N$.
5. La suite $(B_N)$ est croissante au sens de l'inclusion : $B_0 \subset B_1 \subset B_2 \dots$
6. La limite croissante de cette suite est exactement $\bigcup_{n=0}^{\infty} A_n$.
7. Puisque $\mathcal{A}$ est une classe monotone, la limite croissante d'une suite d'éléments de $\mathcal{A}$ appartient à $\mathcal{A}$.
8. Par conséquent, $\bigcup_{n=0}^{\infty} A_n \in \mathcal{A}$.
9. L'algèbre $\mathcal{A}$ est donc stable par union dénombrable, ce qui prouve que c'est une tribu.
