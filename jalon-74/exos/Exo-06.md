---
title: "Exercice 6 : Inclusion des espaces Lp sur un ensemble de mesure finie"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

# Exercice 6 : Inclusion des espaces $L^p$ sur un ensemble de mesure finie

## Énoncé
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré avec $\mu(X) < \infty$.
Soit $1 \le r < s \le \infty$. Montrer que $L^s(X) \subset L^r(X)$ et que pour tout $f \in L^s(X)$,
$$ \|f\|_r \le \mu(X)^{\frac{1}{r} - \frac{1}{s}} \|f\|_s $$

## Corrigé
Cas $s = \infty$ : $f \in L^\infty$, donc $|f(x)| \le \|f\|_\infty$ pp.
$\int_X |f|^r d\mu \le \int_X \|f\|_\infty^r d\mu = \|f\|_\infty^r \mu(X)$.
Donc $\|f\|_r \le \mu(X)^{1/r} \|f\|_\infty$, ce qui correspond bien à la formule (puisque $1/\infty=0$).
Cas $s < \infty$ : On applique l'inégalité de Hölder aux fonctions $|f|^r$ et $1$.
On choisit les exposants conjugués $p = \frac{s}{r} > 1$ et $q$ tel que $\frac{1}{p} + \frac{1}{q} = 1 \implies \frac{1}{q} = 1 - \frac{r}{s} = \frac{s-r}{s} \implies q = \frac{s}{s-r}$.
$$ \int_X |f|^r \times 1 d\mu \le \left( \int_X (|f|^r)^{\frac{s}{r}} d\mu \right)^{\frac{r}{s}} \left( \int_X 1^q d\mu \right)^{\frac{1}{q}} $$
$$ \int_X |f|^r d\mu \le \left( \int_X |f|^s d\mu \right)^{\frac{r}{s}} \mu(X)^{\frac{s-r}{s}} $$
Soit $\|f\|_r^r \le \|f\|_s^r \mu(X)^{\frac{s-r}{s}}$.
En prenant la puissance $1/r$ :
$$ \|f\|_r \le \|f\|_s \mu(X)^{\frac{s-r}{rs}} = \|f\|_s \mu(X)^{\frac{1}{r} - \frac{1}{s}} $$
Ainsi, $f \in L^r$, l'inclusion et l'inégalité sont prouvées.
