---
uuid: "jalon-37-exo-3"
title: "Exercice 3 : Calculs et Propriétés de l'Intégrale de Riemann"
tags:
  - math/analyse
  - ia/calcul-integral
---

# Exercice 3

**Difficulté :** ★★☆☆☆

**Énoncé :**
Soit $f : [a, b] \to \mathbb{R}$ continue et positive. Montrer que si $\int_a^b f(t) \, dt = 0$, alors $f$ est identiquement nulle sur $[a, b]$.

**Correction détaillée :**
1. Raisonnons par l'absurde. Supposons qu'il existe un point $c \in [a, b]$ tel que $f(c) > 0$.
2. Comme $f$ est continue au point $c$, il existe un voisinage de $c$ sur lequel $f$ reste strictement positive. Précisément, pour $\epsilon = \frac{f(c)}{2} > 0$, la définition de la continuité en $c$ assure l'existence d'un $\eta > 0$ tel que pour tout $x \in [a, b] \cap ]c-\eta, c+\eta[$, on ait $|f(x) - f(c)| < \frac{f(c)}{2}$.
3. Cela implique que $f(x) > f(c) - \frac{f(c)}{2} = \frac{f(c)}{2}$ sur l'intervalle $I = [a, b] \cap [c-\frac{\eta}{2}, c+\frac{\eta}{2}]$.
4. Posons $J = [u, v]$ ce petit intervalle fermé inclus dans $I$, avec $u < v$.
5. Par positivité de l'intégrale et la relation de Chasles, on a :
$$ \int_a^b f(t) \, dt = \int_a^u f(t) \, dt + \int_u^v f(t) \, dt + \int_v^b f(t) \, dt $$
6. Puisque $f \ge 0$, les intégrales sur $[a, u]$ et $[v, b]$ sont positives ou nulles (voir exercice précédent).
7. Donc $\int_a^b f(t) \, dt \ge \int_u^v f(t) \, dt$.
8. Sur l'intervalle $[u, v]$, on a $f(t) \ge \frac{f(c)}{2}$. Par la croissance de l'intégrale :
$$ \int_u^v f(t) \, dt \ge \int_u^v \frac{f(c)}{2} \, dt = \frac{f(c)}{2} (v - u) $$
9. Or $v - u > 0$ et $f(c) > 0$, donc $\frac{f(c)}{2} (v - u) > 0$.
10. Il en résulte que $\int_a^b f(t) \, dt > 0$, ce qui contredit formellement l'hypothèse de départ $\int_a^b f(t) \, dt = 0$.
11. Par conséquent, notre hypothèse initiale est fausse : pour tout $x \in [a, b]$, $f(x) = 0$.
$\blacksquare$
