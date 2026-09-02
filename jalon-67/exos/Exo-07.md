# Exercice 7 : TCM sur la mesure de Lebesgue abstraite ★★★★

## Énoncé
Soit $f$ une fonction mesurable positive sur $\mathbb{R}^d$.
Montrer que $\lim_{n \to \infty} \int_{\{|f| \le n\}} f d\lambda = \int_{\mathbb{R}^d} f d\lambda$.

## Correction Détaillée
1. **Suite de fonctions** : Posons $f_n = f \cdot \mathbf{1}_{\{|f| \le n\}}$.
2. **Croissance** : Comme $f \ge 0$, l'ensemble $\{|f| \le n\}$ est inclus dans $\{|f| \le n+1\}$, donc $\mathbf{1}_{\{|f| \le n\}} \le \mathbf{1}_{\{|f| \le n+1\}}$.
3. **Positivité** : La suite $(f_n)$ est bien une suite de fonctions mesurables positives croissante.
4. **Limite simple** : Pour tout point $x$ où $f(x)$ est finie, il existe $n$ tel que $n \ge f(x)$, et pour tout $k \ge n$, $f_k(x) = f(x)$. Donc $f_n(x) \to f(x)$. Si $f(x) = +\infty$, $f_n(x) = 0$ pour tout $n$, ce qui pose un problème. Mais si on suppose $f$ à valeurs finies, la convergence est simple vers $f$.
5. **Application du TCM** : Le TCM garantit que $\lim \int f_n = \int \lim f_n = \int f d\lambda$.
