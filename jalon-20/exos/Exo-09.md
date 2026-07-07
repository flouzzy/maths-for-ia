---
uuid: "jalon-20-exo-09"
title: "Exercice 09 : ★★★★★"
---
# Exercice 09

## Énoncé
Lemme de Morse (cas scalaire unidimensionnel). Soit $f$ de classe $C^3$ au voisinage de $0$, telle que $f(0)=0, f'(0)=0, f''(0)=2$. Montrer qu'il existe un difféomorphisme local $\varphi$ autour de $0$ tel que $f(\varphi(x)) = x^2$.

## Correction
1. Par la formule de Taylor avec reste intégral (ou en factorisant par $x^2$), puisque $f(0)=0$ et $f'(0)=0$, on peut écrire :
   $f(x) = x^2 h(x)$ avec $h(0) = \frac{f''(0)}{2} = 1$.
   De plus, comme $f$ est $C^3$, $h$ est de classe $C^1$ au voisinage de $0$.
2. Comme $h(0) = 1 > 0$, par continuité de $h$, il existe un voisinage $V$ de $0$ sur lequel $h(x) > 0$.
3. Sur ce voisinage, on peut définir $g(x) = x \sqrt{h(x)}$.
4. La fonction $g$ est de classe $C^1$ sur $V$. Calculons sa dérivée en $0$ :
   $g'(x) = \sqrt{h(x)} + x \frac{h'(x)}{2\sqrt{h(x)}}$.
   $g'(0) = \sqrt{h(0)} + 0 = 1$.
5. Comme $g'(0) \neq 0$, le théorème d'inversion locale assure que $g$ est un difféomorphisme local d'un voisinage $W$ de $0$ sur un voisinage $U$ de $0$.
6. Soit $\varphi = g^{-1}$. $\varphi$ est un difféomorphisme de $U$ vers $W$.
7. Pour $y \in U$, soit $x = \varphi(y) \iff y = g(x)$.
   Calculons $f(x) = x^2 h(x) = (x \sqrt{h(x)})^2 = g(x)^2 = y^2$.
8. Ainsi, pour tout $y \in U$, $f(\varphi(y)) = y^2$. En renommant la variable, la preuve est achevée. $\blacksquare$