# Exercice 7 : Le cas $p = +\infty$
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Démontrer que $L^\infty(X, \mu)$ est un espace de Banach. Indiquer clairement où l'on utilise le fait que $\mathbb{R}$ est complet.

**Correction :**
Soit $(f_n)$ une suite de Cauchy dans $L^\infty$.
Pour tout entier $k \ge 1$, il existe $N_k$ tel que $n, m \ge N_k \implies \|f_n - f_m\|_\infty < 1/k$.
Soit $A_{n,m,k} = \{x \in X \mid |f_n(x) - f_m(x)| \ge 1/k\}$. Par définition, $\mu(A_{n,m,k}) = 0$.
Soit $A = \bigcup_{k=1}^\infty \bigcup_{n,m \ge N_k} A_{n,m,k}$. $A$ est une union dénombrable de négligeables, donc $\mu(A) = 0$.
Pour $x \notin A$, et pour $n,m \ge N_k$, on a $|f_n(x) - f_m(x)| < 1/k$.
Ceci montre que pour tout $x \notin A$, la suite numérique $(f_n(x))$ est de Cauchy dans $\mathbb{R}$.
**Utilisation de la complétude de $\mathbb{R}$ :** Comme $\mathbb{R}$ est complet, la suite de Cauchy numérique $(f_n(x))$ converge. On note $f(x)$ sa limite. Pour $x \in A$, posons $f(x) = 0$.
Faisons tendre $m \to \infty$ dans $|f_n(x) - f_m(x)| < 1/k$ pour $x \notin A$. On obtient $|f_n(x) - f(x)| \le 1/k$ pour tout $x \notin A$ et tout $n \ge N_k$.
Ceci prouve que $\|f_n - f\|_\infty \le 1/k$, donc $f_n \to f$ dans $L^\infty$.
De plus, $f = f - f_{N_1} + f_{N_1} \in L^\infty$ car $L^\infty$ est un espace vectoriel. Donc $L^\infty$ est complet.
