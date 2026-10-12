# Exercice 06 : Produit de variables exponentielles
Difficulté : $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soient $X$ et $Y$ deux variables aléatoires indépendantes suivant des lois exponentielles de paramètres respectifs $\lambda$ et $\mu$.
Calculer $\mathbb{E}[e^{-s(X+Y)}]$ pour $s \geq 0$.

**Correction :**
1. L'espérance à calculer est $\mathbb{E}[e^{-sX - sY}] = \mathbb{E}[e^{-sX} e^{-sY}]$.
2. Puisque $X$ et $Y$ sont indépendantes, par le Théorème 1 sur l'espérance du produit pour des fonctions mesurables (ici $x \mapsto e^{-sx}$ et $y \mapsto e^{-sy}$) :
$\mathbb{E}[e^{-sX} e^{-sY}] = \mathbb{E}[e^{-sX}] \mathbb{E}[e^{-sY}]$.
3. Calculons $\mathbb{E}[e^{-sX}]$ :
$\mathbb{E}[e^{-sX}] = \int_0^\infty e^{-sx} \lambda e^{-\lambda x} dx = \lambda \int_0^\infty e^{-(\lambda+s)x} dx$.
Cette intégrale converge pour $\lambda + s > 0$, ce qui est vrai car $\lambda > 0$ et $s \geq 0$.
$\mathbb{E}[e^{-sX}] = \lambda \left[ \frac{e^{-(\lambda+s)x}}{-(\lambda+s)} \right]_0^\infty = \lambda \left( 0 - \frac{1}{-(\lambda+s)} \right) = \frac{\lambda}{\lambda+s}$.
4. De manière analogue, $\mathbb{E}[e^{-sY}] = \frac{\mu}{\mu+s}$.
5. Finalement :
$\mathbb{E}[e^{-s(X+Y)}] = \frac{\lambda}{\lambda+s} \frac{\mu}{\mu+s} = \frac{\lambda\mu}{(\lambda+s)(\mu+s)}$.
*(Note : Ceci représente la transformée de Laplace, ou fonction génératrice des moments, de $X+Y$)*.
