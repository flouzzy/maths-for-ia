---
title: "Exercice 3 : La parabole périodisée"
difficulty: "$\bigstar\bigstar\star\star\star$"
---

# Exercice 3 : La parabole périodisée et $\zeta(4)$

**Niveau :** $\bigstar\bigstar\star\star\star$

## Énoncé

Soit $f$, $2\pi$-périodique, telle que $f(t) = t^2$ sur $[-\pi, \pi]$.
1. Calculer sa série de Fourier.
2. Déduire de l'identité de Parseval la valeur de $\zeta(4) = \sum_{n=1}^\infty \frac{1}{n^4}$.

## Correction Détaillée

1. **Coefficients :**
La fonction est paire, $b_n = 0$.
$a_0 = \frac{1}{\pi} \int_{-\pi}^\pi t^2 dt = \frac{2\pi^2}{3}$.
Pour $n \ge 1$ :
$$a_n = \frac{2}{\pi} \int_0^\pi t^2 \cos(nt) dt$$
Double intégration par parties :
$$a_n = \frac{2}{\pi} \left( \left[ t^2 \frac{\sin(nt)}{n} \right]_0^\pi - \frac{2}{n} \int_0^\pi t \sin(nt) dt \right) = \frac{-4}{\pi n} \int_0^\pi t \sin(nt) dt$$
Deuxième IPP :
$$a_n = \frac{-4}{\pi n} \left( \left[ t \frac{-\cos(nt)}{n} \right]_0^\pi - \int_0^\pi \frac{-\cos(nt)}{n} dt \right)$$
$$a_n = \frac{-4}{\pi n} \left( -\pi \frac{(-1)^n}{n} \right) = \frac{4(-1)^n}{n^2}$$

2. **Parseval :**
Énergie :
$$\|f\|_{L^2}^2 = \frac{1}{2\pi} \int_{-\pi}^\pi t^4 dt = \frac{1}{2\pi} \left[ \frac{t^5}{5} \right]_{-\pi}^\pi = \frac{\pi^4}{5}$$
Formule de Parseval :
$$\frac{a_0^2}{4} + \frac{1}{2} \sum_{n=1}^\infty a_n^2 = \frac{\pi^4}{5}$$
$$\frac{1}{4} \frac{4\pi^4}{9} + \frac{1}{2} \sum_{n=1}^\infty \frac{16}{n^4} = \frac{\pi^4}{5}$$
$$\frac{\pi^4}{9} + 8 \sum_{n=1}^\infty \frac{1}{n^4} = \frac{\pi^4}{5}$$
$$8 \sum_{n=1}^\infty \frac{1}{n^4} = \frac{\pi^4}{5} - \frac{\pi^4}{9} = \frac{4\pi^4}{45}$$
$$\sum_{n=1}^\infty \frac{1}{n^4} = \frac{\pi^4}{90}$$
