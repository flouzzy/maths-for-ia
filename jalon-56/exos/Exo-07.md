## Exercice 7 : Complétude et suites de Cauchy (Intermédiaire) \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

\textbf{Énoncé :}
Démontrer que l'espace $\ell^\infty(\mathbb{N}, \mathbb{R})$ des suites réelles bornées muni de $\|u\|_\infty = \sup |u_n|$ est complet.

\textbf{Correction Détaillée :}
1. Soit $(u^{(k)})_{k \in \mathbb{N}}$ une suite de Cauchy dans $\ell^\infty$. Chaque $u^{(k)}$ est une suite $(u_n^{(k)})_{n \in \mathbb{N}}$.
2. Pour tout $n$, $|u_n^{(p)} - u_n^{(q)}| \leq \|u^{(p)} - u^{(q)}\|_\infty$.
3. La suite réelle $(u_n^{(k)})_{k}$ est de Cauchy, donc converge dans $\mathbb{R}$ vers une limite $u_n$.
4. Montrons que la suite $u = (u_n)$ est bornée. Il existe $N$ t.q. $\|u^{(p)} - u^{(N)}\|_\infty \le 1$. Chaque composante $u_n^{(p)}$ est bornée indépendamment de $p \ge N$, donc la limite $u$ l'est. $u \in \ell^\infty$.
5. On montre ensuite que $\|u^{(p)} - u\|_\infty \to 0$ exactement comme pour la convergence uniforme.
6. L'espace est donc complet.
