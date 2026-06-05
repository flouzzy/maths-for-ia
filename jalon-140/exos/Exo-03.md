---
uuid: jalon-140-exo-03
title: "Exercice 3 - Classifieur de Bayes"
type: Exercice
difficulty: 2
---

**Énoncé de l'exercice**

Soit $(\Omega, \mathcal{A}, P)$ un espace de probabilité. Nous considérons un problème de classification binaire où les observations $(X, Y)$ sont des réalisations d'une variable aléatoire à valeurs dans $\mathcal{X} \times \mathcal{Y}$, avec $(\mathcal{X}, \mathcal{B}_{\mathcal{X}})$ un espace mesurable (où $\mathcal{B}_{\mathcal{X}}$ est la tribu sur $\mathcal{X}$) et $\mathcal{Y} = \{-1, 1\}$. Nous munissons $\mathcal{Y}$ de la tribu discrète $\mathcal{P}(\mathcal{Y})$. La distribution conjointe de $(X, Y)$ est notée $P_{XY}$.

Nous désignons par $P_X$ la mesure de probabilité marginale de $X$ sur $(\mathcal{X}, \mathcal{B}_{\mathcal{X}})$ et par $P_{Y|X=x}$ la loi de probabilité conditionnelle de $Y$ étant donné $X=x$. Pour chaque $x \in \mathcal{X}$, nous définissons les probabilités conditionnelles :
$$P(Y=1|X=x) = \eta_1(x)$$
$$P(Y=-1|X=x) = \eta_{-1}(x) = 1 - \eta_1(x)$$

Un classifieur est une fonction mesurable $h: (\mathcal{X}, \mathcal{B}_{\mathcal{X}}) \to (\mathcal{Y}, \mathcal{P}(\mathcal{Y}))$. L'objectif est de trouver un classifieur qui minimise le risque de misclassification, défini par la fonction de perte 0-1, $\ell(y, \hat{y}) = \mathbf{1}_{y \neq \hat{y}}$, où $\mathbf{1}$ est la fonction indicatrice.

Le risque d'un classifieur $h$ est donné par :
$$R(h) = E[\ell(Y, h(X))] = E[\mathbf{1}_{Y \neq h(X)}]$$

1.  Définir formellement le risque conditionnel $R(h|X=x)$ pour un point $x \in \mathcal{X}$ donné.
2.  Démontrer que le classifieur de Bayes $h^*$ minimisant le risque $R(h)$ est donné par :
    $$h^*(x) = \begin{cases} 1 & \text{si } \eta_1(x) > \eta_{-1}(x) \\ -1 & \text{si } \eta_1(x) < \eta_{-1}(x) \\ \text{arbitraire dans } \{-1, 1\} & \text{si } \eta_1(x) = \eta_{-1}(x) \end{cases}$$
    pour $P_X$-presque tout $x \in \mathcal{X}$.
3.  Calculer le risque de Bayes $R(h^*)$ en fonction de $\eta_1(x)$.

---

**Correction de l'exercice**

1.  **Définition du risque conditionnel $R(h|X=x)$**

    Le risque d'un classifieur $h$ est défini par $R(h) = E[\mathbf{1}_{Y \neq h(X)}]$. Par la loi de l'espérance totale (ou le théorème de Fubini pour l'espérance), nous pouvons exprimer ce risque comme l'espérance du risque conditionnel par rapport à $X$ :
    $$R(h) = E[E[\mathbf{1}_{Y \neq h(X)} | X]]$$
    Pour un $x \in \mathcal{X}$ donné, le risque conditionnel $R(h|X=x)$ est l'espérance de la perte de misclassification sachant que la variable d'entrée $X$ a pris la valeur $x$. Formellement, il s'agit de :
    $$R(h|X=x) = E[\mathbf{1}_{Y \neq h(x)} | X=x]$$
    Puisque $h(x)$ est une valeur fixe dans $\mathcal{Y}$ pour un $x$ donné, cette espérance conditionnelle peut être exprimée en termes des probabilités conditionnelles de $Y$ :
    $$R(h|X=x) = P(Y \neq h(x) | X=x)$$
    Nous considérons les deux cas possibles pour la valeur de $h(x)$:
    *   Si $h(x) = 1$: La misclassification se produit si $Y = -1$.
        $$R(h|X=x) = P(Y = -1 | X=x) = \eta_{-1}(x)$$
    *   Si $h(x) = -1$: La misclassification se produit si $Y = 1$.
        $$R(h|X=x) = P(Y = 1 | X=x) = \eta_1(x)$$
    En combinant ces deux cas, le risque conditionnel peut s'écrire de manière compacte comme :
    $$R(h|X=x) = \mathbf{1}_{h(x)=1} \cdot \eta_{-1}(x) + \mathbf{1}_{h(x)=-1} \cdot \eta_1(x)$$

2.  **Démonstration du classifieur de Bayes $h^*$**

    Pour minimiser le risque total $R(h) = E[R(h|X)] = \int_{\mathcal{X}} R(h|X=x) \, dP_X(x)$, il est suffisant de minimiser la fonction $R(h|X=x)$ pour $P_X$-presque tout $x \in \mathcal{X}$, puisque l'intégrande est non-négatif.
    Pour chaque $x \in \mathcal{X}$, nous devons choisir $h(x) \in \{-1, 1\}$ de manière à minimiser $R(h|X=x)$. Nous comparons les deux valeurs possibles du risque conditionnel :
    *   Si nous choisissons $h(x) = 1$, le risque conditionnel est $\eta_{-1}(x)$.
    *   Si nous choisissons $h(x) = -1$, le risque conditionnel est $\eta_1(x)$.

    Le classifieur de Bayes $h^*(x)$ doit choisir la classe qui minimise ce risque conditionnel.
    *   **Cas 1 : $\eta_{-1}(x) < \eta_1(x)$**
        Dans ce cas, choisir $h(x) = 1$ conduit à un risque conditionnel $\eta_{-1}(x)$ qui est strictement inférieur à $\eta_1(x)$. Donc, $h^*(x) = 1$.
        Cette condition $\eta_{-1}(x) < \eta_1(x)$ est équivalente à $1 - \eta_1(x) < \eta_1(x)$, ce qui implique $1 < 2\eta_1(x)$, ou $\eta_1(x) > 1/2$.
    *   **Cas 2 : $\eta_1(x) < \eta_{-1}(x)$**
        Dans ce cas, choisir $h(x) = -1$ conduit à un risque conditionnel $\eta_1(x)$ qui est strictement inférieur à $\eta_{-1}(x)$. Donc, $h^*(x) = -1$.
        Cette condition $\eta_1(x) < \eta_{-1}(x)$ est équivalente à $\eta_1(x) < 1 - \eta_1(x)$, ce qui implique $2\eta_1(x) < 1$, ou $\eta_1(x) < 1/2$.
    *   **Cas 3 : $\eta_1(x) = \eta_{-1}(x)$**
        Dans ce cas, les deux choix $h(x)=1$ et $h(x)=-1$ donnent le même risque conditionnel de $\eta_1(x) = \eta_{-1}(x) = 1/2$. La décision est donc arbitraire, car elle n'affecte pas la valeur minimale du risque conditionnel. Nous pouvons choisir n'importe quelle valeur dans $\{-1, 1\}$.

    En résumé, le classifieur de Bayes $h^*(x)$ est défini pour $P_X$-presque tout $x \in \mathcal{X}$ par :
    $$h^*(x) = \begin{cases} 1 & \text{si } \eta_1(x) > \eta_{-1}(x) \\ -1 & \text{si } \eta_1(x) < \eta_{-1}(x) \\ \text{arbitraire dans } \{-1, 1\} & \text{si } \eta_1(x) = \eta_{-1}(x) \end{cases}$$
    On peut également écrire cette fonction en utilisant la relation $\eta_{-1}(x) = 1 - \eta_1(x)$:
    $$h^*(x) = \begin{cases} 1 & \text{si } \eta_1(x) > 1/2 \\ -1 & \text{si } \eta_1(x) < 1/2 \\ \text{arbitraire dans } \{-1, 1\} & \text{si } \eta_1(x) = 1/2 \end{cases}$$

3.  **Calcul du risque de Bayes $R(h^*)$**

    Le risque de Bayes $R(h^*)$ est la valeur minimale du risque total que l'on peut atteindre. Il est obtenu en intégrant les risques conditionnels minimaux sur l'espace $\mathcal{X}$, par rapport à la distribution marginale $P_X$.
    $$R(h^*) = E[R(h^*|X)]$$
    Pour chaque $x \in \mathcal{X}$, le risque conditionnel minimal est $\min(\eta_1(x), \eta_{-1}(x))$.
    $$R(h^*|X=x) = \min(\eta_1(x), \eta_{-1}(x))$$
    En utilisant la relation $\eta_{-1}(x) = 1 - \eta_1(x)$, nous avons :
    $$R(h^*|X=x) = \min(\eta_1(x), 1 - \eta_1(x))$$
    Le risque de Bayes est alors l'espérance de cette quantité par rapport à la variable aléatoire $X$:
    $$R(h^*) = E[\min(\eta_1(X), 1 - \eta_1(X))]$$
    Par définition de l'espérance d'une fonction d'une variable aléatoire, et si $P_X$ est une mesure de probabilité sur $(\mathcal{X}, \mathcal{B}_{\mathcal{X}})$, le risque de Bayes s'exprime par l'intégrale suivante :
    $$R(h^*) = \int_{\mathcal{X}} \min(\eta_1(x), 1 - \eta_1(x)) \, dP_X(x)$$
    Si la distribution $P_X$ admet une densité $f_X(x)$ par rapport à une mesure de référence $\mu$ (par exemple, la mesure de Lebesgue pour $\mathcal{X}=\mathbb{R}^d$ ou la mesure de comptage pour $\mathcal{X}$ discret), alors le risque de Bayes peut s'écrire :
    $$R(h^*) = \int_{\mathcal{X}} \min(\eta_1(x), 1 - \eta_1(x)) f_X(x) \, d\mu(x)$$
    Cette formule montre que le risque de Bayes est la moyenne pondérée des probabilités d'erreur conditionnelles minimales sur l'ensemble de l'espace des entrées $\mathcal{X}$.