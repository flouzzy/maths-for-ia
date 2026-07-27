---
uuid: "jalon-37-exo-5"
title: "Exercice 5 : Calculs et Propriétés de l'Intégrale de Riemann"
tags:
  - math/analyse
  - ia/calcul-integral
---

# Exercice 5

**Difficulté :** ★★★☆☆

**Énoncé :**
Montrer que la fonction $f : [0, 1] \to \mathbb{R}$ définie par $f(x) = 1$ si $x = 1/2$, et $f(x) = 0$ sinon, est Riemann-intégrable et calculer son intégrale.

**Correction détaillée :**
1. Soit $\epsilon > 0$. Nous allons trouver une subdivision $\sigma$ telle que $S_+(\sigma, f) - S_-(\sigma, f) < \epsilon$.
2. Considérons la subdivision $\sigma = (0, \frac{1}{2} - \frac{\epsilon}{4}, \frac{1}{2} + \frac{\epsilon}{4}, 1)$ de l'intervalle $[0, 1]$. (Si $\epsilon$ est grand, on prend $\sigma$ adapté pour rester dans $[0,1]$).
3. Les sous-intervalles sont $I_1 = [0, \frac{1}{2} - \frac{\epsilon}{4}]$, $I_2 = [\frac{1}{2} - \frac{\epsilon}{4}, \frac{1}{2} + \frac{\epsilon}{4}]$ et $I_3 = [\frac{1}{2} + \frac{\epsilon}{4}, 1]$.
4. Sur $I_1$, $f(x) = 0$, donc $m_1 = M_1 = 0$.
5. Sur $I_3$, $f(x) = 0$, donc $m_3 = M_3 = 0$.
6. Sur $I_2$, le point $1/2$ est présent. $f(1/2) = 1$ et pour $x \neq 1/2$, $f(x) = 0$. Donc $m_2 = 0$ et $M_2 = 1$.
7. Calculons les sommes de Darboux :
   - $S_-(\sigma, f) = 0 \cdot (\frac{1}{2} - \frac{\epsilon}{4} - 0) + 0 \cdot (\frac{\epsilon}{2}) + 0 \cdot (1 - (\frac{1}{2} + \frac{\epsilon}{4})) = 0$.
   - $S_+(\sigma, f) = 0 \cdot (\frac{1}{2} - \frac{\epsilon}{4}) + 1 \cdot (\frac{\epsilon}{2}) + 0 \cdot (1 - (\frac{1}{2} + \frac{\epsilon}{4})) = \frac{\epsilon}{2}$.
8. Ainsi, $S_+(\sigma, f) - S_-(\sigma, f) = \frac{\epsilon}{2} < \epsilon$.
9. Ceci prouve que $f$ est Riemann-intégrable sur $[0, 1]$.
10. De plus, comme $\forall \sigma, S_-(\sigma, f) = 0$, on a $I_-(f) = 0$. L'intégrale vaut donc $\int_0^1 f(x) \, dx = 0$.
$\blacksquare$
