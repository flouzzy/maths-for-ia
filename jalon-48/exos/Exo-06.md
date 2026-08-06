# Exercice 6 : Rétropropagation de l'erreur Softmax avec Cross-Entropy (Cas $i=j$)
**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

## Énoncé
Soit un vecteur de probabilités $\hat{y}$ produit par une couche Softmax $\hat{y}_i = \frac{e^{z_i}}{\sum_k e^{z_k}}$ et une fonction de perte entropie croisée $\mathcal{L} = - \sum_k y_k \ln(\hat{y}_k)$, où $y$ est un vecteur one-hot. Montrer que $\frac{\partial \mathcal{L}}{\partial z_i} = \hat{y}_i - 1$ lorsque $y_i = 1$.

## Correction détaillée
1. Supposons que $y_i = 1$ (c'est la vraie classe). Tous les autres $y_k$ sont nuls.
2. La fonction de perte se simplifie en $\mathcal{L} = -\ln(\hat{y}_i)$.
3. Par la règle de la chaîne, $\frac{\partial \mathcal{L}}{\partial z_i} = \frac{\partial \mathcal{L}}{\partial \hat{y}_i} \frac{\partial \hat{y}_i}{\partial z_i}$.
4. On a $\frac{\partial \mathcal{L}}{\partial \hat{y}_i} = -\frac{1}{\hat{y}_i}$.
5. Calculons la dérivée de Softmax par rapport à sa propre entrée $z_i$. On pose le dénominateur $S = \sum_k e^{z_k}$.
6. $\hat{y}_i = \frac{e^{z_i}}{S}$. Par la règle du quotient, $\frac{\partial \hat{y}_i}{\partial z_i} = \frac{e^{z_i} S - e^{z_i} e^{z_i}}{S^2} = \frac{e^{z_i}}{S} \left( \frac{S - e^{z_i}}{S} \right) = \hat{y}_i (1 - \hat{y}_i)$.
7. En substituant dans la règle de la chaîne : $\frac{\partial \mathcal{L}}{\partial z_i} = -\frac{1}{\hat{y}_i} \cdot \hat{y}_i (1 - \hat{y}_i) = -(1 - \hat{y}_i) = \hat{y}_i - 1$.
Ce résultat extrêmement élégant (Prédiction - Cible) est à la base de l'apprentissage des classifieurs modernes.
