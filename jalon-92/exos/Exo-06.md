# Exercice 06

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $(X_n)_{n \ge 1}$ des variables I.I.D. strictement positives, telles que $\mathbb{E}[|\ln X_1|] < +\infty$.
On s'intéresse au comportement asymptotique du produit géométrique $G_n = \left(\prod_{i=1}^n X_i\right)^{1/n}$.
Montrer que $G_n$ converge presque sûrement vers une limite que l'on précisera en fonction de $X_1$.

**Correction :**
1. L'expression de $G_n$ suggère de passer au logarithme pour transformer le produit en somme :
$\ln G_n = \ln\left( \left(\prod_{i=1}^n X_i\right)^{1/n} \right) = \frac{1}{n} \sum_{i=1}^n \ln X_i$.
2. Posons $Y_i = \ln X_i$. Les variables $X_i$ étant I.I.D. et la fonction $\ln$ étant mesurable, les variables $(Y_i)$ sont I.I.D.
3. Par hypothèse, on a $\mathbb{E}[|Y_1|] = \mathbb{E}[|\ln X_1|] < +\infty$. La condition d'intégrabilité pour appliquer la LFGN est donc satisfaite.
4. Par la LFGN, on a :
$\ln G_n = \frac{1}{n} \sum_{i=1}^n Y_i \xrightarrow{p.s.} \mathbb{E}[Y_1] = \mathbb{E}[\ln X_1]$.
5. La fonction exponentielle est continue sur $\mathbb{R}$. Par composition continue de la limite presque sûre :
$G_n = \exp(\ln G_n) \xrightarrow{p.s.} \exp(\mathbb{E}[\ln X_1])$.
La limite cherchée est donc $\exp(\mathbb{E}[\ln X_1])$. (On peut noter que par l'inégalité de Jensen, cette limite est inférieure ou égale à $\mathbb{E}[X_1]$).
