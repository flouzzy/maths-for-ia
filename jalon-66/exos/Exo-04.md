# Exercice 4 : L'inégalité de Markov
$\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré et $f \in \mathcal{M}^+(X)$.
Démontrer l'inégalité de Markov : pour tout $t > 0$,
$$\mu(\{x \in X \mid f(x) \ge t\}) \le \frac{1}{t} \int_X f \, d\mu$$

**Correction :**
1. Fixons un $t > 0$. Notons $A_t = \{x \in X \mid f(x) \ge t\}$. C'est un ensemble mesurable car $f$ est mesurable.
2. Construisons une fonction minorant judicieusement $f$.
   Par définition de l'ensemble $A_t$, pour tout $x \in A_t$, $f(x) \ge t$.
   Pour tout $x \notin A_t$, $f(x) \ge 0$.
   On peut donc écrire l'inégalité point par point sur tout l'espace $X$ :
   $$f(x) \ge t \mathbf{1}_{A_t}(x)$$
3. En effet :
   - Si $x \in A_t$, $\mathbf{1}_{A_t}(x) = 1$, et on a $f(x) \ge t = t \cdot 1$. L'inégalité est vérifiée.
   - Si $x \notin A_t$, $\mathbf{1}_{A_t}(x) = 0$, et on a $f(x) \ge 0 = t \cdot 0$. L'inégalité est vérifiée.
4. Intégrons cette inégalité. La fonction $t \mathbf{1}_{A_t}$ est une fonction étagée positive.
   Par la propriété de croissance de l'intégrale :
   $$\int_X f \, d\mu \ge \int_X t \mathbf{1}_{A_t} \, d\mu$$
5. Calculons l'intégrale de la fonction étagée :
   $$\int_X t \mathbf{1}_{A_t} \, d\mu = t \mu(A_t)$$
6. On obtient donc :
   $$\int_X f \, d\mu \ge t \mu(A_t)$$
7. Puisque $t > 0$, on divise de part et d'autre par $t$ pour conclure :
   $$\mu(A_t) \le \frac{1}{t} \int_X f \, d\mu$$
   Ce résultat est un outil fondamental en théorie des probabilités pour borner la probabilité d'écarts à la moyenne.
