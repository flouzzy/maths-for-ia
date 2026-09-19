### Exercice 4 : Normes $L^p$ emboîtées $\bigstar\bigstar\star$

**Énoncé :** Soit $(X, \mathcal{F}, \mu)$ un espace mesuré tel que $\mu(X)=1$. Montrer que pour $1 \le p < q < +\infty$, on a $\|f\|_p \le \|f\|_q$ pour toute fonction $f \in L^q(\mu)$.

**Correction Détaillée :**
*Analyse :* On peut utiliser l'inégalité de Jensen car la mesure est de probabilité, ou Hölder avec des exposants bien choisis.
*Méthode par Jensen :*
1. On pose $\phi(x) = |x|^{q/p}$. Comme $q > p$, l'exposant $q/p$ est strictement supérieur à 1. La fonction $\phi$ est convexe sur $\mathbb{R}$.
2. On applique Jensen à la fonction $|f|^p$, qui est dans $L^1$ puisque $f \in L^q \subset L^p$ (mesure finie).
3. $\phi(\int_X |f|^p d\mu) \le \int_X \phi(|f|^p) d\mu$.
4. Ce qui donne : $\left(\int_X |f|^p d\mu\right)^{q/p} \le \int_X (|f|^p)^{q/p} d\mu = \int_X |f|^q d\mu$.
5. On élève les deux membres à la puissance $1/q$ (fonction croissante) :
   $$\left(\int_X |f|^p d\mu\right)^{1/p} \le \left(\int_X |f|^q d\mu\right)^{1/q}$$
6. Ce qui est exactement $\|f\|_p \le \|f\|_q$.
