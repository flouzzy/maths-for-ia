# Exercice 3 : Convergence Presque Sûre de la Variance Empirique : Une Illustration Avancée de la LFGN
$\bigstar\bigstar\star\star\star$

## Énoncé

Soit $(X_n)_{n \ge 1}$ une suite de variables aléatoires réelles indépendantes et identiquement distribuées (i.i.d.). On suppose que $X_1$ possède une espérance finie $E[X_1] = \mu$ et une variance finie $Var(X_1) = \sigma^2 < \infty$.

On définit la moyenne empirique $\bar{X}_n$ pour $n \ge 1$ par :
$$ \bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i $$

Et la variance empirique $S_n^2$ pour $n \ge 2$ par :
$$ S_n^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X}_n)^2 $$

Démontrez que la variance empirique $S_n^2$ converge presque sûrement vers la variance théorique $\sigma^2$ lorsque $n \to \infty$.

$$ S_n^2 \xrightarrow{p.s.} \sigma^2 $$

## Correction

Pour démontrer la convergence presque sûre de la variance empirique $S_n^2$ vers $\sigma^2$, nous allons d'abord manipuler l'expression de $S_n^2$ pour la décomposer en termes auxquels la Loi Forte des Grands Nombres (LFGN) peut être appliquée.

### Étape 1 : Réécriture de la variance empirique

Commençons par développer l'expression de $S_n^2$ :
$$ S_n^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X}_n)^2 $$
$$ S_n^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i^2 - 2X_i\bar{X}_n + \bar{X}_n^2) $$
Nous pouvons séparer la somme en trois termes :
$$ S_n^2 = \frac{1}{n-1} \left( \sum_{i=1}^n X_i^2 - \sum_{i=1}^n 2X_i\bar{X}_n + \sum_{i=1}^n \bar{X}_n^2 \right) $$
Le terme $\bar{X}_n$ est constant par rapport à l'indice de sommation $i$. Nous pouvons donc le sortir des sommes :
$$ S_n^2 = \frac{1}{n-1} \left( \sum_{i=1}^n X_i^2 - 2\bar{X}_n \sum_{i=1}^n X_i + n\bar{X}_n^2 \right) $$
Par définition, $\sum_{i=1}^n X_i = n\bar{X}_n$. En substituant cette expression dans l'équation :
$$ S_n^2 = \frac{1}{n-1} \left( \sum_{i=1}^n X_i^2 - 2\bar{X}_n (n\bar{X}_n) + n\bar{X}_n^2 \right) $$
$$ S_n^2 = \frac{1}{n-1} \left( \sum_{i=1}^n X_i^2 - 2n\bar{X}_n^2 + n\bar{X}_n^2 \right) $$
$$ S_n^2 = \frac{1}{n-1} \left( \sum_{i=1}^n X_i^2 - n\bar{X}_n^2 \right) $$
Pour faire apparaître des moyennes empiriques, nous pouvons factoriser par $n$ :
$$ S_n^2 = \frac{n}{n-1} \left( \frac{1}{n}\sum_{i=1}^n X_i^2 - \bar{X}_n^2 \right) $$
Nous allons maintenant analyser la convergence presque sûre de chaque terme de cette expression.

### Étape 2 : Application de la Loi Forte des Grands Nombres (LFGN)

La Loi Forte des Grands Nombres (LFGN) stipule que si $(Y_k)_{k \ge 1}$ est une suite de variables aléatoires indépendantes et identiquement distribuées (i.i.d.) avec $E[|Y_1|] < \infty$, alors la moyenne empirique $\frac{1}{n}\sum_{k=1}^n Y_k$ converge presque sûrement vers l'espérance $E[Y_1]$ lorsque $n \to \infty$.

#### Convergence de $\bar{X}_n$

Nous avons la suite $(X_n)_{n \ge 1}$ qui est i.i.d. avec $E[X_1] = \mu$ et $Var(X_1) = \sigma^2 < \infty$.
La condition $Var(X_1) < \infty$ implique que $E[X_1^2] < \infty$.
Par l'inégalité de Cauchy-Schwarz, nous savons que $E[|X_1|] \le \sqrt{E[X_1^2]}$. Puisque $E[X_1^2] < \infty$, il s'ensuit que $E[|X_1|] < \infty$.
Les conditions de la LFGN sont donc satisfaites pour la suite $(X_n)_{n \ge 1}$.
Par conséquent, nous avons :
$$ \bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i \xrightarrow{p.s.} E[X_1] = \mu $$

#### Convergence de $\frac{1}{n}\sum_{i=1}^n X_i^2$

Considérons la suite de variables aléatoires $(X_n^2)_{n \ge 1}$. Puisque les $X_n$ sont i.i.d., les $X_n^2$ sont également i.i.d.
Nous devons vérifier la condition d'intégrabilité pour appliquer la LFGN à cette nouvelle suite.
Nous avons supposé que $Var(X_1) = \sigma^2 < \infty$. Par définition de la variance, $Var(X_1) = E[X_1^2] - (E[X_1])^2$.
Donc, $E[X_1^2] = Var(X_1) + (E[X_1])^2 = \sigma^2 + \mu^2$.
Puisque $\sigma^2 < \infty$ et $\mu$ est finie (car $E[|X_1|] < \infty$), il s'ensuit que $E[X_1^2] < \infty$.
La condition $E[|X_1^2|] < \infty$ est donc satisfaite (car $X_1^2 \ge 0$, donc $|X_1^2| = X_1^2$).
Les conditions de la LFGN sont donc satisfaites pour la suite $(X_n^2)_{n \ge 1}$.
Par conséquent, nous obtenons :
$$ \frac{1}{n}\sum_{i=1}^n X_i^2 \xrightarrow{p.s.} E[X_1^2] $$
En substituant l'expression de $E[X_1^2]$ :
$$ \frac{1}{n}\sum_{i=1}^n X_i^2 \xrightarrow{p.s.} \sigma^2 + \mu^2 $$

### Étape 3 : Utilisation des propriétés de la convergence presque sûre

#### Convergence de $\bar{X}_n^2$

Nous avons établi que $\bar{X}_n \xrightarrow{p.s.} \mu$.
La fonction $f(x) = x^2$ est une fonction continue sur $\mathbb{R}$.
Par le théorème de la transformation continue pour la convergence presque sûre, si une suite de variables aléatoires $Y_n$ converge presque sûrement vers une variable aléatoire $Y$ (ou une constante $c$), et si $g$ est une fonction continue, alors $g(Y_n)$ converge presque sûrement vers $g(Y)$ (ou $g(c)$).
En appliquant ce théorème avec $Y_n = \bar{X}_n$ et $g(x) = x^2$, nous obtenons :
$$ \bar{X}_n^2 \xrightarrow{p.s.} \mu^2 $$

#### Convergence de la différence

Nous disposons des convergences presque sûres suivantes :
1.  $\frac{1}{n}\sum_{i=1}^n X_i^2 \xrightarrow{p.s.} \sigma^2 + \mu^2$
2.  $\bar{X}_n^2 \xrightarrow{p.s.} \mu^2$
Par la propriété de linéarité de la convergence presque sûre (si $Y_n \xrightarrow{p.s.} Y$ et $Z_n \xrightarrow{p.s.} Z$, alors $Y_n - Z_n \xrightarrow{p.s.} Y - Z$), nous avons :
$$ \left( \frac{1}{n}\sum_{i=1}^n X_i^2 \right) - \bar{X}_n^2 \xrightarrow{p.s.} (\sigma^2 + \mu^2) - \mu^2 $$
$$ \frac{1}{n}\sum_{i=1}^n X_i^2 - \bar{X}_n^2 \xrightarrow{p.s.} \sigma^2 $$

#### Convergence du facteur $\frac{n}{n-1}$

Enfin, nous devons considérer le facteur $\frac{n}{n-1}$. Pour $n \ge 2$, ce terme est bien défini et sa limite déterministe est :
$$ \lim_{n \to \infty} \frac{n}{n-1} = \lim_{n \to \infty} \frac{1}{1 - 1/n} = 1 $$

### Étape 4 : Conclusion

Nous avons la convergence presque sûre de la différence $\left( \frac{1}{n}\sum_{i=1}^n X_i^2 - \bar{X}_n^2 \right)$ vers $\sigma^2$, et la convergence déterministe du facteur $\frac{n}{n-1}$ vers $1$.
Par la propriété de produit de la convergence presque sûre (si $Y_n \xrightarrow{p.s.} Y$ et $c_n \to c$ déterministiquement, alors $c_n Y_n \xrightarrow{p.s.} cY$), nous pouvons conclure :
$$ S_n^2 = \frac{n}{n-1} \left( \frac{1}{n}\sum_{i=1}^n X_i^2 - \bar{X}_n^2 \right) \xrightarrow{p.s.} 1 \cdot \sigma^2 $$
$$ S_n^2 \xrightarrow{p.s.} \sigma^2 $$
Ceci achève la démonstration de la convergence presque sûre de la variance empirique vers la variance théorique.