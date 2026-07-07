---
uuid: "jalon-20-exo-04"
title: "Exercice 04 : ★★☆☆☆"
---
# Exercice 04

## Énoncé
Calculer le développement limité de la fonction $f(x) = \frac{1}{1 - x + x^2}$ à l'ordre 3 en $x = 0$. Démontrer chaque étape avec rigueur.

## Correction
1. Soit $u = -x + x^2$. Comme $x \to 0$, $u \to 0$.
2. On utilise le DL usuel : $\frac{1}{1 + u} = 1 - u + u^2 - u^3 + o(u^3)$ en posant l'expression avec $1 - (-u)$.
   Ici la forme est $1 / (1 - u')$ avec $u' = x - x^2$.
   DL : $\frac{1}{1 - u'} = 1 + u' + (u')^2 + (u')^3 + o((u')^3)$.
3. Substitution de $u' = x - x^2$ :
   $f(x) = 1 + (x - x^2) + (x - x^2)^2 + (x - x^2)^3 + o(x^3)$.
4. Développement et troncature à l'ordre 3 :
   - $(x - x^2)^2 = x^2 - 2x^3 + x^4 = x^2 - 2x^3 + o(x^3)$
   - $(x - x^2)^3 = x^3 + o(x^3)$
5. Sommation :
   $f(x) = 1 + x - x^2 + x^2 - 2x^3 + x^3 + o(x^3)$
   $f(x) = 1 + x - x^3 + o(x^3)$. $\blacksquare$