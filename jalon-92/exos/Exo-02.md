# Exercice 2 : Convergence des fréquences empiriques

$\bigstar\star\star\star\star$

On lance une pièce de monnaie équilibrée un grand nombre de fois.
Soit $X_i$ la variable aléatoire qui vaut $1$ si le $i$-ème lancer donne "Pile", et $0$ s'il donne "Face".
Soit $F_n$ la fréquence d'apparition de "Pile" au cours des $n$ premiers lancers.

1. Déterminer la loi de $X_i$, son espérance et sa variance.
2. Exprimer $F_n$ en fonction des $X_i$.
3. Montrer rigoureusement que $F_n$ converge presque sûrement vers $1/2$.

**Correction détaillée :**

1. Puisque la pièce est équilibrée, on a $\mathbb{P}(X_i = 1) = \frac{1}{2}$ et $\mathbb{P}(X_i = 0) = \frac{1}{2}$.
   $X_i$ suit donc une loi de Bernoulli de paramètre $p = 1/2$, soit $X_i \sim \mathcal{B}(1/2)$.
   Son espérance est $\mathbb{E}[X_i] = p = \frac{1}{2}$.
   Sa variance est $\text{Var}(X_i) = p(1-p) = \frac{1}{4}$.
2. La fréquence d'apparition de "Pile" sur $n$ lancers est le nombre total de "Pile" divisé par $n$.
   Le nombre total de "Pile" est la somme des indicatrices $X_i$.
   Donc, $F_n = \frac{1}{n} \sum_{i=1}^n X_i$.
3. La suite $(X_n)_{n \geq 1}$ est une suite de variables I.I.D. d'espérance finie ($\mu = 1/2$).
   D'après la loi forte des grands nombres, la moyenne empirique $F_n = \overline{X}_n$ converge presque sûrement vers $\mathbb{E}[X_1]$.
   Ainsi, $\lim_{n \to +\infty} F_n = \frac{1}{2}$ avec une probabilité de $1$.
