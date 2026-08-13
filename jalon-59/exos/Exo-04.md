# Exercice 4 : Norme de la convergence uniforme

## Énoncé
On se place dans l'espace $\mathcal{C}([0, 1], \mathbb{R})$ muni de la norme $\|f\|_\infty = \sup_{x \in [0, 1]} |f(x)|$.
Soit $A = \left\lbrace f \in \mathcal{C}([0, 1], \mathbb{R}) \mid f(0) = 0 \text{ et } f(1) = 1 \right\rbrace$.
Montrer que $A$ est un fermé de $(\mathcal{C}([0, 1], \mathbb{R}), \|\cdot\|_\infty)$.

## Correction Détaillée

Pour montrer que $A$ est fermé, on va utiliser la caractérisation séquentielle.
Soit $(f_n)_{n\in\mathbb{N}}$ une suite de fonctions de $A$ convergeant vers $f$ dans $\mathcal{C}([0, 1], \mathbb{R})$ pour la norme infinie.
Cela signifie que $f_n$ converge uniformément vers $f$ sur $[0, 1]$.
La convergence uniforme implique la convergence simple. Donc, pour tout $x \in [0, 1]$, $f_n(x) \to f(x)$.

En particulier, pour $x = 0$, $f_n(0) \to f(0)$.
Comme pour tout $n$, $f_n(0) = 0$ (car $f_n \in A$), on a nécessairement $f(0) = 0$.

De même, pour $x = 1$, $f_n(1) \to f(1)$.
Comme $f_n(1) = 1$ pour tout $n$, on a nécessairement $f(1) = 1$.

Donc $f \in A$. $A$ contient la limite de toutes ses suites convergentes, c'est donc un fermé.
