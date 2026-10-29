$\bigstar\bigstar\bigstar\bigstar\star$
**Énoncé :** Toute suite faiblement convergente est bornée.
Soit $E$ un espace de Banach. Démontrer, en utilisant le théorème de Banach-Steinhaus, que si une suite $(x_n)$ converge faiblement, alors elle est bornée.

**Correction Détaillée :**
Soit $(x_n)$ convergeant faiblement vers $x$. Pour toute $L \in E^*$, la suite de scalaires $(L(x_n))$ converge vers $L(x)$.
Toute suite convergente dans $\mathbb{K}$ étant bornée, il existe une constante $M_L > 0$ (qui dépend de $L$) telle que $\sup_{n} |L(x_n)| \le M_L$.
Plongeons $E$ dans son bidual $E^{**}$ via l'isométrie canonique $J : E \to E^{**}$ définie par $J(x)(L) = L(x)$.
Pour chaque $n$, $J(x_n)$ est un opérateur linéaire continu de $E^*$ dans $\mathbb{K}$.
La condition précédente se réécrit : pour tout $L \in E^*$, $\sup_{n} |J(x_n)(L)| \le M_L < \infty$.
La famille d'opérateurs $\{J(x_n)\}_{n \in \mathbb{N}}$ est donc simplement bornée sur l'espace de Banach $E^*$.
D'après le théorème de Banach-Steinhaus (ou principe de la borne uniforme), cette famille est uniformément bornée en norme d'opérateur.
Il existe donc $M > 0$ tel que pour tout $n$, $\|J(x_n)\|_{E^{**}} \le M$.
Or l'injection $J$ est isométrique : $\|J(x_n)\|_{E^{**}} = \|x_n\|_E$.
On conclut que pour tout $n$, $\|x_n\| \le M$. La suite est bornée.
