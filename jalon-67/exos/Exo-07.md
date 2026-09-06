---
uuid: "exo-67-07"
title: "Exercice 07 : Désintégration d'une masse de Dirac"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

# Exercice 07 : Désintégration d'une masse de Dirac ($\bigstar\bigstar\bigstar\bigstar\star$)

## Énoncé

Soit $\delta_0$ la mesure de Dirac en 0 sur $\mathbb{R}$. Soit $f_n(x) = n e^{-nx^2}$. Calculer $\lim_n \int f_n(x) d\delta_0$ et $\int \lim_n f_n(x) d\delta_0$. Le TCM s'applique-t-il ?

## Corrigé Rigoureux

1. **Calcul direct :** $f_n(x) \ge 0$.
L'intégrale vaut $\int f_n(x) d\delta_0 = f_n(0) = n e^0 = n$. Donc $\lim_n \int f_n d\delta_0 = +\infty$.
La limite ponctuelle : $\lim_n f_n(0) = \lim_n n = +\infty$.
2. **Beppo Levi :** La suite $(f_n(0))_{n}$ est-elle croissante ? $f_{n+1}(0) - f_n(0) = (n+1) - n = 1 > 0$. Oui, $\mu$-presque partout (ici en $x=0$, qui est le seul point de masse).
Le TCM s'applique bien, et $\int \lim f_n d\delta_0 = \int (+\infty) d\delta_0 = +\infty$. Les deux valeurs coïncident.
