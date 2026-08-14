# Approximation de fonctions multivariables

### Énoncé $\quad \bigstar\bigstar\bigstar\bigstar\bigstar$

Étendre explicitement le théorème d'approximation à une fonction de deux variables $f(x_1, x_2) = x_1 x_2$ sur le carré unité.

### Démonstration Détaillée

L'identité algébrique remarquable $4 x_1 x_2 = (x_1 + x_2)^2 - (x_1 - x_2)^2$ montre qu'il suffit d'approcher la fonction univariée carrée $u \mapsto u^2$. On sait qu'un réseau à une couche peut approcher $u^2$. On forme donc deux sous-réseaux, un prenant l'entrée $w^T x = x_1 + x_2$ et l'autre $w^T x = x_1 - x_2$. La combinaison linéaire des sorties de ces sous-réseaux permet d'approcher la multiplication $x_1 x_2$, brique de base des polynômes multivariés.
