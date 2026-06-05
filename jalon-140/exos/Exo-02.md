---
uuid: jalon-140-exo-02
title: "Exercice 2 - Classifieur de Bayes"
type: Exercice
difficulty: 1
---

## Énoncé

Soit un problème de classification binaire où l'espace des caractéristiques est un espace mesurable $(\mathcal{X}, \mathcal{B}_{\mathcal{X}})$ et l'espace des étiquettes est $\mathcal{Y} = \{-1, 1\}$ muni de la tribu discrète $\mathcal{P}(\mathcal{Y})$. Nous considérons un vecteur aléatoire $(X, Y)$ défini sur un espace de probabilité $(\Omega, \mathcal{A}, P)$, dont la loi conjointe est $P_{X,Y}$ sur $(\mathcal{X} \times \mathcal{Y}, \mathcal{B}_{\mathcal{X}} \otimes \mathcal{P}(\mathcal{Y}))$.
Un classifieur est une fonction mesurable $h: \mathcal{X} \to \mathcal{Y}$.
La fonction de perte utilisée est la perte 0-1 (ou perte de misclassification), définie par $L: \mathcal{Y} \times \mathcal{Y} \to \{0, 1\}$ telle que $L(y', y) = \mathbb{I}(y' \neq y)$, où $\mathbb{I}$ est la fonction indicatrice.

Le risque d'un classifieur $h$ est défini comme $R(h) = \mathbb{E}[L(h(X), Y)]$.
Nous définissons la probabilité conditionnelle a posteriori de l'étiquette $Y=1$ étant donné $X=x$ comme $\eta(x) := P(Y=1|X=x)$, pour tout $x \in \mathcal{X}$. Cette fonction $\eta: \mathcal{X} \to [0, 1]$ est supposée mesurable.

1.  Définir formellement le classifieur de Bayes $h^*$ pour la perte 0-1.
2.  Démontrer que le classifieur de Bayes $h^*$ peut s'écrire sous la forme suivante, en justifiant chaque étape :
    $$h^*(x) = \begin{cases} 1 & \text{si } \eta(x) > 1/2 \\ -1 & \text{si } \eta(x) < 1/2 \\ 1 & \text{si } \eta(x) = 1/2 \text{ (par convention)} \end{cases}$$
3.  Définir formellement le risque de Bayes $R^*$ pour la perte 0-1.
4.  Démontrer que le risque de Bayes $R^*$ peut s'écrire sous la forme suivante, en justifiant chaque étape :
    $$R^* = \mathbb{E}_X[\min(\eta(X), 1 - \eta(X))]$$

---

## Correction

### Rappels et Définitions Préliminaires

Soit $(\Omega, \mathcal{A}, P)$ un espace de probabilité. Soient $(\mathcal{X}, \mathcal{B}_{\mathcal{X}})$ un espace mesurable et $(\mathcal{Y}, \mathcal{P}(\mathcal{Y}))$ l'espace mesurable des étiquettes, où $\mathcal{Y} = \{-1, 1\}$ et $\mathcal{P}(\mathcal{Y})$ est la tribu discrète.
Un couple aléatoire $(X, Y): \Omega \to \mathcal{X} \times \mathcal{Y}$ a pour loi $P_{X,Y}$ sur $(\mathcal{X} \times \mathcal{Y}, \mathcal{B}_{\mathcal{X}} \otimes \mathcal{P}(\mathcal{Y}))$.
La loi marginale de $X$ est $P_X$ sur $(\mathcal{X}, \mathcal{B}_{\mathcal{X}})$.
Un classifieur est une fonction mesurable $h: \mathcal{X} \to \mathcal{Y}$.
La perte 0-1 est $L: \mathcal{Y} \times \mathcal{Y} \to \{0, 1\}$ définie par $L(y', y) = \mathbb{I}(y' \neq y)$.
Le risque d'un classifieur $h$ est $R(h) = \mathbb{E}[L(h(X), Y)]$.
La fonction $\eta(x) = P(Y=1|X=x)$ est la probabilité a posteriori de $Y=1$ étant donné $X=x$. Par définition des probabilités conditionnelles régulières, $\eta: \mathcal{X} \to [0, 1]$ est une fonction mesurable. Par conséquent, $P(Y=-1|X=x) = 1 - P(Y=1|X=x) = 1 - \eta(x)$.

### Question 1 : Définition formelle du classifieur de Bayes $h^*$

Le classifieur de Bayes $h^*$ est le classifieur qui minimise le risque $R(h)$ parmi tous les classifieurs mesurables $h: \mathcal{X} \to \mathcal{Y}$.
Formellement :
$$h^* = \operatorname{argmin}_{h: \mathcal{X} \to \mathcal{Y} \text{ mesurable}} R(h)$$

### Question 2 : Dérivation de la forme du classifieur de Bayes $h^*$

Le risque d'un classifieur $h$ est donné par :
$$R(h) = \mathbb{E}[L(h(X), Y)]$$
Nous pouvons décomposer cette espérance en utilisant le théorème de l'espérance totale ou en conditionnant par rapport à $X$. Pour tout $X=x \in \mathcal{X}$, le risque conditionnel est :
$$R(h|X=x) = \mathbb{E}[L(h(X), Y)|X=x] = \mathbb{E}[L(h(x), Y)|X=x]$$
Puis, par la loi de l'espérance totale, le risque total est $R(h) = \mathbb{E}_X[R(h|X=X)]$.
Pour minimiser $R(h)$, il est suffisant de minimiser $R(h|X=x)$ pour chaque $x \in \mathcal{X}$ de manière ponctuelle.
L'objectif est donc de trouver, pour chaque $x$, la valeur $h^*(x) \in \mathcal{Y}$ qui minimise $R(h|X=x)$.

Soit $h(x) = y' \in \{-1, 1\}$.
Le risque conditionnel est :
$$R(h|X=x) = \mathbb{E}[L(y', Y)|X=x]$$
En utilisant la définition de la perte 0-1, $L(y', Y) = \mathbb{I}(y' \neq Y)$ :
$$R(h|X=x) = \mathbb{E}[\mathbb{I}(y' \neq Y)|X=x]$$
Par la propriété de l'espérance d'une indicatrice (qui est égale à la probabilité de l'événement), $\mathbb{E}[\mathbb{I}(A)] = P(A)$ :
$$R(h|X=x) = P(y' \neq Y|X=x)$$
Nous devons minimiser $P(y' \neq Y|X=x)$ pour $y' \in \{-1, 1\}$.

Deux cas se présentent pour le choix de $y'$ :

**Cas 1 : Choisir $y' = 1$**
Si $h(x) = 1$, le risque conditionnel est :
$$P(1 \neq Y|X=x) = P(Y = -1|X=x)$$
En utilisant la définition de $\eta(x)$:
$$P(Y = -1|X=x) = 1 - P(Y=1|X=x) = 1 - \eta(x)$$

**Cas 2 : Choisir $y' = -1$**
Si $h(x) = -1$, le risque conditionnel est :
$$P(-1 \neq Y|X=x) = P(Y = 1|X=x)$$
En utilisant la définition de $\eta(x)$:
$$P(Y = 1|X=x) = \eta(x)$$

Pour chaque $x \in \mathcal{X}$, le classifieur de Bayes $h^*(x)$ doit choisir l'étiquette $y'$ qui minimise le risque conditionnel. Autrement dit :
$$h^*(x) = \operatorname{argmin}_{y' \in \{-1, 1\}} P(y' \neq Y|X=x)$$
Nous comparons les deux valeurs possibles de risque conditionnel : $\eta(x)$ et $1-\eta(x)$.

*   Si $1-\eta(x) < \eta(x)$ : Cela signifie que le choix $y'=1$ conduit à un risque conditionnel plus faible.
    L'inégalité $1-\eta(x) < \eta(x)$ est équivalente à $1 < 2\eta(x)$, ce qui implique $\eta(x) > 1/2$.
    Dans ce cas, $h^*(x) = 1$.

*   Si $\eta(x) < 1-\eta(x)$ : Cela signifie que le choix $y'=-1$ conduit à un risque conditionnel plus faible.
    L'inégalité $\eta(x) < 1-\eta(x)$ est équivalente à $2\eta(x) < 1$, ce qui implique $\eta(x) < 1/2$.
    Dans ce cas, $h^*(x) = -1$.

*   Si $\eta(x) = 1-\eta(x)$ : Cela signifie que $2\eta(x) = 1$, d'où $\eta(x) = 1/2$. Dans ce cas, les deux choix $y'=1$ et $y'=-1$ donnent le même risque conditionnel. La convention standard est de choisir l'une des deux valeurs, par exemple $1$.
    Dans ce cas, $h^*(x) = 1$ (par convention).

En combinant ces cas, nous obtenons la forme du classifieur de Bayes :
$$h^*(x) = \begin{cases} 1 & \text{si } \eta(x) > 1/2 \\ -1 & \text{si } \eta(x) < 1/2 \\ 1 & \text{si } \eta(x) = 1/2 \text{ (par convention)} \end{cases}$$
Cette expression peut également s'écrire de manière plus compacte en utilisant une fonction signe adaptée, $\operatorname{sgn}_*(z)$, telle que $\operatorname{sgn}_*(z) = 1$ si $z \ge 0$ et $\operatorname{sgn}_*(z) = -1$ si $z < 0$:
$$h^*(x) = \operatorname{sgn}_*(\eta(x) - 1/2)$$

### Question 3 : Définition formelle du risque de Bayes $R^*$

Le risque de Bayes $R^*$ est la valeur minimale du risque atteignable par n'importe quel classifieur mesurable. C'est le risque du classifieur de Bayes $h^*$.
Formellement :
$$R^* = R(h^*) = \min_{h: \mathcal{X} \to \mathcal{Y} \text{ mesurable}} R(h)$$

### Question 4 : Dérivation de la forme du risque de Bayes $R^*$

Le risque de Bayes $R^*$ est le risque associé au classifieur $h^*$:
$$R^* = R(h^*) = \mathbb{E}[L(h^*(X), Y)]$$
En utilisant la décomposition de l'espérance par conditionnement sur $X$:
$$R^* = \mathbb{E}_X[\mathbb{E}[L(h^*(X), Y)|X=X]]$$
Pour chaque $x \in \mathcal{X}$, la valeur de $\mathbb{E}[L(h^*(x), Y)|X=x]$ est le minimum du risque conditionnel atteint par $h^*(x)$.
Nous avons montré à la Question 2 que $P(y' \neq Y|X=x)$ est le risque conditionnel pour un choix $y'$.
Le classifieur $h^*(x)$ choisit $y'$ pour minimiser cette quantité. Donc :
$$\mathbb{E}[L(h^*(x), Y)|X=x] = \min_{y' \in \{-1, 1\}} P(y' \neq Y|X=x)$$
En substituant les expressions des risques conditionnels pour les deux cas de $y'$ (démontrées à la Question 2) :
$$\mathbb{E}[L(h^*(x), Y)|X=x] = \min(P(Y=-1|X=x), P(Y=1|X=x))$$
En utilisant la définition de $\eta(x)$:
$$\mathbb{E}[L(h^*(x), Y)|X=x] = \min(1-\eta(x), \eta(x))$$
Finalement, en substituant cette expression dans la formule du risque de Bayes :
$$R^* = \mathbb{E}_X[\min(\eta(X), 1 - \eta(X))]$$
Cette formule exprime le risque de Bayes comme l'espérance par rapport à la distribution de $X$ de la probabilité de misclassification minimale conditionnellement à $X$.