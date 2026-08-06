# Exercice 9 : Rétropropagation à travers une couche de normalisation (Batch Normalization)
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé
Soit $z = \gamma \hat{x} + \beta$ où $\hat{x} = \frac{x - \mu}{\sqrt{\sigma^2 + \epsilon}}$. Sachant qu'on a le gradient entrant $\frac{\partial \mathcal{L}}{\partial z}$, exprimer rigoureusement $\frac{\partial \mathcal{L}}{\partial \gamma}$ et $\frac{\partial \mathcal{L}}{\partial \beta}$ sur un mini-batch de taille $N$.

## Correction détaillée
1. Les paramètres $\gamma$ (facteur d'échelle) et $\beta$ (décalage) sont des vecteurs de la même taille que $x$. Soit $i$ l'indice de la dimension. On somme sur les $N$ exemples du mini-batch, indexés par $k$.
2. Pour l'exemple $k$, on a la pré-activation $z_{k,i} = \gamma_i \hat{x}_{k,i} + \beta_i$.
3. La dérivée totale de la perte par rapport au paramètre $\beta_i$ nécessite de sommer les contributions de tous les exemples du batch.
4. Par la règle de la chaîne : $\frac{\partial \mathcal{L}}{\partial \beta_i} = \sum_{k=1}^N \frac{\partial \mathcal{L}}{\partial z_{k,i}} \frac{\partial z_{k,i}}{\partial \beta_i}$.
5. On calcule trivialement $\frac{\partial z_{k,i}}{\partial \beta_i} = 1$.
6. Donc, $\frac{\partial \mathcal{L}}{\partial \beta_i} = \sum_{k=1}^N \frac{\partial \mathcal{L}}{\partial z_{k,i}}$. Le gradient par rapport à $\beta$ est la somme des erreurs propagées sur le batch.
7. De manière similaire pour $\gamma_i$ : $\frac{\partial \mathcal{L}}{\partial \gamma_i} = \sum_{k=1}^N \frac{\partial \mathcal{L}}{\partial z_{k,i}} \frac{\partial z_{k,i}}{\partial \gamma_i}$.
8. La dérivée est $\frac{\partial z_{k,i}}{\partial \gamma_i} = \hat{x}_{k,i}$.
9. Ainsi, $\frac{\partial \mathcal{L}}{\partial \gamma_i} = \sum_{k=1}^N \frac{\partial \mathcal{L}}{\partial z_{k,i}} \hat{x}_{k,i}$.
Ces gradients paramétriques sont essentiels pour que la couche de normalisation puisse restaurer le pouvoir d'expressivité du réseau si la normalisation stricte s'avérait sous-optimale.
