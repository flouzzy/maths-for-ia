---
title: "Exercice 8 : Influence des Points Aberrants (Levier)"
difficulty: ★★★★★
---
# Énoncé
La "Hat Matrix" $\mathbf{H} = \mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top$ projette les observations $\mathbf{y}$ sur les prédictions $\hat{\mathbf{y}}$.
Montrer que $\mathbf{H}$ est idempotente et symétrique. En déduire que la diagonale $h_{ii}$ vérifie $0 \le h_{ii} \le 1$ et interpréter cette valeur vis-à-vis des points aberrants.

# Correction Détaillée
1. **Symétrie :**
   $\mathbf{H}^\top = (\mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top)^\top = (\mathbf{X}^\top)^\top ((\mathbf{X}^\top\mathbf{X})^{-1})^\top \mathbf{X}^\top = \mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top = \mathbf{H}$.
2. **Idempotence :**
   $\mathbf{H}^2 = (\mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top)(\mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top) = \mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}(\mathbf{X}^\top\mathbf{X})(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top = \mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top = \mathbf{H}$.
3. **Encadrement de la diagonale :**
   Soit $\mathbf{e}_i$ le $i$-ème vecteur de la base canonique. $h_{ii} = \mathbf{e}_i^\top \mathbf{H} \mathbf{e}_i$.
   Comme $\mathbf{H}$ est idempotente et symétrique, $\mathbf{H} = \mathbf{H}^\top \mathbf{H}$.
   Donc $h_{ii} = \mathbf{e}_i^\top \mathbf{H}^\top \mathbf{H} \mathbf{e}_i = \|\mathbf{H}\mathbf{e}_i\|_2^2 \ge 0$.
   De plus, $\mathbf{I} - \mathbf{H}$ est aussi symétrique et idempotente.
   Donc $1 - h_{ii} = \mathbf{e}_i^\top (\mathbf{I} - \mathbf{H}) \mathbf{e}_i = \|(\mathbf{I} - \mathbf{H})\mathbf{e}_i\|_2^2 \ge 0$, ce qui implique $h_{ii} \le 1$.
   D'où $0 \le h_{ii} \le 1$.
4. **Interprétation :**
   $h_{ii}$ est le "leverage" (effet de levier) de la $i$-ème observation. Comme $\hat{y}_i = \sum_j h_{ij} y_j = h_{ii} y_i + \sum_{j \neq i} h_{ij} y_j$, un point de données ayant $h_{ii} \approx 1$ dicte presque à lui seul sa propre prédiction. Si ce point est aberrant, il va "tirer" le polynôme vers lui violemment, détruisant l'ajustement global.
