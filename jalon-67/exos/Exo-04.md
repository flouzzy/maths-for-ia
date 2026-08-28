# Exercice 4 : Contre-exemple sans la croissance ★★★★★

**Énoncé :**
Considérons l'espace $(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$. Soit $f_n(x) = \frac{1}{n} \chi_{[0, n]}(x)$. La suite $(f_n)$ est-elle croissante ? Calculer la limite de l'intégrale et l'intégrale de la limite. Conclure.

**Correction :**
1. $f_n(x)$ prend la valeur $1/n$ sur $[0, n]$ et $0$ ailleurs. $f_{n+1}(x)$ prend la valeur $1/(n+1)$ sur $[0, n+1]$. Sur $[0, n]$, $f_n(x) = 1/n > 1/(n+1) = f_{n+1}(x)$. La suite n'est donc **pas** croissante (elle est décroissante sur les compacts).
2. La limite ponctuelle est $f(x) = \lim_{n \to \infty} \frac{1}{n} \chi_{[0, n]}(x) = 0$. Donc $\int_{\mathbb{R}} f(x) dx = 0$.
3. Calculons l'intégrale de chaque terme : $\int_{\mathbb{R}} f_n(x) dx = \int_0^n \frac{1}{n} dx = 1$.
4. La limite des intégrales est $\lim 1 = 1$.
5. On a $\int \lim f_n = 0 \neq 1 = \lim \int f_n$. Le théorème de convergence monotone ne s'applique pas car l'hypothèse de croissance est indispensable pour éviter la 'fuite de masse' à l'infini.
