# Exercice 1 : Application directe du premier lemme

$\bigstar\star\star\star\star$

**Énoncé :**
Soit $(X_n)_{n \in \mathbb{N}^*}$ une suite de variables aléatoires réelles. On suppose que pour tout $n \ge 1$, $\mathbb{P}(X_n > n) = \frac{1}{n^2}$.
Montrer que presque sûrement, à partir d'un certain rang, on a $X_n \le n$.

**Correction :**
Considérons la suite d'événements $A_n = \{X_n > n\}$.
La probabilité de chaque événement est $\mathbb{P}(A_n) = \frac{1}{n^2}$.
La série des probabilités s'écrit $\sum_{n=1}^\infty \mathbb{P}(A_n) = \sum_{n=1}^\infty \frac{1}{n^2}$.
Cette série est une série de Riemann convergente (car l'exposant $2 > 1$).
Puisque $\sum \mathbb{P}(A_n) < +\infty$, le premier lemme de Borel-Cantelli affirme que :
$$ \mathbb{P}(\limsup_{n \to \infty} A_n) = 0 $$
Ainsi, presque sûrement, seul un nombre fini d'événements $A_n$ se réalisent.
Par définition, dire que $A_n$ ne se réalise qu'un nombre fini de fois signifie qu'il existe un rang $N(\omega)$ (dépendant du résultat $\omega$) tel que pour tout $n \ge N(\omega)$, l'événement $A_n$ ne se réalise pas, c'est-à-dire que son complémentaire $A_n^c$ se réalise.
Or $A_n^c = \{X_n \le n\}$.
Donc, presque sûrement, il existe un rang à partir duquel $X_n \le n$.
