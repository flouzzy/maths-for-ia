# Exercice 2 : Contre-exemple classique ★★

## Énoncé
Soit $f_n(x) = \frac{1}{n} \mathbf{1}_{[0, n]}(x)$.
Calculer $\int_{\mathbb{R}} f_n d\lambda$ et $\int_{\mathbb{R}} \lim f_n d\lambda$. Le TCM est-il vérifié ? Pourquoi ?

## Correction Détaillée
1. **Intégrale de la suite** : $\int_{\mathbb{R}} f_n d\lambda = \frac{1}{n} \cdot n = 1$.
2. **Limite des intégrales** : $\lim_{n \to \infty} \int f_n d\lambda = 1$.
3. **Limite de la fonction** : Pour tout $x \in \mathbb{R}$, $f_n(x) = \frac{1}{n}$ pour $n > x$, donc $\lim_{n \to \infty} f_n(x) = 0$.
4. **Intégrale de la limite** : $\int_{\mathbb{R}} 0 d\lambda = 0$.
5. **Conclusion** : On a $1 \neq 0$. Le TCM ne s'applique pas car la suite $(f_n)$ n'est pas croissante : $f_{n+1}(x) = \frac{1}{n+1} < \frac{1}{n} = f_n(x)$ pour $x \in [0, n]$.
