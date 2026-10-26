# Exercice 5 : LFGN pour une loi exponentielle

$\bigstar\bigstar\bigstar\star\star$

Soit $(X_n)_{n \geq 1}$ une suite de variables aléatoires I.I.D. de loi exponentielle $\mathcal{E}(\lambda)$ avec $\lambda > 0$.
Soit $S_n = \sum_{i=1}^n X_i$.
1. Quelle est l'espérance de $X_1$ ?
2. Vers quelle limite la suite $\frac{n}{S_n}$ converge-t-il presque sûrement ? Justifier soigneusement.

**Correction détaillée :**

1. Pour une loi exponentielle de paramètre $\lambda$, la densité est $f(x) = \lambda e^{-\lambda x}$ sur $\mathbb{R}^+$. L'espérance est connue par intégration par parties : $\mathbb{E}[X_1] = \frac{1}{\lambda}$.
2. Par définition, $S_n = \sum_{i=1}^n X_i$, donc $\frac{S_n}{n} = \overline{X}_n$ est la moyenne empirique.
   Puisque les $X_i$ sont I.I.D. et admettent une espérance finie $\mathbb{E}[X_1] = \frac{1}{\lambda}$, la loi forte des grands nombres garantit que :
   $$ \frac{S_n}{n} \xrightarrow{p.s.} \mathbb{E}[X_1] = \frac{1}{\lambda} $$
   Considérons la fonction $g(x) = \frac{1}{x}$. Cette fonction est continue sur $]0, +\infty[$.
   Puisque $X_i > 0$ presque sûrement, $\frac{S_n}{n} > 0$ presque sûrement.
   Par le théorème de composition des limites presque sûres (la continuité de $g$), on a :
   $$ g\left(\frac{S_n}{n}\right) \xrightarrow{p.s.} g\left(\frac{1}{\lambda}\right) $$
   Soit :
   $$ \frac{n}{S_n} \xrightarrow{p.s.} \lambda $$
   Ainsi, l'inverse de la moyenne empirique est un estimateur fortement consistant du paramètre $\lambda$ de la loi exponentielle.
