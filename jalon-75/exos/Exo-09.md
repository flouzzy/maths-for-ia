# Exercice 9 : Convergence Rapide et Extraction
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit $(f_n)$ une suite dans $L^p(X)$ convergeant vers $f \in L^p(X)$.
1. Montrer qu'il existe une sous-suite $(f_{n_k})$ telle que $\|f_{n_{k+1}} - f_{n_k}\|_p \le 2^{-k}$.
2. En déduire directement l'existence d'une sous-suite convergeant presque partout vers $f$.

**Correction :**
1. Puisque $f_n \to f$, c'est une suite de Cauchy. Pour $\varepsilon = 1/2$, il existe $n_1$ tel que $m \ge n_1 \implies \|f_m - f_{n_1}\|_p \le 1/2$.
Par récurrence, ayant choisi $n_k$, il existe $n_{k+1} > n_k$ tel que $m \ge n_{k+1} \implies \|f_m - f\|_p \le 2^{-(k+2)}$.
Alors $\|f_{n_{k+1}} - f_{n_k}\|_p \le \|f_{n_{k+1}} - f\|_p + \|f - f_{n_k}\|_p \le 2^{-(k+2)} + 2^{-(k+1)} < 2^{-k}$.
2. Soit $u_k = f_{n_{k+1}} - f_{n_k}$. On a $\sum_{k=1}^\infty \|u_k\|_p \le \sum 2^{-k} = 1 < \infty$.
Par l'argument vu au Théorème de Riesz-Fischer, la série $\sum u_k(x)$ converge absolument pour presque tout $x$.
Or $f_{n_{K+1}}(x) = f_{n_1}(x) + \sum_{k=1}^K u_k(x)$.
Donc $f_{n_K}(x)$ converge p.p. vers une limite finie $\tilde{f}(x)$.
Puisque $f_{n_K}$ converge vers $\tilde{f}$ p.p., on a par le lemme de Fatou que $\tilde{f} \in L^p$ et $f_{n_K} \to \tilde{f}$ dans $L^p$.
Mais on sait déjà que $f_{n_K} \to f$ dans $L^p$. Par unicité de la limite dans $L^p$, $f = \tilde{f}$ p.p.
Donc $f_{n_K}(x) \to f(x)$ p.p.
