# Exercice 9 : Intégrale de Lebesgue et inégalité de Markov $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit $f \in \mathcal{M}_+(X, \mathcal{F})$ intégrable par rapport à $\mu$ (donc $\int f \, d\mu < +\infty$).
Montrer rigoureusement l'inégalité de Markov : pour tout $t > 0$,
$$\mu(\{x \in X \mid f(x) \ge t\}) \le \frac{1}{t} \int_X f \, d\mu$$

**Correction Détaillée :**
1. Fixons un réel strictement positif $t > 0$.
2. Définissons l'ensemble de niveau $A_t = \{x \in X \mid f(x) \ge t\}$. Par définition de la mesurabilité de $f$, $A_t \in \mathcal{F}$.
3. Nous construisons une fonction étagée très simple qui minore $f$.
   Posons $s = t \cdot \mathbf{1}_{A_t}$. C'est clairement une fonction étagée positive ($s \in \mathcal{E}_+$).
4. Vérifions que $s(x) \le f(x)$ pour tout $x \in X$ :
   - Si $x \notin A_t$, alors $s(x) = 0$. Comme $f$ est positive ($f \in \mathcal{M}_+$), on a bien $s(x) = 0 \le f(x)$.
   - Si $x \in A_t$, alors $s(x) = t$. Par définition même de l'ensemble $A_t$, on a $f(x) \ge t$, donc $s(x) \le f(x)$.
   L'inégalité fonctionnelle $s \le f$ est donc inconditionnellement vraie sur tout $X$.
5. Par la propriété de croissance de l'intégrale (qui découle directement de la définition par supremum) :
   $$\int_X s \, d\mu \le \int_X f \, d\mu$$
6. Mais l'intégrale de la fonction étagée $s$ est connue de façon exacte par définition :
   $$\int_X s \, d\mu = \int_X t \cdot \mathbf{1}_{A_t} \, d\mu = t \cdot \mu(A_t)$$
7. En substituant ceci dans l'inégalité précédente :
   $$t \cdot \mu(A_t) \le \int_X f \, d\mu$$
8. Comme $t > 0$, on peut diviser de part et d'autre par $t$ en conservant le sens de l'inégalité :
   $$\mu(A_t) \le \frac{1}{t} \int_X f \, d\mu$$
   Ce qui démontre précisément le théorème de Markov, pilier incontournable de la théorie des probabilités.
