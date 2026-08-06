# Exercice 7 : Rétropropagation de l'erreur Softmax avec Cross-Entropy (Cas $i \neq j$)
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé
Sous les mêmes hypothèses que l'exercice précédent ($y$ est one-hot avec $y_j = 1$ et $\mathcal{L} = -\ln(\hat{y}_j)$), montrer que pour $i \neq j$, la dérivée est $\frac{\partial \mathcal{L}}{\partial z_i} = \hat{y}_i$.

## Correction détaillée
1. La perte est $\mathcal{L} = -\ln(\hat{y}_j)$. On cherche la dérivée par rapport à $z_i$ ($i \neq j$).
2. Par la règle de la chaîne, $\frac{\partial \mathcal{L}}{\partial z_i} = \frac{\partial \mathcal{L}}{\partial \hat{y}_j} \frac{\partial \hat{y}_j}{\partial z_i} = -\frac{1}{\hat{y}_j} \frac{\partial \hat{y}_j}{\partial z_i}$.
3. Calculons la dérivée croisée de la fonction Softmax. On a $\hat{y}_j = \frac{e^{z_j}}{S}$.
4. Le numérateur ne dépend pas de $z_i$. La dérivée porte uniquement sur le dénominateur $S = \sum_k e^{z_k}$.
5. $\frac{\partial \hat{y}_j}{\partial z_i} = e^{z_j} \cdot \frac{\partial (S^{-1})}{\partial z_i} = e^{z_j} \cdot (-S^{-2}) \frac{\partial S}{\partial z_i}$.
6. Or $\frac{\partial S}{\partial z_i} = e^{z_i}$.
7. Donc $\frac{\partial \hat{y}_j}{\partial z_i} = -\frac{e^{z_j} e^{z_i}}{S^2} = - \left(\frac{e^{z_j}}{S}\right) \left(\frac{e^{z_i}}{S}\right) = -\hat{y}_j \hat{y}_i$.
8. En remplaçant dans l'expression du gradient de la perte : $\frac{\partial \mathcal{L}}{\partial z_i} = -\frac{1}{\hat{y}_j} (-\hat{y}_j \hat{y}_i) = \hat{y}_i$.
9. Synthèse avec le cas $i=j$ (Exo 6) : Pour toute composante $i$, le gradient de la pré-activation est $\frac{\partial \mathcal{L}}{\partial z_i} = \hat{y}_i - y_i$. Forme vectorielle : $\nabla_z \mathcal{L} = \hat{y} - y$.
