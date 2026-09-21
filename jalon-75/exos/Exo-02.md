\subsection*{Exercice 2 : Inégalité de Hölder et inclusion des espaces $L^p$ \quad $\bigstar\bigstar$}
**Énoncé :**
Soit $(X, \mathcal{F}, \mu)$ un espace mesuré de mesure finie (i.e. $\mu(X) < \infty$). Soient $1 \le p \le q < \infty$.
Montrer que $L^q(X) \subset L^p(X)$ et trouver une constante $C$ telle que $\|f\|_p \le C \|f\|_q$ pour tout $f \in L^q(X)$.

**Correction détaillée :**
Soit $f \in L^q(X)$. On veut intégrer $|f|^p$.
On applique l'inégalité de Hölder à $|f|^p$ et à la fonction constante $\mathbf{1}$.
L'exposant conjugué r de $q/p$ est tel que $\frac{1}{q/p} + \frac{1}{r} = 1$, d'où $r = \frac{q}{q-p}$.
On a :
$\int_X |f|^p \times 1 \, d\mu \le \left( \int_X (|f|^p)^{q/p} \, d\mu \right)^{p/q} \left( \int_X 1^r \, d\mu \right)^{1/r}$
Ce qui se réécrit :
$\int_X |f|^p \, d\mu \le \left( \int_X |f|^q \, d\mu \right)^{p/q} \mu(X)^{(q-p)/q}$
En élevant à la puissance $1/p$, on obtient :
$\|f\|_p = \left( \int_X |f|^p \, d\mu \right)^{1/p} \le \|f\|_q \cdot \mu(X)^{\frac{q-p}{pq}}$
Comme $\mu(X) < \infty$, si $f \in L^q$, l'intégrale $\int_X |f|^q$ est finie, donc la norme $\|f\|_p$ est finie, d'où $f \in L^p$.
La constante est $C = \mu(X)^{\frac{1}{p} - \frac{1}{q}}$. \qed
