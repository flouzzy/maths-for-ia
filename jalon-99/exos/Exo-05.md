# Exercice 5 : $\bigstar\bigstar\bigstar\star\star$

## Énoncé

Soit $E$ un espace vectoriel normé, et $A, B$ deux ensembles convexes disjoints. On suppose $A$ et $B$ ouverts. Montrer qu'il existe un hyperplan séparant strictement $A$ et $B$ ? Est-ce vrai en général pour deux ouverts convexes disjoints quelconques ?

## Correction

Pour des ensembles ouverts, la première forme géométrique de Hahn-Banach garantit seulement une séparation au sens *large* :
Il existe $f \in E', f \neq 0$ et $\alpha$ tels que $f(A) \le \alpha \le f(B)$.
Cependant, comme $A$ et $B$ sont ouverts, et $f$ est une application linéaire continue non nulle, le théorème de l'application ouverte (pour la dimension 1 de l'image) indique que $f(A)$ et $f(B)$ sont des ensembles ouverts de $\mathbb{R}$.
Ainsi, l'image $f(A)$ est un intervalle ouvert, disons $(a, \alpha')$, et $f(B)$ est un intervalle ouvert $(\beta', b)$.
Puisque $f(A) \le f(B)$, on a nécessairement $\sup f(A) \le \inf f(B)$.
De plus, la borne supérieure n'est pas atteinte dans un ouvert. Donc pour tout $a \in A, f(a) < \sup f(A) \le \alpha$.
De même, pour tout $b \in B, f(b) > \inf f(B) \ge \alpha$.
Ainsi, $\forall a \in A, \forall b \in B, f(a) < \alpha < f(b)$.
C'est bien une séparation stricte ponctuelle (il n'y a pas forcément d'epsilon uniforme si les ensembles s'approchent asymptotiquement du plan), mais l'hyperplan $f(x) = \alpha$ ne coupe ni $A$ ni $B$. $\blacksquare$
