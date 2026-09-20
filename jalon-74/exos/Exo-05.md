### Exercice 5 : Inégalité de Hölder généralisée \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soient $p_1, p_2, p_3 \in [1, +\infty]$ tels que $\frac{1}{p_1} + \frac{1}{p_2} + \frac{1}{p_3} = 1$.
Montrer que pour $f_i \in L^{p_i}$, le produit $f_1 f_2 f_3$ est dans $L^1$ et $\|f_1 f_2 f_3\|_1 \le \|f_1\|_{p_1} \|f_2\|_{p_2} \|f_3\|_{p_3}$.

**Correction Détaillée :**
1. On pose $g = f_1$ et $h = f_2 f_3$. On veut appliquer l'inégalité de Hölder standard entre $g$ et $h$.
2. L'exposant pour $g$ est $p_1$. Le conjugué de $p_1$ est un exposant $q$ tel que $\frac{1}{p_1} + \frac{1}{q} = 1$. Par hypothèse, on a donc $\frac{1}{q} = \frac{1}{p_2} + \frac{1}{p_3}$.
3. Par Hölder, $\|g h\|_1 \le \|g\|_{p_1} \|h\|_q$, soit :
$$\|f_1 f_2 f_3\|_1 \le \|f_1\|_{p_1} \|f_2 f_3\|_q$$
4. Il faut maintenant estimer $\|f_2 f_3\|_q = \left( \int |f_2 f_3|^q \right)^{1/q}$. Appliquons à nouveau l'inégalité de Hölder à l'intégrale $\int |f_2|^q |f_3|^q$.
5. On cherche des exposants $r$ et $s$ conjugués ($\frac{1}{r} + \frac{1}{s} = 1$) tels que $|f_2|^q \in L^r$ et $|f_3|^q \in L^s$. Posons $r = \frac{p_2}{q}$ et $s = \frac{p_3}{q}$.
Vérifions que ce sont des conjugués : $\frac{1}{r} + \frac{1}{s} = \frac{q}{p_2} + \frac{q}{p_3} = q \left(\frac{1}{p_2} + \frac{1}{p_3}\right) = q \left(\frac{1}{q}\right) = 1$. C'est vérifié.
6. Appliquons Hölder pour $r$ et $s$ sur l'intégrale $\int |f_2|^q |f_3|^q$ :
$$\int |f_2|^q |f_3|^q \le \left( \int (|f_2|^q)^r \right)^{1/r} \left( \int (|f_3|^q)^s \right)^{1/s} = \left( \int |f_2|^{p_2} \right)^{q/p_2} \left( \int |f_3|^{p_3} \right)^{q/p_3}$$
$$\int |f_2 f_3|^q \le \|f_2\|_{p_2}^q \|f_3\|_{p_3}^q$$
7. En élevant à la puissance $1/q$ : $\|f_2 f_3\|_q \le \|f_2\|_{p_2} \|f_3\|_{p_3}$.
8. En réinjectant dans l'étape 3 : $\|f_1 f_2 f_3\|_1 \le \|f_1\|_{p_1} \|f_2\|_{p_2} \|f_3\|_{p_3}$.
