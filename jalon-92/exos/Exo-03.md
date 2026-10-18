# Exercice 3 : Estimation d'un moment d'ordre supérieur \quad $\bigstar\bigstar\star\star\star$

Soit $(X_n)_{n \geq 1}$ une suite de variables I.I.D. suivant la loi uniforme sur l'intervalle $[0, 1]$.
1. Calculer $\mathbb{E}[X_1^k]$ pour tout entier $k \geq 1$.
2. Soit $M_n^{(k)} = \frac{1}{n} \sum_{i=1}^n X_i^k$. Étudier la convergence de la suite $(M_n^{(k)})_{n \geq 1}$.
3. En déduire une méthode d'estimation presque sûre du paramètre $k$ si celui-ci est inconnu mais que l'on observe la suite $X_i$.

**Correction :**
1. La variable $X_1$ suit une loi uniforme $\mathcal{U}([0,1])$, dont la densité est $f(x) = 1$ si $x \in [0,1]$ et $0$ sinon. Par le théorème de transfert, pour tout $k \geq 1$, on a :
$$\mathbb{E}[X_1^k] = \int_{\mathbb{R}} x^k f(x) dx = \int_0^1 x^k \cdot 1 dx = \left[ \frac{x^{k+1}}{k+1} \right]_0^1 = \frac{1}{k+1}$$
2. Fixons l'entier $k \geq 1$. Considérons la suite de variables aléatoires $Z_i = X_i^k$. Les variables $X_i$ étant I.I.D., les variables $Z_i$ sont également I.I.D. Leur espérance est $\mathbb{E}[Z_1] = \mathbb{E}[X_1^k] = \frac{1}{k+1}$. Comme $X_i$ prend ses valeurs dans $[0,1]$, $Z_i$ est bornée entre 0 et 1, donc son espérance est bien finie. D'après la loi forte des grands nombres de Kolmogorov appliquée à la suite $(Z_n)$, la moyenne empirique converge presque sûrement vers l'espérance :
$$M_n^{(k)} = \frac{1}{n} \sum_{i=1}^n Z_i \xrightarrow{p.s.} \mathbb{E}[Z_1] = \frac{1}{k+1}$$
3. Puisque $M_n^{(k)}$ converge presque sûrement vers $\frac{1}{k+1}$, la quantité $\frac{1}{M_n^{(k)}} - 1$ converge presque sûrement vers $\frac{1}{\frac{1}{k+1}} - 1 = (k+1) - 1 = k$. La fonction $x \mapsto \frac{1}{x} - 1$ étant continue pour $x > 0$ (et $M_n^{(k)} > 0$ presque sûrement car les $X_i$ sont à valeurs dans $[0,1]$ de loi diffuse), cette composition de limites conserve la convergence presque sûre. Ainsi, on peut estimer $k$ par l'estimateur convergent $\hat{k}_n = \frac{1}{M_n^{(k)}} - 1$.
