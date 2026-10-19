# Exercice 7 : Au-delà de l'i.i.d. : Une Loi Forte de Kolmogorov pour Variables Indépendantes Centrées

$\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé

Soit $(X_k)_{k \ge 1}$ une suite de variables aléatoires indépendantes définies sur un espace de probabilité $(\Omega, \mathcal{F}, P)$.
On suppose que pour tout $k \ge 1$, l'espérance $E[X_k]$ existe et est nulle, c'est-à-dire $E[X_k] = 0$.
De plus, on suppose que la série des variances normalisées converge :
$$ \sum_{k=1}^{\infty} \frac{\text{Var}(X_k)}{k^2} < \infty $$
Démontrer que la moyenne empirique des $X_k$ converge presque sûrement vers 0, c'est-à-dire :
$$ \frac{1}{n} \sum_{k=1}^n X_k \xrightarrow[n \to \infty]{\text{p.s.}} 0 $$

Ce résultat est une version de la Loi Forte des Grands Nombres de Kolmogorov pour des variables indépendantes mais non nécessairement identiquement distribuées.

## Correction

Nous allons démontrer ce résultat en suivant les étapes classiques de la preuve de la Loi Forte des Grands Nombres de Kolmogorov, impliquant la troncature des variables, le lemme de Borel-Cantelli et le lemme de Kronecker.

Soit $(X_k)_{k \ge 1}$ une suite de variables aléatoires indépendantes telle que $E[X_k] = 0$ pour tout $k \ge 1$ et $\sum_{k=1}^{\infty} \frac{\text{Var}(X_k)}{k^2} < \infty$.

### Étape 1 : Troncature des variables et application du lemme de Borel-Cantelli

Pour chaque $k \ge 1$, nous définissons une variable aléatoire tronquée $Y_k$ comme suit :
$$ Y_k = X_k \mathbf{1}_{\{|X_k| \le k\}} $$
où $\mathbf{1}_{\{|X_k| \le k\}}$ est la fonction indicatrice de l'événement $\{|X_k| \le k\}$.

Nous allons montrer que la différence entre $X_k$ et $Y_k$ est négligeable pour la convergence presque sûre de la moyenne.
Considérons la série des probabilités que $X_k$ et $Y_k$ diffèrent :
$$ \sum_{k=1}^{\infty} P(X_k \ne Y_k) = \sum_{k=1}^{\infty} P(|X_k| > k) $$
Puisque $E[X_k] = 0$, nous avons $\text{Var}(X_k) = E[X_k^2]$. Par l'inégalité de Markov (ou de Chebyshev pour $X_k^2$), pour tout $k \ge 1$ :
$$ P(|X_k| > k) = P(X_k^2 > k^2) \le \frac{E[X_k^2]}{k^2} = \frac{\text{Var}(X_k)}{k^2} $$
Par conséquent, la série $\sum_{k=1}^{\infty} P(|X_k| > k)$ est majorée par la série convergente $\sum_{k=1}^{\infty} \frac{\text{Var}(X_k)}{k^2}$ :
$$ \sum_{k=1}^{\infty} P(|X_k| > k) \le \sum_{k=1}^{\infty} \frac{\text{Var}(X_k)}{k^2} < \infty $$
D'après le premier lemme de Borel-Cantelli, la convergence de cette série implique que l'événement $\{|X_k| > k\}$ ne se produit qu'un nombre fini de fois presque sûrement. C'est-à-dire :
$$ P(|X_k| > k \text{ infiniment souvent}) = 0 $$
Cela signifie qu'il existe un ensemble $\Omega_0 \subset \Omega$ de probabilité 1 tel que pour tout $\omega \in \Omega_0$, il existe un entier $N(\omega)$ tel que pour tout $k > N(\omega)$, on a $|X_k(\omega)| \le k$.
Pour $\omega \in \Omega_0$ et $k > N(\omega)$, nous avons $X_k(\omega) = Y_k(\omega)$.
Par conséquent, pour $\omega \in \Omega_0$, la suite $(X_k(\omega) - Y_k(\omega))$ est nulle pour $k$ suffisamment grand.
La moyenne des différences converge donc presque sûrement vers 0 :
$$ \frac{1}{n} \sum_{k=1}^n (X_k - Y_k) \xrightarrow[n \to \infty]{\text{p.s.}} 0 $$

Pour conclure la démonstration, il nous suffit de montrer que $\frac{1}{n} \sum_{k=1}^n Y_k \xrightarrow[n \to \infty]{\text{p.s.}} 0$.

### Étape 2 : Convergence presque sûre de la somme des variables tronquées centrées

Considérons les variables tronquées centrées $Z_k = Y_k - E[Y_k]$. Les variables $Z_k$ sont indépendantes car les $Y_k$ le sont (les $X_k$ sont indépendantes et la troncature est une fonction mesurable). De plus, $E[Z_k] = 0$.
Nous allons appliquer le critère de convergence de Kolmogorov pour les séries de variables aléatoires indépendantes. Ce critère stipule que si $\sum_{k=1}^{\infty} \text{Var}(Z_k) < \infty$, alors $\sum_{k=1}^{\infty} Z_k$ converge presque sûrement.
Ici, nous allons l'appliquer à la série $\sum_{k=1}^{\infty} \frac{Z_k}{k}$.
Nous devons donc vérifier que $\sum_{k=1}^{\infty} \text{Var}\left(\frac{Z_k}{k}\right) < \infty$.
$$ \sum_{k=1}^{\infty} \text{Var}\left(\frac{Z_k}{k}\right) = \sum_{k=1}^{\infty} \frac{\text{Var}(Z_k)}{k^2} = \sum_{k=1}^{\infty} \frac{\text{Var}(Y_k - E[Y_k])}{k^2} = \sum_{k=1}^{\infty} \frac{\text{Var}(Y_k)}{k^2} $$
Nous savons que $\text{Var}(Y_k) \le E[Y_k^2]$.
De plus, $Y_k^2 = X_k^2 \mathbf{1}_{\{|X_k| \le k\}}$.
Donc, $E[Y_k^2] = E[X_k^2 \mathbf{1}_{\{|X_k| \le k\}}]$.
Puisque $\mathbf{1}_{\{|X_k| \le k\}} \le 1$, nous avons $E[X_k^2 \mathbf{1}_{\{|X_k| \le k\}}] \le E[X_k^2]$.
Ainsi, $\text{Var}(Y_k) \le E[Y_k^2] \le E[X_k^2] = \text{Var}(X_k)$.
Par conséquent :
$$ \sum_{k=1}^{\infty} \frac{\text{Var}(Y_k)}{k^2} \le \sum_{k=1}^{\infty} \frac{\text{Var}(X_k)}{k^2} $$
Puisque la série $\sum_{k=1}^{\infty} \frac{\text{Var}(X_k)}{k^2}$ converge par hypothèse, la série $\sum_{k=1}^{\infty} \frac{\text{Var}(Y_k)}{k^2}$ converge également.
D'après le critère de convergence de Kolmogorov, la série $\sum_{k=1}^{\infty} \frac{Y_k - E[Y_k]}{k}$ converge presque sûrement.
Soit $S_n' = \sum_{k=1}^n \frac{Y_k - E[Y_k]}{k}$. Nous avons $S_n' \xrightarrow[n \to \infty]{\text{p.s.}} S'$ pour une variable aléatoire $S'$.
Nous appliquons maintenant le lemme de Kronecker. Le lemme de Kronecker stipule que si une série $\sum_{k=1}^{\infty} a_k$ converge, alors $\frac{1}{n} \sum_{k=1}^n k a_k \to 0$.
En posant $a_k = \frac{Y_k - E[Y_k]}{k}$, nous avons que $\sum_{k=1}^{\infty} a_k$ converge presque sûrement.
Alors, par le lemme de Kronecker :
$$ \frac{1}{n} \sum_{k=1}^n k \left(\frac{Y_k - E[Y_k]}{k}\right) = \frac{1}{n} \sum_{k=1}^n (Y_k - E[Y_k]) \xrightarrow[n \to \infty]{\text{p.s.}} 0 $$

### Étape 3 : Convergence de la moyenne des espérances des variables tronquées

Il nous reste à montrer que $\frac{1}{n} \sum_{k=1}^n E[Y_k] \xrightarrow[n \to \infty]{} 0$.
Nous avons $E[Y_k] = E[X_k \mathbf{1}_{\{|X_k| \le k\}}]$.
Puisque $E[X_k] = 0$, nous pouvons écrire :
$$ E[Y_k] = E[X_k \mathbf{1}_{\{|X_k| \le k\}}] = E[X_k] - E[X_k \mathbf{1}_{\{|X_k| > k\}}] = 0 - E[X_k \mathbf{1}_{\{|X_k| > k\}}] = -E[X_k \mathbf{1}_{\{|X_k| > k\}}] $$
Donc, $|E[Y_k]| = |E[X_k \mathbf{1}_{\{|X_k| > k\}}]| \le E[|X_k| \mathbf{1}_{\{|X_k| > k\}}]$.
Nous voulons montrer que $\frac{1}{n} \sum_{k=1}^n E[Y_k] \to 0$. D'après le lemme de Cesaro, si $\sum_{k=1}^\infty \frac{|E[Y_k]|}{k}$ converge, alors $\frac{1}{n} \sum_{k=1}^n E[Y_k] \to 0$. (En fait, le lemme de Kronecker est plus général : si $\sum a_k$ converge, alors $\frac{1}{n} \sum_{k=1}^n k a_k \to 0$. Ici, nous voulons $\frac{1}{n} \sum_{k=1}^n E[Y_k] \to 0$. Si $\sum E[Y_k]$ converge, alors la moyenne de Cesaro converge vers 0. Mais $\sum E[Y_k]$ ne converge pas nécessairement. Cependant, si $\sum \frac{E[Y_k]}{k}$ converge, alors $\frac{1}{n} \sum E[Y_k]$ converge vers 0 par Kronecker. Non, c'est $\frac{1}{n} \sum k a_k$.
Si $\sum_{k=1}^\infty \frac{E[Y_k]}{k}$ converge, alors par Kronecker, $\frac{1}{n} \sum_{k=1}^n E[Y_k] \to 0$.
Nous allons montrer que $\sum_{k=1}^{\infty} \frac{|E[Y_k]|}{k} < \infty$.
$$ \sum_{k=1}^{\infty} \frac{|E[Y_k]|}{k} \le \sum_{k=1}^{\infty} \frac{E[|X_k| \mathbf{1}_{\{|X_k| > k\}}]}{k} $$
Pour le terme $E[|X_k| \mathbf{1}_{\{|X_k| > k\}}]$, nous utilisons l'inégalité suivante : pour tout $x > k$, on a $x < x^2/k$.
Donc, $|X_k| \mathbf{1}_{\{|X_k| > k\}} \le \frac{X_k^2}{k} \mathbf{1}_{\{|X_k| > k\}}$.
En prenant l'espérance :
$$ E[|X_k| \mathbf{1}_{\{|X_k| > k\}}] \le E\left[\frac{X_k^2}{k} \mathbf{1}_{\{|X_k| > k\}}\right] = \frac{1}{k} E[X_k^2 \mathbf{1}_{\{|X_k| > k\}}] $$
En substituant cette inégalité dans la somme :
$$ \sum_{k=1}^{\infty} \frac{|E[Y_k]|}{k} \le \sum_{k=1}^{\infty} \frac{1}{k} \left( \frac{1}{k} E[X_k^2 \mathbf{1}_{\{|X_k| > k\}}] \right) = \sum_{k=1}^{\infty} \frac{E[X_k^2 \mathbf{1}_{\{|X_k| > k\}}]}{k^2} $$
Nous savons que $\sum_{k=1}^{\infty} \frac{\text{Var}(X_k)}{k^2} = \sum_{k=1}^{\infty} \frac{E[X_k^2]}{k^2} < \infty$.
De plus, $E[X_k^2 \mathbf{1}_{\{|X_k| > k\}}] \le E[X_k^2]$.
Par conséquent, la série $\sum_{k=1}^{\infty} \frac{E[X_k^2 \mathbf{1}_{\{|X_k| > k\}}]}{k^2}$ est une série à termes positifs majorée par une série convergente, donc elle converge.
$$ \sum_{k=1}^{\infty} \frac{E[X_k^2 \mathbf{1}_{\{|X_k| > k\}}]}{k^2} \le \sum_{k=1}^{\infty} \frac{E[X_k^2]}{k^2} = \sum_{k=1}^{\infty} \frac{\text{Var}(X_k)}{k^2} < \infty $$
Ainsi, nous avons montré que $\sum_{k=1}^{\infty} \frac{|E[Y_k]|}{k} < \infty$.
Puisque la série $\sum_{k=1}^{\infty} \frac{E[Y_k]}{k}$ converge absolument, elle converge.
En appliquant le lemme de Kronecker à la suite $a_k = \frac{E[Y_k]}{k}$, nous obtenons :
$$ \frac{1}{n} \sum_{k=1}^n k \left(\frac{E[Y_k]}{k}\right) = \frac{1}{n} \sum_{k=1}^n E[Y_k] \xrightarrow[n \to \infty]{} 0 $$

### Étape 4 : Conclusion

En combinant les résultats des étapes 1, 2 et 3, nous avons :
$$ \frac{1}{n} \sum_{k=1}^n X_k = \frac{1}{n} \sum_{k=1}^n (X_k - Y_k) + \frac{1}{n} \sum_{k=1}^n (Y_k - E[Y_k]) + \frac{1}{n} \sum_{k=1}^n E[Y_k] $$
D'après l'étape 1 : $\frac{1}{n} \sum_{k=1}^n (X_k - Y_k) \xrightarrow[n \to \infty]{\text{p.s.}} 0$.
D'après l'étape 2 : $\frac{1}{n} \sum_{k=1}^n (Y_k - E[Y_k]) \xrightarrow[n \to \infty]{\text{p.s.}} 0$.
D'après l'étape 3 : $\frac{1}{n} \sum_{k=1}^n E[Y_k] \xrightarrow[n \to \infty]{} 0$.

En additionnant ces trois convergences, nous obtenons la convergence presque sûre de la moyenne empirique :
$$ \frac{1}{n} \sum_{k=1}^n X_k \xrightarrow[n \to \infty]{\text{p.s.}} 0 $$
Ceci conclut la démonstration.