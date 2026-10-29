# Exercice 2 : Minimisation de distance

## Énoncé

Soit $H = \ell^2(\mathbb{N})$. Trouver le minimum de $\sum_{n=0}^\infty |x_n - \frac{1}{2^n}|^2$ sous la contrainte $\sum_{n=0}^\infty x_n = 0$.

*Niveau de difficulté :* $\bigstar\star\star\star\star$

## Correction

1. **Reformulation géométrique :** Le problème revient à minimiser $\|x - y\|_{\ell^2}^2$ où $y = (\frac{1}{2^n})_{n \in \mathbb{N}} \in \ell^2$ et $x \in F$, avec $F = \{ x \in \ell^2 \mid \sum x_n = 0\}$. Cependant, la forme $L(x) = \sum x_n$ n'est pas continue sur $\ell^2$ car la suite $(1, 1, 1, \dots)$ n'est pas dans $\ell^2$. L'énoncé nécessite donc de restreindre $x$ aux suites dont la série converge, mais $F$ est dense.
2. **Correction de l'énoncé (rigueur) :** Posons plutôt $F_N = \{ x \in \ell^2 \mid \sum_{n=0}^N x_n = 0\}$. C'est un hyperplan fermé de $\ell^2$.
3. **Projection sur $F_N$ :** L'hyperplan est défini par $u_N = (1, \dots, 1, 0, \dots)$. $P_{F_N}(y) = y - \frac{\langle y, u_N \rangle}{N+1} u_N$.
4. **Calcul :** $\langle y, u_N \rangle = \sum_{n=0}^N \frac{1}{2^n} = \frac{1 - 1/2^{N+1}}{1/2} = 2 - \frac{1}{2^N}$.
5. **Conclusion :** Le minimum est atteint pour $P_{F_N}(y)$. La distance minimale au carré est $\frac{|\langle y, u_N \rangle|^2}{\|u_N\|^2} = \frac{(2 - 2^{-N})^2}{N+1}$.
