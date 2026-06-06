---
uuid: "jalon-140-exo-03"
title: "Exercice 3 - Jalon 140"
---
# Exercice 3 : Démonstration de l'Optimalité du Classifieur de Bayes
**Difficulté:** ★★

## Énoncé
Soit un problème de classification binaire où nous cherchons à prédire une variable aléatoire $Y \in \{-1, 1\}$ à partir d'une variable aléatoire $X$.
Nous utilisons la fonction de perte 0-1, définie par $L(y, \hat{y}) = \mathbb{I}(y \neq \hat{y})$, où $\mathbb{I}(\cdot)$ est la fonction indicatrice qui vaut $1$ si la condition est vraie et $0$ sinon.
Le risque d'un classifieur $h: \mathcal{X} \to \{-1, 1\}$ est défini comme l'espérance de la perte : $R(h) = \mathbb{E}[L(Y, h(X))]$.
Le classifieur de Bayes $h^*(x)$ est défini pour chaque $x \in \mathcal{X}$ comme $h^*(x) = \text{argmax}_{y \in \{-1, 1\}} P(Y=y | X=x)$.
Démontrez que le classifieur de Bayes $h^*$ minimise le risque $R(h)$ parmi tous les classifieurs possibles.

## Correction Pas-à-Pas
1.  **Définition du risque d'un classifieur $h$**:
    Le risque $R(h)$ est l'espérance de la perte 0-1 :
    $R(h) = \mathbb{E}[L(Y, h(X))]$

2.  **Application de la loi de l'espérance totale**:
    Nous pouvons décomposer l'espérance totale en conditionnant par $X$:
    $R(h) = \mathbb{E}[\mathbb{E}[L(Y, h(X)) | X]]$
    En utilisant la formule de l'espérance pour une variable continue $X$ (ou une somme pour une variable discrète), cela s'écrit :
    $R(h) = \int_{\mathcal{X}} \mathbb{E}[L(Y, h(x)) | X=x] p(x) dx$
    où $p(x)$ est la fonction de densité de probabilité de $X$.

3.  **Minimisation point par point**:
    Pour minimiser $R(h)$, il est suffisant de minimiser l'intégrande pour chaque valeur $x \in \mathcal{X}$, car $p(x) \ge 0$.
    Ainsi, nous devons trouver la fonction $h(x)$ qui minimise $\mathbb{E}[L(Y, h(x)) | X=x]$ pour chaque $x$ fixé.

4.  **Calcul de l'espérance conditionnelle de la perte pour un $x$ fixé**:
    Pour un $x$ fixé, $h(x)$ prend une valeur spécifique, soit $1$ soit $-1$.
    L'espérance conditionnelle de la perte est donnée par :
    $\mathbb{E}[L(Y, h(x)) | X=x] = \sum_{y \in \{-1, 1\}} L(y, h(x)) P(Y=y | X=x)$

    **Cas 1 : $h(x) = 1$**
    $\mathbb{E}[L(Y, 1) | X=x] = L(-1, 1) P(Y=-1 | X=x) + L(1, 1) P(Y=1 | X=x)$
    En utilisant la définition de la perte 0-1 ($L(y, \hat{y}) = \mathbb{I}(y \neq \hat{y})$) :
    $L(-1, 1) = \mathbb{I}(-1 \neq 1) = 1$
    $L(1, 1) = \mathbb{I}(1 \neq 1) = 0$
    Donc :
    $\mathbb{E}[L(Y, 1) | X=x] = 1 \cdot P(Y=-1 | X=x) + 0 \cdot P(Y=1 | X=x)$
    $\mathbb{E}[L(Y, 1) | X=x] = P(Y=-1 | X=x)$

    **Cas 2 : $h(x) = -1$}**
    $\mathbb{E}[L(Y, -1) | X=x] = L(-1, -1) P(Y=-1 | X=x) + L(1, -1) P(Y=1 | X=x)$
    En utilisant la définition de la perte 0-1 :
    $L(-1, -1) = \mathbb{I}(-1 \neq -1) = 0$
    $L(1, -1) = \mathbb{I}(1 \neq -1) = 1$
    Donc :
    $\mathbb{E}[L(Y, -1) | X=x] = 0 \cdot P(Y=-1 | X=x) + 1 \cdot P(Y=1 | X=x)$
    $\mathbb{E}[L(Y, -1) | X=x] = P(Y=1 | X=x)$

    En résumé, l'espérance de la perte conditionnelle est $P(Y \neq h(x) | X=x)$.

5.  **Choix de $h(x)$ pour minimiser la perte conditionnelle**:
    Pour minimiser $\mathbb{E}[L(Y, h(x)) | X=x]$, nous devons choisir $h(x)$ de manière à minimiser la probabilité d'erreur conditionnelle $P(Y \neq h(x) | X=x)$.
    Nous comparons les deux options :
    *   Si nous choisissons $h(x) = 1$, la perte conditionnelle est $P(Y=-1 | X=x)$.
    *   Si nous choisissons $h(x) = -1$, la perte conditionnelle est $P(Y=1 | X=x)$.

    Pour minimiser, nous devons choisir la classe qui a la plus faible probabilité d'être incorrecte. Cela signifie choisir la classe qui a la plus forte probabilité d'être correcte.
    Donc, nous choisissons :
    $h(x) = 1$ si $P(Y=1 | X=x) > P(Y=-1 | X=x)$
    $h(x) = -1$ si $P(Y=-1 | X=x) > P(Y=1 | X=x)$
    Si $P(Y=1 | X=x) = P(Y=-1 | X=x)$, le choix est arbitraire (par exemple, on peut choisir $1$ par convention).

6.  **Lien avec le classifieur de Bayes**:
    Le classifieur de Bayes $h^*(x)$ est défini comme :
    $h^*(x) = \text{argmax}_{y \in \{-1, 1\}} P(Y=y | X=x)$
    Cette définition signifie que $h^*(x)$ est la classe $y$ qui maximise la probabilité conditionnelle $P(Y=y | X=x)$.
    *   Si $P(Y=1 | X=x) > P(Y=-1 | X=x)$, alors $h^*(x) = 1$.
    *   Si $P(Y=-1 | X=x) > P(Y=1 | X=x)$, alors $h^*(x) = -1$.
    *   En cas d'égalité, la définition de l'argmax peut être complétée par une règle de désambiguïsation (par exemple, choisir $1$), ce qui correspond exactement à la règle de minimisation de la perte conditionnelle établie au point 5.

    Par conséquent, la fonction $h(x)$ qui minimise l'espérance de la perte conditionnelle $\mathbb{E}[L(Y, h(x)) | X=x]$ pour chaque $x$ est précisément le classifieur de Bayes $h^*(x)$.

7.  **Conclusion sur l'optimalité**:
    Puisque le classifieur de Bayes $h^*(x)$ minimise l'espérance de la perte conditionnelle $\mathbb{E}[L(Y, h(x)) | X=x]$ pour chaque $x \in \mathcal{X}$, et que le risque total $R(h)$ est l'espérance de cette perte conditionnelle sur $X$, il s'ensuit que le classifieur de Bayes $h^*$ minimise le risque $R(h)$.
    $R(h^*) = \int_{\mathcal{X}} \min_{h(x)} \mathbb{E}[L(Y, h(x)) | X=x] p(x) dx$
    Pour tout autre classifieur $h$, nous avons :
    $R(h^*) \le \int_{\mathcal{X}} \mathbb{E}[L(Y, h(x)) | X=x] p(x) dx = R(h)$
    Le classifieur de Bayes est donc le classifieur optimal en termes de minimisation du risque de classification (perte 0-1).
