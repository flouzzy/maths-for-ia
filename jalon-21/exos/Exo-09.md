# Exercice 9 : Sommes partielles et convergence uniforme
**Énoncé :**
Soit $S_n(x) = \sum_{k=1}^n \frac{\cos(kx)}{k^2}$. Montrer la convergence uniforme de cette suite de fonctions.

**Solution Rigoureuse :**
1. **Critère de Cauchy uniforme (Critère de Weierstrass) :**
Il s'agit d'une suite de sommes partielles définissant une série de fonctions. On l'étudie via la convergence normale.
Posons $u_k(x) = \frac{\cos(kx)}{k^2}$.
Pour tout $x \in \mathbb{R}$, on a la majoration évidente en valeur absolue :
$$|u_k(x)| = \frac{|\cos(kx)|}{k^2} \le \frac{1}{k^2}$$
Ainsi, la norme infinie de $u_k$ sur $\mathbb{R}$ satisfait :
$$\|u_k\|_{\infty, \mathbb{R}} \le \frac{1}{k^2}$$
2. **Convergence normale vers convergence uniforme :**
La série numérique $\sum \frac{1}{k^2}$ est une série de Riemann convergente (d'exposant $2 > 1$).
Puisque la série des normes infinis $\sum \|u_k\|_{\infty, \mathbb{R}}$ converge, la série de fonctions $\sum u_k(x)$ converge normalement sur $\mathbb{R}$.
Par un théorème fondamental de l'analyse, la convergence normale implique la convergence uniforme.
Donc la suite des sommes partielles $(S_n)$ converge uniformément sur $\mathbb{R}$ vers une fonction continue $S$.
Le transfert de continuité s'applique car chaque composante est continue et la somme est uniforme.
