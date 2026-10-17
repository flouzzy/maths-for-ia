# Exercice 9 : Convergence de la variance empirique (estimateur sans biais) \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé
Soit $(X_n)$ une suite i.i.d. de variables de carré intégrable, d'espérance $\mu$ et de variance $\sigma^2$.
On pose l'estimateur de la variance empirique (sans biais) : $S_n^2 = \frac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X}_n)^2$.
Montrer en utilisant la LFGN que $S_n^2 \xrightarrow{p.s.} \sigma^2$.

## Correction Détaillée
### Étape 1 : Développement algébrique de la somme des carrés
Développons le terme $(X_i - \bar{X}_n)^2$ :
$$ (X_i - \bar{X}_n)^2 = X_i^2 - 2X_i \bar{X}_n + \bar{X}_n^2 $$
En sommant sur $i=1$ à $n$ :
$$ \sum_{i=1}^n (X_i - \bar{X}_n)^2 = \sum_{i=1}^n X_i^2 - 2\bar{X}_n \sum_{i=1}^n X_i + \sum_{i=1}^n \bar{X}_n^2 $$
Or $\sum_{i=1}^n X_i = n \bar{X}_n$. Remplaçons :
$$ \sum_{i=1}^n (X_i - \bar{X}_n)^2 = \sum_{i=1}^n X_i^2 - 2n \bar{X}_n^2 + n \bar{X}_n^2 = \sum_{i=1}^n X_i^2 - n \bar{X}_n^2 $$

### Étape 2 : Réécriture de l'estimateur
L'estimateur $S_n^2$ s'écrit donc :
$$ S_n^2 = \frac{1}{n-1} \left( \sum_{i=1}^n X_i^2 - n \bar{X}_n^2 \right) = \frac{n}{n-1} \left( \frac{1}{n}\sum_{i=1}^n X_i^2 - \bar{X}_n^2 \right) $$

### Étape 3 : Application de la LFGN aux deux termes
- Par la LFGN classique, puisque $X_i \in L^1$, on a $\bar{X}_n \xrightarrow{p.s.} \mu$. Par continuité du carré, $\bar{X}_n^2 \xrightarrow{p.s.} \mu^2$.
- Les variables aléatoires $Y_i = X_i^2$ sont i.i.d. et $\mathbb{E}[|Y_i|] = \mathbb{E}[X_i^2] = \text{Var}(X_i) + \mu^2 = \sigma^2 + \mu^2 < +\infty$ (car $X_i \in L^2$).
Par la LFGN appliquée aux $Y_i$, la moyenne empirique des carrés converge :
$$ \frac{1}{n} \sum_{i=1}^n X_i^2 \xrightarrow{p.s.} \sigma^2 + \mu^2 $$

### Étape 4 : Conclusion par algèbre des limites presque sûres
Les limites presque sûres se comportent comme les limites classiques pour les opérations algébriques d'addition et de multiplication.
Ainsi :
$$ \frac{1}{n}\sum_{i=1}^n X_i^2 - \bar{X}_n^2 \xrightarrow{p.s.} (\sigma^2 + \mu^2) - \mu^2 = \sigma^2 $$
De plus, la constante de normalisation $\frac{n}{n-1}$ tend trivialement vers $1$ quand $n \to \infty$.
Le produit des limites nous donne :
$$ S_n^2 \xrightarrow{p.s.} 1 \times \sigma^2 = \sigma^2 $$
L'estimateur de la variance empirique est donc fortement convergent (ou fortement consistant). $\blacksquare$
