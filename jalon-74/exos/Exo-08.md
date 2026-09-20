# Exercice 8 : Majoration de la norme Lp par la norme Lq

**Difficulté :** ★★★★☆


## Énoncé
Soit $(X, \mathcal{T}, \mu)$ un espace mesuré tel que $\mu(X) < \infty$. Soient $1 \le p \le q < \infty$.
Démontrer que $L^q(\mu) \subset L^p(\mu)$ et prouver l'inégalité :
$$ \|f\|_p \le \mu(X)^{\frac{1}{p} - \frac{1}{q}} \|f\|_q $$

## Correction Détaillée
Puisque $p \le q$, l'exposant $r = q/p$ vérifie $r \ge 1$.
Son exposant conjugué $s$ est donné par $\frac{1}{r} + \frac{1}{s} = 1$, soit $\frac{p}{q} + \frac{1}{s} = 1$, ce qui donne $s = \frac{q}{q-p}$.
Appliquons l'inégalité de Hölder à la fonction intégrande $|f|^p$ et à la fonction constante $\mathbf{1}_X$, avec les exposants conjugués $r$ et $s$ :
$$ \int_X |f|^p \cdot 1 \, d\mu \le \left( \int_X (|f|^p)^r \, d\mu \right)^{1/r} \left( \int_X 1^s \, d\mu \right)^{1/s} $$
Calculons les différents termes :
1. $(|f|^p)^r = |f|^{p \cdot (q/p)} = |f|^q$. Donc $\left(\int_X |f|^q \, d\mu\right)^{1/r} = \left(\|f\|_q^q\right)^{p/q} = \|f\|_q^p$.
2. $\int_X 1^s \, d\mu = \int_X 1 \, d\mu = \mu(X)$. Donc $\left(\int_X 1^s \, d\mu\right)^{1/s} = \mu(X)^{1/s} = \mu(X)^{\frac{q-p}{q}} = \mu(X)^{1 - p/q}$.
Substituons dans l'inégalité :
$$ \|f\|_p^p \le \|f\|_q^p \cdot \mu(X)^{1 - p/q} $$
En élevant les deux membres à la puissance $1/p$ :
$$ \|f\|_p \le \|f\|_q \cdot \mu(X)^{\frac{1}{p}(1 - p/q)} = \|f\|_q \cdot \mu(X)^{\frac{1}{p} - \frac{1}{q}} $$
L'inégalité est prouvée. Puisque $\mu(X) < \infty$, si $f \in L^q(\mu)$ (c.-à-d. $\|f\|_q < \infty$), alors $\|f\|_p < \infty$, ce qui prouve l'inclusion formelle $L^q(\mu) \subset L^p(\mu)$.
