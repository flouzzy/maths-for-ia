---
uuid: "jalon-20-exo-05"
title: "Exercice 05 : ★★★☆☆"
---
# Exercice 05

## Énoncé
Déterminer la limite en $0$ de la fonction $g(x) = \frac{\sin(x) - x}{x^3}$.

## Correction
1. C'est une forme indéterminée $0/0$. L'utilisation des développements limités est la méthode la plus robuste.
2. Écrivons le DL du numérateur $\sin(x) - x$ à l'ordre 3 (l'ordre du dénominateur).
3. DL de $\sin(x)$ en $0$ à l'ordre 3 :
   $\sin(x) = x - \frac{x^3}{6} + o(x^3)$.
4. Soustraction :
   $\sin(x) - x = -\frac{x^3}{6} + o(x^3)$.
5. Division par $x^3$ pour $x \neq 0$ :
   $g(x) = \frac{-\frac{x^3}{6} + o(x^3)}{x^3} = -\frac{1}{6} + o(1)$.
6. Par définition, $o(1)$ est une fonction qui tend vers 0 lorsque $x \to 0$.
7. Conclusion :
   $\lim_{x \to 0} g(x) = -\frac{1}{6}$. $\blacksquare$