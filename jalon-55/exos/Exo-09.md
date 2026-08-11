---
uuid: "exo-55-09"
title: "Le théorème de la valeur intermédiaire de Darboux"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\bigstar$"
---

# Exercice 9 : Le théorème de la valeur intermédiaire de Darboux

**Énoncé :**
Soit $f : [a, b] \to \mathbb{R}$ une fonction dérivable. Montrer que l'image de la dérivée $f'([a, b])$ est un intervalle, bien que $f'$ ne soit pas nécessairement continue.

**Solution :**
1. Soient $u, v \in f'([a, b])$ avec $u < v$. Il existe $x_1, x_2 \in [a, b]$ tels que $f'(x_1) = u$ et $f'(x_2) = v$. Sans perte de généralité, supposons $x_1 < x_2$.
2. Soit $\gamma \in ]u, v[$. On veut montrer qu'il existe $c \in [x_1, x_2]$ tel que $f'(c) = \gamma$.
3. Considérons la fonction $g(x) = f(x) - \gamma x$. Elle est dérivable sur $[a, b]$, et $g'(x) = f'(x) - \gamma$.
4. On a $g'(x_1) = u - \gamma < 0$ et $g'(x_2) = v - \gamma > 0$.
5. Comme $[x_1, x_2]$ est compact, la fonction continue $g$ y atteint son minimum en un point $c \in [x_1, x_2]$.
6. Puisque $g'(x_1) < 0$, pour $x$ juste après $x_1$, $g(x) < g(x_1)$, donc le minimum n'est pas en $x_1$. De même $g'(x_2) > 0$ implique que le minimum n'est pas en $x_2$.
7. Le minimum est donc atteint à l'intérieur de l'intervalle : $c \in ]x_1, x_2[$.
8. En un extremum local à l'intérieur de l'intervalle, la dérivée s'annule : $g'(c) = 0$.
9. Par suite, $f'(c) - \gamma = 0$, soit $f'(c) = \gamma$. L'image $f'([a, b])$ contient donc tout élément entre $u$ et $v$. Ainsi, par caractérisation des intervalles de $\mathbb{R}$, $f'([a, b])$ est un intervalle. Ceci illustre que l'image d'un connexe par une application dérivée partage des propriétés de connexité !
