# Exercice 6 : Hölder généralisé pour trois fonctions

**Difficulté :** ★★★☆☆


## Énoncé
Soient $p, q, r \in [1, +\infty]$ tels que $\frac{1}{p} + \frac{1}{q} + \frac{1}{r} = 1$. Démontrer que pour $f \in L^p$, $g \in L^q$ et $h \in L^r$, l'on a :
$$ \|fgh\|_1 \le \|f\|_p \|g\|_q \|h\|_r $$

## Correction Détaillée
Posons $s$ tel que $\frac{1}{s} = \frac{1}{p} + \frac{1}{q}$. Puisque $\frac{1}{p} + \frac{1}{q} + \frac{1}{r} = 1$, il s'ensuit que $\frac{1}{s} + \frac{1}{r} = 1$, ce qui signifie que $s$ et $r$ sont des exposants conjugués.
De plus, $\frac{p}{s} + \frac{q}{s} = 1$, ce qui implique que $p/s$ et $q/s$ sont également conjugués.
Commençons par appliquer l'inégalité de Hölder classique à $|f|^s$ et $|g|^s$ avec les exposants conjugués $p/s$ et $q/s$ :
$$ \int |fg|^s = \int |f|^s |g|^s \le \left( \int (|f|^s)^{p/s} \right)^{s/p} \left( \int (|g|^s)^{q/s} \right)^{s/q} = \left(\int |f|^p\right)^{s/p} \left(\int |g|^q\right)^{s/q} $$
En élevant à la puissance $1/s$, on obtient :
$$ \left( \int |fg|^s \right)^{1/s} \le \left(\int |f|^p\right)^{1/p} \left(\int |g|^q\right)^{1/q} $$
C'est-à-dire $\|fg\|_s \le \|f\|_p \|g\|_q$. Le produit $fg$ appartient donc à $L^s$.
Appliquons maintenant l'inégalité de Hölder au produit $(fg)$ et $h$, avec les exposants conjugués $s$ et $r$ :
$$ \|fgh\|_1 = \|(fg)h\|_1 \le \|fg\|_s \|h\|_r $$
En substituant la majoration obtenue précédemment pour $\|fg\|_s$, on arrive au résultat final :
$$ \|fgh\|_1 \le \|f\|_p \|g\|_q \|h\|_r $$
La preuve est ainsi rigoureusement établie par application itérée de l'inégalité classique.
