# Exercice 04

**Difficulté :** $\bigstar\bigstar\star\star\star$

**Énoncé :**
Convergence de la moyenne empirique (Loi Faible)

Soit $(X_n)_{n \ge 1}$ une suite de variables aléatoires indépendantes et identiquement distribuées, d'espérance $\mu = \mathbb{E}[X_1]$ et de variance $\sigma^2 = \text{Var}(X_1) < \infty$.
Posons la moyenne empirique $S_n = \frac{1}{n} \sum_{i=1}^n X_i$.
Montrez en utilisant l'inégalité de Bienaymé-Chebyshev que $S_n$ converge en probabilité vers $\mu$.

**Correction exhaustive :**
La moyenne empirique $S_n$ est une combinaison linéaire de variables aléatoires.
Par linéarité de l'espérance, nous calculons l'espérance de $S_n$ :
$$ \mathbb{E}[S_n] = \mathbb{E}\left[\frac{1}{n} \sum_{i=1}^n X_i\right] = \frac{1}{n} \sum_{i=1}^n \mathbb{E}[X_i] = \frac{1}{n} \cdot (n\mu) = \mu $$
Par indépendance des variables aléatoires $X_i$, la variance de la somme est la somme des variances :
$$ \text{Var}(S_n) = \text{Var}\left(\frac{1}{n} \sum_{i=1}^n X_i\right) = \frac{1}{n^2} \sum_{i=1}^n \text{Var}(X_i) = \frac{1}{n^2} \cdot (n\sigma^2) = \frac{\sigma^2}{n} $$
Nous voulons montrer la convergence en probabilité vers $\mu$, c'est-à-dire que pour tout $\epsilon > 0$, $\lim_{n \to \infty} \mathbb{P}(|S_n - \mu| > \epsilon) = 0$.
Fixons un réel $\epsilon > 0$. Appliquons l'inégalité de Bienaymé-Chebyshev à la variable aléatoire $S_n$ :
$$ \mathbb{P}(|S_n - \mathbb{E}[S_n]| \ge \epsilon) \le \frac{\text{Var}(S_n)}{\epsilon^2} $$
En remplaçant l'espérance et la variance par les valeurs calculées :
$$ \mathbb{P}(|S_n - \mu| \ge \epsilon) \le \frac{\sigma^2}{n\epsilon^2} $$
Puisque $\sigma^2$ et $\epsilon$ sont des constantes indépendantes de $n$, lorsque nous passons à la limite $n \to \infty$ :
$$ \lim_{n \to \infty} \frac{\sigma^2}{n\epsilon^2} = 0 $$
Étant donné qu'une probabilité est positive ou nulle, le théorème d'encadrement donne :
$$ \lim_{n \to \infty} \mathbb{P}(|S_n - \mu| \ge \epsilon) = 0 $$
Ainsi, $S_n \xrightarrow{\mathbb{P}} \mu$. C'est la démonstration de la Loi Faible des Grands Nombres dans le cas fini-variant.
