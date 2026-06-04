# Exercice 5 : Inégalité de Bernstein vs Inégalité de Hoeffding (Niveau 5)

## Énoncé
Soient $X_1, \dots, X_n$ des variables aléatoires indépendantes centrées ($\mathbb{E}[X_i] = 0$) et bornées presque sûrement par une constante $M > 0$ (c'est-à-dire $|X_i| \le M$).
On note $\sigma_i^2 = \text{Var}(X_i)$ la variance de chaque variable, et $\sigma^2 = \frac{1}{n} \sum_{i=1}^n \sigma_i^2$ la variance moyenne.
Soit $S_n = \sum_{i=1}^n X_i$.
1. Rappeler l'inégalité de Bernstein pour cette somme.
2. Rappeler la borne de Hoeffding pour cette même somme.
3. Soit un cas où les variables $X_i$ ont une très faible variance (par exemple, $\sigma_i^2 \ll M^2$). Démontrer que l'inégalité de Bernstein donne une borne exponentiellement plus serrée que l'inégalité de Hoeffding pour des déviations modérées.

---

## Correction Détaillée

### 1. Inégalité de Bernstein
L'inégalité de Bernstein prend en compte l'information de variance pour affiner la borne de concentration. Elle s'énonce ainsi :
$$\mathbb{P}(S_n \ge t) \le \exp\left( - \frac{t^2}{2 \sum_{i=1}^n \sigma_i^2 + \frac{2}{3} M t} \right)$$
En utilisant la variance moyenne $\sigma^2 = \frac{1}{n} \sum_{i=1}^n \sigma_i^2$, la formule se réécrit :
$$\mathbb{P}(S_n \ge t) \le \exp\left( - \frac{t^2}{2 n \sigma^2 + \frac{2}{3} M t} \right)$$

### 2. Inégalité de Hoeffding
Puisque $|X_i| \le M$, chaque variable $X_i$ est à valeurs dans $[-M, M]$, d'amplitude $b_i - a_i = 2M$.
L'inégalité de Hoeffding donne :
$$\mathbb{P}(S_n \ge t) \le \exp\left( - \frac{2 t^2}{\sum_{i=1}^n (2M)^2} \right) = \exp\left( - \frac{2 t^2}{4 n M^2} \right) = \exp\left( - \frac{t^2}{2 n M^2} \right)$$

### 3. Comparaison des bornes (Bernstein vs Hoeffding)
Comparons les dénominateurs des arguments de l'exponentielle (ce qui revient à comparer les exposants en valeur absolue).
- Pour Hoeffding, l'exposant (en valeur absolue) est :
$$E_H = \frac{t^2}{2 n M^2}$$
- Pour Bernstein, l'exposant (en valeur absolue) est :
$$E_B = \frac{t^2}{2 n \sigma^2 + \frac{2}{3} M t}$$

Pour que Bernstein soit plus serrée (c'est-à-dire que la probabilité soit plus petite), il faut que $E_B > E_H$, ce qui équivaut à :
$$2 n \sigma^2 + \frac{2}{3} M t < 2 n M^2$$

Analysons ce cas sous l'hypothèse d'une faible variance relative : $\sigma^2 \ll M^2$.
Supposons que nous nous intéressons à des déviations modérées de la forme $t = n \epsilon$ (où $\epsilon > 0$ représente le seuil de déviation moyen par variable). L'inégalité devient :
$$2 n \sigma^2 + \frac{2}{3} n M \epsilon < 2 n M^2 \iff 2 \sigma^2 + \frac{2}{3} M \epsilon < 2 M^2$$

Si $\sigma^2$ est très petit (par exemple $\sigma^2 = \frac{M^2}{100}$) et que l'on choisit un seuil de déviation fin $\epsilon < M$, alors :
- Le terme de gauche vaut environ $\frac{2 M^2}{100} + \frac{2}{3} M \epsilon$. Si $\epsilon = \frac{M}{10}$, cela donne $\frac{2 M^2}{100} + \frac{2 M^2}{30} \approx 0.087 M^2$.
- Le terme de droite vaut $2 M^2$.
L'inégalité est largement vérifiée ($0.087 M^2 \ll 2 M^2$).

Calculons le rapport des exposants dans ce régime :
$$\frac{E_B}{E_H} = \frac{2 n M^2}{2 n \sigma^2 + \frac{2}{3} M t} = \frac{M^2}{\sigma^2 + \frac{M \epsilon}{3}}$$

Si $\sigma^2 \to 0$ et $\epsilon \to 0$, le rapport est dominé par le ratio $\frac{M^2}{\sigma^2}$, qui peut être arbitrairement grand.
Ainsi, Bernstein capture le fait que si les variables fluctuent très peu (faible variance), la somme va se concentrer beaucoup plus rapidement que ce que prédit la borne pessimiste de Hoeffding (qui ne regarde que les bornes extrêmes $M$). C'est un comportement crucial en IA pour l'analyse des algorithmes d'apprentissage sur des données peu bruitées.
