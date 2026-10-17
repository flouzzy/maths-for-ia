# Exercice 04

**Difficulté :** $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $(X_n)_{n \ge 1}$ une suite de variables I.I.D. admettant un moment d'ordre 2 fini, c'est-à-dire que $\mathbb{E}[X_1^2] < +\infty$.
On note $\mu = \mathbb{E}[X_1]$ et $\sigma^2 = \text{Var}(X_1)$.
Montrer que la variance empirique définie par $V_n = \frac{1}{n}\sum_{i=1}^n (X_i - \bar{X}_n)^2$ converge presque sûrement vers $\sigma^2$, où $\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i$.

**Correction :**
1. Développons l'expression de $V_n$ :
$V_n = \frac{1}{n}\sum_{i=1}^n (X_i^2 - 2X_i\bar{X}_n + \bar{X}_n^2) = \frac{1}{n}\sum_{i=1}^n X_i^2 - 2\bar{X}_n\frac{1}{n}\sum_{i=1}^n X_i + \bar{X}_n^2 = \frac{1}{n}\sum_{i=1}^n X_i^2 - 2\bar{X}_n^2 + \bar{X}_n^2 = \left(\frac{1}{n}\sum_{i=1}^n X_i^2\right) - \bar{X}_n^2$.
2. Étudions le premier terme : Posons $Y_i = X_i^2$. Les $(Y_i)$ sont I.I.D. et $\mathbb{E}[|Y_1|] = \mathbb{E}[X_1^2] < +\infty$. Par la LFGN, $\frac{1}{n}\sum_{i=1}^n X_i^2$ converge p.s. vers $\mathbb{E}[X_1^2]$.
3. Étudions le deuxième terme : Par la LFGN appliquée aux $(X_i)$ (car $\mathbb{E}[X_1^2] < +\infty \implies \mathbb{E}[|X_1|] < +\infty$), $\bar{X}_n$ converge p.s. vers $\mu$. Par continuité de la fonction carré, $\bar{X}_n^2$ converge p.s. vers $\mu^2$.
4. En rassemblant ces limites :
$V_n \xrightarrow{p.s.} \mathbb{E}[X_1^2] - \mu^2$.
5. Or, par définition de la variance, $\text{Var}(X_1) = \mathbb{E}[X_1^2] - (\mathbb{E}[X_1])^2 = \mathbb{E}[X_1^2] - \mu^2$.
Donc $V_n \xrightarrow{p.s.} \sigma^2$.
