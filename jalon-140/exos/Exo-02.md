---
uuid: "jalon-140-exo-02"
title: "Exercice 2 - Jalon 140"
---
# Exercice 2 : Compréhension de la Fonction de Perte 0-1
**Difficulté:** ★

## Énoncé
Soit un problème de classification binaire où nous cherchons à prédire une variable aléatoire $Y \in \{-1, 1\}$ à partir d'une variable aléatoire $X$.
La fonction de perte 0-1, notée $L_{0-1}(y, \hat{y})$, est une fonction couramment utilisée pour évaluer la performance d'un classifieur.

1.  Définissez formellement la fonction de perte 0-1 pour une prédiction $\hat{y}$ et une vraie étiquette $y$.
2.  Interprétez la signification de $L_{0-1}(y, \hat{y})$ dans le contexte de la classification.
3.  Expliquez comment la minimisation de l'espérance de la perte 0-1 est directement liée à la minimisation du taux d'erreur de classification.

## Correction Pas-à-Pas
1.  **Définition formelle de la fonction de perte 0-1 :**
    La fonction de perte 0-1, $L_{0-1}(y, \hat{y})$, est définie comme suit :
    $L_{0-1}(y, \hat{y}) = 1$ si $y \neq \hat{y}$
    $L_{0-1}(y, \hat{y}) = 0$ si $y = \hat{y}$
    Cette définition peut également être exprimée à l'aide de la fonction indicatrice $\mathbb{I}(\cdot)$ :
    $L_{0-1}(y, \hat{y}) = \mathbb{I}(y \neq \hat{y})$
    où $\mathbb{I}(A)$ vaut 1 si l'événement $A$ est vrai, et 0 sinon.

2.  **Interprétation de la signification de $L_{0-1}(y, \hat{y})$ :**
    *   Lorsque la valeur de $L_{0-1}(y, \hat{y})$ est égale à 1, cela signifie que la prédiction $\hat{y}$ effectuée par le classifieur est différente de la vraie étiquette $y$. Dans ce cas, le classifieur a commis une erreur de classification.
    *   Lorsque la valeur de $L_{0-1}(y, \hat{y})$ est égale à 0, cela signifie que la prédiction $\hat{y}$ effectuée par le classifieur est identique à la vraie étiquette $y$. Dans ce cas, le classifieur a correctement classifié l'instance.
    En résumé, la fonction de perte 0-1 attribue un coût unitaire (1) pour chaque erreur de classification et un coût nul (0) pour chaque classification correcte. Elle quantifie directement si une prédiction est correcte ou incorrecte.

3.  **Lien entre la minimisation de l'espérance de la perte 0-1 et la minimisation du taux d'erreur de classification :**
    L'objectif principal d'un classifieur est de minimiser son risque attendu, qui est défini comme l'espérance de la fonction de perte sur l'ensemble des données. Pour la fonction de perte 0-1, le risque attendu pour un classifieur $h(X)$, noté $R(h)$, est donné par :
    $R(h) = \mathbb{E}[L_{0-1}(Y, h(X))]$
    En substituant la définition de la fonction de perte 0-1 à l'aide de la fonction indicatrice :
    $R(h) = \mathbb{E}[\mathbb{I}(Y \neq h(X))]$
    Par la propriété fondamentale de l'espérance d'une fonction indicatrice, l'espérance de $\mathbb{I}(A)$ est égale à la probabilité de l'événement $A$.
    Par conséquent, nous avons :
    $R(h) = P(Y \neq h(X))$
    La quantité $P(Y \neq h(X))$ représente la probabilité que le classifieur $h(X)$ produise une prédiction qui ne corresponde pas à la vraie étiquette $Y$. Cette probabilité est précisément la définition du taux d'erreur de classification (ou risque de classification).
    Ainsi, minimiser l'espérance de la perte 0-1 revient directement à minimiser la probabilité d'erreur de classification du classifieur. Le classifieur de Bayes optimal est le classifieur qui minimise ce risque 0-1, et par conséquent, minimise le taux d'erreur de classification.
