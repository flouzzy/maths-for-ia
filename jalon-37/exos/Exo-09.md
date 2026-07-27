---
uuid: "jalon-37-exo-9"
title: "Exercice 9 : Calculs et Propriétés de l'Intégrale de Riemann"
tags:
  - math/analyse
  - ia/calcul-integral
---

# Exercice 9

**Difficulté :** ★★★★★

**Énoncé :**
Caractérisation de Lebesgue (théorème admis).
Une fonction bornée est Riemann-intégrable si et seulement si l'ensemble de ses points de discontinuité est de mesure de Lebesgue nulle.
Utiliser ce critère pour montrer que si $f \in \mathcal{R}([a, b])$, alors $|f| \in \mathcal{R}([a, b])$ et que la composée d'une fonction continue $g$ avec $f$ (soit $g \circ f$) est dans $\mathcal{R}([a, b])$.

**Correction détaillée :**
1. Soit $f \in \mathcal{R}([a, b])$. D'après la caractérisation de Lebesgue (admise ici), l'ensemble $D_f$ des points de discontinuité de $f$ est de mesure de Lebesgue nulle.
2. Considérons la fonction valeur absolue $|\cdot| : \mathbb{R} \to \mathbb{R}$. Elle est continue sur $\mathbb{R}$.
3. Par composition, si $f$ est continue en un point $x$, alors $|f|$ est continue en $x$. Autrement dit, un point de discontinuité de $|f|$ est nécessairement un point de discontinuité de $f$.
4. Formellement, $D_{|f|} \subset D_f$.
5. Comme $D_f$ est de mesure nulle, tout sous-ensemble de $D_f$ est également de mesure nulle. Donc $D_{|f|}$ est de mesure nulle.
6. La fonction $f$ étant bornée, il existe $M$ tel que $|f(x)| \le M$, donc $|f|$ est également bornée.
7. $|f|$ satisfait donc les deux conditions (bornée, discontinuités de mesure nulle), par la caractérisation de Lebesgue, $|f| \in \mathcal{R}([a, b])$.
8. Soit maintenant une fonction $g$ continue sur un intervalle contenant l'image de $f$.
9. Si $f$ est continue en $x$, par la continuité de la composition, $g \circ f$ est continue en $x$.
10. Donc $D_{g \circ f} \subset D_f$. La mesure de $D_{g \circ f}$ est donc nulle.
11. L'image de $f$ (bornée) est contenue dans un compact $[-M, M]$. Sur ce compact, la fonction continue $g$ est bornée. Donc $g \circ f$ est bornée.
12. Par la caractérisation de Lebesgue, $g \circ f \in \mathcal{R}([a, b])$. $\blacksquare$
