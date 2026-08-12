## Exercice 9 : Complétude et suites de Cauchy (Avancé) \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

\textbf{Énoncé :}
Étude de la complétude de l'espace des fonctions polynomiales muni de la norme infinie.

\textbf{Correction Détaillée :}
1. Soit $E = \mathbb{R}[X]$ muni de la norme $\|P\| = \sup_{x \in [0,1]} |P(x)|$.
2. Cet espace n'est pas complet. Pour le démontrer, exhibons une suite de Cauchy qui ne converge pas dans $E$.
3. Considérons $P_n(X) = \sum_{k=0}^n \frac{X^k}{k!}$.
4. Pour $p > q$, $\|P_p - P_q\| = \sup_{x \in [0,1]} \sum_{k=q+1}^p \frac{x^k}{k!} \leq \sum_{k=q+1}^p \frac{1}{k!}$.
5. Comme la série $\sum \frac{1}{k!}$ converge vers $e$, ses restes tendent vers 0. La suite $(P_n)$ est donc de Cauchy pour la norme uniforme.
6. Si $P_n$ convergeait vers un polynôme $P \in \mathbb{R}[X]$, on aurait $P_n(x) \to P(x)$ pour tout $x \in [0,1]$.
7. Or $P_n(x) \to e^x$. Donc $P(x) = e^x$ sur $[0,1]$, ce qui est absurde car $e^x$ n'est pas polynomiale (ses dérivées successives ne s'annulent jamais).
8. L'espace n'est pas complet.
