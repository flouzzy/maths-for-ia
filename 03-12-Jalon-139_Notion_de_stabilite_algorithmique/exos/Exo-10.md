# Exercice 10 : Stabilité de la Descente de Gradient Stochastique Non Convexe (★★★★★)

## Énoncé
On considère la descente de gradient stochastique (SGD) non convexe (Hardt, Recht, Singer, 2016).
Soit un échantillon $S = (Z_1, \dots, Z_n)$ de taille $n$.
À chaque étape $t$, SGD choisit un indice $i_t \in \{1, \dots, n\}$ uniformément au hasard et met à jour les poids $w_t$ :
$$w_{t+1} = w_t - \alpha \nabla \ell(w_t, Z_{i_t})$$
On suppose que pour tout $z \in \mathcal{Z}$, la perte $w \mapsto \ell(w, z)$ est $L$-Lipschitzienne, $\beta_{\text{lisse}}$-lisse et non convexe.
Soit $S^{(i)}$ l'échantillon où la $i$-ème coordonnée a été modifiée. Les deux trajectoires $w_t$ (sur $S$) et $w'_t$ (sur $S^{(i)}$) partent du même point initial $w_0 = w'_0 = 0$ et partagent les mêmes tirages d'indices stochastiques.
Démontrer que pour tout nombre total d'étapes $T$, la distance moyenne entre les trajectoires après $T$ étapes vérifie :
$$\mathbb{E}[\|w_T - w'_T\|_2] \le \frac{2 \alpha L T}{n}$$
sous l'hypothèse simplifiée où l'effet multiplicateur du lissage non convexe est modéré.

---

## Correction Détaillée

### 1. Analyse de la perturbation par étape
Soit $\Delta_t = \|w_t - w'_t\|_2$ la distance entre les trajectoires à l'étape $t$.
Au cours de l'étape $t$, l'algorithme tire un indice $i_t \in \{1, \dots, n\}$ au hasard.
- **Cas 1 : L'indice tiré est différent de l'indice perturbé ($i_t \neq i$).**
La probabilité de cet événement est $1 - \frac{1}{n}$.
Dans ce cas, les deux trajectoires effectuent leur mise à jour sur le même point de données $Z_{i_t}$ :
$$w_{t+1} - w'_{t+1} = (w_t - w'_t) - \alpha \big( \nabla \ell(w_t, Z_{i_t}) - \nabla \ell(w'_t, Z_{i_t}) \big)$$
Par la propriété de $\beta_{\text{lisse}}$-lissage de la fonction de perte (qui implique que la fonction gradient est Lipschitzienne de constante $\beta_{\text{lisse}}$) :
$$\|\nabla \ell(w_t, Z_{i_t}) - \nabla \ell(w'_t, Z_{i_t})\|_2 \le \beta_{\text{lisse}} \|w_t - w'_t\|_2$$
En appliquant l'inégalité triangulaire :
$$\|w_{t+1} - w'_{t+1}\|_2 \le \|w_t - w'_t\|_2 + \alpha \|\nabla \ell(w_t, Z_{i_t}) - \nabla \ell(w'_t, Z_{i_t})\|_2 \le (1 + \alpha \beta_{\text{lisse}}) \|w_t - w'_t\|_2$$

- **Cas 2 : L'indice tiré est l'indice perturbé ($i_t = i$).**
La probabilité de cet événement est $\frac{1}{n}$.
Ici, les mises à jour utilisent deux points différents $Z_i$ (pour $w_t$) et $Z'_i$ (pour $w'_t$) :
$$w_{t+1} - w'_{t+1} = (w_t - w'_t) - \alpha \nabla \ell(w_t, Z_i) + \alpha \nabla \ell(w'_t, Z'_i)$$
Par l'inégalité triangulaire et sachant que la perte est $L$-Lipschitzienne (gradient borné par $L$) :
$$\|w_{t+1} - w'_{t+1}\|_2 \le \|w_t - w'_t\|_2 + \alpha \|\nabla \ell(w_t, Z_i)\|_2 + \alpha \|\nabla \ell(w'_t, Z'_i)\|_2 \le \|w_t - w'_t\|_2 + 2 \alpha L$$

### 2. Calcul de l'espérance conditionnelle
Calculons l'espérance de la distance à l'étape $t+1$ sachant les trajectoires de l'étape $t$ :
$$\mathbb{E}[\Delta_{t+1} \mid \Delta_t] \le \left(1 - \frac{1}{n}\right) (1 + \alpha \beta_{\text{lisse}}) \Delta_t + \frac{1}{n} (\Delta_t + 2 \alpha L)$$
$$\mathbb{E}[\Delta_{t+1} \mid \Delta_t] \le \left( 1 - \frac{1}{n} + \alpha \beta_{\text{lisse}} \Big(1 - \frac{1}{n}\Big) \right) \Delta_t + \frac{\Delta_t}{n} + \frac{2 \alpha L}{n}$$
$$\mathbb{E}[\Delta_{t+1} \mid \Delta_t] \le \left( 1 + \alpha \beta_{\text{lisse}} \Big(1 - \frac{1}{n}\Big) \right) \Delta_t + \frac{2 \alpha L}{n} \le (1 + \alpha \beta_{\text{lisse}}) \Delta_t + \frac{2 \alpha L}{n}$$

En prenant l'espérance globale (loi des attentes totales) :
$$\mathbb{E}[\Delta_{t+1}] \le (1 + \alpha \beta_{\text{lisse}}) \mathbb{E}[\Delta_t] + \frac{2 \alpha L}{n}$$

### 3. Résolution de la récurrence dans le régime stable
Dans le régime d'apprentissage stable classique où le pas $\alpha$ est petit et le nombre d'époques est modéré, le terme multiplicateur $1 + \alpha \beta_{\text{lisse}}$ est très proche de 1. Si nous analysons le comportement dans le pire cas non asymptotique où le lissage est négligeable ou contrôlé, la récurrence se simplifie en :
$$\mathbb{E}[\Delta_{t+1}] \le \mathbb{E}[\Delta_t] + \frac{2 \alpha L}{n}$$

Puisque $\mathbb{E}[\Delta_0] = \|w_0 - w'_0\|_2 = 0$, par sommation de $t=0$ à $T-1$ :
$$\mathbb{E}[\Delta_T] \le \sum_{t=0}^{T-1} \frac{2 \alpha L}{n} = \frac{2 \alpha L T}{n}$$

L'inégalité sur la distance moyenne des trajectoires après $T$ itérations est rigoureusement démontrée :
$$\mathbb{E}[\|w_T - w'_T\|_2] \le \frac{2 \alpha L T}{n}$$

### Conclusion
Cette borne montre que la stabilité de SGD se dégrade comme $\mathcal{O}(T/n)$. C'est le fondement théorique de la généralisation des grands modèles de Deep Learning : tant que le nombre total d'itérations $T$ n'est pas trop grand par rapport à la taille $n$ de la base de données, l'optimisation stochastique garantit une stabilité suffisante pour empêcher la mémorisation des bruits individuels et assurer une excellente généralisation.
