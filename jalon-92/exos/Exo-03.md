# Exercice 3 : Moyenne empirique d'une loi de Poisson \quad $\bigstar\bigstar\star\star\star$

## Énoncé
Soit $(X_n)_{n \ge 1}$ une suite de variables i.i.d. suivant une loi de Poisson de paramètre $\lambda > 0$.
1. Rappeler $\mathbb{E}[X_1]$ et $\text{Var}(X_1)$.
2. Vers quelle valeur converge presque sûrement $\frac{1}{n} \sum_{i=1}^n X_i$ ? Justifier précisément en énonçant le théorème utilisé.
3. Vers quelle valeur converge presque sûrement $\frac{1}{n} \sum_{i=1}^n X_i^2$ ?

## Correction Détaillée
### 1. Espérance et variance de la loi de Poisson
Pour $X_1 \sim \mathcal{P}(\lambda)$, par définition classique des séries entières, $\mathbb{E}[X_1] = \lambda$ et $\text{Var}(X_1) = \lambda$.

### 2. Convergence de la moyenne empirique
Les variables $X_n$ sont i.i.d. et $\mathbb{E}[|X_1|] = \mathbb{E}[X_1] = \lambda < +\infty$.
Nous pouvons appliquer directement le théorème de la loi forte des grands nombres de Kolmogorov. Il garantit que la moyenne empirique converge presque sûrement vers l'espérance théorique :
$$ \frac{1}{n} \sum_{i=1}^n X_i \xrightarrow{p.s.} \mathbb{E}[X_1] = \lambda $$

### 3. Convergence du moment d'ordre 2
Considérons la suite de variables aléatoires $(Y_n)_{n \ge 1}$ définie par $Y_n = X_n^2$.
Puisque les $X_n$ sont i.i.d., les $Y_n$ le sont aussi.
L'espérance de $Y_1$ est $\mathbb{E}[Y_1] = \mathbb{E}[X_1^2]$.
On sait que $\text{Var}(X_1) = \mathbb{E}[X_1^2] - (\mathbb{E}[X_1])^2$, donc $\mathbb{E}[X_1^2] = \text{Var}(X_1) + (\mathbb{E}[X_1])^2 = \lambda + \lambda^2$.
Comme $Y_1$ est positive, $\mathbb{E}[|Y_1|] = \lambda + \lambda^2 < +\infty$.
Par la loi forte des grands nombres appliquée à la suite $(Y_n)$ :
$$ \frac{1}{n} \sum_{i=1}^n X_i^2 \xrightarrow{p.s.} \lambda + \lambda^2 $$ $\blacksquare$
