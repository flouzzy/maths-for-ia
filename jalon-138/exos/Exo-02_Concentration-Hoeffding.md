# Exercice 2 : Inégalité de Hoeffding classique et optimalité (Niveau 2)

## Énoncé
Soient $X_1, \dots, X_n$ des variables aléatoires indépendantes et identiquement distribuées (i.i.d.) de Rademacher (c'est-à-dire $\mathbb{P}(X_i = 1) = \mathbb{P}(X_i = -1) = 1/2$).
On note $S_n = \sum_{i=1}^n X_i$.
1. Calculer la moyenne et la variance de $S_n$.
2. En utilisant l'inégalité de Hoeffding pour les variables bornées, donner une borne supérieure pour la probabilité de déviation $\mathbb{P}(S_n \ge t)$ pour tout $t > 0$.
3. Comparer cette borne avec l'approximation gaussienne donnée par le Théorème Central Limite (TCL) lorsque $n$ est grand.

---

## Correction Détaillée

### 1. Moyenne et variance de $S_n$
Puisque les variables $X_i$ sont de Rademacher :
$$\mathbb{E}[X_i] = 1 \times \frac{1}{2} + (-1) \times \frac{1}{2} = 0$$
$$\text{Var}(X_i) = \mathbb{E}[X_i^2] - (\mathbb{E}[X_i])^2 = 1^2 \times \frac{1}{2} + (-1)^2 \times \frac{1}{2} - 0^2 = 1$$

Par linéarité de l'espérance et par indépendance des variables :
$$\mathbb{E}[S_n] = \sum_{i=1}^n \mathbb{E}[X_i] = 0$$
$$\text{Var}(S_n) = \sum_{i=1}^n \text{Var}(X_i) = n$$

### 2. Application de l'inégalité de Hoeffding
L'inégalité de Hoeffding s'applique à des variables aléatoires indépendantes $X_i$ presque sûrement bornées par des intervalles $[a_i, b_i]$.
Ici, pour chaque variable de Rademacher $X_i$, on a $X_i \in [-1, 1]$ presque sûrement, donc :
$$a_i = -1 \quad \text{et} \quad b_i = 1$$
Ce qui donne une amplitude $b_i - a_i = 2$.

L'inégalité de Hoeffding énonce que pour toute somme $S_n = \sum_{i=1}^n X_i$ de variables indépendantes et pour tout $t > 0$ :
$$\mathbb{P}(S_n - \mathbb{E}[S_n] \ge t) \le \exp\left( - \frac{2 t^2}{\sum_{i=1}^n (b_i - a_i)^2} \right)$$

En remplaçant les valeurs :
$$\mathbb{P}(S_n \ge t) \le \exp\left( - \frac{2 t^2}{\sum_{i=1}^n 2^2} \right) = \exp\left( - \frac{2 t^2}{4 n} \right) = \exp\left( - \frac{t^2}{2 n} \right)$$

### 3. Comparaison avec le Théorème Central Limite (TCL)
Le Théorème Central Limite nous dit que lorsque $n \to \infty$, la variable aléatoire renormalisée $\frac{S_n}{\sqrt{n}}$ converge en loi vers une loi normale centrée réduite $\mathcal{N}(0, 1)$.
Pour $n$ grand, on a donc l'approximation :
$$\mathbb{P}(S_n \ge t) = \mathbb{P}\left(\frac{S_n}{\sqrt{n}} \ge \frac{t}{\sqrt{n}}\right) \approx 1 - \Phi\left(\frac{t}{\sqrt{n}}\right)$$
où $\Phi(x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^x e^{-u^2/2} du$ est la fonction de répartition de la loi normale standard.

Pour des grandes valeurs de $x = \frac{t}{\sqrt{n}}$, nous pouvons utiliser l'approximation classique de la queue de la loi normale (borne de Mill) :
$$1 - \Phi(x) \approx \frac{1}{x\sqrt{2\pi}} e^{-x^2/2}$$
Ce qui donne pour notre somme :
$$\mathbb{P}(S_n \ge t) \approx \frac{\sqrt{n}}{t\sqrt{2\pi}} \exp\left( - \frac{t^2}{2 n} \right)$$

En comparant avec la borne de Hoeffding $\exp\left( - \frac{t^2}{2 n} \right)$, on remarque que les deux exposants $-\frac{t^2}{2 n}$ sont identiques. L'inégalité de Hoeffding est donc extrêmement précise, à un facteur pré-exponentiel près de l'ordre de $\frac{\sqrt{n}}{t\sqrt{2\pi}}$, et ce de manière non asymptotique (valable pour tout $n$, pas seulement à la limite).
