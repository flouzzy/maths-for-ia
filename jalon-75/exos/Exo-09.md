\subsection*{Exercice 9 : Contre-exemple sur l'inclusion inverse $L^p \subset L^q$ \quad $\bigstar\bigstar\bigstar$}
**Énoncé :**
Sur l'espace $\mathbb{R}$ muni de la mesure de Lebesgue.
1. Trouver $f$ telle que $f \in L^1(\mathbb{R})$ mais $f \notin L^2(\mathbb{R})$.
2. Trouver $g$ telle que $g \in L^2(\mathbb{R})$ mais $g \notin L^1(\mathbb{R})$.

**Correction détaillée :**
1. Pour avoir $f \in L^1$ mais hors de $L^2$, il faut créer une singularité violente mais d'aire finie. On regarde au voisinage de 0.
   Soit $f(x) = \frac{1}{\sqrt{x}} \mathbf{1}_{]0, 1]}(x)$.
   $\int f = \int_0^1 x^{-1/2} \, dx = [2x^{1/2}]_0^1 = 2 < \infty$. Donc $f \in L^1(\mathbb{R})$.
   $\int |f|^2 = \int_0^1 \frac{1}{x} \, dx = [\ln x]_0^1 = \infty$. Donc $f \notin L^2(\mathbb{R})$.
2. Pour avoir $g \in L^2$ mais hors de $L^1$, il faut une fonction qui décroît lentement à l'infini (les singularités sont lissées).
   Soit $g(x) = \frac{1}{x} \mathbf{1}_{[1, \infty[}(x)$.
   $\int |g|^2 = \int_1^\infty \frac{1}{x^2} \, dx = 1 < \infty$. Donc $g \in L^2(\mathbb{R})$.
   $\int |g| = \int_1^\infty \frac{1}{x} \, dx = \infty$. Donc $g \notin L^1(\mathbb{R})$.
Ces contre-exemples illustrent qu'il n'y a pas d'inclusion stricte entre espaces $L^p$ sur un espace de mesure infinie comme $\mathbb{R}$. \qed
