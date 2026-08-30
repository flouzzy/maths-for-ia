---
title: "Exercice 2 : Convergence non monotone"
difficulty: "$\bigstar\star\star\star\star$"
---

# Exercice 2 : Convergence non monotone

## Énoncé

Sur $([0, 1], \mathcal{B}([0, 1]), \lambda)$, on définit $f_n(x) = n e^{-nx}$.
1. Déterminer la limite ponctuelle $f$ de la suite $(f_n)$.
2. Calculer $\int_0^1 f_n(x) d\lambda$.
3. Le théorème de convergence monotone peut-il s'appliquer ici ? Pourquoi ?

## Correction

1. **Limite ponctuelle :**
Pour $x = 0$, $f_n(0) = n$, qui tend vers $+\infty$.
Pour $x > 0$, la croissance exponentielle l'emporte sur le facteur polynomial. $\lim_{n \to \infty} n e^{-nx} = 0$.
Donc $f(x) = 0$ presque partout (sauf en $x=0$, qui est de mesure nulle).

2. **Calcul de l'intégrale :**
$\int_0^1 n e^{-nx} dx = \left[ -e^{-nx} \right]_0^1 = -e^{-n} - (-1) = 1 - e^{-n}$.
Donc $\lim_{n \to \infty} \int_0^1 f_n(x) dx = \lim_{n \to \infty} (1 - e^{-n}) = 1$.

3. **Analyse de Beppo Levi :**
L'intégrale de la limite presque partout est $\int_0^1 0 dx = 0$.
On a donc $\lim \int f_n = 1 \neq \int f = 0$.
Le théorème de convergence monotone ne s'applique pas car la suite $(f_n)$ **n'est pas croissante**. En effet, pour un $x>0$ fixé, dès que $nx > 1$, la fonction $t \mapsto t e^{-tx}$ est décroissante, donc la suite diminue vers 0, elle ne "gonfle" pas vers sa limite. La "masse" s'échappe vers la singularité en 0.
