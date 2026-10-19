# Exercice 6 : Moyenne géométrique empirique

$\bigstar\bigstar\bigstar\star\star$

Soit $(X_n)_{n \geq 1}$ une suite de variables aléatoires I.I.D. strictements positives, telles que $\mathbb{E}[\ln(X_1)]$ soit bien définie et finie.
On définit la moyenne géométrique $G_n = \left( \prod_{i=1}^n X_i \right)^{1/n}$.

1. Montrer que $\ln(G_n)$ s'exprime comme une moyenne empirique.
2. En déduire la limite presque sûre de $G_n$ lorsque $n \to +\infty$.

**Correction détaillée :**

1. En appliquant la fonction logarithme naturel (qui est bijective et transforme les produits en sommes) à $G_n$, on obtient :
   $$ \ln(G_n) = \ln\left( \left( \prod_{i=1}^n X_i \right)^{1/n} \right) = \frac{1}{n} \ln\left( \prod_{i=1}^n X_i \right) = \frac{1}{n} \sum_{i=1}^n \ln(X_i) $$
   Ainsi, $\ln(G_n)$ est la moyenne empirique de la suite de variables aléatoires $Y_i = \ln(X_i)$.
2. Les variables $Y_i = \ln(X_i)$ sont I.I.D. (car les $X_i$ le sont).
   Par hypothèse, $\mathbb{E}[|Y_1|] = \mathbb{E}[|\ln(X_1)|] < +\infty$, donc la loi forte des grands nombres s'applique à la suite $(Y_n)$.
   Par la LFGN, on a :
   $$ \frac{1}{n} \sum_{i=1}^n Y_i \xrightarrow{p.s.} \mathbb{E}[Y_1] $$
   Donc :
   $$ \ln(G_n) \xrightarrow{p.s.} \mathbb{E}[\ln(X_1)] $$
   Puisque la fonction exponentielle est continue sur $\mathbb{R}$, on peut la composer avec la limite presque sûre :
   $$ G_n = \exp(\ln(G_n)) \xrightarrow{p.s.} \exp(\mathbb{E}[\ln(X_1)]) $$
   La limite presque sûre de la moyenne géométrique est donc $e^{\mathbb{E}[\ln(X_1)]}$.
   (Note : Par l'inégalité de Jensen, comme $-\ln$ est convexe, on a toujours $e^{\mathbb{E}[\ln(X_1)]} \leq \mathbb{E}[X_1]$).
