---
uuid: "jalon-58-exo-09"
title: "Exercice 09 : Espace des fonctions $L^p$"
---

## Espace des fonctions $L^p$ \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

Considérons les espaces de Lebesgue $L^p([0,1])$. Prouver que $\bigcup_{p > 1} L^p([0,1])$ est maigre dans $L^1([0,1])$.

## Correction Détaillée (Zéro Ellipse)


1. Les $L^p$ sont des espaces de Banach.
2. On définit $F_n = \{f \in L^1([0,1]) \mid \int_0^1 |f|^n \leq n\}$.
3. $F_n$ est un fermé de $L^1$ par le Lemme de Fatou.
4. $F_n$ est d'intérieur vide dans $L^1$. En effet, pour toute fonction $f \in F_n$, on peut lui ajouter une fonction $g$ très concentrée de sorte que sa norme $L^1$ soit très petite (donc $f+g$ est dans une boule $L^1$ arbitrairement petite autour de $f$), mais sa norme $L^n$ explose.
5. Ainsi, chaque $F_n$ est nulle part dense.
6. De plus, tout espace $L^p$ pour $p > 1$ est inclus dans l'union des $F_n$. (Car si $p > 1$, la fonction est dans un certain $L^q$ avec $q$ entier positif).
7. Donc l'union des $L^p$ pour $p>1$ est une partie maigre de $L^1$.
