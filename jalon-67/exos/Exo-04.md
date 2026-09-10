---
uuid: "jalon-67-exo-04"
title: "Exercice 04 - Convergence d'une somme exponentielle"
difficulty: "\bigstar\bigstar\bigstar\star\star"
---

# Exercice 04 - Convergence d'une somme exponentielle

## Énoncé

Soit $X = \mathbb{R}^+$ muni de la mesure de Lebesgue. Calculer $\lim_{n \to \infty} \int_0^n (1 + \frac{x}{n})^n e^{-2x} dx$.

## Correction Détaillée

1. **Construction de la suite :**
On pose $f_n(x) = (1 + \frac{x}{n})^n e^{-2x} \mathbf{1}_{[0, n]}(x)$.
Les $f_n$ sont continues (donc mesurables) et positives sur $\mathbb{R}^+$.

2. **Croissance de la suite :**
Étudions $g_n(x) = (1 + \frac{x}{n})^n$ pour $x \in [0, n]$.
On sait que la suite $u_n = (1 + \frac{x}{n})^n$ est strictement croissante avec $n$ (cela se montre par l'inégalité arithmético-géométrique ou par dérivation). De plus l'indicatrice croît (l'ensemble grandit).
Donc la suite $(f_n)$ est croissante presque partout.

3. **Limite simple :**
Pour tout $x > 0$, pour $n$ assez grand ($n > x$), $\mathbf{1}_{[0, n]}(x) = 1$.
On sait de plus que $\lim_{n \to \infty} (1 + \frac{x}{n})^n = e^x$.
Donc $\lim_{n \to \infty} f_n(x) = e^x e^{-2x} = e^{-x}$.

4. **Application du TCM :**
D'après le TCM, l'intégrale de la limite est la limite des intégrales.
$\lim_{n \to \infty} \int_0^\infty f_n(x) dx = \int_0^\infty e^{-x} dx = \left[-e^{-x}\right]_0^\infty = 1$.
