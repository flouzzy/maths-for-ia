## Exercice 8 : Complétude et suites de Cauchy (Avancé) \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

\textbf{Énoncé :}
Complétion de l'espace des fonctions nulles à l'infini : $C_0(\mathbb{R})$. L'espace des fonctions continues s'annulant à l'infini muni de la norme uniforme est-il complet ?

\textbf{Correction Détaillée :}
1. Soit $(f_n)$ une suite de Cauchy dans $C_0(\mathbb{R})$ pour la norme $\|\cdot\|_\infty$.
2. Comme $C_b(\mathbb{R})$ (fonctions continues bornées) est complet, et que $(f_n)$ y est une suite de Cauchy, $(f_n)$ converge uniformément vers une fonction $f \in C_b(\mathbb{R})$.
3. Il reste à montrer que $f \in C_0(\mathbb{R})$, c'est-à-dire que $\lim_{|x| \to \infty} f(x) = 0$.
4. Soit $\epsilon > 0$. Par convergence uniforme, il existe $N$ tel que $\|f_N - f\|_\infty < \epsilon/2$.
5. Comme $f_N \in C_0(\mathbb{R})$, il existe $M > 0$ tel que pour $|x| > M$, $|f_N(x)| < \epsilon/2$.
6. Pour $|x| > M$, $|f(x)| \leq |f(x) - f_N(x)| + |f_N(x)| < \epsilon/2 + \epsilon/2 = \epsilon$.
7. Donc $\lim_{|x| \to \infty} f(x) = 0$, d'où $f \in C_0(\mathbb{R})$. $C_0(\mathbb{R})$ est un espace de Banach.
