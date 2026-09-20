### Exercice 1 : Application directe de Jensen pour l'inégalité de la moyenne arithmético-géométrique \quad $\bigstar\star\star\star\star$

**Énoncé :**
Montrer, en utilisant l'inégalité de Jensen, que pour tous réels strictement positifs $x_1, \dots, x_n$, on a :
$$\sqrt[n]{x_1 x_2 \dots x_n} \le \frac{x_1 + x_2 + \dots + x_n}{n}$$

**Correction Détaillée :**
1. Considérons l'espace de probabilité discret uniforme sur $\{1, \dots, n\}$, où chaque issue $i$ a une probabilité de $1/n$.
2. Définissons la variable aléatoire $X$ qui prend la valeur $x_i$ avec probabilité $1/n$. L'espérance de $X$ est $\mathbb{E}[X] = \frac{1}{n}\sum_{i=1}^n x_i$, ce qui correspond à la moyenne arithmétique.
3. La fonction logarithme naturel $\phi(x) = \ln(x)$ est strictement concave sur $\mathbb{R}^{+*}$. L'inégalité de Jensen pour les fonctions concaves s'écrit $\ln(\mathbb{E}[X]) \ge \mathbb{E}[\ln(X)]$.
4. Remplaçons par nos valeurs :
$$\ln\left(\frac{1}{n}\sum_{i=1}^n x_i\right) \ge \frac{1}{n}\sum_{i=1}^n \ln(x_i)$$
5. Par les propriétés du logarithme, la somme des logarithmes est le logarithme du produit : $\sum \ln(x_i) = \ln(\prod x_i)$. Et le coefficient $1/n$ devient un exposant :
$$\ln\left(\frac{1}{n}\sum_{i=1}^n x_i\right) \ge \ln\left( \left(\prod_{i=1}^n x_i\right)^{\frac{1}{n}} \right)$$
6. La fonction exponentielle est strictement croissante. En appliquant l'exponentielle aux deux membres de l'inégalité, la direction est conservée, et les logarithmes disparaissent :
$$\frac{x_1 + \dots + x_n}{n} \ge \sqrt[n]{x_1 \dots x_n}$$
Ceci démontre l'inégalité de la moyenne arithmético-géométrique (AM-GM).
