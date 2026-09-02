# Exercice 8 : Démonstration du lemme de Borel-Cantelli ★★★★

## Énoncé
En utilisant le TCM sur une série d'indicatrices, démontrer le premier lemme de Borel-Cantelli :
Si $(A_n)$ est une suite d'ensembles mesurables tels que $\sum \mu(A_n) < \infty$, alors $\mu(\limsup A_n) = 0$.

## Correction Détaillée
1. **La série de fonctions** : Posons $f = \sum_{n=1}^\infty \mathbf{1}_{A_n}$. $f(x)$ représente le nombre d'ensembles $A_n$ auxquels $x$ appartient.
2. **Corollaire du TCM** : L'intégrale d'une série à termes positifs est la série des intégrales. $\int f d\mu = \sum \int \mathbf{1}_{A_n} d\mu = \sum \mu(A_n)$.
3. **Finitude** : Par hypothèse, $\sum \mu(A_n) < \infty$, donc $\int f d\mu < \infty$.
4. **Propriété des fonctions intégrables** : Si l'intégrale d'une fonction positive est finie, alors la fonction est finie presque partout. Donc $f(x) < \infty$ presque partout.
5. **Conclusion** : Dire que $x \in \limsup A_n$, c'est dire que $x$ appartient à une infinité de $A_n$, c'est-à-dire que $f(x) = \infty$. Comme cela n'arrive que sur un ensemble de mesure nulle, $\mu(\limsup A_n) = 0$.
