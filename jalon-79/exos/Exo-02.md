---
title: "Exercice 2 : Valeur absolue et sommes de séries"
difficulty: "$\bigstar\bigstar\star\star\star$"
---

# Exercice 2 : Valeur absolue et sommes de séries

**Niveau :** $\bigstar\bigstar\star\star\star$

## Énoncé

Soit $f$ la fonction $2\pi$-périodique, définie sur $[-\pi, \pi]$ par $f(t) = |t|$.
1. Déterminer la série de Fourier de $f$.
2. En déduire, via le théorème de Parseval, la valeur de $\sum_{p=0}^\infty \frac{1}{(2p+1)^4}$.

## Correction Détaillée

1. **Coefficients de Fourier :**
La fonction est paire, donc $b_n = 0$ pour tout $n \ge 1$.
Calcul de $a_0$ :
$$a_0 = \frac{1}{\pi} \int_{-\pi}^\pi |t| dt = \frac{2}{\pi} \int_0^\pi t dt = \frac{2}{\pi} \frac{\pi^2}{2} = \pi$$
Pour $n \ge 1$, calcul de $a_n$ avec une IPP :
$$a_n = \frac{2}{\pi} \int_0^\pi t \cos(nt) dt = \frac{2}{\pi} \left( \left[ t \frac{\sin(nt)}{n} \right]_0^\pi - \int_0^\pi \frac{\sin(nt)}{n} dt \right)$$
Le crochet est nul.
$$a_n = \frac{2}{\pi} \left[ \frac{\cos(nt)}{n^2} \right]_0^\pi = \frac{2}{\pi n^2} ((-1)^n - 1)$$
Ainsi, $a_{2p} = 0$ et $a_{2p+1} = \frac{-4}{\pi(2p+1)^2}$.

2. **Identité de Parseval :**
Énergie de $f$ :
$$\|f\|_{L^2}^2 = \frac{1}{2\pi} \int_{-\pi}^\pi |t|^2 dt = \frac{1}{2\pi} \int_{-\pi}^\pi t^2 dt = \frac{2\pi^3}{6\pi} = \frac{\pi^2}{3}$$
Parseval donne :
$$\frac{a_0^2}{4} + \frac{1}{2} \sum_{n=1}^\infty a_n^2 = \frac{\pi^2}{3}$$
$$\frac{\pi^2}{4} + \frac{1}{2} \sum_{p=0}^\infty \left( \frac{-4}{\pi(2p+1)^2} \right)^2 = \frac{\pi^2}{3}$$
$$\frac{8}{\pi^2} \sum_{p=0}^\infty \frac{1}{(2p+1)^4} = \frac{\pi^2}{3} - \frac{\pi^2}{4} = \frac{\pi^2}{12}$$
$$ \sum_{p=0}^\infty \frac{1}{(2p+1)^4} = \frac{\pi^4}{96} $$
