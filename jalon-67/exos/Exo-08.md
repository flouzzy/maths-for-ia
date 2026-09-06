---
title: "Exercice 8"
---
## Exercice 8 : Contre-exemple classique (Bosses glissantes) $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $f_n(x) = n \mathbf{1}_{]0, 1/n[}(x)$ pour $x \in \mathbb{R}$.
Calculer $\lim_{n \to \infty} \int_{\mathbb{R}} f_n(x) dx$ et $\int_{\mathbb{R}} \lim_{n \to \infty} f_n(x) dx$.
Pourquoi le théorème de convergence monotone ne s'applique-t-il pas ?

**Correction Détaillée :**
1. Pour un $x \in \mathbb{R}$ fixé. Si $x \le 0$, $f_n(x) = 0$ pour tout $n$.
   Si $x > 0$, alors pour $n > 1/x$, on a $x > 1/n$, et donc $f_n(x) = 0$.
2. Donc, pour tout $x \in \mathbb{R}$, $\lim_{n \to \infty} f_n(x) = 0$. La fonction limite $f$ est la fonction nulle.
3. L'intégrale de la limite est donc $\int_{\mathbb{R}} 0 \, dx = 0$.
4. Calculons l'intégrale de $f_n$ : $\int_{\mathbb{R}} f_n(x) dx = \int_0^{1/n} n \, dx = n \times \frac{1}{n} = 1$.
5. La limite des intégrales est $\lim_{n \to \infty} 1 = 1$.
6. On a $0 \neq 1$.
7. Pourquoi Beppo Levi échoue ? Le TCM exige que la suite $(f_n)$ soit croissante.
   Or, si on prend $x = 1/2$, $f_1(1/2) = 1$, mais $f_2(1/2) = 0$. La suite n'est pas croissante.
   C'est le phénomène de "bosse glissante" qui s'échappe vers $0$ et l'infini verticalement.
