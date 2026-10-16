# Exercice 5 : Écart de Tchebychev sur la moyenne empirique

$\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
On dispose de $n$ variables aléatoires indépendantes $X_1, \dots, X_n$ ayant toutes la même espérance $\mu$ et la même variance $\sigma^2$. Soit $\overline{X}_n = \frac{1}{n} \sum_{i=1}^n X_i$.
Déterminer la valeur minimale de $n$ garantissant par l'inégalité de Tchebychev que $\mathbb{P}(|\overline{X}_n - \mu| \ge 0.1\sigma) \le 0.05$.

**Correction :**
Calculons d'abord l'espérance et la variance de la moyenne empirique $\overline{X}_n$.
Par linéarité de l'espérance :
$$ \mathbb{E}[\overline{X}_n] = \frac{1}{n} \sum_{i=1}^n \mathbb{E}[X_i] = \frac{n\mu}{n} = \mu $$
Par indépendance des variables, la variance d'une somme est la somme des variances :
$$ \text{Var}(\overline{X}_n) = \text{Var}\left( \frac{1}{n} \sum_{i=1}^n X_i \right) = \frac{1}{n^2} \sum_{i=1}^n \text{Var}(X_i) = \frac{1}{n^2} (n \sigma^2) = \frac{\sigma^2}{n} $$
Appliquons l'inégalité de Bienaymé-Tchebychev à la variable $\overline{X}_n$ avec l'écart $a = 0.1\sigma$ :
$$ \mathbb{P}(|\overline{X}_n - \mu| \ge a) \le \frac{\text{Var}(\overline{X}_n)}{a^2} $$
En remplaçant :
$$ \mathbb{P}(|\overline{X}_n - \mu| \ge 0.1\sigma) \le \frac{\frac{\sigma^2}{n}}{(0.1\sigma)^2} $$
Le dénominateur est $(0.1\sigma)^2 = 0.01 \sigma^2$.
Donc la borne est :
$$ \frac{\sigma^2}{n \times 0.01 \sigma^2} = \frac{1}{0.01 n} = \frac{100}{n} $$
Nous voulons que cette borne soit inférieure ou égale à la tolérance de $0.05$ :
$$ \frac{100}{n} \le 0.05 $$
En isolant $n$ :
$$ n \ge \frac{100}{0.05} = \frac{100}{1/20} = 2000 $$
Il faut donc au minimum $n = 2000$ échantillons pour garantir ce niveau de précision par Tchebychev, quelle que soit la loi sous-jacente des $X_i$ (pourvu qu'elle admette une variance $\sigma^2$).
