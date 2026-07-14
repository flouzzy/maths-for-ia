---
title: "Exercice 2 : Produit de Cauchy de la série exponentielle"
difficulty: ★☆☆☆☆
---
# Exercice 2 : Produit de Cauchy de la série exponentielle

## Énoncé
Soit la série exponentielle définie par $E(x) = \sum_{n=0}^\infty \frac{x^n}{n!}$. Démontrer, à l'aide du produit de Cauchy, que pour tous réels $x, y$, on a $E(x)E(y) = E(x+y)$.

## Correction

1. **Convergence Absolue :** Fixons $x \in \mathbb{R}$. Étudions la convergence de la série $\sum \frac{x^n}{n!}$. On applique la règle de d'Alembert pour la série des valeurs absolues :
   $\lim_{n\to\infty} \frac{|x|^{n+1}/(n+1)!}{|x|^n/n!} = \lim_{n\to\infty} \frac{|x|}{n+1} = 0$.
   Puisque $0 < 1$, la série converge absolument sur $\mathbb{R}$.
2. **Calcul du produit de Cauchy :** Puisque les deux séries $E(x)$ et $E(y)$ convergent absolument, on peut appliquer le théorème de Mertens. Leur produit de Cauchy converge vers $E(x)E(y)$.
   Le terme général $c_n$ de la série produit de Cauchy est donné par :
   $$c_n = \sum_{k=0}^n a_k b_{n-k} = \sum_{k=0}^n \frac{x^k}{k!} \frac{y^{n-k}}{(n-k)!}$$
3. **Utilisation de la formule du binôme :** On multiplie et divise par $n!$ pour faire apparaître un coefficient binomial :
   $$c_n = \frac{1}{n!} \sum_{k=0}^n \frac{n!}{k!(n-k)!} x^k y^{n-k} = \frac{1}{n!} \sum_{k=0}^n \binom{n}{k} x^k y^{n-k}$$
   D'après la formule du binôme de Newton, la somme de droite vaut $(x+y)^n$. Ainsi, $c_n = \frac{(x+y)^n}{n!}$.
4. **Conclusion :** Le produit de Cauchy est la série $\sum c_n = \sum_{n=0}^\infty \frac{(x+y)^n}{n!}$. D'après le théorème de Mertens, cette série converge vers $E(x)E(y)$. Or par définition, c'est exactement $E(x+y)$. Donc $E(x)E(y) = E(x+y)$.
