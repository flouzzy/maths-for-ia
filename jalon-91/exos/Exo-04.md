# Exercice 4 : Concentration empirique par Hoeffding

$\bigstar\bigstar\star\star\star$

**Énoncé :**
Un sondage politique interroge $n = 1000$ personnes choisies indépendamment et uniformément. La proportion réelle d'intentions de vote pour le candidat A est $p$. Soit $\overline{X}_n$ la proportion estimée par le sondage.
Utiliser l'inégalité de Hoeffding pour trouver la probabilité que le sondage se trompe de plus de $3$ points de pourcentage (soit un écart $\epsilon = 0.03$).

**Correction :**
La proportion empirique est $\overline{X}_n = \frac{1}{n} \sum_{i=1}^n X_i$, où chaque $X_i$ est une variable aléatoire de Bernoulli de paramètre $p$. Les variables $X_i$ sont indépendantes et à valeurs dans l'intervalle $[0, 1]$.
Ainsi, $a_i = 0$ et $b_i = 1$ pour tout $i \in \{1, \dots, n\}$.
L'espérance de la moyenne empirique est $\mathbb{E}[\overline{X}_n] = p$.
L'inégalité de Hoeffding pour la moyenne s'écrit :
$$ \mathbb{P}(|\overline{X}_n - \mathbb{E}[\overline{X}_n]| \ge \epsilon) \le 2 \exp\left( - \frac{2 n^2 \epsilon^2}{\sum_{i=1}^n (b_i - a_i)^2} \right) $$
Puisque $b_i - a_i = 1$, le dénominateur est $\sum_{i=1}^n 1 = n$.
La formule se simplifie pour la moyenne :
$$ \mathbb{P}(|\overline{X}_n - p| \ge \epsilon) \le 2 \exp(-2 n \epsilon^2) $$
Dans notre cas, $n = 1000$ et $\epsilon = 0.03$.
Calculons l'exposant :
$$ 2 n \epsilon^2 = 2 \times 1000 \times (0.03)^2 = 2000 \times 0.0009 = 1.8 $$
Ainsi :
$$ \mathbb{P}(|\overline{X}_n - p| \ge 0.03) \le 2 e^{-1.8} $$
La valeur de $e^{-1.8}$ est approximativement $0.1653$.
La probabilité est donc bornée par :
$$ 2 \times 0.1653 \approx 0.3306 $$
La probabilité que le sondage se trompe de plus de $3\%$ est donc garantie inférieure à environ $33\%$.
