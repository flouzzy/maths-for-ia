# Exercice 8 : Régularisation L2 (Weight Decay) et impact sur le gradient
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé
On ajoute un terme de régularisation L2 à la fonction de coût : $\mathcal{L}_{\text{reg}} = \mathcal{L}(y, \hat{y}) + \frac{\lambda}{2} \|W\|_F^2$, où $\|W\|_F^2 = \sum_{i,j} W_{ij}^2$ est la norme de Frobenius. Démontrer l'expression modifiée du gradient par rapport aux poids $W_{ij}$.

## Correction détaillée
1. La dérivée d'une somme est la somme des dérivées.
2. $\frac{\partial \mathcal{L}_{\text{reg}}}{\partial W_{ij}} = \frac{\partial \mathcal{L}}{\partial W_{ij}} + \frac{\partial}{\partial W_{ij}} \left( \frac{\lambda}{2} \sum_{p,q} W_{pq}^2 \right)$.
3. Dans la double somme, le seul terme non constant par rapport à $W_{ij}$ est le terme où $p=i$ et $q=j$, c'est-à-dire $W_{ij}^2$.
4. La dérivée de $\frac{\lambda}{2} W_{ij}^2$ par rapport à $W_{ij}$ est $\lambda W_{ij}$.
5. En utilisant l'expression du gradient non régularisé $\frac{\partial \mathcal{L}}{\partial W_{ij}} = \delta_i a_j$ (où $\delta$ est l'erreur de la couche et $a$ l'activation de la couche précédente).
6. Le gradient complet est donc : $\frac{\partial \mathcal{L}_{\text{reg}}}{\partial W_{ij}} = \delta_i a_j + \lambda W_{ij}$.
7. Sous forme matricielle : $\nabla_W \mathcal{L}_{\text{reg}} = \delta a^T + \lambda W$.
Cette pénalisation force les poids à rester proches de zéro, d'où le terme empirique de \"déclin du poids\" (Weight Decay) utilisé par les optimiseurs.
