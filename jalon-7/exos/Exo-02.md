---
uuid: "exo-7-2"
title: "Exo 2 - Jalon 7"
---
Mes chers étudiants,

Nous allons aujourd'hui consolider nos connaissances sur les fondements des espaces vectoriels abstraits. Cet exercice, de difficulté modérée, vous permettra de manipuler les définitions de famille libre, génératrice et de base dans un contexte polynomial. Il est crucial de bien comprendre ces concepts pour la suite de votre parcours en algèbre linéaire.

### Énoncé de l'exercice

Soit $E$ l'espace vectoriel réel des polynômes de degré au plus 1, noté $P_1(\mathbb{R})$. Les éléments de $E$ sont des polynômes de la forme $ax+b$, où $a$ et $b$ sont des nombres réels. L'addition vectorielle est l'addition usuelle des polynômes, et la multiplication par un scalaire est la multiplication usuelle d'un polynôme par un nombre réel.

Considérons la famille de polynômes $S = \{P_1(x), P_2(x)\}$ où $P_1(x) = 2x+1$ et $P_2(x) = x-3$.

1.  Démontrer que la famille $S$ est une famille libre dans $E$.
2.  Démontrer que la famille $S$ est une famille génératrice de $E$.
3.  En déduire si la famille $S$ constitue une base de $E$.

### Correction Détaillée

Nous allons aborder chaque question avec la rigueur nécessaire, en explicitant chaque étape du raisonnement et du calcul.

#### 1. Démontrer que la famille $S$ est une famille libre dans $E$.

**Définition :** Une famille de vecteurs $\{v_1, v_2, \ldots, v_n\}$ d'un $K$-espace vectoriel $E$ est dite **libre** (ou linéairement indépendante) si la seule combinaison linéaire de ces vecteurs qui est égale au vecteur nul de $E$ est celle où tous les coefficients scalaires sont nuls. Autrement dit, si pour des scalaires $a_1, a_2, \ldots, a_n \in K$, l'équation $a_1 v_1 + a_2 v_2 + \ldots + a_n v_n = 0_E$ implique nécessairement $a_1 = a_2 = \ldots = a_n = 0_K$.

Dans notre cas, l'espace vectoriel est $E = P_1(\mathbb{R})$, le corps des scalaires est $K = \mathbb{R}$, et la famille est $S = \{P_1(x), P_2(x)\}$. Le vecteur nul de $E$, noté $0_E$, est le polynôme nul, c'est-à-dire le polynôme $Q(x) = 0$ pour tout $x \in \mathbb{R}$.

Pour démontrer que $S$ est une famille libre, nous devons considérer une combinaison linéaire des polynômes $P_1(x)$ et $P_2(x)$ égale au polynôme nul, et montrer que les coefficients de cette combinaison linéaire sont nécessairement nuls.

Soient $a_1$ et $a_2$ deux scalaires réels (c'est-à-dire $a_1, a_2 \in \mathbb{R}$).
Considérons l'équation suivante dans $E$:
$$a_1 P_1(x) + a_2 P_2(x) = 0_E$$

Substituons les expressions des polynômes $P_1(x)$ et $P_2(x)$:
$$a_1 (2x+1) + a_2 (x-3) = 0$$

Développons cette expression en regroupant les termes selon les puissances de $x$:
$$(2a_1 x + a_1) + (a_2 x - 3a_2) = 0$$
$$(2a_1 + a_2)x + (a_1 - 3a_2) = 0$$

Pour qu'un polynôme soit le polynôme nul, tous ses coefficients doivent être nuls. Par conséquent, nous obtenons un système d'équations linéaires avec $a_1$ et $a_2$ comme inconnues:
1.  $2a_1 + a_2 = 0$
2.  $a_1 - 3a_2 = 0$

Nous allons résoudre ce système.
De l'équation (1), nous pouvons exprimer $a_2$ en fonction de $a_1$:
$$a_2 = -2a_1$$

Substituons cette expression de $a_2$ dans l'équation (2):
$$a_1 - 3(-2a_1) = 0$$
$$a_1 + 6a_1 = 0$$
$$7a_1 = 0$$

Cette dernière équation implique directement que:
$$a_1 = 0$$

Maintenant, substituons la valeur de $a_1$ dans l'expression de $a_2$:
$$a_2 = -2(0)$$
$$a_2 = 0$$

Nous avons trouvé que $a_1 = 0$ et $a_2 = 0$ est la seule solution au système d'équations.
Puisque la seule combinaison linéaire des polynômes $P_1(x)$ et $P_2(x)$ qui donne le polynôme nul est celle où les coefficients sont tous nuls, nous pouvons conclure que la famille $S = \{P_1(x), P_2(x)\}$ est une famille libre dans $E$.

#### 2. Démontrer que la famille $S$ est une famille génératrice de $E$.

**Définition :** Une famille de vecteurs $\{v_1, v_2, \ldots, v_n\}$ d'un $K$-espace vectoriel $E$ est dite **génératrice** de $E$ si tout vecteur de $E$ peut être exprimé comme une combinaison linéaire de ces vecteurs. Autrement dit, pour tout vecteur $v \in E$, il existe des scalaires $a_1, a_2, \ldots, a_n \in K$ tels que $v = a_1 v_1 + a_2 v_2 + \ldots + a_n v_n$.

Dans notre cas, l'espace vectoriel est $E = P_1(\mathbb{R})$. Un polynôme arbitraire $Q(x)$ dans $E$ peut s'écrire sous la forme $Q(x) = cx+d$, où $c$ et $d$ sont des nombres réels (c'est-à-dire $c, d \in \mathbb{R}$).

Pour démontrer que $S$ est une famille génératrice de $E$, nous devons montrer que pour tout polynôme $Q(x) = cx+d \in E$, il existe des scalaires $a_1, a_2 \in \mathbb{R}$ tels que:
$$Q(x) = a_1 P_1(x) + a_2 P_2(x)$$

Substituons les expressions des polynômes $P_1(x)$ et $P_2(x)$ ainsi que $Q(x)$:
$$cx+d = a_1 (2x+1) + a_2 (x-3)$$

Développons le membre de droite et regroupons les termes selon les puissances de $x$:
$$cx+d = (2a_1 x + a_1) + (a_2 x - 3a_2)$$
$$cx+d = (2a_1 + a_2)x + (a_1 - 3a_2)$$

Pour que deux polynômes soient égaux, leurs coefficients respectifs doivent être égaux. Cela nous conduit à un nouveau système d'équations linéaires, où $a_1$ et $a_2$ sont les inconnues, et $c$ et $d$ sont des paramètres réels:
1.  $2a_1 + a_2 = c$
2.  $a_1 - 3a_2 = d$

Nous allons résoudre ce système pour exprimer $a_1$ et $a_2$ en fonction de $c$ et $d$.
De l'équation (1), nous pouvons exprimer $a_2$ en fonction de $a_1$ et $c$:
$$a_2 = c - 2a_1$$

Substituons cette expression de $a_2$ dans l'équation (2):
$$a_1 - 3(c - 2a_1) = d$$
$$a_1 - 3c + 6a_1 = d$$
$$7a_1 - 3c = d$$
$$7a_1 = d + 3c$$

Cette dernière équation nous donne la valeur de $a_1$:
$$a_1 = \frac{d+3c}{7}$$

Maintenant, substituons la valeur de $a_1$ dans l'expression de $a_2$:
$$a_2 = c - 2\left(\frac{d+3c}{7}\right)$$
$$a_2 = \frac{7c}{7} - \frac{2(d+3c)}{7}$$
$$a_2 = \frac{7c - 2d - 6c}{7}$$
$$a_2 = \frac{c-2d}{7}$$

Nous avons trouvé des expressions explicites pour $a_1$ et $a_2$ en fonction de $c$ et $d$. Pour tout choix de $c, d \in \mathbb{R}$, nous pouvons calculer des valeurs réelles pour $a_1$ et $a_2$. Cela signifie que tout polynôme $Q(x) = cx+d$ dans $E$ peut être écrit comme une combinaison linéaire de $P_1(x)$ et $P_2(x)$.

Par conséquent, la famille $S = \{P_1(x), P_2(x)\}$ est une famille génératrice de $E$.

#### 3. En déduire si la famille $S$ constitue une base de $E$.

**Définition :** Une famille de vecteurs est une **base** d'un $K$-espace vectoriel $E$ si elle est à la fois une famille libre et une famille génératrice de $E$.

D'après la question 1, nous avons démontré que la famille $S = \{P_1(x), P_2(x)\}$ est une famille libre dans $E$.
D'après la question 2, nous avons démontré que la famille $S = \{P_1(x), P_2(x)\}$ est une famille génératrice de $E$.

Puisque la famille $S$ satisfait aux deux conditions (être libre et être génératrice), nous pouvons conclure qu'elle constitue une base de l'espace vectoriel $E = P_1(\mathbb{R})$.

Ceci conclut l'exercice.
