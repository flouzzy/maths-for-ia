# Exercice 7 : Densité de probabilité et fonction de répartition \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

Soit $f$ une fonction positive et intégrable sur $\mathbb{R}$. Soit $F(x) = \int_{-\infty}^{x} f(t) dt$.

**Question :** Montrer à l'aide du TCM que $\lim_{x \to \infty} F(x) = \int_{-\infty}^{\infty} f(t) dt$.

**Solution Détaillée :**
1. La variable $x$ est continue. Pour utiliser le TCM, prenons une suite quelconque $(x_n)_{n \in \mathbb{N}}$ croissante et tendant vers $+\infty$.
2. Posons la suite de fonctions $f_n(t) = f(t) \mathbf{1}_{]-\infty, x_n]}(t)$.
3. Puisque la suite $(x_n)$ est croissante, la suite d'ensembles $A_n = ]-\infty, x_n]$ est croissante pour l'inclusion.
4. Ainsi, pour tout $t \in \mathbb{R}$, $0 \le f_n(t) \le f_{n+1}(t)$. La suite $(f_n)$ est croissante et positive.
5. La limite simple de $f_n(t)$ est $f(t)$ car $\cup_{n} A_n = \mathbb{R}$.
6. Par le théorème de convergence monotone :
   $$ \lim_{n \to \infty} \int_{\mathbb{R}} f_n(t) dt = \int_{\mathbb{R}} \lim_{n \to \infty} f_n(t) dt = \int_{\mathbb{R}} f(t) dt $$
7. Or, $\int_{\mathbb{R}} f_n(t) dt = \int_{-\infty}^{x_n} f(t) dt = F(x_n)$.
8. Puisque ceci est vrai pour toute suite $(x_n) \nearrow +\infty$, on a bien $\lim_{x \to \infty} F(x) = \int_{\mathbb{R}} f(t) dt$.
