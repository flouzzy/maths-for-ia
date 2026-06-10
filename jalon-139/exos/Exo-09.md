# Exercice 9 : Stabilité de la Descente de Gradient (★★★★★)

## Énoncé
Soit la fonction de perte empirique régularisée :
$$F_S(w) = \frac{1}{n} \sum_{j=1}^n \ell(w, Z_j) + \lambda \|w\|_2^2$$
On suppose que pour tout $z \in \mathcal{Z}$, la fonction de perte $w \mapsto \ell(w, z)$ est $L$-Lipschitzienne, $\beta_{\text{lisse}}$-lisse et convexe.
L'algorithme de descente de gradient effectue les itérations suivantes à partir de $w_0 = 0$ :
$$w_{t+1} = w_t - \alpha \nabla F_S(w_t)$$
où le pas d'apprentissage $\alpha > 0$ vérifie $\alpha \le \frac{1}{\beta_{\text{lisse}} + \lambda}$.
Démontrer que la descente de gradient est stable après $T$ étapes et que la distance entre les poids obtenus sur deux échantillons perturbés d'une coordonnée $S$ et $S^{(i)}$ vérifie :
$$\|w_t - w'_t\|_2 \le \frac{2 L}{\lambda n}$$
pour tout $t \ge 0$, indépendamment du nombre d'itérations $T$ (stabilité uniforme non asymptotique).

---

## Correction Détaillée

### 1. Propriétés contractantes de la descente de gradient
Notons $G_S(w) = w - \alpha \nabla F_S(w)$ l'opérateur de mise à jour de la descente de gradient sur $S$, et $G_{S^{(i)}}(w) = w - \alpha \nabla F_{S^{(i)}}(w)$ sur l'échantillon perturbé $S^{(i)}$.
Puisque la perte $\ell$ est convexe et $\beta_{\text{lisse}}$-lisse, la régularisation $\lambda \|w\|_2^2$ implique que la fonction objective globale $F_S$ est $2\lambda$-fortement convexe et $(\beta_{\text{lisse}} + 2\lambda)$-lisse.
Par un résultat classique d'analyse convexe, si l'on choisit le pas d'apprentissage $\alpha \le \frac{2}{\beta_{\text{lisse}} + 2\lambda + 2\lambda} = \frac{1}{\beta_{\text{lisse}} + 2\lambda}$ (ce qui est garanti par l'hypothèse de l'énoncé), alors l'opérateur de pas de gradient $G_S$ est une co-contraction, et en particulier il est strictement contractant de rapport $1 - \alpha \lambda$ :
$$\|G_S(u) - G_S(v)\|_2 \le (1 - \alpha \lambda) \|u - v\|_2 \quad \forall u, v \in \mathbb{R}^d$$

### 2. Relation de récurrence sur la distance des trajectoires
Notons $w_t$ la trajectoire sur $S$, et $w'_t$ la trajectoire sur $S^{(i)}$. On a :
$$w_{t+1} - w'_{t+1} = G_S(w_t) - G_{S^{(i)}}(w'_t) = \big( G_S(w_t) - G_S(w'_t) \big) + \big( G_S(w'_t) - G_{S^{(i)}}(w'_t) \big)$$

Par l'inégalité triangulaire et la propriété de contraction (1) :
$$\|w_{t+1} - w'_{t+1}\|_2 \le \|G_S(w_t) - G_S(w'_t)\|_2 + \|G_S(w'_t) - G_{S^{(i)}}(w'_t)\|_2$$
$$\|w_{t+1} - w'_{t+1}\|_2 \le (1 - \alpha \lambda) \|w_t - w'_t\|_2 + \alpha \|\nabla F_S(w'_t) - \nabla F_{S^{(i)}}(w'_t)\|_2$$

### 3. Majoration du terme de perturbation locale
Analysons la différence des gradients des deux fonctions objectives :
$$\nabla F_S(w) - \nabla F_{S^{(i)}}(w) = \frac{1}{n} \Big( \nabla \ell(w, Z_i) - \nabla \ell(w, Z'_i) \Big)$$
Puisque la perte $\ell$ est $L$-Lipschitzienne par rapport à son premier argument, la norme de son gradient est bornée presque sûrement par $L$ :
$$\|\nabla \ell(w, z)\|_2 \le L \quad \forall w, z$$
D'où par l'inégalité triangulaire :
$$\|\nabla F_S(w) - \nabla F_{S^{(i)}}(w)\|_2 \le \frac{1}{n} \Big( \|\nabla \ell(w, Z_i)\|_2 + \|\nabla \ell(w, Z'_i)\|_2 \Big) \le \frac{2 L}{n}$$

### 4. Résolution de la récurrence
Injectons cette majoration uniforme dans notre relation de récurrence (2) :
$$\|w_{t+1} - w'_{t+1}\|_2 \le (1 - \alpha \lambda) \|w_t - w'_t\|_2 + \frac{2 \alpha L}{n}$$

Soit $\Delta_t = \|w_t - w'_t\|_2$. On a la récurrence $\Delta_{t+1} \le (1 - \alpha \lambda) \Delta_t + \frac{2 \alpha L}{n}$, avec $\Delta_0 = 0$.
Par sommation de la suite géométrique :
$$\Delta_t \le \frac{2 \alpha L}{n} \sum_{k=0}^{t-1} (1 - \alpha \lambda)^k = \frac{2 \alpha L}{n} \frac{1 - (1 - \alpha \lambda)^t}{1 - (1 - \alpha \lambda)} = \frac{2 \alpha L}{n \alpha \lambda} \Big( 1 - (1 - \alpha \lambda)^t \Big)$$
Puisque $1 - (1 - \alpha \lambda)^t < 1$ pour tout $t \ge 0$ (car $0 < 1 - \alpha \lambda < 1$) :
$$\Delta_t \le \frac{2 L}{\lambda n}$$

La distance entre les trajectoires de la descente de gradient sur les deux échantillons perturbés est uniformément majorée pour toutes les itérations :
$$\|w_t - w'_t\|_2 \le \frac{2 L}{\lambda n}$$

#### Conclusion
Ce résultat remarquable prouve que la descente de gradient sur une fonction fortement convexe est intrinsèquement stable au sens uniforme, et que cette stabilité ne dépend pas du temps d'entraînement $T$ (pas de dégradation asymptotique). La régularisation forte garantit une stabilisation globale de l'algorithme d'optimisation.
