# Exercice 01

**Difficulté :** $\bigstar\star\star\star\star$

**Énoncé :**
Convergence p.s. d'une suite géométrique

Soit $(X_n)$ une suite de variables aléatoires indépendantes et identiquement distribuées selon la loi uniforme sur $[0, 1]$.
Posons $Y_n = \max(X_1, X_2, \dots, X_n)$.
Montrez que $Y_n$ converge presque sûrement vers la variable certaine $Y = 1$.

**Correction exhaustive :**
Puisque $Y_n$ est le maximum de variables à valeurs dans $[0, 1]$, on a pour tout $n$, $0 \le Y_n \le 1$.
De plus, la suite $(Y_n)_{n \ge 1}$ est par définition croissante. En effet, $Y_{n+1} = \max(Y_n, X_{n+1}) \ge Y_n$.
Une suite de variables aléatoires presque sûrement croissante et presque sûrement majorée converge presque sûrement vers une limite.
Appelons cette limite $Y$. Montrons que $Y = 1$ presque sûrement.
Pour tout $\epsilon \in ]0, 1[$, évaluons la probabilité que $Y_n \le 1 - \epsilon$ :
$$ \mathbb{P}(Y_n \le 1 - \epsilon) = \mathbb{P}(\max(X_1, \dots, X_n) \le 1 - \epsilon) $$
Par indépendance des variables $X_i$ :
$$ \mathbb{P}(Y_n \le 1 - \epsilon) = \prod_{i=1}^n \mathbb{P}(X_i \le 1 - \epsilon) = (1 - \epsilon)^n $$
La probabilité de l'événement $\{Y \le 1 - \epsilon\}$ est bornée par $\mathbb{P}(Y_n \le 1 - \epsilon)$ pour tout $n$.
En faisant tendre $n \to \infty$, comme $(1 - \epsilon) \in ]0, 1[$, on a $(1 - \epsilon)^n \to 0$.
Ainsi, $\mathbb{P}(Y \le 1 - \epsilon) = 0$ pour tout $\epsilon > 0$.
Comme $Y_n \le 1$ p.s., on a $Y \le 1$ p.s.
La seule possibilité restante est que $\mathbb{P}(Y = 1) = 1$.
La convergence presque sûre vers 1 est donc établie.
