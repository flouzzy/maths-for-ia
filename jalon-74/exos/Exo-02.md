### Exercice 2 : Inégalité de Cauchy-Schwarz comme cas particulier de Hölder \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
Utiliser l'inégalité de Hölder pour démontrer l'inégalité de Cauchy-Schwarz pour des fonctions dans $L^2$.

**Correction Détaillée :**
1. L'inégalité de Hölder stipule que pour $f \in L^p$ et $g \in L^q$ où $\frac{1}{p} + \frac{1}{q} = 1$, on a $\|fg\|_1 \le \|f\|_p \|g\|_q$.
2. Posons $p = 2$.
3. Cherchons le conjugué $q$ tel que $\frac{1}{2} + \frac{1}{q} = 1$. On trouve immédiatement $\frac{1}{q} = 1 - \frac{1}{2} = \frac{1}{2}$, d'où $q = 2$.
4. En remplaçant $p$ et $q$ par 2 dans la formule de Hölder, on obtient :
$$\|fg\|_1 \le \|f\|_2 \|g\|_2$$
5. Exprimons ces normes sous forme intégrale :
$$\int_X |f(x)g(x)| d\mu \le \left(\int_X |f(x)|^2 d\mu\right)^{\frac{1}{2}} \left(\int_X |g(x)|^2 d\mu\right)^{\frac{1}{2}}$$
6. Puisque $|\int fg d\mu| \le \int |fg| d\mu$, on a a fortiori :
$$\left| \int_X f(x)g(x) d\mu \right| \le \left(\int_X |f(x)|^2 d\mu\right)^{\frac{1}{2}} \left(\int_X |g(x)|^2 d\mu\right)^{\frac{1}{2}}$$
Ce qui est exactement l'inégalité de Cauchy-Schwarz.
