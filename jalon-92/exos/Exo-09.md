# Exercice 9 : Au-delà de l'Identité : La Loi Forte des Grands Nombres pour des Variables Hétérogènes
$\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé

Soit $(X_n)_{n \ge 1}$ une suite de variables aléatoires indépendantes, dont la loi de probabilité de chaque $X_n$ est définie par :
$P(X_n = n) = \frac{1}{n^3}$
$P(X_n = -n) = \frac{1}{n^3}$
$P(X_n = \frac{1}{n}) = 1 - \frac{2}{n^3}$

On s'intéresse à la convergence de la moyenne arithmétique de ces variables.
Soit $S_N = \sum_{n=1}^N X_n$.

Démontrer que la suite de variables aléatoires $\left(\frac{S_N}{N}\right)_{N \ge 1}$ converge presque sûrement vers une limite finie, et déterminer cette limite.

---

## Correction

Pour démontrer la convergence presque sûre de $\frac{S_N}{N}$, nous allons utiliser une version généralisée de la Loi Forte des Grands Nombres (LFGN), notamment le critère de Kolmogorov pour des variables indépendantes mais non nécessairement identiquement distribuées. Ce critère stipule que si $(Y_n)_{n \ge 1}$ est une suite de variables aléatoires indépendantes avec $E[Y_n] = 0$ pour tout $n$, et si $\sum_{n=1}^\infty \frac{\text{Var}(Y_n)}{n^2} < \infty$, alors $\frac{1}{N}\sum_{n=1}^N Y_n \to 0$ presque sûrement.

Notre approche consistera à :
1.  Calculer l'espérance $E[X_n]$ pour chaque $X_n$.
2.  Calculer la variance $\text{Var}(X_n)$ pour chaque $X_n$.
3.  Appliquer le critère de Kolmogorov à la suite $(X_n - E[X_n])_{n \ge 1}$.
4.  Analyser la convergence de la moyenne des espérances $\frac{1}{N}\sum_{n=1}^N E[X_n]$.
5.  Combiner ces résultats pour conclure sur la convergence de $\frac{S_N}{N}$.

### Étape 1 : Calcul de l'espérance $E[X_n]$

L'espérance d'une variable aléatoire discrète est donnée par $E[X] = \sum_x x P(X=x)$.
Pour $X_n$, les valeurs possibles sont $n$, $-n$ et $\frac{1}{n}$.
$E[X_n] = n \cdot P(X_n = n) + (-n) \cdot P(X_n = -n) + \frac{1}{n} \cdot P(X_n = \frac{1}{n})$
$E[X_n] = n \cdot \frac{1}{n^3} + (-n) \cdot \frac{1}{n^3} + \frac{1}{n} \cdot \left(1 - \frac{2}{n^3}\right)$
$E[X_n] = \frac{n}{n^3} - \frac{n}{n^3} + \frac{1}{n} - \frac{2}{n \cdot n^3}$
$E[X_n] = \frac{1}{n^2} - \frac{1}{n^2} + \frac{1}{n} - \frac{2}{n^4}$
$E[X_n] = \frac{1}{n} - \frac{2}{n^4}$

### Étape 2 : Calcul de la variance $\text{Var}(X_n)$

La variance est donnée par $\text{Var}(X_n) = E[X_n^2] - (E[X_n])^2$.
Calculons d'abord $E[X_n^2]$ :
$E[X_n^2] = n^2 \cdot P(X_n = n) + (-n)^2 \cdot P(X_n = -n) + \left(\frac{1}{n}\right)^2 \cdot P(X_n = \frac{1}{n})$
$E[X_n^2] = n^2 \cdot \frac{1}{n^3} + n^2 \cdot \frac{1}{n^3} + \frac{1}{n^2} \cdot \left(1 - \frac{2}{n^3}\right)$
$E[X_n^2] = \frac{n^2}{n^3} + \frac{n^2}{n^3} + \frac{1}{n^2} - \frac{2}{n^2 \cdot n^3}$
$E[X_n^2] = \frac{1}{n} + \frac{1}{n} + \frac{1}{n^2} - \frac{2}{n^5}$
$E[X_n^2] = \frac{2}{n} + \frac{1}{n^2} - \frac{2}{n^5}$

Maintenant, calculons $\text{Var}(X_n)$ :
$\text{Var}(X_n) = \left(\frac{2}{n} + \frac{1}{n^2} - \frac{2}{n^5}\right) - \left(\frac{1}{n} - \frac{2}{n^4}\right)^2$
$\text{Var}(X_n) = \left(\frac{2}{n} + \frac{1}{n^2} - \frac{2}{n^5}\right) - \left(\left(\frac{1}{n}\right)^2 - 2 \cdot \frac{1}{n} \cdot \frac{2}{n^4} + \left(\frac{2}{n^4}\right)^2\right)$
$\text{Var}(X_n) = \left(\frac{2}{n} + \frac{1}{n^2} - \frac{2}{n^5}\right) - \left(\frac{1}{n^2} - \frac{4}{n^5} + \frac{4}{n^8}\right)$
$\text{Var}(X_n) = \frac{2}{n} + \frac{1}{n^2} - \frac{2}{n^5} - \frac{1}{n^2} + \frac{4}{n^5} - \frac{4}{n^8}$
$\text{Var}(X_n) = \frac{2}{n} + \frac{2}{n^5} - \frac{4}{n^8}$

### Étape 3 : Application du critère de Kolmogorov

Soit $Y_n = X_n - E[X_n]$. Par construction, $E[Y_n] = E[X_n - E[X_n]] = E[X_n] - E[X_n] = 0$.
Les variables $Y_n$ sont indépendantes car les $X_n$ sont indépendantes.
La variance de $Y_n$ est $\text{Var}(Y_n) = \text{Var}(X_n - E[X_n]) = \text{Var}(X_n)$.
Nous devons vérifier la condition de Kolmogorov : $\sum_{n=1}^\infty \frac{\text{Var}(Y_n)}{n^2} < \infty$.
$\sum_{n=1}^\infty \frac{\text{Var}(X_n)}{n^2} = \sum_{n=1}^\infty \frac{1}{n^2} \left(\frac{2}{n} + \frac{2}{n^5} - \frac{4}{n^8}\right)$
$\sum_{n=1}^\infty \frac{\text{Var}(X_n)}{n^2} = \sum_{n=1}^\infty \left(\frac{2}{n^3} + \frac{2}{n^7} - \frac{4}{n^{10}}\right)$

Cette somme peut être décomposée en trois séries :
1.  $\sum_{n=1}^\infty \frac{2}{n^3} = 2 \sum_{n=1}^\infty \frac{1}{n^3}$. Cette série est une série de Riemann (ou p-série) de la forme $\sum \frac{1}{n^p}$ avec $p=3$. Puisque $p=3 > 1$, cette série converge.
2.  $\sum_{n=1}^\infty \frac{2}{n^7} = 2 \sum_{n=1}^\infty \frac{1}{n^7}$. Cette série est une série de Riemann avec $p=7$. Puisque $p=7 > 1$, cette série converge.
3.  $\sum_{n=1}^\infty \frac{4}{n^{10}} = 4 \sum_{n=1}^\infty \frac{1}{n^{10}}$. Cette série est une série de Riemann avec $p=10$. Puisque $p=10 > 1$, cette série converge.

Puisque chacune des trois séries converge, leur somme converge également.
Donc, la condition $\sum_{n=1}^\infty \frac{\text{Var}(X_n)}{n^2} < \infty$ est satisfaite.

Par le critère de Kolmogorov, nous pouvons conclure que $\frac{1}{N}\sum_{n=1}^N Y_n \to 0$ presque sûrement.
C'est-à-dire, $\frac{1}{N}\sum_{n=1}^N (X_n - E[X_n]) \to 0$ presque sûrement.

### Étape 4 : Convergence de la moyenne des espérances

Nous avons $\frac{S_N}{N} = \frac{1}{N}\sum_{n=1}^N X_n = \frac{1}{N}\sum_{n=1}^N (X_n - E[X_n]) + \frac{1}{N}\sum_{n=1}^N E[X_n]$.
Nous savons déjà que le premier terme du membre de droite converge presque sûrement vers 0.
Il nous reste à étudier la convergence du second terme : $\lim_{N \to \infty} \frac{1}{N}\sum_{n=1}^N E[X_n]$.

Nous avons trouvé $E[X_n] = \frac{1}{n} - \frac{2}{n^4}$.
Calculons la limite de $E[X_n]$ lorsque $n \to \infty$:
$\lim_{n \to \infty} E[X_n] = \lim_{n \to \infty} \left(\frac{1}{n} - \frac{2}{n^4}\right) = 0 - 0 = 0$.

Puisque la suite des espérances $(E[X_n])_{n \ge 1}$ converge vers 0, nous pouvons appliquer le théorème de Cesaro (ou théorème de la moyenne de Cesaro), qui stipule que si une suite $(a_n)_{n \ge 1}$ converge vers une limite $L$, alors la suite de ses moyennes arithmétiques $\left(\frac{1}{N}\sum_{n=1}^N a_n\right)_{N \ge 1}$ converge également vers $L$.
Dans notre cas, $a_n = E[X_n]$ et $L=0$.
Par conséquent, $\lim_{N \to \infty} \frac{1}{N}\sum_{n=1}^N E[X_n] = 0$.

### Étape 5 : Conclusion

En combinant les résultats des étapes précédentes :
$\frac{S_N}{N} = \frac{1}{N}\sum_{n=1}^N (X_n - E[X_n]) + \frac{1}{N}\sum_{n=1}^N E[X_n]$

Le premier terme converge presque sûrement vers 0.
Le second terme converge vers 0.

Par conséquent, $\frac{S_N}{N}$ converge presque sûrement vers $0 + 0 = 0$.

La limite presque sûre de $\left(\frac{S_N}{N}\right)_{N \ge 1}$ est $0$.