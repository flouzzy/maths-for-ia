---
uuid: "jalon-37-exo-4"
title: "Exercice 4 : Calculs et Propriétés de l'Intégrale de Riemann"
tags:
  - math/analyse
  - ia/calcul-integral
---

# Exercice 4

**Difficulté :** ★★★☆☆

**Énoncé :**
On considère la suite $u_n = \sum_{k=1}^n \frac{n}{n^2 + k^2}$. En reconnaissant une somme de Riemann, déterminer la limite de cette suite lorsque $n \to +\infty$.

**Correction détaillée :**
1. Exprimons le terme général $u_n$ de manière à faire apparaître un facteur $\frac{1}{n}$ en évidence, caractéristique d'un pas régulier d'une subdivision de l'intervalle $[0, 1]$.
2. On factorise le numérateur et le dénominateur de chaque terme de la somme par $n^2$ :
$$ u_n = \sum_{k=1}^n \frac{n}{n^2(1 + (\frac{k}{n})^2)} = \sum_{k=1}^n \frac{1}{n} \frac{1}{1 + (\frac{k}{n})^2} $$
3. Posons $f(x) = \frac{1}{1 + x^2}$.
4. On remarque alors que $u_n = \frac{1}{n} \sum_{k=1}^n f(\frac{k}{n})$.
5. La fonction $f$ est une fraction rationnelle dont le dénominateur ne s'annule pas sur $\mathbb{R}$. Elle est donc continue sur $\mathbb{R}$, et en particulier sur le segment $[0, 1]$.
6. Étant continue sur le segment $[0, 1]$, la fonction $f$ y est Riemann-intégrable.
7. L'expression de $u_n$ est exactement la somme de Riemann de $f$ sur $[0, 1]$ associée à la subdivision régulière de pas $\frac{1}{n}$, évaluée aux bornes droites $x_k = \frac{k}{n}$.
8. D'après le théorème de convergence des sommes de Riemann :
$$ \lim_{n \to +\infty} u_n = \int_0^1 f(x) \, dx = \int_0^1 \frac{1}{1 + x^2} \, dx $$
9. Une primitive usuelle de $x \mapsto \frac{1}{1 + x^2}$ est la fonction $\arctan$.
10. On évalue cette primitive entre les bornes :
$$ \int_0^1 \frac{1}{1 + x^2} \, dx = [\arctan(x)]_0^1 = \arctan(1) - \arctan(0) $$
11. Comme $\arctan(1) = \frac{\pi}{4}$ et $\arctan(0) = 0$, on conclut que :
$$ \lim_{n \to +\infty} u_n = \frac{\pi}{4} $$
$\blacksquare$
