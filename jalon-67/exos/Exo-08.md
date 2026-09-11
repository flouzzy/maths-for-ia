---
title: "Exercice 8 : TCM"
difficulty: "★★★★☆"
---
# Exercice 8 : TCM et Dirac

**Niveau :** $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $\delta_0$ la mesure de Dirac en 0. On pose $f_n(x) = \exp(-x^2/n)$. Calculer $\lim_{n \to \infty} \int_\mathbb{R} f_n(x) d\delta_0(x)$.

**Correction détaillée :**
1. Les fonctions $f_n(x) = e^{-x^2/n}$ sont strictement positives. Pour $n \le n+1$, $1/n \ge 1/(n+1)$, donc $-x^2/n \le -x^2/(n+1)$, donc $f_n(x) \le f_{n+1}(x)$. La suite est croissante.
2. Par le théorème de convergence monotone : $\lim \int f_n d\delta_0 = \int \lim f_n d\delta_0$.
3. La limite de $f_n(x)$ est $e^0 = 1$ pour tout $x$.
4. Ainsi l'intégrale vaut $\int 1 d\delta_0 = 1$.
5. Alternativement, $\int f_n d\delta_0 = f_n(0) = 1$ pour tout $n$, la limite est trivialement 1.
