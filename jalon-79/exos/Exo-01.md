---
title: "Exercice 1 : Fonction Signe et série numérique"
difficulty: "$\bigstar\star\star\star\star$"
---

# Exercice 1 : Fonction Signe et série de Bâle modifiée

**Niveau :** $\bigstar\star\star\star\star$

## Énoncé

Soit la fonction $f$, $2\pi$-périodique, définie sur $]-\pi, \pi]$ par :
$f(t) = -1$ si $t \in ]-\pi, 0[$, $f(t) = 1$ si $t \in ]0, \pi]$, et $f(0)=0$.
1. Calculer les coefficients de Fourier de $f$.
2. En utilisant l'identité de Parseval, calculer la somme $\sum_{p=0}^\infty \frac{1}{(2p+1)^2}$.

## Correction Détaillée

1. **Calcul des coefficients :**
La fonction est impaire, donc $a_n = 0$ pour tout $n \ge 0$.
Pour $n \ge 1$ :
$$b_n = \frac{1}{\pi} \int_{-\pi}^\pi f(t) \sin(nt) dt = \frac{2}{\pi} \int_0^\pi \sin(nt) dt$$
$$b_n = \frac{2}{\pi} \left[ \frac{-\cos(nt)}{n} \right]_0^\pi = \frac{2}{\pi n} (1 - \cos(n\pi)) = \frac{2(1 - (-1)^n)}{\pi n}$$
Si $n=2p$, $b_{2p} = 0$.
Si $n=2p+1$, $b_{2p+1} = \frac{4}{\pi(2p+1)}$.

2. **Identité de Parseval :**
Calculons l'énergie totale sur une période :
$$\|f\|_{L^2}^2 = \frac{1}{2\pi} \int_{-\pi}^\pi (f(t))^2 dt = \frac{1}{2\pi} \int_{-\pi}^\pi 1 dt = 1$$
D'après l'identité de Parseval :
$$\frac{a_0^2}{4} + \frac{1}{2} \sum_{n=1}^\infty (a_n^2 + b_n^2) = \|f\|_{L^2}^2$$
$$ \frac{1}{2} \sum_{p=0}^\infty \left( \frac{4}{\pi(2p+1)} \right)^2 = 1 $$
$$ \frac{8}{\pi^2} \sum_{p=0}^\infty \frac{1}{(2p+1)^2} = 1 \implies \sum_{p=0}^\infty \frac{1}{(2p+1)^2} = \frac{\pi^2}{8} $$
