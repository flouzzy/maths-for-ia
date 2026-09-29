---
title: "Exercice 4 : Onde de fréquence non entière"
difficulty: "$\bigstar\bigstar\bigstar\star\star$"
---

# Exercice 4 : Onde de fréquence non entière

**Niveau :** $\bigstar\bigstar\bigstar\star\star$

## Énoncé

Soit $a \in \mathbb{R} \setminus \mathbb{Z}$. On pose $f(t) = \cos(at)$ sur $[-\pi, \pi]$, prolongée par $2\pi$-périodicité.
1. Calculer les coefficients de Fourier de $f$.
2. Écrire l'identité de Parseval pour obtenir une formule pour $\sum_{n=1}^\infty \frac{1}{(a^2-n^2)^2}$.

## Correction Détaillée

1. **Coefficients :**
$f$ est paire, donc $b_n=0$.
$a_0 = \frac{2}{\pi} \int_0^\pi \cos(at) dt = \frac{2\sin(a\pi)}{a\pi}$.
Pour $n \ge 1$ :
$$a_n = \frac{2}{\pi} \int_0^\pi \cos(at)\cos(nt) dt = \frac{1}{\pi} \int_0^\pi (\cos((a+n)t) + \cos((a-n)t)) dt$$
$$a_n = \frac{1}{\pi} \left[ \frac{\sin((a+n)t)}{a+n} + \frac{\sin((a-n)t)}{a-n} \right]_0^\pi$$
Comme $\sin((a \pm n)\pi) = \sin(a\pi \pm n\pi) = (-1)^n \sin(a\pi)$ :
$$a_n = \frac{(-1)^n \sin(a\pi)}{\pi} \left( \frac{1}{a+n} + \frac{1}{a-n} \right) = \frac{(-1)^n \sin(a\pi)}{\pi} \frac{2a}{a^2-n^2}$$

2. **Parseval :**
Énergie :
$$\|f\|_{L^2}^2 = \frac{1}{2\pi} \int_{-\pi}^\pi \cos^2(at) dt = \frac{1}{2\pi} \int_{-\pi}^\pi \frac{1+\cos(2at)}{2} dt = \frac{1}{2} + \frac{\sin(2a\pi)}{4a\pi}$$
Parseval :
$$\frac{a_0^2}{4} + \frac{1}{2} \sum_{n=1}^\infty a_n^2 = \|f\|_{L^2}^2$$
$$\frac{\sin^2(a\pi)}{a^2\pi^2} + \frac{1}{2} \sum_{n=1}^\infty \frac{4a^2 \sin^2(a\pi)}{\pi^2 (a^2-n^2)^2} = \frac{1}{2} + \frac{\sin(2a\pi)}{4a\pi}$$
On divise par $\frac{2a^2 \sin^2(a\pi)}{\pi^2}$ pour isoler la somme :
$$\sum_{n=1}^\infty \frac{1}{(a^2-n^2)^2} = \frac{\pi^2}{2a^2 \sin^2(a\pi)} \left( \frac{1}{2} + \frac{\sin(2a\pi)}{4a\pi} - \frac{\sin^2(a\pi)}{a^2\pi^2} \right)$$
C'est une formule exacte et rigoureuse.
