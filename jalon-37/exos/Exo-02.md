---
uuid: "jalon-37-exo-2"
title: "Exercice 2 : Calculs et Propriétés de l'Intégrale de Riemann"
tags:
  - math/analyse
  - ia/calcul-integral
---

# Exercice 2

**Difficulté :** ★★☆☆☆

**Énoncé :**
Montrer que si $f \in \mathcal{R}([a, b])$ et $f(x) \ge 0$ pour tout $x \in [a, b]$, alors $\int_a^b f(x) \, dx \ge 0$.
En déduire que si $f, g \in \mathcal{R}([a, b])$ vérifient $f \le g$, alors $\int_a^b f \le \int_a^b g$.

**Correction détaillée :**
1. Soit $f \in \mathcal{R}([a, b])$ telle que $\forall x \in [a, b], f(x) \ge 0$.
2. Considérons une subdivision quelconque $\sigma = (x_0, \dots, x_n)$ de $[a, b]$.
3. Sur chaque intervalle $[x_{i-1}, x_i]$, la borne inférieure $m_i = \inf_{x \in [x_{i-1}, x_i]} f(x)$ est nécessairement positive ou nulle puisque $f$ est positive.
4. La somme de Darboux inférieure pour cette subdivision est $S_-(\sigma, f) = \sum_{i=1}^n m_i (x_i - x_{i-1})$.
5. Puisque $x_i > x_{i-1}$ et $m_i \ge 0$, chaque terme de la somme est positif, d'où $S_-(\sigma, f) \ge 0$.
6. L'intégrale de Riemann $\int_a^b f$ étant égale à la borne supérieure des sommes de Darboux inférieures sur toutes les subdivisions, on a :
$$ \int_a^b f(x) \, dx = \sup_{\sigma} S_-(\sigma, f) \ge 0 $$
7. Soient maintenant $f, g \in \mathcal{R}([a, b])$ telles que $f(x) \le g(x)$ pour tout $x \in [a, b]$.
8. Posons $h(x) = g(x) - f(x)$. Alors $h(x) \ge 0$ pour tout $x$.
9. De plus, la linéarité de l'intégrale de Riemann garantit que $h \in \mathcal{R}([a, b])$.
10. D'après la première partie de la démonstration, $\int_a^b h(x) \, dx \ge 0$.
11. Par linéarité, $\int_a^b g(x) \, dx - \int_a^b f(x) \, dx \ge 0$, ce qui équivaut à $\int_a^b f(x) \, dx \le \int_a^b g(x) \, dx$.
$\blacksquare$
