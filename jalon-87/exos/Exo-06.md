# Exercice 6 : Inégalité de Chebyshev et concentration

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

Soit $X$ une variable aléatoire admettant une espérance $\mu$ et une variance $\sigma^2$ finies.
Démontrer l'inégalité de Bienaymé-Chebyshev en utilisant l'inégalité de Markov, puis l'appliquer pour majorer la probabilité que $X$ s'écarte de son espérance d'au moins $3$ écart-types.

### Correction détaillée

1. **Démonstration de l'inégalité de Bienaymé-Chebyshev :**
   L'inégalité de Markov stipule que pour une variable aléatoire positive $Y$ et un réel $a > 0$, $\mathbb{P}(Y \ge a) \le \frac{\mathbb{E}[Y]}{a}$.
   Posons $Y = (X - \mu)^2$. Cette variable est bien positive ou nulle (c'est un carré).
   Posons $a = t^2$ avec $t > 0$.
   L'inégalité de Markov donne :
   $$ \mathbb{P}((X - \mu)^2 \ge t^2) \le \frac{\mathbb{E}[(X - \mu)^2]}{t^2} $$
   Par définition, $\mathbb{E}[(X - \mu)^2] = \mathrm{Var}(X) = \sigma^2$.
   De plus, l'événement $\{(X - \mu)^2 \ge t^2\}$ est strictement équivalent à l'événement $\{|X - \mu| \ge t\}$.
   En remplaçant, on obtient l'inégalité de Bienaymé-Chebyshev :
   $$ \mathbb{P}(|X - \mu| \ge t) \le \frac{\sigma^2}{t^2} $$

2. **Application (règle des 3 sigmas) :**
   On cherche une borne supérieure pour la probabilité que $X$ s'écarte de sa moyenne d'au moins $3\sigma$, c'est-à-dire l'événement $\{|X - \mu| \ge 3\sigma\}$.
   En appliquant l'inégalité démontrée ci-dessus avec $t = 3\sigma$ :
   $$ \mathbb{P}(|X - \mu| \ge 3\sigma) \le \frac{\sigma^2}{(3\sigma)^2} $$
   $$ \mathbb{P}(|X - \mu| \ge 3\sigma) \le \frac{\sigma^2}{9\sigma^2} = \frac{1}{9} $$
   Conclusion : Quelle que soit la loi de distribution de $X$ (pourvu que la variance existe), la probabilité de se trouver à plus de 3 écart-types de la moyenne est inférieure à environ $11.1\%$.
