# Calcul par supremum d'étagées

**Difficulté :** $\star\star\star☆☆$

## Énoncé

Soit la fonction continue $f(x) = x$ sur $X = [0, 1]$ muni de la mesure de Lebesgue $\lambda$. En utilisant la définition de l'intégrale de Lebesgue via le supremum des fonctions étagées minorantes, construisez une suite de fonctions étagées $s_n$ pour retrouver $\int_{[0,1]} x \, d\lambda = \frac{1}{2}$.

---

## Correction détaillée

Découpons l'intervalle $[0,1]$ en $n$ sous-intervalles de même longueur : $I_k = \left[\frac{k}{n}, \frac{k+1}{n}\right[$ pour $k=0, \dots, n-1$ (et on ferme le dernier en $1$).
Sur chaque $I_k$, la fonction $f(x)=x$ est minorée par $\frac{k}{n}$. Définissons la fonction étagée :
$$ s_n = \sum_{k=0}^{n-1} \frac{k}{n} \mathbb{1}_{I_k} $$
On a bien $0 \leq s_n \leq f$. L'intégrale de $s_n$ est :
$$ \int_{[0,1]} s_n \, d\lambda = \sum_{k=0}^{n-1} \frac{k}{n} \lambda(I_k) = \sum_{k=0}^{n-1} \frac{k}{n} \times \frac{1}{n} = \frac{1}{n^2} \sum_{k=0}^{n-1} k = \frac{1}{n^2} \frac{(n-1)n}{2} = \frac{n-1}{2n} $$
Lorsque $n \to \infty$, la limite de cette suite d'intégrales est $\frac{1}{2}$. Par définition du supremum, $\int_{[0,1]} x \, d\lambda = \frac{1}{2}$.
