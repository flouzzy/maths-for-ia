---
uuid: "jalon-37-exo-1"
title: "Exercice 1 : Calculs et Propriétés de l'Intégrale de Riemann"
tags:
  - math/analyse
  - ia/calcul-integral
---

# Exercice 1

**Difficulté :** ★☆☆☆☆

**Énoncé :**
Calculer l'intégrale $\int_0^1 x^2 \, dx$ en utilisant la limite des sommes de Riemann associées à la subdivision régulière $x_k = \frac{k}{n}$ pour $0 \le k \le n$, et en évaluant la fonction aux bornes droites de chaque sous-intervalle.

**Correction détaillée :**
1. Soit $f(x) = x^2$. La fonction $f$ est continue sur $[0, 1]$, elle y est donc Riemann-intégrable.
2. On considère la subdivision régulière de l'intervalle $[0, 1]$ en $n$ sous-intervalles. Le pas est $\delta_n = \frac{1-0}{n} = \frac{1}{n}$.
3. Les points de subdivision sont $x_k = \frac{k}{n}$ pour $k \in \llbracket 0, n \rrbracket$.
4. Les points d'évaluation choisis sont les bornes droites $\xi_k = x_k = \frac{k}{n}$ pour $k \in \llbracket 1, n \rrbracket$.
5. La somme de Riemann correspondante est :
$$ S_n = \sum_{k=1}^n f(\xi_k) (x_k - x_{k-1}) = \sum_{k=1}^n \left(\frac{k}{n}\right)^2 \frac{1}{n} = \frac{1}{n^3} \sum_{k=1}^n k^2 $$
6. Nous savons par récurrence que la somme des carrés des $n$ premiers entiers est donnée par :
$$ \sum_{k=1}^n k^2 = \frac{n(n+1)(2n+1)}{6} $$
7. En substituant cette expression dans $S_n$ :
$$ S_n = \frac{1}{n^3} \frac{n(n+1)(2n+1)}{6} = \frac{(n+1)(2n+1)}{6n^2} = \frac{2n^2 + 3n + 1}{6n^2} $$
8. On factorise par le terme de plus haut degré $n^2$ au numérateur et au dénominateur :
$$ S_n = \frac{n^2 (2 + \frac{3}{n} + \frac{1}{n^2})}{6n^2} = \frac{2 + \frac{3}{n} + \frac{1}{n^2}}{6} $$
9. Lorsque $n$ tend vers l'infini, les termes $\frac{3}{n}$ et $\frac{1}{n^2}$ tendent vers 0.
10. Par conséquent, la limite de la somme de Riemann est :
$$ \lim_{n \to \infty} S_n = \frac{2}{6} = \frac{1}{3} $$
11. D'après le théorème des sommes de Riemann, comme $f$ est intégrable, cette limite coïncide avec l'intégrale :
$$ \int_0^1 x^2 \, dx = \frac{1}{3} $$
$\blacksquare$
