---
title: "Exercice 4 : Interpolation des normes Lp"
difficulty: "$\bigstar\bigstar\bigstar\star\star$"
---

# Exercice 4 : Interpolation des normes $L^p$

## Énoncé
Soit $1 \le r \le p \le s \le \infty$. Démontrer que si $f \in L^r(X) \cap L^s(X)$, alors $f \in L^p(X)$.
Plus précisément, prouver qu'il existe $\theta \in [0, 1]$ tel que $\|f\|_p \le \|f\|_r^\theta \|f\|_s^{1-\theta}$.

## Corrigé
Puisque $r \le p \le s$, on peut écrire $\frac{1}{p}$ comme une combinaison convexe de $\frac{1}{r}$ et $\frac{1}{s}$ : il existe $\theta \in [0, 1]$ tel que $\frac{1}{p} = \frac{\theta}{r} + \frac{1-\theta}{s}$.
On écrit $|f|^p = |f|^{p\theta} |f|^{p(1-\theta)}$.
On intègre ce produit sur $X$ : $\int_X |f|^p d\mu = \int_X |f|^{p\theta} |f|^{p(1-\theta)} d\mu$.
Appliquons l'inégalité de Hölder pour les exposants conjugués $\alpha$ et $\beta$.
On choisit $\alpha = \frac{r}{p\theta}$ et $\beta = \frac{s}{p(1-\theta)}$.
Vérifions qu'ils sont conjugués : $\frac{1}{\alpha} + \frac{1}{\beta} = \frac{p\theta}{r} + \frac{p(1-\theta)}{s} = p \left( \frac{\theta}{r} + \frac{1-\theta}{s} \right) = p \left( \frac{1}{p} \right) = 1$.
On a donc :
$$ \int_X |f|^p d\mu \le \left( \int_X (|f|^{p\theta})^\alpha d\mu \right)^{1/\alpha} \left( \int_X (|f|^{p(1-\theta)})^\beta d\mu \right)^{1/\beta} $$
Or $(p\theta)\alpha = r$ et $1/\alpha = \frac{p\theta}{r}$. Et $p(1-\theta)\beta = s$ et $1/\beta = \frac{p(1-\theta)}{s}$.
D'où :
$$ \|f\|_p^p \le \left( \int_X |f|^r d\mu \right)^{\frac{p\theta}{r}} \left( \int_X |f|^s d\mu \right)^{\frac{p(1-\theta)}{s}} = (\|f\|_r^r)^{\frac{p\theta}{r}} (\|f\|_s^s)^{\frac{p(1-\theta)}{s}} = \|f\|_r^{p\theta} \|f\|_s^{p(1-\theta)} $$
En prenant la puissance $1/p$, on obtient $\|f\|_p \le \|f\|_r^\theta \|f\|_s^{1-\theta}$. $f \in L^p$ est démontré.
