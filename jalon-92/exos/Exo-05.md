# Exercice 5 : LFGN pour une variable de Cauchy (Le contre-exemple) \quad $\bigstar\bigstar\bigstar\star\star$

## Énoncé
Soit $(C_n)_{n \ge 1}$ des variables i.i.d. de Cauchy de densité $f(x) = \frac{1}{\pi(1+x^2)}$.
On pose $S_n = \sum_{i=1}^n C_i$.
1. Démontrer que $\mathbb{E}[|C_1|] = +\infty$.
2. Sachant que la loi de $S_n$ est de même type (à un facteur d'échelle près, on admet que $\frac{S_n}{n}$ suit la même loi de Cauchy que $C_1$), conclure quant à l'applicabilité de la LFGN.

## Correction Détaillée
### 1. Divergence de l'espérance de la valeur absolue
Calculons l'espérance de $|C_1|$ :
$$ \mathbb{E}[|C_1|] = \int_{-\infty}^{+\infty} |x| \frac{1}{\pi(1+x^2)} dx = \frac{2}{\pi} \int_0^{+\infty} \frac{x}{1+x^2} dx $$
On effectue le changement de variable $u = 1+x^2$, donc $du = 2x dx$, soit $x dx = \frac{1}{2} du$ :
$$ \mathbb{E}[|C_1|] = \frac{2}{\pi} \int_1^{+\infty} \frac{1}{2u} du = \frac{1}{\pi} [\ln(u)]_1^{+\infty} $$
La limite en l'infini de $\ln(u)$ est $+\infty$. Donc l'intégrale diverge. La variable n'est pas intégrable ($C_1 \notin L^1$).

### 2. Conclusion sur la LFGN
Le théorème de la Loi Forte des Grands Nombres (Kolmogorov) exige strictement que $\mathbb{E}[|C_1|] < +\infty$. Cette condition n'étant pas remplie, le théorème ne s'applique pas.
On observe effectivement le phénomène : puisque $\frac{S_n}{n}$ suit la même loi de Cauchy que $C_1$, la moyenne empirique ne se concentre jamais autour d'une valeur (sa distribution reste invariante). Les valeurs extrêmes ont une probabilité suffisamment grande pour faire "sauter" la moyenne en permanence. Il n'y a donc pas de convergence presque sûre vers une constante. $\blacksquare$
