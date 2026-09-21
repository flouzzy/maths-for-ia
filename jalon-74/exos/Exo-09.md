---
title: "Exercice 9 : Continuité de la norme p en fonction de p"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\bigstar$"
---

# Exercice 9 : Continuité de la norme p en fonction de p

## Énoncé
Soit $f \in L^p(X) \cap L^q(X)$ avec $1 \le p < q \le \infty$. Démontrer que l'application $r \mapsto \|f\|_r$ est continue sur l'intervalle $[p, q]$. (Indic : utiliser l'interpolation).

## Corrigé
Soit $r_0 \in [p, q]$. On veut montrer la continuité en $r_0$.
L'exercice sur l'interpolation montrait que pour $r \le r_0 \le s$, $\|f\|_{r_0} \le \|f\|_r^\theta \|f\|_s^{1-\theta}$ avec $\frac{1}{r_0} = \frac{\theta}{r} + \frac{1-\theta}{s}$.
De plus, par le théorème de convergence dominée (ou par Hölder), on peut montrer que la fonction $r \mapsto \int |f|^r d\mu$ est continue.
En effet, pour $r$ proche de $r_0$, $|f|^r \le |f|^p + |f|^q \in L^1$. Comme $r \mapsto |f(x)|^r$ est continue pp, par le théorème de convergence dominée, $\lim_{r\to r_0} \int |f|^r d\mu = \int |f|^{r_0} d\mu$.
Comme l'application $x \mapsto x^{1/r}$ est continue conjointement avec $r$, la limite de $(\int |f|^r)^{1/r}$ est bien $(\int |f|^{r_0})^{1/r_0}$.
Donc $r \mapsto \|f\|_r$ est bien continue sur $[p, q]$.
