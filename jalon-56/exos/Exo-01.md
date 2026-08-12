## Exercice 1 : Complétude et suites de Cauchy (Facile) \quad $\bigstar\star\star\star\star$

\textbf{Énoncé :}
Montrer que l'espace des rationnels $\mathbb{Q}$ muni de la distance usuelle $d(x, y) = |x - y|$ n'est pas complet.
\textbf{Correction Détaillée :}
1. Considérons la suite $x_n = \sum_{k=0}^n \frac{1}{k!}$.
2. On montre que $(x_n)$ est de Cauchy. Soit $p > q$.
$$|x_p - x_q| = \sum_{k=q+1}^p \frac{1}{k!} \leq \frac{1}{(q+1)!} \sum_{j=0}^{\infty} \frac{1}{2^j} \leq \frac{2}{(q+1)!}$$
Pour tout $\epsilon > 0$, il existe $N$ tel que pour $q \geq N$, $\frac{2}{(q+1)!} < \epsilon$.
3. La suite est de Cauchy dans $\mathbb{Q}$.
4. Or, on sait que $\lim_{n \to \infty} x_n = e \notin \mathbb{Q}$.
5. Conclusion : on a trouvé une suite de Cauchy dans $\mathbb{Q}$ qui n'y admet pas de limite. $\mathbb{Q}$ n'est pas complet.
