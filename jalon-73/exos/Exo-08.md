# Exercice 8 : Produit de fonctions et exposants conjugués (Hölder rudimentaire) \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soient $f \in L^p(\mu)$ et $g \in L^q(\mu)$ où $\frac{1}{p} + \frac{1}{q} = 1$ avec $1 < p, q < +\infty$.
En utilisant l'inégalité de Young ($ab \le \frac{a^p}{p} + \frac{b^q}{q}$ pour $a,b \ge 0$), montrer que la fonction $f \cdot g$ est dans $L^1(\mu)$, c'est-à-dire que $\int_X |fg| d\mu < +\infty$.

**Correction :**
Si $\|f\|_p = 0$ ou $\|g\|_q = 0$, alors $f=0$ p.p. ou $g=0$ p.p., donc $fg = 0$ p.p. et l'intégrale est nulle, le résultat est trivial.
Supposons $\|f\|_p > 0$ et $\|g\|_q > 0$.
Considérons les fonctions normalisées : $\tilde{f} = \frac{f}{\|f\|_p}$ et $\tilde{g} = \frac{g}{\|g\|_q}$.
Par définition, $\|\tilde{f}\|_p = 1$ et $\|\tilde{g}\|_q = 1$, ce qui signifie que $\int_X |\tilde{f}|^p d\mu = 1$ et $\int_X |\tilde{g}|^q d\mu = 1$.

Pour tout $x \in X$, on applique l'inégalité de Young à $a = |\tilde{f}(x)|$ et $b = |\tilde{g}(x)|$ :
$|\tilde{f}(x) \cdot \tilde{g}(x)| \le \frac{|\tilde{f}(x)|^p}{p} + \frac{|\tilde{g}(x)|^q}{q}$.

En intégrant cette inégalité sur $X$ :
$\int_X |\tilde{f} \cdot \tilde{g}| d\mu \le \frac{1}{p} \int_X |\tilde{f}|^p d\mu + \frac{1}{q} \int_X |\tilde{g}|^q d\mu = \frac{1}{p}(1) + \frac{1}{q}(1) = 1$.

L'intégrale $\int_X |\tilde{f} \cdot \tilde{g}| d\mu$ est finie.
En remplaçant $\tilde{f}$ et $\tilde{g}$ par leurs définitions, on obtient :
$\frac{1}{\|f\|_p \|g\|_q} \int_X |f \cdot g| d\mu \le 1$.
Donc $\int_X |f \cdot g| d\mu \le \|f\|_p \|g\|_q < +\infty$.
Ainsi, $f \cdot g \in L^1(\mu)$.
