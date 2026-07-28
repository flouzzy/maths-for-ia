---
uuid: "jalon-38-exo-03"
title: "Exercice 3 : Intégrale d'une fraction rationnelle"
tags:
  - math/analyse
  - ia/calcul-differentiel
---

# Exercice 3

**Difficulté :** ★★☆☆☆

**Énoncé :**
Calculer l'intégrale $K = \int_1^2 \frac{2x + 3}{x^2 + 3x + 2} \, dx$.

**Correction détaillée :**
1. Soit la fonction intégrande $f(x) = \frac{2x + 3}{x^2 + 3x + 2}$. Le dénominateur $x^2 + 3x + 2$ s'annule lorsque $x = -1$ ou $x = -2$. Puisque l'intervalle d'intégration est $[1, 2]$, le dénominateur ne s'y annule pas. La fonction $f$ est donc continue sur $[1, 2]$, et Riemann-intégrable.
2. Observons la forme de la fonction $f$. Le numérateur est exactement la dérivée du dénominateur.
3. Posons $u(x) = x^2 + 3x + 2$. La fonction $u$ est de classe $\mathcal{C}^1$ sur $[1, 2]$.
4. Sa dérivée est $u'(x) = 2x + 3$.
5. La fonction intégrande s'écrit donc sous la forme $f(x) = \frac{u'(x)}{u(x)}$.
6. Puisque $x \in [1, 2]$, $u(x) = x^2+3x+2 > 0$. La fonction $u$ est strictement positive sur l'intervalle d'intégration.
7. Par le premier théorème fondamental de l'analyse, une primitive de la fonction $x \mapsto \frac{u'(x)}{u(x)}$ sur un intervalle où $u > 0$ est la fonction $x \mapsto \ln(u(x))$.
8. Ainsi, une primitive de $f$ est $F(x) = \ln(x^2 + 3x + 2)$.
9. Par le second théorème fondamental de l'analyse, l'intégrale s'évalue en prenant la différence des valeurs de la primitive aux bornes :
$$ K = [ \ln(x^2 + 3x + 2) ]_1^2 = \ln(2^2 + 3(2) + 2) - \ln(1^2 + 3(1) + 2) $$
10. Calculons les arguments du logarithme :
$$ 2^2 + 3(2) + 2 = 4 + 6 + 2 = 12 $$
$$ 1^2 + 3(1) + 2 = 1 + 3 + 2 = 6 $$
11. Donc $K = \ln(12) - \ln(6)$.
12. Par les propriétés algébriques du logarithme ($\ln(a) - \ln(b) = \ln(a/b)$), on obtient :
$$ K = \ln\left(\frac{12}{6}\right) = \ln(2) $$
$\blacksquare$
