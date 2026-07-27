---
uuid: "jalon-37-exo-6"
title: "Exercice 6 : Calculs et Propriétés de l'Intégrale de Riemann"
tags:
  - math/analyse
  - ia/calcul-integral
---

# Exercice 6

**Difficulté :** ★★★☆☆

**Énoncé :**
Inégalité de Cauchy-Schwarz pour les intégrales.
Soient $f, g \in \mathcal{R}([a, b])$. Montrer que :
$$ \left( \int_a^b f(t)g(t) \, dt \right)^2 \le \left( \int_a^b f(t)^2 \, dt \right) \left( \int_a^b g(t)^2 \, dt \right) $$

**Correction détaillée :**
1. Pour tout $\lambda \in \mathbb{R}$, considérons la fonction $h_\lambda(t) = (f(t) + \lambda g(t))^2$.
2. Le produit de fonctions intégrables étant intégrable, $h_\lambda \in \mathcal{R}([a, b])$.
3. De plus, comme c'est un carré, pour tout $t \in [a, b]$, $h_\lambda(t) \ge 0$.
4. Par la propriété de positivité de l'intégrale (démontrée dans l'exercice 2) :
$$ \int_a^b (f(t) + \lambda g(t))^2 \, dt \ge 0 $$
5. En développant le carré à l'intérieur de l'intégrale :
$$ \int_a^b (f(t)^2 + 2\lambda f(t)g(t) + \lambda^2 g(t)^2) \, dt \ge 0 $$
6. Par la linéarité de l'intégrale de Riemann, on obtient un trinôme du second degré en $\lambda$ :
$$ P(\lambda) = \lambda^2 \int_a^b g(t)^2 \, dt + 2\lambda \int_a^b f(t)g(t) \, dt + \int_a^b f(t)^2 \, dt \ge 0 $$
7. Soit $A = \int_a^b g(t)^2 \, dt$, $B = \int_a^b f(t)g(t) \, dt$ et $C = \int_a^b f(t)^2 \, dt$.
8. Cas 1 : $A = 0$. Alors d'après l'exercice 3 (appliqué à $g^2 \ge 0$ intégrable), l'intégrale nulle d'une fonction positive n'implique pas que $g=0$ si $g$ n'est pas continue. Cependant, si $A=0$, alors $\int_a^b g(t)^2 \, dt = 0$. L'inégalité à prouver se réduit à $B^2 \le 0 \cdot C = 0$. Il faut prouver $B=0$. Si $A=0$, $P(\lambda) = 2\lambda B + C \ge 0$ pour tout $\lambda \in \mathbb{R}$. Ceci n'est possible pour une fonction affine que si le coefficient directeur $2B$ est nul, donc $B=0$. L'inégalité est vérifiée ($0 \le 0$).
9. Cas 2 : $A > 0$. Le trinôme $P(\lambda) = A\lambda^2 + 2B\lambda + C$ garde un signe constant positif ou nul.
10. Cela implique que son discriminant réduit $\Delta' = B^2 - AC$ est négatif ou nul.
11. Donc $B^2 \le AC$, ce qui donne en remplaçant :
$$ \left( \int_a^b f(t)g(t) \, dt \right)^2 \le \left( \int_a^b f(t)^2 \, dt \right) \left( \int_a^b g(t)^2 \, dt \right) $$
$\blacksquare$
