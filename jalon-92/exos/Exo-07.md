# Exercice 07

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $(X_n)$ des variables I.I.D. suivant la loi de Cauchy de densité $f(x) = \frac{1}{\pi(1+x^2)}$.
1. Démontrer rigoureusement que $X_1$ n'admet pas d'espérance finie.
2. Sachant que la moyenne empirique $\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i$ a la même loi de Cauchy que $X_1$ (sans démonstration), la LFGN est-elle respectée ?

**Correction :**
1. L'espérance de $X_1$ existe (au sens de Lebesgue) si et seulement si $\mathbb{E}[|X_1|] < +\infty$.
Calculons cette intégrale :
$\mathbb{E}[|X_1|] = \int_{-\infty}^{+\infty} |x| \frac{1}{\pi(1+x^2)} dx = 2 \int_{0}^{+\infty} \frac{x}{\pi(1+x^2)} dx$.
Effectuons le changement de variable $u = 1+x^2$, $du = 2x dx$ :
$\int_{0}^{A} \frac{2x}{2\pi(1+x^2)} dx = \frac{1}{\pi} [\ln(1+x^2)]_0^A = \frac{\ln(1+A^2)}{\pi}$.
Lorsque $A \to +\infty$, $\frac{\ln(1+A^2)}{\pi} \to +\infty$.
Ainsi, l'intégrale diverge et $\mathbb{E}[|X_1|] = +\infty$. La variable $X_1$ n'est pas intégrable.
2. Comme $\mathbb{E}[|X_1|] = +\infty$, les hypothèses de la LFGN ne sont pas satisfaites.
De plus, si $\bar{X}_n$ convergeait presque sûrement vers une constante $c$, alors $\bar{X}_n$ convergerait en loi vers la mesure de Dirac $\delta_c$. Or, $\bar{X}_n$ suit la loi de Cauchy $f(x)$ pour tout $n$, sa distribution ne se concentre donc pas. Il n'y a aucune convergence vers une constante. La LFGN est bel et bien mise en échec.
