---
title: "Exercice 6 : Application des Inégalités"
difficulty: "★★★★☆"
---

# Exercice 6 : Application des Inégalités

**Niveau :** ★★★★☆

**Énoncé :**
Inégalité d'interpolation (Hölder itéré) : Si $p < r < q$, prouver que $\|f\|_r \le \|f\|_p^{1-\theta} \|f\|_q^\theta$ pour un certain $\theta \in ]0,1[$. Préciser $\theta$.

**Correction Détaillée :**
Puisque $p < r < q$, on peut écrire $r$ comme une combinaison convexe de $p$ et $q$ sous la forme $\frac{1}{r} = \frac{1-\theta}{p} + \frac{\theta}{q}$ pour un certain $\theta \in ]0,1[$.<br>On a $r = r(1-\theta) + r\theta$.<br>L'intégrale de $\|f\|_r^r$ est $\int |f|^r = \int |f|^{r(1-\theta)} |f|^{r\theta}$.<br>Appliquons Hölder avec les exposants conjugués $u$ et $v$. On veut $u$ tel que $r(1-\theta)u = p$, donc $u = \frac{p}{r(1-\theta)}$.<br>Vérifions le conjugué $v$ : $1 - \frac{1}{u} = 1 - \frac{r(1-\theta)}{p}$.<br>Or $\frac{1-\theta}{p} = \frac{1}{r} - \frac{\theta}{q}$, donc $\frac{r(1-\theta)}{p} = 1 - \frac{r\theta}{q}$.<br>Ainsi $1 - \frac{1}{u} = 1 - (1 - \frac{r\theta}{q}) = \frac{r\theta}{q}$. Soit $v = \frac{q}{r\theta}$.<br>On applique Hölder : $\int |f|^r \le (\int (|f|^{r(1-\theta)})^u)^{1/u} (\int (|f|^{r\theta})^v)^{1/v}$.<br>$\int |f|^r \le (\int |f|^p)^{r(1-\theta)/p} (\int |f|^q)^{r\theta/q}$.<br>En élevant à la puissance $1/r$ : $\|f\|_r \le (\|f\|_p^p)^{\frac{1-\theta}{p}} (\|f\|_q^q)^{\frac{\theta}{q}} = \|f\|_p^{1-\theta} \|f\|_q^\theta$.<br>Cette inégalité garantit que $L^p \cap L^q \subset L^r$.
