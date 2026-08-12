## Exercice 4 : Complétude et suites de Cauchy (Intermédiaire) \quad $\bigstar\bigstar\bigstar\bigstar\star$

\textbf{Énoncé :}
Soit $(X, d)$ un espace métrique. Montrer que deux suites de Cauchy équivalentes convergent vers la même limite si $X$ est complet.

\textbf{Correction Détaillée :}
1. Soit $(x_n)$ et $(y_n)$ deux suites de Cauchy telles que $d(x_n, y_n) \to 0$.
2. Supposons $X$ complet. La suite $(x_n)$ converge vers $l \in X$.
3. Montrons que $y_n \to l$.
4. Par l'inégalité triangulaire, $d(y_n, l) \leq d(y_n, x_n) + d(x_n, l)$.
5. Soit $\epsilon > 0$. Il existe $N_1$ tel que pour $n \ge N_1$, $d(x_n, l) < \epsilon/2$.
6. Il existe $N_2$ tel que pour $n \ge N_2$, $d(y_n, x_n) < \epsilon/2$.
7. Pour $n \ge \max(N_1, N_2)$, $d(y_n, l) < \epsilon/2 + \epsilon/2 = \epsilon$.
8. Ainsi, $(y_n)$ converge bien vers $l$.
