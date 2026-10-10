# Exercice 08 : Minimum de variables uniformes indépendantes
Difficulté : $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soient $U_1, U_2, \dots, U_n$ des variables aléatoires indépendantes suivant toutes la loi uniforme $\mathcal{U}([0, 1])$.
Soit $M_n = \min(U_1, U_2, \dots, U_n)$.
1. Déterminer la fonction de répartition de $M_n$, notée $F_{M_n}(x)$.
2. En déduire la densité de $M_n$ et son espérance $\mathbb{E}[M_n]$.

**Correction :**
1. Par définition, $F_{M_n}(x) = \mathbb{P}(M_n \leq x)$.
Il est plus simple de passer par le complémentaire : $\mathbb{P}(M_n \leq x) = 1 - \mathbb{P}(M_n > x)$.
Dire que le minimum est strictement plus grand que $x$ équivaut à dire que *toutes* les variables sont strictement plus grandes que $x$ :
$\mathbb{P}(M_n > x) = \mathbb{P}(U_1 > x, U_2 > x, \dots, U_n > x)$.
Par indépendance mutuelle, la probabilité de l'intersection est le produit des probabilités :
$\mathbb{P}(M_n > x) = \prod_{i=1}^n \mathbb{P}(U_i > x)$.
Pour une loi $\mathcal{U}([0, 1])$, si $x \in [0, 1]$, $\mathbb{P}(U_i > x) = 1 - x$.
Ainsi, $\mathbb{P}(M_n > x) = (1-x)^n$.
Donc $F_{M_n}(x) = 1 - (1-x)^n$ pour $x \in [0, 1]$. (Elle vaut $0$ pour $x < 0$ et $1$ pour $x > 1$).
2. La densité $f_{M_n}(x)$ est la dérivée de $F_{M_n}(x)$ pour $x \in [0, 1]$ :
$f_{M_n}(x) = \frac{d}{dx} (1 - (1-x)^n) = -n(1-x)^{n-1}(-1) = n(1-x)^{n-1}$.
Calcul de l'espérance :
$\mathbb{E}[M_n] = \int_0^1 x \cdot n(1-x)^{n-1} dx$.
On procède par intégration par parties ou changement de variable $u = 1-x$ ($dx = -du$, $x = 1-u$) :
$\mathbb{E}[M_n] = \int_1^0 (1-u) \cdot n u^{n-1} (-du) = n \int_0^1 (u^{n-1} - u^n) du$.
$\mathbb{E}[M_n] = n \left[ \frac{u^n}{n} - \frac{u^{n+1}}{n+1} \right]_0^1 = n \left( \frac{1}{n} - \frac{1}{n+1} \right) = n \left( \frac{n+1-n}{n(n+1)} \right) = \frac{1}{n+1}$.
