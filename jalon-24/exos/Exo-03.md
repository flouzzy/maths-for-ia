---
title: "Exercice 3 : Régularisation de Tikhonov (Ridge Regression)"
difficulty: ★★★☆☆
---
# Énoncé
Pour pallier la multicolinéarité (matrice $\mathbf{X}^\top\mathbf{X}$ mal conditionnée), on introduit une pénalité : $\mathcal{L}_{Ridge}(\mathbf{a}) = \|\mathbf{X}\mathbf{a} - \mathbf{y}\|_2^2 + \lambda \|\mathbf{a}\|_2^2$, avec $\lambda > 0$.
Montrer que l'estimateur Ridge $\hat{\mathbf{a}}_\lambda = (\mathbf{X}^\top\mathbf{X} + \lambda \mathbf{I})^{-1}\mathbf{X}^\top\mathbf{y}$ est toujours défini, et calculer son biais sous le modèle $\mathbf{y} = \mathbf{X}\mathbf{a}^* + \boldsymbol{\epsilon}$.

# Correction Détaillée
1. **Inversibilité de $\mathbf{X}^\top\mathbf{X} + \lambda \mathbf{I}$ :**
   Soit $\mathbf{M} = \mathbf{X}^\top\mathbf{X} + \lambda \mathbf{I}$. Soit $\mathbf{u} \neq \mathbf{0}$.
   $\mathbf{u}^\top\mathbf{M}\mathbf{u} = \mathbf{u}^\top\mathbf{X}^\top\mathbf{X}\mathbf{u} + \lambda \mathbf{u}^\top\mathbf{u} = \|\mathbf{X}\mathbf{u}\|_2^2 + \lambda \|\mathbf{u}\|_2^2$.
   Comme $\lambda > 0$ et $\|\mathbf{u}\|_2 > 0$, la somme est strictement positive.
   $\mathbf{M}$ est donc strictement définie positive, et par conséquent inversible.

2. **Calcul du biais de $\hat{\mathbf{a}}_\lambda$ :**
   Substituons $\mathbf{y}$ par $\mathbf{X}\mathbf{a}^* + \boldsymbol{\epsilon}$ :
   $\hat{\mathbf{a}}_\lambda = (\mathbf{X}^\top\mathbf{X} + \lambda \mathbf{I})^{-1}\mathbf{X}^\top(\mathbf{X}\mathbf{a}^* + \boldsymbol{\epsilon})$.
   Prenons l'espérance :
   $\mathbb{E}[\hat{\mathbf{a}}_\lambda] = (\mathbf{X}^\top\mathbf{X} + \lambda \mathbf{I})^{-1}(\mathbf{X}^\top\mathbf{X})\mathbf{a}^*$.
   Remarquons que $\mathbf{X}^\top\mathbf{X} = (\mathbf{X}^\top\mathbf{X} + \lambda \mathbf{I}) - \lambda \mathbf{I}$.
   Donc $\mathbb{E}[\hat{\mathbf{a}}_\lambda] = (\mathbf{X}^\top\mathbf{X} + \lambda \mathbf{I})^{-1}((\mathbf{X}^\top\mathbf{X} + \lambda \mathbf{I}) - \lambda \mathbf{I})\mathbf{a}^* = (\mathbf{I} - \lambda(\mathbf{X}^\top\mathbf{X} + \lambda \mathbf{I})^{-1})\mathbf{a}^*$.
   Le biais est donc : $\text{Biais} = \mathbb{E}[\hat{\mathbf{a}}_\lambda] - \mathbf{a}^* = -\lambda(\mathbf{X}^\top\mathbf{X} + \lambda \mathbf{I})^{-1}\mathbf{a}^* \neq \mathbf{0}$.
   L'estimateur Ridge est **biaisé**. Le compromis consiste à accepter ce biais pour réduire drastiquement la variance.
