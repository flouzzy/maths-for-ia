---
uuid: "jalon-20-exo-02"
title: "Exercice 02 : ★☆☆☆☆"
---
# Exercice 02

## Énoncé
Calculer le développement limité de la fonction $f(x) = \frac{\sin(x)}{x}$ à l'ordre 4 en $x = 0$. Démontrer chaque étape avec rigueur.

## Correction
1. Le DL de $\sin(x)$ en $0$ à l'ordre 5 (nécessaire pour obtenir l'ordre 4 après division par $x$) est :
   $\sin(x) = x - \frac{x^3}{6} + \frac{x^5}{120} + o(x^5)$.
2. Pour $x \neq 0$, divisons par $x$ :
   $f(x) = \frac{x - \frac{x^3}{6} + \frac{x^5}{120} + o(x^5)}{x}$
3. Simplification algébrique :
   $f(x) = 1 - \frac{x^2}{6} + \frac{x^4}{120} + \frac{o(x^5)}{x}$
4. Par définition de l'équivalence asymptotique, $\frac{o(x^5)}{x} = o(x^4)$.
5. Résultat final :
   $f(x) = 1 - \frac{x^2}{6} + \frac{x^4}{120} + o(x^4)$.

Cette fonction, prolongée par continuité en 0 par $f(0)=1$, admet bien un DL d'ordre 4. $\blacksquare$