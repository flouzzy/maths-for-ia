---
uuid: "jalon-38-exo-10"
title: "Exercice 10 : Sommes de Riemann et exponentielle"
tags:
  - math/analyse
  - ia/calcul-differentiel
---

# Exercice 10

**Difficulté :** ★★★★★

**Énoncé :**
Calculer la limite de la suite $u_n = \sum_{k=1}^n \frac{n}{n^2 + k^2}$ lorsque $n \to +\infty$.

**Correction détaillée :**
1. Il s'agit d'une limite de somme. Cherchons à la mettre sous la forme d'une somme de Riemann.
2. Rappel du théorème des sommes de Riemann : si $f$ est intégrable sur $[0, 1]$, alors $\lim_{n \to \infty} \frac{1}{n} \sum_{k=1}^n f\left(\frac{k}{n}\right) = \int_0^1 f(x) \, dx$.
3. Factorisons le terme général de la suite $u_n$ pour faire apparaître la forme $f(k/n) \times (1/n)$.
4. Dans l'expression $\frac{n}{n^2 + k^2}$, factorisons par $n^2$ au dénominateur :
$$ \frac{n}{n^2(1 + \frac{k^2}{n^2})} = \frac{1}{n(1 + (\frac{k}{n})^2)} $$
5. On peut alors réécrire la somme ainsi :
$$ u_n = \sum_{k=1}^n \frac{1}{n} \frac{1}{1 + (k/n)^2} = \frac{1}{n} \sum_{k=1}^n \frac{1}{1 + (k/n)^2} $$
6. On reconnaît exactement la structure d'une somme de Riemann pour la fonction $f(x) = \frac{1}{1 + x^2}$ sur l'intervalle $[0, 1]$.
7. La fonction $f$ est une fraction rationnelle dont le dénominateur ne s'annule jamais sur $\mathbb{R}$. Elle est donc continue sur $\mathbb{R}$, et en particulier sur $[0, 1]$.
8. Par le théorème des sommes de Riemann, la suite $u_n$ converge et sa limite est :
$$ \lim_{n \to \infty} u_n = \int_0^1 f(x) \, dx = \int_0^1 \frac{1}{1 + x^2} \, dx $$
9. Il ne reste plus qu'à calculer formellement cette intégrale par le théorème fondamental.
10. La primitive usuelle de $x \mapsto \frac{1}{1+x^2}$ est la fonction arctangente (notée $\arctan$).
11. On évalue la primitive aux bornes :
$$ \int_0^1 \frac{1}{1 + x^2} \, dx = [\arctan(x)]_0^1 = \arctan(1) - \arctan(0) $$
12. Les valeurs remarquables de la fonction arctangente sont $\arctan(1) = \frac{\pi}{4}$ et $\arctan(0) = 0$.
13. Finalement :
$$ \lim_{n \to \infty} u_n = \frac{\pi}{4} $$
$\blacksquare$
