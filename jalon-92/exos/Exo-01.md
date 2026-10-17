# Exercice 1 : Calcul direct de variance et application de Bienaymé-Tchebychev \quad $\bigstar\star\star\star\star$

## Énoncé
Soit $(X_n)_{n \ge 1}$ une suite de variables aléatoires indépendantes suivant une loi de Bernoulli de paramètre $p = 0.5$. On note $S_n = \sum_{i=1}^n X_i$.
1. Calculer $\mathbb{E}[S_n/n]$ et $\text{Var}(S_n/n)$.
2. En utilisant l'inégalité de Bienaymé-Tchebychev, donner une majoration de $\mathbb{P}(|S_n/n - 0.5| \ge 0.1)$ pour $n=100$.

## Correction Détaillée
### 1. Espérance et Variance
On sait que pour $X_i \sim \mathcal{B}(p)$, $\mathbb{E}[X_i] = p = 0.5$ et $\text{Var}(X_i) = p(1-p) = 0.25$.
Par linéarité de l'espérance :
$$ \mathbb{E}\left[\frac{S_n}{n}\right] = \frac{1}{n} \sum_{i=1}^n \mathbb{E}[X_i] = \frac{n \cdot 0.5}{n} = 0.5 $$
Par indépendance des $X_i$, la variance d'une somme est la somme des variances :
$$ \text{Var}\left(\frac{S_n}{n}\right) = \frac{1}{n^2} \sum_{i=1}^n \text{Var}(X_i) = \frac{n \cdot 0.25}{n^2} = \frac{0.25}{n} $$

### 2. Inégalité de Bienaymé-Tchebychev
L'inégalité s'écrit :
$$ \mathbb{P}\left( \left| \frac{S_n}{n} - \mathbb{E}\left[\frac{S_n}{n}\right] \right| \ge \epsilon \right) \le \frac{\text{Var}(S_n/n)}{\epsilon^2} $$
Ici, $\epsilon = 0.1$ et $n = 100$. Donc $\text{Var}(S_{100}/100) = 0.25/100 = 0.0025$.
On applique l'inégalité :
$$ \mathbb{P}\left( \left| \frac{S_{100}}{100} - 0.5 \right| \ge 0.1 \right) \le \frac{0.0025}{0.1^2} = \frac{0.0025}{0.01} = 0.25 $$
Ainsi, la probabilité de s'écarter de plus de $0.1$ de la moyenne est majorée par $25\%$. $\blacksquare$
