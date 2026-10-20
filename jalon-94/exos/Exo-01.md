# Exercice 1 : Application directe : Approximation d'une loi binomiale \quad $\bigstar\star\star\star\star$

**Énoncé :**
Une compagnie aérienne sait que 5% des passagers ayant réservé un vol ne se présentent pas à l'embarquement. Elle vend 400 billets pour un vol ayant une capacité de 385 places.
Soit $X$ la variable aléatoire représentant le nombre de passagers se présentant à l'embarquement.
1. Quelle est la loi exacte de $X$ ?
2. En utilisant le Théorème Central Limite, estimer la probabilité que tous les passagers se présentant puissent embarquer (c'est-à-dire $\mathbb{P}(X \le 385)$).

**Correction :**

1. La décision de chaque passager de se présenter ou non peut être modélisée par une variable de Bernoulli $Y_i$.
La probabilité qu'un passager se présente est $p = 1 - 0.05 = 0.95$.
Les variables $(Y_i)_{1 \le i \le 400}$ sont supposées I.I.D. de loi $\mathcal{B}(0.95)$.
La somme $X = \sum_{i=1}^{400} Y_i$ représente le nombre total de passagers se présentant.
Ainsi, $X$ suit une loi binomiale exacte : $X \sim \mathcal{B}(n=400, p=0.95)$.

2. L'espérance de $Y_i$ est $\mu = 0.95$.
La variance de $Y_i$ est $\sigma^2 = p(1-p) = 0.95 \times 0.05 = 0.0475$.
Par conséquent, pour la somme $X$, l'espérance est $\mathbb{E}[X] = n\mu = 400 \times 0.95 = 380$ et la variance est $\text{Var}(X) = n\sigma^2 = 400 \times 0.0475 = 19$.
L'écart-type de $X$ est $\sqrt{19} \approx 4.3589$.

Puisque $n=400$ est grand, on peut approcher la loi de la somme par le Théorème Central Limite.
La variable aléatoire $Z = \frac{X - 380}{\sqrt{19}}$ suit approximativement une loi normale centrée réduite $\mathcal{N}(0, 1)$.
On cherche $\mathbb{P}(X \le 385)$.
Cela équivaut à :
$$\mathbb{P}\left( \frac{X - 380}{\sqrt{19}} \le \frac{385 - 380}{\sqrt{19}} \right)$$
$$\mathbb{P}(Z \le 1.147)$$

En utilisant la table de la fonction de répartition $\Phi$ de la loi $\mathcal{N}(0, 1)$ :
$$\Phi(1.147) \approx 0.874$$
La probabilité que tous les passagers puissent embarquer est donc d'environ $87.4\%$.
