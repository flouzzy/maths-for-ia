---
title: "Exercice 10 : Validation Croisée Leave-One-Out (LOOCV)"
difficulty: ★★★★★
---
# Énoncé
Prouver la formule magique du Leave-One-Out : on peut calculer l'erreur LOOCV sans ré-entraîner le modèle $n$ fois, via l'équation $y_i - \hat{y}_{i}^{(-i)} = \frac{y_i - \hat{y}_i}{1 - h_{ii}}$, où $\hat{y}_{i}^{(-i)}$ est la prédiction sur $x_i$ par le modèle entraîné sur toutes les données sauf la $i$-ème, et $h_{ii}$ l'effet de levier.

# Correction Détaillée
1. **Définition de l'estimateur perturbé :**
   Le modèle retirant l'observation $i$ s'écrit $\hat{\mathbf{a}}^{(-i)} = (\mathbf{X}_{(-i)}^\top \mathbf{X}_{(-i)})^{-1} \mathbf{X}_{(-i)}^\top \mathbf{y}_{(-i)}$.
   Remarquons que $\mathbf{X}^\top\mathbf{X} = \mathbf{X}_{(-i)}^\top \mathbf{X}_{(-i)} + \mathbf{x}_i \mathbf{x}_i^\top$.
2. **Lemme d'inversion matricielle (Sherman-Morrison) :**
   $(\mathbf{A} - \mathbf{u}\mathbf{v}^\top)^{-1} = \mathbf{A}^{-1} + \frac{\mathbf{A}^{-1}\mathbf{u}\mathbf{v}^\top\mathbf{A}^{-1}}{1 - \mathbf{v}^\top\mathbf{A}^{-1}\mathbf{u}}$.
   Appliqué avec $\mathbf{A} = \mathbf{X}^\top\mathbf{X}$ et $\mathbf{u}=\mathbf{v}=\mathbf{x}_i$ :
   $(\mathbf{X}_{(-i)}^\top \mathbf{X}_{(-i)})^{-1} = (\mathbf{X}^\top\mathbf{X})^{-1} + \frac{(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{x}_i\mathbf{x}_i^\top(\mathbf{X}^\top\mathbf{X})^{-1}}{1 - \mathbf{x}_i^\top(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{x}_i}$.
   Notons que $h_{ii} = \mathbf{x}_i^\top(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{x}_i$.
3. **Calcul de la différence des prédictions :**
   En développant $\hat{\mathbf{a}}^{(-i)}$ en fonction de $\hat{\mathbf{a}}$ et en multipliant par $\mathbf{x}_i^\top$, des simplifications algébriques massives se produisent. L'astuce consiste à écrire $\mathbf{X}_{(-i)}^\top \mathbf{y}_{(-i)} = \mathbf{X}^\top\mathbf{y} - \mathbf{x}_i y_i$.
   On obtient finalement $\hat{\mathbf{a}} - \hat{\mathbf{a}}^{(-i)} = \frac{(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{x}_i}{1 - h_{ii}} (y_i - \hat{y}_i)$.
4. **Conclusion de l'erreur :**
   Prédisons sur le point retiré : $\hat{y}_{i}^{(-i)} = \mathbf{x}_i^\top \hat{\mathbf{a}}^{(-i)} = \mathbf{x}_i^\top \hat{\mathbf{a}} - \frac{\mathbf{x}_i^\top(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{x}_i}{1 - h_{ii}} (y_i - \hat{y}_i)$.
   $\hat{y}_{i}^{(-i)} = \hat{y}_i - \frac{h_{ii}}{1 - h_{ii}} (y_i - \hat{y}_i)$.
   Calculons l'erreur : $y_i - \hat{y}_{i}^{(-i)} = y_i - \hat{y}_i + \frac{h_{ii}}{1 - h_{ii}} (y_i - \hat{y}_i) = (y_i - \hat{y}_i) \left(1 + \frac{h_{ii}}{1 - h_{ii}}\right) = \frac{y_i - \hat{y}_i}{1 - h_{ii}}$.
   Cette formule fondamentale permet d'évaluer la généralisation du modèle en un seul passage algorithmique !
