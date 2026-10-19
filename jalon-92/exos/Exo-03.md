# Exercice 3 : Estimateur de la variance

$\bigstar\bigstar\star\star\star$

Soit $(X_n)_{n \geq 1}$ une suite de variables aléatoires I.I.D. d'espérance $\mu$ et de variance $\sigma^2$ finies.
On définit le moment empirique d'ordre 2 par $M_{2,n} = \frac{1}{n} \sum_{i=1}^n X_i^2$.

1. Vers quoi $M_{2,n}$ converge-t-il presque sûrement ? Justifier.
2. En déduire que l'estimateur de la variance défini par $V_n = \frac{1}{n} \sum_{i=1}^n X_i^2 - (\overline{X}_n)^2$ converge presque sûrement vers $\sigma^2$.

**Correction détaillée :**

1. Considérons la suite de variables aléatoires $Y_i = X_i^2$.
   Puisque les $X_i$ sont I.I.D., les variables $Y_i$ sont également I.I.D.
   De plus, puisque $X_1$ admet une variance finie $\sigma^2$ et une espérance finie $\mu$, on sait que $\mathbb{E}[X_1^2] = \sigma^2 + \mu^2 < +\infty$.
   Les $Y_i$ vérifient les hypothèses de la loi forte des grands nombres.
   Par conséquent, la moyenne empirique des $Y_i$, qui est exactement $M_{2,n}$, converge presque sûrement vers $\mathbb{E}[Y_1]$.
   $$ M_{2,n} \xrightarrow{p.s.} \mathbb{E}[X_1^2] $$
2. L'estimateur $V_n$ s'écrit $V_n = M_{2,n} - (\overline{X}_n)^2$.
   D'après la LFGN appliquée à $X_i$, on sait que $\overline{X}_n \xrightarrow{p.s.} \mu$.
   Puisque la fonction $x \mapsto x^2$ est continue, la convergence presque sûre est préservée par composition : $(\overline{X}_n)^2 \xrightarrow{p.s.} \mu^2$.
   Par linéarité des limites presque sûres :
   $$ V_n = M_{2,n} - (\overline{X}_n)^2 \xrightarrow{p.s.} \mathbb{E}[X_1^2] - \mu^2 $$
   Or, par définition de la variance, $\mathbb{E}[X_1^2] - \mu^2 = \sigma^2$.
   Donc $V_n \xrightarrow{p.s.} \sigma^2$.
