---
title: "Exercice 10"
---
## Exercice 10 : Démonstration du Lemme de Borel-Cantelli via TCM $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $(A_n)$ une suite d'ensembles mesurables telle que $\sum_{n=1}^\infty \mu(A_n) < +\infty$.
En utilisant le TCM, montrer que $\mu(\limsup A_n) = 0$, c'est-à-dire que presque tout $x$ n'appartient qu'à un nombre fini de $A_n$.

**Correction Détaillée :**
1. Soit $f(x) = \sum_{n=1}^\infty \mathbf{1}_{A_n}(x)$. Cette fonction compte le nombre d'ensembles $A_n$ auxquels $x$ appartient.
2. $f$ est la somme d'une série de fonctions mesurables positives.
3. Par le corollaire de Beppo Levi :
   $$\int_X f(x) d\mu = \sum_{n=1}^\infty \int_X \mathbf{1}_{A_n} d\mu = \sum_{n=1}^\infty \mu(A_n)$$
4. Par hypothèse, cette somme est finie. Donc $\int_X f d\mu < +\infty$.
5. Or, on sait que si l'intégrale d'une fonction positive est finie, alors la fonction est finie presque partout.
   (Rappel: si on note $E = \{x \mid f(x) = +\infty\}$, $E = \cap_k \{f > k\}$. $\mu(E) \le \frac{1}{k} \int f \to 0$).
6. Donc, $f(x) < +\infty$ pour presque tout $x \in X$.
7. Avoir $f(x) < +\infty$ signifie exactement que $x$ appartient à un nombre fini de $A_n$.
8. L'ensemble $\limsup A_n$ (les $x$ appartenant à une infinité de $A_n$) est précisément l'ensemble où $f(x) = +\infty$.
9. Donc $\mu(\limsup A_n) = 0$.
