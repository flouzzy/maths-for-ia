---
uuid: "jalon-20-exo-03"
title: "Exercice 03 : ★★☆☆☆"
---
# Exercice 03

## Énoncé
Calculer le développement limité de la fonction $f(x) = \ln(1 + \sin(x))$ à l'ordre 3 en $x = 0$. Démontrer chaque étape avec rigueur.

## Correction
1. Soit $u = \sin(x)$. Comme $x \to 0$, on a $u \to 0$.
2. Le DL de $\sin(x)$ en $0$ à l'ordre 3 est :
   $u(x) = x - \frac{x^3}{6} + o(x^3)$.
3. Le DL de $\ln(1+u)$ en $u=0$ à l'ordre 3 est :
   $\ln(1+u) = u - \frac{u^2}{2} + \frac{u^3}{3} + o(u^3)$.
4. Substitution de $u$ par sa partie principale $P(x) = x - \frac{x^3}{6}$ :
   $f(x) = (x - \frac{x^3}{6}) - \frac{1}{2}(x - \frac{x^3}{6})^2 + \frac{1}{3}(x - \frac{x^3}{6})^3 + o(x^3)$.
5. Développement avec troncature à l'ordre 3 :
   - $(x - \frac{x^3}{6})^2 = x^2 + o(x^3)$
   - $(x - \frac{x^3}{6})^3 = x^3 + o(x^3)$
6. Sommation :
   $f(x) = x - \frac{x^3}{6} - \frac{x^2}{2} + \frac{x^3}{3} + o(x^3)$
   $f(x) = x - \frac{x^2}{2} + (\frac{1}{3} - \frac{1}{6})x^3 + o(x^3) = x - \frac{x^2}{2} + \frac{x^3}{6} + o(x^3)$. $\blacksquare$