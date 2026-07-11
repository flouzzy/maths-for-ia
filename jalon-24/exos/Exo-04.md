---
title: "Exercice 4 : Décomposition en Valeurs Singulières (SVD) et Pseudo-inverse"
difficulty: ★★★☆☆
---
# Énoncé
Soit la décomposition SVD de la matrice de conception : $\mathbf{X} = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^\top$.
Exprimer l'estimateur des moindres carrés $\hat{\mathbf{a}}$ en fonction de $\mathbf{U}$, $\mathbf{\Sigma}$ et $\mathbf{V}$. Montrer comment la régularisation Ridge modifie les valeurs singulières inversées.

# Correction Détaillée
1. **Expression via SVD classique :**
   $\mathbf{X}^\top\mathbf{X} = (\mathbf{V} \mathbf{\Sigma}^\top \mathbf{U}^\top)(\mathbf{U} \mathbf{\Sigma} \mathbf{V}^\top) = \mathbf{V} \mathbf{\Sigma}^\top \mathbf{\Sigma} \mathbf{V}^\top = \mathbf{V} \mathbf{\Sigma}^2 \mathbf{V}^\top$ (car $\mathbf{U}^\top\mathbf{U} = \mathbf{I}$).
   Donc $(\mathbf{X}^\top\mathbf{X})^{-1} = \mathbf{V} \mathbf{\Sigma}^{-2} \mathbf{V}^\top$.
   L'estimateur devient : $\hat{\mathbf{a}} = (\mathbf{V} \mathbf{\Sigma}^{-2} \mathbf{V}^\top) (\mathbf{V} \mathbf{\Sigma}^\top \mathbf{U}^\top) \mathbf{y} = \mathbf{V} \mathbf{\Sigma}^{-2} \mathbf{\Sigma} \mathbf{U}^\top \mathbf{y} = \mathbf{V} \mathbf{\Sigma}^{-1} \mathbf{U}^\top \mathbf{y}$.
   Ceci correspond à multiplier $\mathbf{y}$ par la pseudo-inverse de Moore-Penrose $\mathbf{X}^+$.

2. **Effet de la régularisation Ridge sur SVD :**
   Pour l'estimateur Ridge :
   $\mathbf{X}^\top\mathbf{X} + \lambda \mathbf{I} = \mathbf{V} \mathbf{\Sigma}^2 \mathbf{V}^\top + \lambda \mathbf{V} \mathbf{I} \mathbf{V}^\top = \mathbf{V} (\mathbf{\Sigma}^2 + \lambda \mathbf{I}) \mathbf{V}^\top$.
   Donc $(\mathbf{X}^\top\mathbf{X} + \lambda \mathbf{I})^{-1} = \mathbf{V} (\mathbf{\Sigma}^2 + \lambda \mathbf{I})^{-1} \mathbf{V}^\top$.
   L'estimateur devient : $\hat{\mathbf{a}}_\lambda = \mathbf{V} (\mathbf{\Sigma}^2 + \lambda \mathbf{I})^{-1} \mathbf{\Sigma} \mathbf{U}^\top \mathbf{y}$.
   Pour la $j$-ème composante principale, la valeur singulière inverse $\frac{1}{\sigma_j}$ est remplacée par $\frac{\sigma_j}{\sigma_j^2 + \lambda}$.
   Si $\sigma_j$ est grand ($\sigma_j^2 \gg \lambda$), on retrouve $\approx \frac{1}{\sigma_j}$.
   Si $\sigma_j$ est très petit (colinéarité), au lieu de diverger vers l'infini, la fraction tend vers 0. La régularisation étouffe l'amplification du bruit dans les directions de faible variance.
