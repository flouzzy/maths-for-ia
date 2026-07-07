---
uuid: "jalon-20-exo-06"
title: "Exercice 06 : ★★★☆☆"
---
# Exercice 06

## Énoncé
Montrer que l'équation $e^x = 1 + x + \frac{x^2}{2}$ admet exactement une racine réelle strictement positive ou aucune. Préciser le cas.

## Correction
1. Soit $f(x) = e^x - (1 + x + \frac{x^2}{2})$.
2. D'après la formule de Taylor-Lagrange à l'ordre 2 sur $[0, x]$ avec $x > 0$ :
   Il existe $c \in ]0, x[$ tel que $e^x = 1 + x + \frac{x^2}{2} + \frac{e^c}{6} x^3$.
3. Réécrivons l'équation $f(x) = 0$ :
   $1 + x + \frac{x^2}{2} + \frac{e^c}{6} x^3 - (1 + x + \frac{x^2}{2}) = 0$.
   $\frac{e^c}{6} x^3 = 0$.
4. Puisque l'exponentielle $e^c$ est strictement positive pour tout réel $c$, et que nous cherchons des solutions $x > 0$ (donc $x^3 > 0$), le produit $\frac{e^c}{6} x^3$ est strictement positif.
5. Par conséquent, il est impossible que $f(x) = 0$ pour $x > 0$.
6. Conclusion : L'équation n'admet aucune racine réelle strictement positive. $\blacksquare$