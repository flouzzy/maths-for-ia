---
title: "Exercice 7 : Signal redressé simple alternance"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

# Exercice 7 : Redressement simple alternance d'un sinus

**Niveau :** $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé

Soit $f$ $2\pi$-périodique définie par $f(t) = \sin(t)$ sur $[0, \pi]$ et $0$ sur $]-\pi, 0[$.
1. Calculer ses coefficients de Fourier $a_n$ et $b_n$.
2. Utiliser Parseval pour calculer $\sum_{p=1}^\infty \frac{1}{(4p^2-1)^2}$.

## Correction Détaillée

1. **Coefficients :**
$a_0 = \frac{1}{\pi} \int_0^\pi \sin(t) dt = \frac{2}{\pi}$.
$a_n = \frac{1}{\pi} \int_0^\pi \sin(t)\cos(nt) dt = \frac{1}{2\pi} \int_0^\pi (\sin((1+n)t) + \sin((1-n)t)) dt$.
Si $n=1$, $a_1 = \frac{1}{2\pi} \int_0^\pi \sin(2t) dt = 0$.
Si $n>1$, $a_n = \frac{1}{2\pi} \left[ -\frac{\cos((n+1)t)}{n+1} + \frac{\cos((n-1)t)}{n-1} \right]_0^\pi$.
$a_n = \frac{1}{2\pi} \left( \frac{1 - (-1)^{n+1}}{n+1} - \frac{1 - (-1)^{n-1}}{n-1} \right)$.
Pour $n$ impair, $(-1)^{n+1}=1$, $a_n = 0$.
Pour $n$ pair ($n=2p$), $(-1)^{n+1}=-1$, $a_{2p} = \frac{1}{2\pi} \left( \frac{2}{2p+1} - \frac{2}{2p-1} \right) = \frac{-2}{\pi(4p^2-1)}$.

Pour $b_n$ : $b_n = \frac{1}{\pi} \int_0^\pi \sin(t)\sin(nt) dt$.
$b_1 = \frac{1}{\pi} \int_0^\pi \sin^2(t) dt = \frac{1}{2}$.
Pour $n>1$, $b_n = \frac{1}{2\pi} \int_0^\pi (\cos((n-1)t) - \cos((n+1)t)) dt = 0$.

2. **Parseval :**
$\|f\|_{L^2}^2 = \frac{1}{2\pi} \int_0^\pi \sin^2(t) dt = \frac{1}{4}$.
Parseval : $\frac{a_0^2}{4} + \frac{1}{2} a_1^2 + \frac{1}{2} b_1^2 + \frac{1}{2} \sum_{p=1}^\infty a_{2p}^2 = \frac{1}{4}$.
$\frac{1}{\pi^2} + 0 + \frac{1}{8} + \frac{1}{2} \sum_{p=1}^\infty \frac{4}{\pi^2(4p^2-1)^2} = \frac{1}{4}$.
$\frac{2}{\pi^2} \sum_{p=1}^\infty \frac{1}{(4p^2-1)^2} = \frac{1}{8} - \frac{1}{\pi^2}$.
$\sum_{p=1}^\infty \frac{1}{(4p^2-1)^2} = \frac{\pi^2}{16} - \frac{1}{2}$.
