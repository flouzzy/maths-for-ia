---
title: "Exercice 9 : Polynôme impair"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\bigstar$"
---

# Exercice 9 : Le polynôme $t^3 - \pi^2 t$

**Niveau :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé

Soit $f$ $2\pi$-périodique définie sur $]-\pi, \pi]$ par $f(t) = t(t^2 - \pi^2)$.
1. Calculer les coefficients de Fourier de $f$.
2. En déduire la valeur de $\zeta(6) = \sum_{n=1}^\infty \frac{1}{n^6}$.

## Correction Détaillée

1. **Coefficients :**
$f$ est impaire, $a_n = 0$.
$b_n = \frac{2}{\pi} \int_0^\pi (t^3 - \pi^2 t) \sin(nt) dt$.
Par IPP successives (ou en utilisant les résultats sur $t^3$ et $t$), on trouve :
$b_n = \frac{12(-1)^n}{n^3}$.
Détail de l'IPP pour $t^3$ : $\int_0^\pi t^3 \sin(nt) = [t^3 \frac{-\cos}{n}] - \int 3t^2 \frac{-\cos}{n} = \dots$
Pour $f(t)$ qui s'annule aux bords ainsi que ses dérivées secondes :
$\int_0^\pi (t^3 - \pi^2 t) \sin(nt) dt = \frac{6(-1)^n \pi}{n^3}$.
D'où $b_n = \frac{12(-1)^n}{n^3}$.

2. **Parseval :**
$\|f\|_{L^2}^2 = \frac{1}{2\pi} \int_{-\pi}^\pi (t^3 - \pi^2 t)^2 dt = \frac{1}{\pi} \int_0^\pi (t^6 - 2\pi^2 t^4 + \pi^4 t^2) dt$.
$= \frac{1}{\pi} (\frac{\pi^7}{7} - \frac{2\pi^7}{5} + \frac{\pi^7}{3}) = \pi^6 (\frac{15 - 42 + 35}{105}) = \frac{8\pi^6}{105}$.
Parseval : $\frac{1}{2} \sum_{n=1}^\infty b_n^2 = \frac{8\pi^6}{105}$.
$\frac{1}{2} \sum_{n=1}^\infty \frac{144}{n^6} = \frac{8\pi^6}{105}$.
$72 \sum_{n=1}^\infty \frac{1}{n^6} = \frac{8\pi^6}{105}$.
$\sum_{n=1}^\infty \frac{1}{n^6} = \frac{\pi^6}{945}$.
