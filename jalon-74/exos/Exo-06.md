### Exercice 6 : Inclusion des espaces $L^p$ en probabilité \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $(X, \mathcal{A}, \mathbb{P})$ un espace de probabilité. Soient $1 \le p < q \le \infty$.
Montrer que $L^q(\mathbb{P}) \subset L^p(\mathbb{P})$ et que $\|X\|_p \le \|X\|_q$.

**Correction Détaillée :**
1. L'idée est d'utiliser Hölder en scindant $|X|^p$ en le produit de $|X|^p$ par la fonction constante $1$.
2. On applique l'inégalité de Hölder à $|X|^p \in L^r$ et $1 \in L^s$, avec $\frac{1}{r} + \frac{1}{s} = 1$.
3. On choisit $r$ tel que le produit $pr$ donne $q$. Donc $r = \frac{q}{p}$. Puisque $q > p \ge 1$, on a $r > 1$. Le conjugué est $s = \frac{r}{r-1} = \frac{q/p}{q/p - 1} = \frac{q}{q-p}$.
4. Appliquons Hölder sur l'espace de probabilité :
$$\int_X |X|^p \cdot 1 d\mathbb{P} \le \left( \int_X (|X|^p)^r d\mathbb{P} \right)^{\frac{1}{r}} \left( \int_X 1^s d\mathbb{P} \right)^{\frac{1}{s}}$$
5. Puisque la mesure de l'espace entier est $\mathbb{P}(X) = 1$, l'intégrale de 1 est 1, donc $(1)^{\frac{1}{s}} = 1$.
6. L'inégalité devient :
$$\int_X |X|^p d\mathbb{P} \le \left( \int_X |X|^{pr} d\mathbb{P} \right)^{\frac{1}{r}} = \left( \int_X |X|^q d\mathbb{P} \right)^{\frac{p}{q}}$$
7. En élevant tout à la puissance $1/p$ :
$$\|X\|_p = \left( \int_X |X|^p d\mathbb{P} \right)^{\frac{1}{p}} \le \left( \int_X |X|^q d\mathbb{P} \right)^{\frac{1}{q}} = \|X\|_q$$
Ceci montre que la norme $p$ est dominée par la norme $q$, et donc l'inclusion topologique $L^q \subset L^p$ pour les espaces de probabilité.
