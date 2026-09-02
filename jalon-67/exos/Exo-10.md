# Exercice 10 : TCM et Espaces $L^1$ ★★★★★

## Énoncé
Montrer que l'espace des fonctions intégrables $\mathcal{L}^1(X, \mu)$ muni de la norme $\|f\|_1 = \int |f| d\mu$ est complet (c'est un espace de Banach), en admettant que toute série absolument convergente dans l'espace y converge, en utilisant le corollaire du TCM.

## Correction Détaillée
1. **Critère de complétude** : Un espace normé est complet si et seulement si toute série absolument convergente est convergente. Soit $(f_n)$ une suite dans $\mathcal{L}^1$ telle que $\sum \|f_n\|_1 = M < \infty$.
2. **Série des valeurs absolues** : Soit $g_n = \sum_{k=1}^n |f_k|$. C'est une suite croissante de fonctions mesurables positives.
3. **Application du TCM** : Par le TCM, $\int \lim g_n d\mu = \lim \int g_n d\mu \le M$.
4. **Finitude presque partout** : La limite $g(x) = \sum_{k=1}^\infty |f_k(x)|$ est d'intégrale finie, donc $g(x)$ est finie presque partout.
5. **Convergence simple** : Puisque la série des valeurs absolues converge presque partout, la série originale $S(x) = \sum_{k=1}^\infty f_k(x)$ converge absolument, donc simplement, presque partout.
6. **Convergence en norme** : On doit encore prouver que la convergence a lieu dans l'espace (convergence de la norme de la différence). Cela nécessitera un théorème plus avancé (convergence dominée), car la convergence en norme n'est pas garantie uniquement par le TCM sur les valeurs absolues. Cet exercice anticipe les propriétés fondamentales des espaces $L^p$.
