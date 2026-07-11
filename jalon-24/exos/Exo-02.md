---
title: "Exercice 2 : Biais et Variance de l'estimateur des moindres carrés"
difficulty: ★★☆☆☆
---
# Énoncé
On suppose que les observations sont générées par $\mathbf{y} = \mathbf{X}\mathbf{a}^* + \boldsymbol{\epsilon}$, où $\boldsymbol{\epsilon} \in \mathbb{R}^n$ est un vecteur aléatoire de bruit centré ($\mathbb{E}[\boldsymbol{\epsilon}] = \mathbf{0}$) et de matrice de covariance $\text{Var}(\boldsymbol{\epsilon}) = \sigma^2 \mathbf{I}_n$.
Montrer que l'estimateur des moindres carrés $\hat{\mathbf{a}} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}$ est sans biais et déterminer sa matrice de covariance.

# Correction Détaillée
1. **Calcul de l'espérance (Biais) :**
   Par définition, $\hat{\mathbf{a}} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top(\mathbf{X}\mathbf{a}^* + \boldsymbol{\epsilon})$.
   En développant par linéarité :
   $\hat{\mathbf{a}} = (\mathbf{X}^\top\mathbf{X})^{-1}(\mathbf{X}^\top\mathbf{X})\mathbf{a}^* + (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\boldsymbol{\epsilon} = \mathbf{a}^* + (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\boldsymbol{\epsilon}$.
   En prenant l'espérance, comme $\mathbf{X}$ est déterministe et $\mathbb{E}[\boldsymbol{\epsilon}] = \mathbf{0}$ :
   $\mathbb{E}[\hat{\mathbf{a}}] = \mathbf{a}^* + (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbb{E}[\boldsymbol{\epsilon}] = \mathbf{a}^*$.
   L'estimateur est donc **sans biais**.

2. **Calcul de la covariance :**
   La matrice de covariance est $\text{Var}(\hat{\mathbf{a}}) = \mathbb{E}[(\hat{\mathbf{a}} - \mathbf{a}^*)(\hat{\mathbf{a}} - \mathbf{a}^*)^\top]$.
   D'après le calcul précédent, $\hat{\mathbf{a}} - \mathbf{a}^* = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\boldsymbol{\epsilon}$.
   Ainsi, $\text{Var}(\hat{\mathbf{a}}) = \mathbb{E}[((\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\boldsymbol{\epsilon})((\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\boldsymbol{\epsilon})^\top]$.
   En utilisant la propriété de transposition $(AB)^\top = B^\top A^\top$ :
   $\text{Var}(\hat{\mathbf{a}}) = \mathbb{E}[(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top \boldsymbol{\epsilon} \boldsymbol{\epsilon}^\top \mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}]$.
   Par linéarité de l'espérance :
   $\text{Var}(\hat{\mathbf{a}}) = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top \mathbb{E}[\boldsymbol{\epsilon} \boldsymbol{\epsilon}^\top] \mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}$.
   Comme $\mathbb{E}[\boldsymbol{\epsilon} \boldsymbol{\epsilon}^\top] = \sigma^2 \mathbf{I}_n$ :
   $\text{Var}(\hat{\mathbf{a}}) = \sigma^2 (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top \mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1} = \sigma^2 (\mathbf{X}^\top\mathbf{X})^{-1}$.
