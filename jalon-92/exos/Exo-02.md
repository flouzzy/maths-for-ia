# Exercice 2 : Moyenne empirique des lois de Poisson \quad $\bigstar\bigstar\star\star\star$

Soit $(X_n)_{n \geq 1}$ une suite de variables aléatoires I.I.D. suivant une loi de Poisson de paramètre $\lambda > 0$. On pose $\bar{X}_n = \frac{1}{n} \sum_{i=1}^n X_i$.
1. Quelle est la loi de la somme $S_n = \sum_{i=1}^n X_i$ ?
2. Montrer que $\bar{X}_n \xrightarrow{p.s.} \lambda$.
3. Montrer que $\frac{1}{n} \sum_{i=1}^n X_i^2$ converge presque sûrement vers une limite à préciser.

**Correction :**
1. La somme de variables aléatoires indépendantes de lois de Poisson de paramètres respectifs $\lambda_i$ suit une loi de Poisson de paramètre $\sum \lambda_i$. Ici, les $X_i$ sont I.I.D. de loi $\mathcal{P}(\lambda)$. Par conséquent, $S_n = \sum_{i=1}^n X_i$ suit une loi de Poisson de paramètre $n\lambda$.
2. La suite $(X_n)$ est I.I.D. et admet une espérance $\mathbb{E}[X_1] = \lambda < \infty$. La loi forte des grands nombres stipule que la moyenne empirique converge presque sûrement vers l'espérance de la loi. Donc, $\bar{X}_n = \frac{1}{n} S_n \xrightarrow{p.s.} \mathbb{E}[X_1] = \lambda$.
3. Considérons la suite de variables aléatoires $Y_i = X_i^2$. Puisque les $X_i$ sont I.I.D., les variables $Y_i$ le sont également par le lemme des coalitions. Calculons l'espérance de $Y_1$ : $\mathbb{E}[Y_1] = \mathbb{E}[X_1^2]$. On sait que la variance d'une loi de Poisson de paramètre $\lambda$ est $\lambda$. Or $\text{Var}(X_1) = \mathbb{E}[X_1^2] - (\mathbb{E}[X_1])^2$, d'où $\lambda = \mathbb{E}[X_1^2] - \lambda^2$. Ainsi, $\mathbb{E}[Y_1] = \mathbb{E}[X_1^2] = \lambda + \lambda^2$. Cette espérance est finie. D'après la loi forte des grands nombres appliquée à la suite I.I.D. $(Y_n)$, on a $\frac{1}{n} \sum_{i=1}^n Y_i \xrightarrow{p.s.} \mathbb{E}[Y_1]$. Par conséquent, $\frac{1}{n} \sum_{i=1}^n X_i^2 \xrightarrow{p.s.} \lambda + \lambda^2$.
