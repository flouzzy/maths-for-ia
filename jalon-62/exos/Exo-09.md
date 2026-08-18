## Exercice 9 : Tribu produit (Introduction) \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$


\textbf{Énoncé :}
Soient $(X, \mathcal{A})$ et $(Y, \mathcal{B})$ deux espaces mesurables. On note $\mathcal{R} = \{A \times B \mid A \in \mathcal{A}, B \in \mathcal{B}\}$ la famille des pavés mesurables. Montrer que $\mathcal{R}$ n'est en général pas une algèbre (donc pas une tribu).

\textbf{Correction exhaustive pas-à-pas :}
1. Soient $A \times B \in \mathcal{R}$. Son complémentaire dans $X \times Y$ est :
   $(X \times Y) \setminus (A \times B) = ((X \setminus A) \times Y) \cup (X \times (Y \setminus B))$.
2. En général, la réunion de deux pavés n'est pas un pavé. Prenons $X = Y = \mathbb{R}$, avec $\mathcal{A} = \mathcal{B} = \mathcal{B}(\mathbb{R})$.
   Soit $A = [0, 1]$ et $B = [0, 1]$. $A \times B$ est le carré unité.
3. Son complémentaire est la région plane privée du carré. Cette région ne peut pas s'écrire sous la forme d'un unique produit cartésien $U \times V$.
4. Puisque le complémentaire d'un élément de $\mathcal{R}$ n'est pas dans $\mathcal{R}$, la famille $\mathcal{R}$ n'est pas stable par passage au complémentaire.
5. Elle n'est donc pas une algèbre, et *a fortiori* pas une tribu.
