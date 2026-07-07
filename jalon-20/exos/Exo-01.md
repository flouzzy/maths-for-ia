---
uuid: "jalon-20-exo-01"
title: "Exercice 01 : ★☆☆☆☆"
---
# Exercice 01

## Énoncé
Calculer le développement limité de la fonction $f(x) = e^x \cos(x)$ à l'ordre 2 en $x = 0$. Démontrer chaque étape avec rigueur.

## Correction
1. Le DL de $e^x$ en $0$ à l'ordre 2 est : $e^x = 1 + x + \frac{x^2}{2} + o(x^2)$.
2. Le DL de $\cos(x)$ en $0$ à l'ordre 2 est : $\cos(x) = 1 - \frac{x^2}{2} + o(x^2)$.
3. Par produit des parties principales :
   $f(x) = (1 + x + \frac{x^2}{2})(1 - \frac{x^2}{2}) + o(x^2)$
4. En développant et en ne conservant que les monômes de degré inférieur ou égal à 2 :
   $f(x) = 1(1 - \frac{x^2}{2}) + x(1 - \frac{x^2}{2}) + \frac{x^2}{2}(1 - \frac{x^2}{2}) + o(x^2)$
   $f(x) = 1 - \frac{x^2}{2} + x - \frac{x^3}{2} + \frac{x^2}{2} - \frac{x^4}{4} + o(x^2)$
5. Troncature :
   $f(x) = 1 + x + (-\frac{1}{2} + \frac{1}{2})x^2 + o(x^2) = 1 + x + o(x^2)$.

La rigueur de la troncature justifie la validité du polynôme obtenu par unicité du DL. $\blacksquare$