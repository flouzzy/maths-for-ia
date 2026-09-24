# Exercice 7 : Approximation par convolution de fonctions indicatrices $\star\star\star\star\star$

**Énoncé :**
Soit $f = \mathbf{1}_{[a, b]}$. Construire une suite de fonctions $(f_n)_{n \in \mathbb{N}} \in C_c^\infty(\mathbb{R})$ convergeant vers $f$ dans $L^p(\mathbb{R})$ ($1 \le p < \infty$) en utilisant l'outil de la convolution avec une approximation de l'identité usuelle (mollifier).

**Correction détaillée :**
1. **La fonction mollifier (régularisante) standard :** On définit $\rho(x) = c \exp\left(-\frac{1}{1-x^2}\right)$ si $|x| < 1$, et $0$ sinon, où $c$ est choisi de sorte que $\int_{\mathbb{R}} \rho(x) \, dx = 1$. Il est bien connu que $\rho \in C_c^\infty(\mathbb{R})$ avec un support $[-1, 1]$.
On construit l'approximation de l'identité : $\rho_n(x) = n \rho(nx)$. Son support est $[-1/n, 1/n]$ et son intégrale vaut $1$.
2. **La suite d'approximation :** On définit $f_n = f * \rho_n$.
Comme la convolution d'une fonction localement intégrable $f$ à support compact et d'une fonction de $C_c^\infty(\mathbb{R})$ donne une fonction $C_c^\infty(\mathbb{R})$, on a bien $f_n \in C_c^\infty(\mathbb{R})$.
Le support de $f_n$ est inclus dans le compact $[a - 1/n, b + 1/n]$.
3. **Calcul explicite et convergence :**
$f_n(x) = (f * \rho_n)(x) = \int_{\mathbb{R}} \mathbf{1}_{[a, b]}(y) \rho_n(x-y) \, dy = \int_a^b \rho_n(x-y) \, dy = \int_{x-b}^{x-a} \rho_n(u) \, du$.
- Si $x$ est un point intérieur de $[a, b]$, alors pour $n$ assez grand (tel que $x-a > 1/n$ et $b-x > 1/n$), l'intervalle d'intégration $[x-b, x-a]$ contient le support $[-1/n, 1/n]$ de $\rho_n$. Donc $f_n(x) = \int_{-1/n}^{1/n} \rho_n(u) \, du = 1 = f(x)$.
- Si $x \notin [a, b]$ (point extérieur), pour $n$ assez grand, $[x-b, x-a]$ ne rencontre pas $[-1/n, 1/n]$, donc $f_n(x) = 0 = f(x)$.
Ainsi $f_n(x)$ converge simplement vers $f(x)$ presque partout (sauf aux bords $a$ et $b$).
4. **Conclusion par le TCD :**
Comme $\rho_n \ge 0$ et d'intégrale $1$, on a $0 \le f_n(x) \le \int_{\mathbb{R}} \rho_n = 1$ pour tout $x$.
On peut dominer l'intégrande : $|f_n(x) - f(x)|^p \le 2^p$ sur un intervalle borné commun contenant tous les supports des $f_n$ (par exemple $[a-1, b+1]$), et $0$ en dehors.
La majorante constante sur un compact est intégrable.
Par le Théorème de Convergence Dominée de Lebesgue, $\int_{\mathbb{R}} |f_n - f|^p \, dx \to 0$. Les $f_n$ sont infiniment dérivables à support compact et convergent vers $f$ dans $L^p$. $\blacksquare$
