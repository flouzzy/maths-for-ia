---
title: "Exercice 4 : Topologie induite par des distances équivalentes"
---

### Exercice 4 : Topologie induite par des distances équivalentes \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit un ensemble $X$. Soient $d_1$ et $d_2$ deux distances sur $X$ fortement équivalentes, c'est-à-dire qu'il existe $\alpha, \beta > 0$ telles que :
$$\forall x, y \in X, \quad \alpha d_1(x, y) \le d_2(x, y) \le \beta d_1(x, y)$$
Démontrer que toute boule ouverte pour la distance $d_2$ contient une boule ouverte pour la distance $d_1$ de même centre.

**Correction Détaillée :**
Soit $x_0 \in X$ et $R > 0$. Considérons la boule ouverte $B_2(x_0, R)$ relative à la distance $d_2$, définie par :
$$B_2(x_0, R) = \{x \in X \mid d_2(x_0, x) < R\}$$
Nous cherchons un rayon $r > 0$ tel que la boule ouverte $B_1(x_0, r)$, relative à $d_1$, soit incluse dans $B_2(x_0, R)$.

Considérons un élément $x \in B_1(x_0, r)$. Par définition, on a :
$$d_1(x_0, x) < r$$
D'après l'hypothèse d'équivalence forte, nous avons :
$$d_2(x_0, x) \le \beta d_1(x_0, x)$$
En combinant ces deux inégalités, nous obtenons :
$$d_2(x_0, x) < \beta r$$
Pour que $x$ appartienne à $B_2(x_0, R)$, il suffit que $d_2(x_0, x) < R$. Ceci est garanti si l'on impose :
$$\beta r \le R \implies r \le \frac{R}{\beta}$$
Puisque $\beta > 0$ et $R > 0$, la quantité $R/\beta$ est strictement positive. En posant par exemple $r = R/\beta$, on assure que tout point de $B_1(x_0, r)$ est dans $B_2(x_0, R)$.

Donc, $B_1(x_0, r) \subset B_2(x_0, R)$. Cela implique que les ouverts de la topologie induite par $d_2$ sont des ouverts de la topologie induite par $d_1$ (et vice versa par symétrie), montrant que les deux distances définissent la même topologie.
