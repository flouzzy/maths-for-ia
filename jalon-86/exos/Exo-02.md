# Exercice 2 : Fonction de répartition discrète \quad $\bigstar\bigstar\star\star\star$

## Énoncé

Soit une variable aléatoire $X$ suivant une loi de Bernoulli de paramètre $p \in ]0, 1[$.
Donner l'expression analytique rigoureuse de sa fonction de répartition $F_X(x)$ pour tout réel $x \in \mathbb{R}$ et tracer schématiquement son allure.

## Correction

La loi de Bernoulli de paramètre $p$ indique que la variable aléatoire $X$ prend ses valeurs dans l'ensemble $\{0, 1\}$ avec les probabilités :
$$ \mathbb{P}(X = 1) = p \quad \text{et} \quad \mathbb{P}(X = 0) = 1 - p $$
La fonction de répartition $F_X$ d'une variable aléatoire réelle est définie, pour tout $x \in \mathbb{R}$, par :
$$ F_X(x) = \mathbb{P}(X \leq x) $$
Nous devons examiner les différentes valeurs possibles du réel $x$ par rapport aux points de saut $0$ et $1$.

1. Pour $x < 0$ :
   Aucune valeur prise par $X$ n'est inférieure à un nombre strictement négatif.
   $$ F_X(x) = \mathbb{P}(X \leq x) = \mathbb{P}(\emptyset) = 0 $$

2. Pour $0 \leq x < 1$ :
   La seule valeur possible pour $X$ vérifiant $X \leq x$ est $X = 0$.
   $$ F_X(x) = \mathbb{P}(X = 0) = 1 - p $$

3. Pour $x \geq 1$ :
   Les valeurs $X=0$ et $X=1$ vérifient toutes deux la condition $X \leq x$. Comme les événements $\{X=0\}$ et $\{X=1\}$ sont disjoints, on somme leurs probabilités :
   $$ F_X(x) = \mathbb{P}(X = 0) + \mathbb{P}(X = 1) = (1 - p) + p = 1 $$

L'expression analytique finale est donc :
$$ F_X(x) = \begin{cases} 0 & \text{si } x < 0 \\ 1 - p & \text{si } 0 \leq x < 1 \\ 1 & \text{si } x \geq 1 \end{cases} $$
Cette fonction est bien croissante, continue à droite, et présente des sauts en $x=0$ (d'amplitude $1-p$) et en $x=1$ (d'amplitude $p$). Les limites en $-\infty$ et $+\infty$ sont bien 0 et 1. $\blacksquare$
