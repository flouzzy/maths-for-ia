# Exercice 1 : Moyenne empirique d'une loi de Poisson

$\bigstar\star\star\star\star$

Soit $(X_n)_{n \geq 1}$ une suite de variables aléatoires indépendantes et identiquement distribuées, suivant toutes la loi de Poisson de paramètre $\lambda > 0$, c'est-à-dire $X_n \sim \mathcal{P}(\lambda)$.
On rappelle que $\mathbb{E}[X_1] = \lambda$.
On pose $\overline{X}_n = \frac{1}{n} \sum_{i=1}^n X_i$.

1. Que représente $\overline{X}_n$ en termes statistiques ?
2. Énoncer le théorème de la loi forte des grands nombres et l'appliquer à cette suite. Que peut-on conclure sur le comportement asymptotique de $\overline{X}_n$ ?

**Correction détaillée :**

1. La variable $\overline{X}_n$ représente la moyenne empirique de l'échantillon de taille $n$. C'est un estimateur naturel de l'espérance de la loi sous-jacente.
2. Le théorème de la loi forte des grands nombres (LFGN) stipule que si $(X_n)_{n \geq 1}$ est une suite de variables aléatoires I.I.D. admettant une espérance finie $\mathbb{E}[X_1] = \mu$, alors la moyenne empirique $\overline{X}_n$ converge presque sûrement vers $\mu$ lorsque $n$ tend vers l'infini : $\mathbb{P}\left(\lim_{n \to \infty} \overline{X}_n = \mu\right) = 1$.
   Ici, les $X_n$ sont I.I.D. suivant $\mathcal{P}(\lambda)$. Puisque $\mathbb{E}[X_1] = \lambda < +\infty$, les hypothèses de la LFGN sont satisfaites.
   Par conséquent, on conclut que $\overline{X}_n$ converge presque sûrement vers $\lambda$ :
   $$ \overline{X}_n \xrightarrow{p.s.} \lambda $$
