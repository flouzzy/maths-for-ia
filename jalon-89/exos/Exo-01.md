# Exercice 1

**Difficulté :** $\bigstar\star\star\star\star$

## Application directe du premier lemme

Soit $(X_n)_{n \in \mathbb{N}^*}$ une suite de variables aléatoires réelles. On suppose que pour tout $n$, $\mathbb{P}(X_n > n) = \frac{1}{n^2}$.
Montrer que presque sûrement, l'événement $\{X_n > n\}$ ne se réalise qu'un nombre fini de fois.

**Correction détaillée :**
1. Soit $A_n = \{X_n > n\}$. La probabilité de $A_n$ est donnée par $\mathbb{P}(A_n) = \frac{1}{n^2}$.
2. On considère la série de terme général $\mathbb{P}(A_n)$. Il s'agit de la série de Riemann $\sum_{n=1}^{\infty} \frac{1}{n^2}$.
3. Comme $2 > 1$, on sait d'après le critère de Riemann que la série $\sum_{n=1}^{\infty} \mathbb{P}(A_n)$ est convergente.
4. Ainsi, par le premier lemme de Borel-Cantelli, on a : $\mathbb{P}(\limsup_{n \to \infty} A_n) = 0$.
5. Par définition, l'événement complémentaire $(\limsup A_n)^c$ est de probabilité 1. Cela signifie que presque sûrement, il n'existe qu'un nombre fini d'indices $n$ tels que l'événement $A_n$ soit réalisé.
