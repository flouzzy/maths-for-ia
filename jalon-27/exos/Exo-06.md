---
uuid: "jalon-27-exo-06"
title: "Exercice 06 : Noyau et image de l'adjoint"
---
# Exercice 06 : Noyau et image de l'adjoint

**Difficulté :** ★★★☆☆

## Énoncé

Montrer que $\ker(f^*) = (\operatorname{Im}(f))^\perp$.

## Démonstration sans ellipse

Montrons la double inclusion.
Soit $y \in \ker(f^*)$. Alors $f^*(y) = 0$.
Pour tout $x \in E$, on a :
$$ \langle f(x), y \rangle = \langle x, f^*(y) \rangle = \langle x, 0 \rangle = 0 $$
Ainsi, $y$ est orthogonal à tout vecteur de la forme $f(x)$, donc $y \in (\operatorname{Im}(f))^\perp$.
Réciproquement, soit $y \in (\operatorname{Im}(f))^\perp$.
Alors pour tout $x \in E$, $\langle f(x), y \rangle = 0$.
Par définition de l'adjoint, cela signifie que pour tout $x \in E, \langle x, f^*(y) \rangle = 0$.
En prenant $x = f^*(y)$, on obtient $\langle f^*(y), f^*(y) \rangle = 0$, soit $\|f^*(y)\|^2 = 0$.
Donc $f^*(y) = 0$, et $y \in \ker(f^*)$.
Ainsi, $\ker(f^*) = (\operatorname{Im}(f))^\perp$. $\blacksquare$
