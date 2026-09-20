### Exercice 4 : Interpolation des normes $L^p$ \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $f \in L^1(\mu) \cap L^\infty(\mu)$. Montrer que pour tout $p > 1$, $f \in L^p(\mu)$ et que $\|f\|_p \le \|f\|_1^{1/p} \|f\|_\infty^{1 - 1/p}$.

**Correction Détaillée :**
1. Par définition, $|f(x)| \le \|f\|_\infty$ presque pour tout $x$.
2. Écrivons $|f(x)|^p$ en le scindant : $|f(x)|^p = |f(x)| \cdot |f(x)|^{p-1}$.
3. Puisque $|f(x)| \le \|f\|_\infty$ p.p., on a $|f(x)|^{p-1} \le \|f\|_\infty^{p-1}$ p.p.
4. Ainsi, $|f(x)|^p \le |f(x)| \cdot \|f\|_\infty^{p-1}$.
5. Intégrons cette inégalité sur $X$ :
$$\int_X |f(x)|^p d\mu \le \int_X |f(x)| \cdot \|f\|_\infty^{p-1} d\mu$$
$$\int_X |f(x)|^p d\mu \le \|f\|_\infty^{p-1} \int_X |f(x)| d\mu$$
$$\|f\|_p^p \le \|f\|_\infty^{p-1} \|f\|_1$$
6. Prenons la racine $p$-ième des deux membres :
$$\|f\|_p \le (\|f\|_\infty^{p-1} \|f\|_1)^{1/p} = \|f\|_\infty^{\frac{p-1}{p}} \|f\|_1^{\frac{1}{p}}$$
$$\|f\|_p \le \|f\|_1^{\frac{1}{p}} \|f\|_\infty^{1 - \frac{1}{p}}$$
Ce qui démontre la relation d'interpolation et prouve que $f \in L^p(\mu)$ puisque la borne droite est finie.
