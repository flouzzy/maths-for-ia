## Exercice 3 : Intégrale sur un domaine infini (Tonelli) \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Calculer $I = \iint_{\mathbb{R}_+^2} e^{-(x+y)} \cos^2(xy) dx dy$.

**Correction :**
1. La fonction $f(x, y) = e^{-(x+y)} \cos^2(xy)$ est continue et positive sur $\mathbb{R}_+^2 = [0, +\infty[ \times [0, +\infty[$.
2. Tonelli nous autorise à évaluer l'intégrale, mais le terme $\cos^2(xy)$ est difficile à intégrer directement.
3. Nous allons utiliser une majoration pour montrer que l'intégrale est finie. Remarquons que pour tout $(x, y)$, $0 \le \cos^2(xy) \le 1$.
4. Ainsi, $0 \le f(x, y) \le e^{-x} e^{-y}$.
5. Considérons $g(x, y) = e^{-x} e^{-y}$. C'est une fonction à variables séparables.
   $$ \iint_{\mathbb{R}_+^2} g(x, y) dx dy = \left( \int_0^{+\infty} e^{-x} dx \right) \left( \int_0^{+\infty} e^{-y} dy \right) $$
6. Or, $\int_0^{+\infty} e^{-t} dt = \lim_{A \to +\infty} [-e^{-t}]_0^A = \lim_{A \to +\infty} (1 - e^{-A}) = 1$.
7. Donc $\iint_{\mathbb{R}_+^2} g(x, y) dx dy = 1 \times 1 = 1$.
8. Par monotonie de l'intégrale de Lebesgue, $0 \le I \le 1$. L'intégrale est donc finie (et existe bien grâce à Tonelli). Le calcul exact nécessite des développements en séries ou des fonctions spéciales. Cet exercice illustre l'usage de Tonelli pour la domination.
