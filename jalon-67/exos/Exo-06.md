---
uuid: "jalon-67-exo-06"
title: "Exercice 06 - Fonction pôle et sommation"
difficulty: "\bigstar\bigstar\bigstar\bigstar\star"
---

# Exercice 06 - Fonction pôle et sommation

## Énoncé

En utilisant un développement en série et le TCM, calculer rigoureusement $\int_0^1 \frac{-\ln(x)}{1-x} dx$.

## Correction Détaillée

1. **Développement en série :**
Pour $x \in (0, 1)$, $\frac{1}{1-x} = \sum_{n=0}^\infty x^n$.
Donc $f(x) = \frac{-\ln(x)}{1-x} = \sum_{n=0}^\infty (-x^n \ln(x))$.
Posons $u_n(x) = -x^n \ln(x)$. Pour $x \in (0, 1)$, $\ln(x) < 0$, donc $u_n(x) \ge 0$. Les $u_n$ sont continues et positives.

2. **Application du Corollaire du TCM :**
Puisque tous les termes sont positifs, on peut intervertir série et intégrale :
$$\int_0^1 \frac{-\ln(x)}{1-x} dx = \sum_{n=0}^\infty \int_0^1 (-x^n \ln(x)) dx$$

3. **Calcul de l'intégrale par IPP :**
On pose $u(x) = -\ln(x) \implies u'(x) = -1/x$
$v'(x) = x^n \implies v(x) = \frac{x^{n+1}}{n+1}$.
$\int_0^1 (-x^n \ln(x)) dx = \left[ -\ln(x) \frac{x^{n+1}}{n+1} \right]_0^1 - \int_0^1 (-\frac{1}{x}) \frac{x^{n+1}}{n+1} dx$.
Le terme de bord tend vers 0 en 0 (par croissances comparées) et est nul en 1.
Il reste $\int_0^1 \frac{x^n}{n+1} dx = \left[ \frac{x^{n+1}}{(n+1)^2} \right]_0^1 = \frac{1}{(n+1)^2}$.

4. **Sommation finale :**
La série vaut $\sum_{n=0}^\infty \frac{1}{(n+1)^2} = \sum_{k=1}^\infty \frac{1}{k^2} = \frac{\pi^2}{6}$.
