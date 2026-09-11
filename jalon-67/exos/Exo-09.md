---
uuid: "jalon-67-exo-09"
title: "Exercice 09 - Intégrale de Dirichlet et séries"
difficulty: "\bigstar\bigstar\bigstar\bigstar\bigstar"
---

# Exercice 09 - Intégrale de Dirichlet et séries

## Énoncé

Montrer que pour tout $p > 1$, $\int_0^\infty \frac{x^{p-1}}{e^x - 1} dx = \Gamma(p) \zeta(p)$, où $\Gamma$ est la fonction d'Euler et $\zeta$ la fonction zêta de Riemann.

## Correction Détaillée

1. **Développement en série :**
Pour $x > 0$, $e^x > 1$, on a $e^{-x} < 1$.
$\frac{x^{p-1}}{e^x - 1} = \frac{x^{p-1} e^{-x}}{1 - e^{-x}}$.
En utilisant le développement de la série géométrique $\frac{1}{1-q} = \sum_{n=0}^\infty q^n$ pour $q = e^{-x} \in (0, 1)$ :
$\frac{x^{p-1} e^{-x}}{1 - e^{-x}} = x^{p-1} e^{-x} \sum_{n=0}^\infty e^{-nx} = \sum_{n=1}^\infty x^{p-1} e^{-nx}$.

2. **Positivité :**
Pour $x > 0$, les termes $u_n(x) = x^{p-1} e^{-nx}$ sont strictement positifs. La somme est mesurable.

3. **Interversion par le TCM :**
D'après le corollaire du TCM pour les séries positives, on peut intervertir l'intégrale et la somme :
$$\int_0^\infty \left( \sum_{n=1}^\infty x^{p-1} e^{-nx} \right) dx = \sum_{n=1}^\infty \int_0^\infty x^{p-1} e^{-nx} dx$$

4. **Calcul de l'intégrale (Changement de variable) :**
Pour calculer $I_n = \int_0^\infty x^{p-1} e^{-nx} dx$, posons le changement de variable $u = nx$.
$dx = \frac{du}{n}$, et $x = \frac{u}{n}$.
$I_n = \int_0^\infty \left(\frac{u}{n}\right)^{p-1} e^{-u} \frac{du}{n} = \frac{1}{n^p} \int_0^\infty u^{p-1} e^{-u} du$.
On reconnaît l'intégrale définissant la fonction Gamma : $I_n = \frac{1}{n^p} \Gamma(p)$.

5. **Sommation finale :**
La série totale devient :
$\sum_{n=1}^\infty I_n = \sum_{n=1}^\infty \frac{\Gamma(p)}{n^p} = \Gamma(p) \sum_{n=1}^\infty \frac{1}{n^p} = \Gamma(p) \zeta(p)$.
Le calcul est rigoureusement prouvé par le TCM.
