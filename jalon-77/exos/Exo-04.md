## Exercice 4 : Densité par convolution (Mollification) \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $f \in L^1(\mathbb{R})$. On considère une fonction test positive $\varphi \in C_c^\infty(\mathbb{R})$ telle que $\int_{\mathbb{R}} \varphi(x) dx = 1$.
Pour $\epsilon > 0$, on pose $\varphi_\epsilon(x) = \frac{1}{\epsilon}\varphi(\frac{x}{\epsilon})$.
La fonction régularisée est $f_\epsilon = f * \varphi_\epsilon$, soit $f_\epsilon(x) = \int_{\mathbb{R}} f(x-y)\varphi_\epsilon(y) dy$.
Montrer que si $f$ est uniformément continue et bornée, alors $f_\epsilon \to f$ uniformément sur $\mathbb{R}$ quand $\epsilon \to 0$.

**Correction :**
Puisque $\int_{\mathbb{R}} \varphi_\epsilon(y) dy = \int_{\mathbb{R}} \frac{1}{\epsilon}\varphi(\frac{y}{\epsilon}) dy = 1$ (par le changement de variable $z = y/\epsilon$), nous pouvons écrire pour tout $x \in \mathbb{R}$ :
$f(x) = \int_{\mathbb{R}} f(x) \varphi_\epsilon(y) dy$.

La différence s'écrit alors :
$f_\epsilon(x) - f(x) = \int_{\mathbb{R}} (f(x-y) - f(x)) \varphi_\epsilon(y) dy$.

La fonction $f$ étant uniformément continue, pour tout $\eta > 0$, il existe $\delta > 0$ tel que $|z| < \delta \implies |f(w-z) - f(w)| < \eta$ pour tout $w$.
Le support de $\varphi$ est compact, disons inclus dans $[-M, M]$.
Ainsi, le support de $\varphi_\epsilon$ est inclus dans $[-\epsilon M, \epsilon M]$.
Pour $\epsilon < \frac{\delta}{M}$, si $y$ est dans le support de $\varphi_\epsilon$, alors $|y| \le \epsilon M < \delta$.

Pour un tel $\epsilon$, et pour tout $x \in \mathbb{R}$ :
$|f_\epsilon(x) - f(x)| \le \int_{-\epsilon M}^{\epsilon M} |f(x-y) - f(x)| \varphi_\epsilon(y) dy$
Puisque $|y| < \delta$, $|f(x-y) - f(x)| < \eta$.
$|f_\epsilon(x) - f(x)| \le \eta \int_{-\epsilon M}^{\epsilon M} \varphi_\epsilon(y) dy = \eta \times 1 = \eta$.

Comme cette majoration est indépendante de $x$, nous avons $\| f_\epsilon - f \|_\infty \le \eta$ pour tout $\epsilon < \delta/M$.
Ceci démontre la convergence uniforme $f_\epsilon \to f$ sur $\mathbb{R}$.
