## Exercice 8 : Produit de Lebesgue $\quad \bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $f \in \mathcal{M}_+(\mathbb{R})$ t.q. $\int f d\lambda < \infty$. La fonction $F(x) = \int_{(-\infty, x]} f d\lambda$ est-elle absolument continue ?

**Correction :**
Oui. L'absolue continuité requiert que pour tout $\epsilon > 0$, il existe $\delta > 0$ tel que pour toute famille finie d'intervalles disjoints $(a_i, b_i)$ de somme des longueurs $\sum (b_i - a_i) < \delta$, on ait $\sum |F(b_i) - F(a_i)| < \epsilon$.
Or $F(b_i) - F(a_i) = \int_{(a_i, b_i]} f d\lambda$.
Ainsi, $\sum (F(b_i) - F(a_i)) = \int_A f d\lambda$, où $A = \bigcup (a_i, b_i]$.
Il faut donc montrer que si $\lambda(A) < \delta$, $\int_A f d\lambda < \epsilon$.
Par convergence dominée (ou propriétés des mesures), comme $\int f < \infty$, on peut tronquer $f$ : posons $f_n = \min(f, n)$.
$\int f_n \to \int f$, donc on choisit $n$ tel que $\int (f - f_n) < \epsilon/2$.
Ensuite, $\int_A f \le \int_A (f - f_n) + \int_A f_n \le \epsilon/2 + n \lambda(A)$.
Il suffit de prendre $\delta = \frac{\epsilon}{2n}$ pour conclure.
