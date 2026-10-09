# Exercice 7 : Minimisation de l'Erreur Quadratique (MSE)

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

Soit $X$ une variable aléatoire de carré intégrable (dans $\mathcal{L}^2$).
On cherche une constante réelle $c$ qui minimise l'erreur quadratique moyenne $f(c) = \mathbb{E}[(X - c)^2]$.
1. Montrer que $f(c)$ est bien définie et l'exprimer comme un polynôme en $c$.
2. En déduire la valeur de $c^*$ qui minimise $f(c)$ et interpréter le résultat.

### Correction détaillée

1. Puisque $X \in \mathcal{L}^2$, alors $X^2$ est intégrable. Comme $X \in \mathcal{L}^2 \implies X \in \mathcal{L}^1$, $X$ admet aussi une espérance $\mathbb{E}[X]$.
   On développe la fonction $f(c)$ :
   $$ (X - c)^2 = X^2 - 2cX + c^2 $$
   Par linéarité de l'espérance :
   $$ f(c) = \mathbb{E}[X^2 - 2cX + c^2] = \mathbb{E}[X^2] - 2c\mathbb{E}[X] + c^2 $$
   $f(c)$ est un trinôme du second degré en $c$, de la forme $f(c) = c^2 - 2\mathbb{E}[X]c + \mathbb{E}[X^2]$.

2. Pour trouver le minimum de ce polynôme du second degré (dont le coefficient dominant est $1 > 0$), on annule sa dérivée par rapport à $c$ :
   $$ f'(c) = 2c - 2\mathbb{E}[X] $$
   $$ f'(c) = 0 \iff 2c = 2\mathbb{E}[X] \iff c = \mathbb{E}[X] $$
   Vérifions qu'il s'agit bien d'un minimum en regardant la dérivée seconde :
   $$ f''(c) = 2 > 0 $$
   Le minimum est donc atteint en $c^* = \mathbb{E}[X]$.

   **Interprétation :** La constante réelle qui "résume" le mieux une variable aléatoire au sens de l'erreur quadratique moyenne (MSE, couramment utilisée en IA) est précisément son espérance mathématique. L'erreur minimale associée vaut alors $\mathbb{E}[(X - \mathbb{E}[X])^2]$, ce qui est la définition exacte de la variance de $X$.
