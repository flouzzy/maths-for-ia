# Exercice 05 : Critère de finitude intégrale (Borel-Cantelli analytique) ($\bigstar$$\bigstar$$\bigstar$$\star$$\star$)

## Énoncé

Soit $(f_n)$ une suite de fonctions mesurables positives. Si $\sum_{n=1}^\infty \int f_n \,d\mu < +\infty$, prouver que la série $\sum_{n=1}^\infty f_n(x)$ converge presque partout.

## Correction Détaillée

1. **Beppo Levi :** Soit $g(x) = \sum_{n=1}^\infty f_n(x)$. La suite des sommes partielles $S_N(x) = \sum_{n=1}^N f_n(x)$ est croissante et positive. Par le corollaire du TCM :
   $$ \int_X g \,d\mu = \int_X \sum_{n=1}^\infty f_n \,d\mu = \sum_{n=1}^\infty \int_X f_n \,d\mu $$
2. **Finitude :** L'énoncé stipule que cette série numérique est convergente, et vaut une constante $C < +\infty$.
3. **Propriété de l'intégrale :** Si l'intégrale d'une fonction positive $g$ est finie ($\int_X g \,d\mu = C < +\infty$), alors la fonction $g$ doit être finie presque partout. En effet, soit $A = \{x \in X \mid g(x) = +\infty\}$. Pour tout $M > 0$, on a $g(x) \ge M \cdot \mathbf{1}_A(x)$. Donc $\int g \ge M \mu(A)$. Comme $C \ge M \mu(A)$ pour tout $M$, cela force $\mu(A) = 0$.
4. **Conclusion :** Par conséquent, $g(x)$ est finie presque partout, ce qui signifie que la série $\sum_{n=1}^\infty f_n(x)$ converge (vers un réel fini) presque partout. C'est l'équivalent analytique du lemme de Borel-Cantelli.
