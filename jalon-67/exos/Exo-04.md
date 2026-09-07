# Exercice 4 : Intégration d'une série avec exponentielles

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Montrer que $\int_0^\infty \frac{x}{e^x - 1} dx = \sum_{n=1}^\infty \frac{1}{n^2}$.

**Solution Détaillée :**
1. Transformons l'intégrande pour faire apparaître une série :
Pour $x > 0$, $e^x > 1$. On peut factoriser par $e^x$ :
$$\frac{x}{e^x - 1} = \frac{x e^{-x}}{1 - e^{-x}}$$
Comme $e^{-x} \in ]0, 1[$, on développe en série géométrique :
$$\frac{x e^{-x}}{1 - e^{-x}} = x e^{-x} \sum_{n=0}^\infty (e^{-x})^n = \sum_{n=0}^\infty x e^{-(n+1)x} = \sum_{n=1}^\infty x e^{-nx}$$

2. Soit $u_n(x) = x e^{-nx}$. Sur $]0, +\infty[$, $u_n(x)$ est une fonction mesurable et strictement **positive**.

3. Le corollaire de Beppo Levi pour les séries positives s'applique, nous permettant d'intervertir l'intégrale et la somme :
$$\int_0^\infty \frac{x}{e^x - 1} dx = \sum_{n=1}^\infty \int_0^\infty x e^{-nx} dx$$

4. Calculons l'intégrale $\int_0^\infty x e^{-nx} dx$ par intégration par parties :
Posons $u = x \implies u' = 1$ et $v' = e^{-nx} \implies v = -\frac{1}{n}e^{-nx}$.
$$\int_0^\infty x e^{-nx} dx = \left[ -\frac{x}{n} e^{-nx} \right]_0^\infty + \frac{1}{n} \int_0^\infty e^{-nx} dx$$
Le terme tout intégré s'annule en $+\infty$ (croissance comparée) et en 0.
$$= \frac{1}{n} \left[ -\frac{1}{n} e^{-nx} \right]_0^\infty = \frac{1}{n^2}$$

5. En substituant dans l'égalité issue de Beppo Levi, nous obtenons bien la célèbre identité (qui est reliée à la fonction Zêta de Riemann et vaut $\pi^2/6$) :
$$\int_0^\infty \frac{x}{e^x - 1} dx = \sum_{n=1}^\infty \frac{1}{n^2}$$
