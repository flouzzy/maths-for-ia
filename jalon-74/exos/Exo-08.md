### Exercice 8 : Minkowski pour les intégrales (Continue) $\bigstar\bigstar\star\star$

**Énoncé :** Soit $f(x,y)$ mesurable positive sur $X \times Y$. Pour $1 \le p < +\infty$, montrer l'inégalité de Minkowski continue :
$\left[ \int_X \left( \int_Y f(x,y) dy \right)^p dx \right]^{1/p} \le \int_Y \left( \int_X f(x,y)^p dx \right)^{1/p} dy$.

**Correction Détaillée :**
*Analyse :* C'est la généralisation de $\| \sum_j f_j \|_p \le \sum_j \| f_j \|_p$ où la somme discrète est remplacée par une intégrale sur $y$. On utilise la même technique que pour Minkowski discret : dualité et Hölder.
*Résolution pas-à-pas :*
1. Posons $F(x) = \int_Y f(x,y) dy$. Nous cherchons à majorer $\|F\|_p$.
2. Écrivons $F(x)^p = F(x) F(x)^{p-1} = \left(\int_Y f(x,y) dy\right) F(x)^{p-1} = \int_Y f(x,y) F(x)^{p-1} dy$.
3. On intègre sur $x$ et on utilise Tonelli pour inverser l'ordre (fonctions positives) :
   $$\|F\|_p^p = \int_X F(x)^p dx = \int_X \left( \int_Y f(x,y) F(x)^{p-1} dy \right) dx = \int_Y \left( \int_X f(x,y) F(x)^{p-1} dx \right) dy$$
4. Pour l'intégrale intérieure sur $X$, on applique Hölder en $x$ avec $p$ et $q$ (tels que $\frac{1}{p}+\frac{1}{q}=1$) :
   $$\int_X f(x,y) F(x)^{p-1} dx \le \left(\int_X f(x,y)^p dx\right)^{1/p} \left(\int_X F(x)^{(p-1)q} dx\right)^{1/q}$$
5. Comme $(p-1)q = p$, on a $\left(\int_X F(x)^{(p-1)q} dx\right)^{1/q} = \|F\|_p^{p/q}$.
6. En reportant dans l'intégrale sur $Y$ :
   $$\|F\|_p^p \le \int_Y \left(\int_X f(x,y)^p dx\right)^{1/p} \|F\|_p^{p/q} dy = \|F\|_p^{p/q} \int_Y \left(\int_X f(x,y)^p dx\right)^{1/p} dy$$
7. Si $0 < \|F\|_p < \infty$, on divise par $\|F\|_p^{p/q}$. Sachant que $p - p/q = 1$, on obtient :
   $$\|F\|_p \le \int_Y \left(\int_X f(x,y)^p dx\right)^{1/p} dy$$
