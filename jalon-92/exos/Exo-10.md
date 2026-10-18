# Exercice 10 : Méthode de Monte-Carlo pour l'intégration de fonctions non bornées \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

On souhaite calculer $I = \int_0^1 \frac{1}{\sqrt{x}} dx$ par la méthode de Monte-Carlo.
1. Calculer la valeur exacte de l'intégrale $I$.
2. On tire une suite $(U_n)$ I.I.D. de loi uniforme sur $[0,1]$. On pose $X_n = \frac{1}{\sqrt{U_n}}$. La LFGN s'applique-t-elle à la suite $(X_n)$ ?
3. Quelle est la variance de $X_n$ ? Que cela implique-t-il sur la vitesse de convergence si l'on voulait appliquer le Théorème Central Limite (TCL) ultérieurement ?

**Correction :**
1. La valeur exacte est :
$$I = \int_0^1 x^{-1/2} dx = \left[ 2x^{1/2} \right]_0^1 = 2$$
2. Les variables $U_n$ sont I.I.D. $\mathcal{U}([0,1])$. Soit $X_n = \frac{1}{\sqrt{U_n}}$. L'espérance de $X_n$ par le théorème de transfert est :
$$\mathbb{E}[X_n] = \mathbb{E}\left[\frac{1}{\sqrt{U_1}}\right] = \int_0^1 \frac{1}{\sqrt{x}} \times 1 dx = 2$$
L'espérance est finie, et les $X_n$ sont I.I.D. Donc la Loi Forte des Grands Nombres de Kolmogorov s'applique bien : la moyenne empirique $\frac{1}{n}\sum_{i=1}^n X_i$ converge presque sûrement vers $\mathbb{E}[X_1] = 2$.
3. Calculons le moment d'ordre 2 :
$$\mathbb{E}[X_n^2] = \mathbb{E}\left[\frac{1}{U_1}\right] = \int_0^1 \frac{1}{x} dx = [\ln(x)]_0^1 = +\infty$$
La variance est donc infinie. Bien que l'estimateur converge presque sûrement (LFGN), son erreur ne peut pas être encadrée par les outils classiques utilisant la variance (inégalité de Tchebychev) ou le Théorème Central Limite standard, car la normalisation en $\sqrt{n}$ donnera un comportement non gaussien (elle relève de la théorie des lois stables). La convergence existe, mais elle est très lente et erratique.
