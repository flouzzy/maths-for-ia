---
uuid: "jalon-67-exo-07"
title: "Exercice 07 - La fonction de Dirac analytique"
difficulty: "\bigstar\bigstar\bigstar\bigstar\star"
---

# Exercice 07 - La fonction de Dirac analytique

## Énoncé

Soit $f_n(x) = n e^{-nx}$ sur $(0, \infty)$.
1. Déterminer la limite simple de $f_n(x)$.
2. Calculer $\lim_{n \to \infty} \int_0^\infty f_n(x) dx$.
3. Le théorème de convergence monotone est-il applicable ? Pourquoi ?

## Correction Détaillée

1. **Limite simple :**
Pour $x > 0$ fixé, $\lim_{n \to \infty} n e^{-nx} = 0$ par croissances comparées (l'exponentielle l'emporte). Donc $f(x) = 0$ partout.

2. **Intégrale des termes de la suite :**
$\int_0^\infty n e^{-nx} dx = \left[ -e^{-nx} \right]_0^\infty = 0 - (-1) = 1$.
Donc $\lim_{n \to \infty} \int_0^\infty f_n(x) dx = 1$.

3. **Discussion sur le TCM :**
Ici, $\int_0^\infty \lim f_n(x) dx = \int 0 dx = 0$, mais $\lim \int_0^\infty f_n(x) dx = 1$.
L'égalité n'est pas vérifiée. Le théorème de convergence monotone ne s'applique pas car la suite $(f_n)$ **n'est pas croissante**.
En effet, pour $x=1$, $f_1(1) = e^{-1} \approx 0.36$, mais pour $n=10$, $f_{10}(1) = 10 e^{-10} \approx 0.00045$, la fonction décroît vers 0 en dehors de l'origine (la masse se concentre vers 0).
