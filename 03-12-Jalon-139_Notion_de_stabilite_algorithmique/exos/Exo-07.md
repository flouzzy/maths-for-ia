# Exercice 7 : Lien Entre Stabilité Uniforme et Variance de l'Erreur Empirique (★★★★☆)

## Énoncé
Soit $A$ un algorithme d'apprentissage $\beta$-uniformément stable par rapport à une fonction de perte $\ell$ bornée par $M > 0$.
Soit $S$ un échantillon de $n$ variables i.i.d. tirées selon la distribution $\mathcal{D}$.
On note pour simplifier $L(S) = R(A(S))$ et $L_n(S) = R_n(A(S))$.
Démontrer que la variance de la différence entre le risque théorique et le risque empirique est majorée comme suit :
$$\text{Var}\big( L(S) - L_n(S) \big) \le \frac{(2n\beta + M)^2}{2n}$$

---

## Correction Détaillée

### 1. Initialisation et stratégie
Pour contrôler la variance d'une fonction générale de plusieurs variables indépendantes, un outil classique et extrêmement efficace est l'inégalité d'Efron-Stein (démontrée dans le Jalon 138).
Soit $F(S) = L(S) - L_n(S) = R(A(S)) - R_n(A(S))$.
Puisque $S = (Z_1, \dots, Z_n)$ est composé de variables aléatoires indépendantes $Z_j \sim \mathcal{D}$, l'inégalité d'Efron-Stein énonce :
$$\text{Var}(F(S)) \le \frac{1}{2} \sum_{i=1}^n \mathbb{E}\big[ (F(S) - F(S^{(i)}))^2 \big]$$
où $S^{(i)} = (Z_1, \dots, Z'_i, \dots, Z_n)$ avec $Z'_i \sim \mathcal{D}$ indépendant de $S$.

### 2. Majoration de la différence quadratique
Dans le Jalon 139 (section 3, Étape 1), nous avons démontré de manière très détaillée et rigoureuse que pour tout échantillon $S$ et tout échantillon perturbé d'une coordonnée $S^{(i)}$, la différence $|F(S) - F(S^{(i)})|$ est bornée presque sûrement par :
$$|F(S) - F(S^{(i)})| \le 2\beta + \frac{M}{n}$$
où $\beta$ est la constante de stabilité uniforme et $M$ est la borne supérieure de la fonction de perte $\ell$.

En élevant cette inégalité presque sûre au carré :
$$(F(S) - F(S^{(i)}))^2 \le \left( 2\beta + \frac{M}{n} \right)^2 \quad \text{presque sûrement.}$$

### 3. Intégration et sommation
Prenons l'espérance mathématique de chaque côté de cette inégalité :
$$\mathbb{E}\big[ (F(S) - F(S^{(i)}))^2 \big] \le \left( 2\beta + \frac{M}{n} \right)^2$$

Sommons maintenant cette borne supérieure sur l'ensemble des $n$ indices de coordonnées de $i=1$ à $n$ :
$$\sum_{i=1}^n \mathbb{E}\big[ (F(S) - F(S^{(i)}))^2 \big] \le \sum_{i=1}^n \left( 2\beta + \frac{M}{n} \right)^2 = n \left( 2\beta + \frac{M}{n} \right)^2$$
Re-factorisons le terme sous le carré :
$$n \left( 2\beta + \frac{M}{n} \right)^2 = n \left( \frac{2n\beta + M}{n} \right)^2 = n \frac{(2n\beta + M)^2}{n^2} = \frac{(2n\beta + M)^2}{n}$$

### 4. Application d'Efron-Stein (Conclusion)
En injectant cette somme dans l'inégalité d'Efron-Stein :
$$\text{Var}(F(S)) \le \frac{1}{2} \left[ \sum_{i=1}^n \mathbb{E}\big[ (F(S) - F(S^{(i)}))^2 \big] \right] \le \frac{1}{2} \frac{(2n\beta + M)^2}{n} = \frac{(2n\beta + M)^2}{2n}$$

La majoration de la variance de l'écart de généralisation est rigoureusement démontrée :
$$\text{Var}\big( L(S) - L_n(S) \big) \le \frac{(2n\beta + M)^2}{2n}$$

#### Commentaire d'excellence :
Ce résultat montre que si l'algorithme est stable avec $\beta(n) = \mathcal{O}(1/n)$, alors la variance de l'écart décroît en $\mathcal{O}(1/n)$, ce qui garantit que pour presque tout échantillon d'entraînement, l'écart de généralisation sera extrêmement proche de sa moyenne.
