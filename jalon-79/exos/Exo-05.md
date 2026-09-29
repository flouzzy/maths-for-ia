---
title: "Exercice 5 : La fonction exponentielle"
difficulty: "$\bigstar\bigstar\bigstar\star\star$"
---

# Exercice 5 : La fonction exponentielle et Parseval

**Niveau :** $\bigstar\bigstar\bigstar\star\star$

## Énoncé

Soit $a \in \mathbb{R}^*$. $f$ est définie par $f(t) = e^{at}$ sur $]-\pi, \pi]$ et $2\pi$-périodique.
1. Calculer les coefficients de Fourier complexes $c_n$.
2. En appliquant l'identité de Parseval, évaluer la somme $\sum_{n=1}^\infty \frac{1}{a^2 + n^2}$.

## Correction Détaillée

1. **Coefficients de Fourier complexes :**
$$c_n = \frac{1}{2\pi} \int_{-\pi}^\pi e^{at} e^{-int} dt = \frac{1}{2\pi} \int_{-\pi}^\pi e^{(a-in)t} dt$$
$$c_n = \frac{1}{2\pi} \left[ \frac{e^{(a-in)t}}{a-in} \right]_{-\pi}^\pi = \frac{e^{(a-in)\pi} - e^{-(a-in)\pi}}{2\pi(a-in)}$$
Puisque $e^{\pm in\pi} = (-1)^n$, on obtient :
$$c_n = (-1)^n \frac{e^{a\pi} - e^{-a\pi}}{2\pi(a-in)} = (-1)^n \frac{\sinh(a\pi)}{\pi(a-in)}$$
Son module au carré est :
$$|c_n|^2 = \frac{\sinh^2(a\pi)}{\pi^2 (a^2 + n^2)}$$

2. **Identité de Parseval :**
Énergie :
$$\|f\|_{L^2}^2 = \frac{1}{2\pi} \int_{-\pi}^\pi |e^{at}|^2 dt = \frac{1}{2\pi} \int_{-\pi}^\pi e^{2at} dt = \frac{e^{2a\pi} - e^{-2a\pi}}{4a\pi} = \frac{\sinh(2a\pi)}{2a\pi}$$
Parseval donne : $\sum_{n=-\infty}^\infty |c_n|^2 = \|f\|_{L^2}^2$.
$$ \sum_{n=-\infty}^\infty \frac{\sinh^2(a\pi)}{\pi^2 (a^2 + n^2)} = \frac{\sinh(2a\pi)}{2a\pi} $$
On sépare le terme $n=0$ :
$$ \frac{\sinh^2(a\pi)}{\pi^2 a^2} + 2 \sum_{n=1}^\infty \frac{\sinh^2(a\pi)}{\pi^2 (a^2 + n^2)} = \frac{2\sinh(a\pi)\cosh(a\pi)}{2a\pi} $$
En simplifiant et en utilisant $\sinh(2a\pi) = 2\sinh(a\pi)\cosh(a\pi)$, et en divisant par $\frac{2\sinh^2(a\pi)}{\pi^2}$ :
$$ \sum_{n=1}^\infty \frac{1}{a^2+n^2} = \frac{\pi \coth(a\pi)}{2a} - \frac{1}{2a^2} $$
