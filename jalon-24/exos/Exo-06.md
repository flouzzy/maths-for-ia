---
title: "Exercice 6 : Théorème de Pythagore Statistique"
difficulty: ★★★★☆
---
# Énoncé
Soit $\hat{\mathbf{y}} = \mathbf{X}\hat{\mathbf{a}}$ le vecteur des prédictions (projection orthogonale).
Démontrer que la somme totale des carrés (SST) se décompose exactement en somme des carrés expliqués (SSR) et somme des carrés résiduels (SSE) : $\|\mathbf{y} - \bar{y}\mathbf{1}\|_2^2 = \|\hat{\mathbf{y}} - \bar{y}\mathbf{1}\|_2^2 + \|\mathbf{y} - \hat{\mathbf{y}}\|_2^2$, à condition que le modèle contienne une ordonnée à l'origine.

# Correction Détaillée
1. **Condition d'orthogonalité :**
   Les résidus sont $\mathbf{e} = \mathbf{y} - \hat{\mathbf{y}}$.
   Puisque $\hat{\mathbf{y}}$ est la projection orthogonale de $\mathbf{y}$ sur l'image de $\mathbf{X}$, $\mathbf{e}$ est orthogonal à toutes les colonnes de $\mathbf{X}$.
   Donc $\mathbf{X}^\top \mathbf{e} = \mathbf{0}$.
2. **Propriété de l'ordonnée à l'origine :**
   Si le modèle inclut $a_0$, la première colonne de $\mathbf{X}$ est le vecteur $\mathbf{1} = (1, \dots, 1)^\top$.
   Donc $\mathbf{1}^\top \mathbf{e} = 0 \implies \sum_{i=1}^n e_i = 0$.
   La moyenne des résidus est nulle, donc la moyenne des prédictions égale la moyenne des observations : $\bar{\hat{y}} = \bar{y}$.
3. **Décomposition de la variance (Pythagore) :**
   Écrivons $\mathbf{y} - \bar{y}\mathbf{1} = (\hat{\mathbf{y}} - \bar{y}\mathbf{1}) + (\mathbf{y} - \hat{\mathbf{y}})$.
   Élevons à la norme au carré :
   $\|\mathbf{y} - \bar{y}\mathbf{1}\|_2^2 = \|\hat{\mathbf{y}} - \bar{y}\mathbf{1}\|_2^2 + \|\mathbf{y} - \hat{\mathbf{y}}\|_2^2 + 2\langle \hat{\mathbf{y}} - \bar{y}\mathbf{1}, \mathbf{y} - \hat{\mathbf{y}} \rangle$.
   Calculons le produit scalaire croisé :
   $\langle \hat{\mathbf{y}} - \bar{y}\mathbf{1}, \mathbf{e} \rangle = \hat{\mathbf{y}}^\top \mathbf{e} - \bar{y}\mathbf{1}^\top \mathbf{e}$.
   Or $\hat{\mathbf{y}} \in \text{Im}(\mathbf{X})$, donc $\hat{\mathbf{y}}^\top \mathbf{e} = 0$.
   Et d'après l'étape 2, $\mathbf{1}^\top \mathbf{e} = 0$.
   Le terme croisé est donc strictement nul.
   D'où SST = SSR + SSE.
