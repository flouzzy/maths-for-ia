## Exercice 2 : Complétude et suites de Cauchy (Facile) \quad $\bigstar\bigstar\star\star\star$

\textbf{Énoncé :}
Montrer que toute suite de Cauchy admettant une valeur d'adhérence est convergente.
\textbf{Correction Détaillée :}
1. Soit $(x_n)$ une suite de Cauchy dans $(X,d)$.
2. Supposons qu'elle admette une valeur d'adhérence $l \in X$. Par définition, il existe une sous-suite $(x_{\phi(n)})$ qui converge vers $l$.
3. Soit $\epsilon > 0$. Comme $(x_n)$ est de Cauchy, il existe $N_1$ tel que pour $p, q \geq N_1$, $d(x_p, x_q) < \frac{\epsilon}{2}$.
4. Comme $x_{\phi(n)} \to l$, il existe $N_2$ tel que pour $n \geq N_2$, $d(x_{\phi(n)}, l) < \frac{\epsilon}{2}$.
5. Soit $N = \max(N_1, N_2)$. Pour $n \geq N$, on choisit $k \geq N$ tel que $\phi(k) \geq N$.
6. $d(x_n, l) \leq d(x_n, x_{\phi(k)}) + d(x_{\phi(k)}, l)$.
7. Comme $n, \phi(k) \geq N \geq N_1$, on a $d(x_n, x_{\phi(k)}) < \frac{\epsilon}{2}$. Et comme $k \geq N_2$, $d(x_{\phi(k)}, l) < \frac{\epsilon}{2}$.
8. Ainsi, $d(x_n, l) < \epsilon$. Donc $(x_n)$ converge vers $l$.
