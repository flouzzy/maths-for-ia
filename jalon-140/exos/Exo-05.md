---
uuid: "jalon-140-exo-05"
title: "Exercice 5 - Classifieur de Bayes Optimal et Fonctions de Perte Substituts"
---
# Exercice 5 : Classifieur de Bayes Optimal et Fonctions de Perte Substituts
**Difficulté:** ★★★

## Énoncé
Soit un problème de classification binaire où la variable cible $Y \in \{-1, 1\}$ et la variable d'entrée $X \in \mathbb{R}^d$.
Nous disposons des probabilités a priori $P(Y=1) = \pi$ et $P(Y=-1) = 1-\pi$.
Nous disposons également des densités de probabilité conditionnelles $p(x|Y=1)$ et $p(x|Y=-1)$.

1.  **Classifieur de Bayes Optimal (0-1 loss)**
    Le classifieur de Bayes optimal $h^*(x)$ minimise le risque attendu sous la fonction de perte 0-1, définie par $\ell_{0-1}(y, \hat{y}) = \mathbb{I}(y \neq \hat{y})$, où $\mathbb{I}(\cdot)$ est la fonction indicatrice.
    Dérivez l'expression du classifieur de Bayes optimal $h^*(x)$ en fonction des probabilités a priori $P(Y=1)$, $P(Y=-1)$ et des densités conditionnelles $p(x|Y=1)$, $p(x|Y=-1)$.

2.  **Risque de Bayes**
    Exprimez le risque de Bayes $R(h^*) = E[\ell_{0-1}(Y, h^*(X))]$ en fonction des probabilités a priori et des densités conditionnelles.

3.  **Fonction de Perte Substitut (Hinge Loss)**
    Considérons une fonction de score $f(x) \in \mathbb{R}$ et un classifieur $\hat{y} = \text{sgn}(f(x))$.
    La fonction de perte charnière (hinge loss) est définie par $\ell_{hinge}(y, f(x)) = \max(0, 1 - y f(x))$.
    Pour les cas suivants, calculez la perte 0-1 $\ell_{0-1}(y, \text{sgn}(f(x)))$ et la perte charnière $\ell_{hinge}(y, f(x))$ :
    a.  $y = 1, f(x) = 2$
    b.  $y = 1, f(x) = 0.5$
    c.  $y = 1, f(x) = -1$
    d.  $y = -1, f(x) = -2$
    e.  $y = -1, f(x) = 0.8$
    f.  $y = -1, f(x) = 1.5$
    Commentez les différences observées entre les deux fonctions de perte.

## Correction Pas-à-Pas

**Partie 1 : Classifieur de Bayes Optimal (0-1 loss)**

Le classifieur de Bayes optimal $h^*(x)$ minimise le risque conditionnel $R(h|x) = E[\ell_{0-1}(Y, h(x))|X=x]$ pour chaque valeur de $x$.
Pour la fonction de perte 0-1, le risque conditionnel est donné par :
$R(h|x) = P(Y \neq h(x)|X=x)$

Pour un $x$ donné, nous devons choisir $h(x) \in \{-1, 1\}$ pour minimiser $P(Y \neq h(x)|X=x)$.
Si nous choisissons $h(x) = 1$, le risque est $P(Y = -1|X=x)$.
Si nous choisissons $h(x) = -1$, le risque est $P(Y = 1|X=x)$.

Le classifieur de Bayes optimal $h^*(x)$ est donc défini par la règle de décision suivante :
$h^*(x) = \begin{cases} 1 & \text{si } P(Y=1|X=x) \ge P(Y=-1|X=x) \\ -1 & \text{si } P(Y=1|X=x) < P(Y=-1|X=x) \end{cases}$

Nous utilisons le théorème de Bayes pour exprimer les probabilités a posteriori en fonction des probabilités a priori et des densités conditionnelles :
$P(Y=1|X=x) = \frac{p(x|Y=1)P(Y=1)}{p(x)}$
$P(Y=-1|X=x) = \frac{p(x|Y=-1)P(Y=-1)}{p(x)}$
où $p(x) = p(x|Y=1)P(Y=1) + p(x|Y=-1)P(Y=-1)$ est la densité marginale de $X$.

En substituant ces expressions dans la règle de décision :
$h^*(x) = \begin{cases} 1 & \text{si } \frac{p(x|Y=1)P(Y=1)}{p(x)} \ge \frac{p(x|Y=-1)P(Y=-1)}{p(x)} \\ -1 & \text{si } \frac{p(x|Y=1)P(Y=1)}{p(x)} < \frac{p(x|Y=-1)P(Y=-1)}{p(x)} \end{cases}$

Puisque la densité marginale $p(x)$ est positive, nous pouvons multiplier les deux côtés de l'inégalité par $p(x)$ sans changer le sens de l'inégalité :
$h^*(x) = \begin{cases} 1 & \text{si } p(x|Y=1)P(Y=1) \ge p(x|Y=-1)P(Y=-1) \\ -1 & \text{si } p(x|Y=1)P(Y=1) < p(x|Y=-1)P(Y=-1) \end{cases}$

En utilisant les probabilités a priori données $P(Y=1) = \pi$ et $P(Y=-1) = 1-\pi$ :
$h^*(x) = \begin{cases} 1 & \text{si } p(x|Y=1)\pi \ge p(x|Y=-1)(1-\pi) \\ -1 & \text{si } p(x|Y=1)\pi < p(x|Y=-1)(1-\pi) \end{cases}$

**Partie 2 : Risque de Bayes**

Le risque de Bayes $R(h^*)$ est le risque attendu du classifieur de Bayes optimal.
$R(h^*) = E[\ell_{0-1}(Y, h^*(X))]$
Par la loi de l'espérance totale, nous pouvons écrire :
$R(h^*) = \int_{\mathbb{R}^d} E[\ell_{0-1}(Y, h^*(X))|X=x] p(x) dx$
$R(h^*) = \int_{\mathbb{R}^d} P(Y \neq h^*(x)|X=x) p(x) dx$
Pour chaque $x$, le classifieur de Bayes $h^*(x)$ est choisi pour minimiser $P(Y \neq h(x)|X=x)$.
Donc, $P(Y \neq h^*(x)|X=x) = \min(P(Y=1|X=x), P(Y=-1|X=x))$.

Ainsi, le risque de Bayes est :
$R(h^*) = \int_{\mathbb{R}^d} \min(P(Y=1|X=x), P(Y=-1|X=x)) p(x) dx$

En utilisant la relation $P(Y=y|X=x)p(x) = p(x|Y=y)P(Y=y)$ :
$R(h^*) = \int_{\mathbb{R}^d} \min(p(x|Y=1)P(Y=1), p(x|Y=-1)P(Y=-1)) dx$

En substituant les probabilités a priori $P(Y=1) = \pi$ et $P(Y=-1) = 1-\pi$ :
$R(h^*) = \int_{\mathbb{R}^d} \min(p(x|Y=1)\pi, p(x|Y=-1)(1-\pi)) dx$

**Partie 3 : Fonction de Perte Substitut (Hinge Loss)**

Nous calculons la perte 0-1 $\ell_{0-1}(y, \text{sgn}(f(x)))$ et la perte charnière $\ell_{hinge}(y, f(x)) = \max(0, 1 - y f(x))$ pour les cas donnés.

a.  $y = 1, f(x) = 2$
    $\hat{y} = \text{sgn}(2) = 1$
    $\ell_{0-1}(1, 1) = \mathbb{I}(1 \neq 1) = 0$
    $\ell_{hinge}(1, 2) = \max(0, 1 - (1)(2)) = \max(0, 1 - 2) = \max(0, -1) = 0$

b.  $y = 1, f(x) = 0.5$
    $\hat{y} = \text{sgn}(0.5) = 1$
    $\ell_{0-1}(1, 1) = \mathbb{I}(1 \neq 1) = 0$
    $\ell_{hinge}(1, 0.5) = \max(0, 1 - (1)(0.5)) = \max(0, 1 - 0.5) = \max(0, 0.5) = 0.5$

c.  $y = 1, f(x) = -1$
    $\hat{y} = \text{sgn}(-1) = -1$
    $\ell_{0-1}(1, -1) = \mathbb{I}(1 \neq -1) = 1$
    $\ell_{hinge}(1, -1) = \max(0, 1 - (1)(-1)) = \max(0, 1 + 1) = \max(0, 2) = 2$

d.  $y = -1, f(x) = -2$
    $\hat{y} = \text{sgn}(-2) = -1$
    $\ell_{0-1}(-1, -1) = \mathbb{I}(-1 \neq -1) = 0$
    $\ell_{hinge}(-1, -2) = \max(0, 1 - (-1)(-2)) = \max(0, 1 - 2) = \max(0, -1) = 0$

e.  $y = -1, f(x) = 0.8$
    $\hat{y} = \text{sgn}(0.8) = 1$
    $\ell_{0-1}(-1, 1) = \mathbb{I}(-1 \neq 1) = 1$
    $\ell_{hinge}(-1, 0.8) = \max(0, 1 - (-1)(0.8)) = \max(0, 1 + 0.8) = \max(0, 1.8) = 1.8$

f.  $y = -1, f(x) = 1.5$
    $\hat{y} = \text{sgn}(1.5) = 1$
    $\ell_{0-1}(-1, 1) = \mathbb{I}(-1 \neq 1) = 1$
    $\ell_{hinge}(-1, 1.5) = \max(0, 1 - (-1)(1.5)) = \max(0, 1 + 1.5) = \max(0, 2.5) = 2.5$

**Commentaires sur les différences observées :**

*   **Classification correcte avec forte confiance (cas a, d) :** Lorsque le produit $y f(x) \ge 1$, cela signifie que le classifieur $\hat{y} = \text{sgn}(f(x))$ prédit la bonne classe ($y = \hat{y}$) et que la magnitude du score $f(x)$ est suffisamment grande dans la bonne direction. Dans ces situations, la perte 0-1 est nulle, et la perte charnière est également nulle. Les deux fonctions de perte sont en accord.

*   **Classification correcte avec faible confiance (cas b) :** Lorsque $0 < y f(x) < 1$, le classifieur $\hat{y} = \text{sgn}(f(x))$ prédit la bonne classe ($y = \hat{y}$), ce qui entraîne une perte 0-1 de 0. Cependant, la perte charnière est positive (0.5 dans l'exemple b). Cela indique que la perte charnière pénalise les classifications correctes qui ne sont pas faites avec une "marge" suffisante (le score $f(x)$ est du bon signe mais sa valeur absolue est inférieure à 1). Elle encourage le modèle à produire des scores $f(x)$ dont la valeur absolue est grande et du bon signe, afin d'augmenter la confiance dans la prédiction.

*   **Classification incorrecte (cas c, e, f) :** Lorsque $\text{sgn}(f(x)) \neq y$, le classifieur prédit la mauvaise classe, ce qui entraîne une perte 0-1 de 1. La perte charnière est également positive et, dans ces exemples, est supérieure ou égale à 1.
    *   La perte charnière pénalise d'autant plus l'erreur que le score $f(x)$ est "confiant" dans la mauvaise direction. Par exemple, dans le cas (f) où $y=-1$ et $f(x)=1.5$, le modèle prédit fortement la classe 1 alors que la vraie classe est -1. La perte charnière est de 2.5. Dans le cas (e) où $y=-1$ et $f(x)=0.8$, le modèle prédit la classe 1 avec une confiance moindre, et la perte charnière est de 1.8.
    *   La perte charnière est donc plus sensible à la magnitude et au signe du score $f(x)$ que la perte 0-1, qui ne considère que la classification finale correcte ou incorrecte.

En résumé, la perte charnière est une fonction de perte substitut convexe et continue qui sert de proxy à la perte 0-1. Elle présente les caractéristiques suivantes :
1.  Elle est nulle pour les classifications correctes avec une marge suffisante ($y f(x) \ge 1$).
2.  Elle pénalise linéairement les classifications correctes avec une marge insuffisante ($0 < y f(x) < 1$), encourageant le modèle à être plus confiant.
3.  Elle pénalise linéairement les classifications incorrectes, avec une pénalité d'autant plus grande que la prédiction est "fausse" et "confiante" ($y f(x) \le 0$).
Cette propriété de convexité et de continuité rend la perte charnière plus facile à optimiser que la perte 0-1, qui est non-convexe et non-différentiable, ce qui est crucial pour l'apprentissage de modèles comme les machines à vecteurs de support (SVM).
