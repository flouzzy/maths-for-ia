---
title: "Exercice 5 : Produit d'espaces métriques"
---

### Exercice 5 : Produit d'espaces métriques \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soient $(X, d_X)$ et $(Y, d_Y)$ deux espaces métriques. On définit sur l'espace produit $X \times Y$ l'application $D$ par :
$$D((x_1, y_1), (x_2, y_2)) = \max(d_X(x_1, x_2), d_Y(y_1, y_2))$$
Démontrer que $D$ est une distance sur $X \times Y$.

**Correction Détaillée :**
Vérifions les axiomes :
1. **Séparation :** $D((x_1, y_1), (x_2, y_2)) = 0$ équivaut à $\max(d_X(x_1, x_2), d_Y(y_1, y_2)) = 0$. Comme les deux distances sont positives, cela implique $d_X(x_1, x_2) = 0$ et $d_Y(y_1, y_2) = 0$. D'où $x_1 = x_2$ et $y_1 = y_2$, donc $(x_1, y_1) = (x_2, y_2)$.
2. **Symétrie :** La symétrie découle immédiatement de la symétrie de $d_X$ et $d_Y$ et de la commutativité de la fonction max.
3. **Inégalité triangulaire :** Soient $A=(x_1, y_1)$, $B=(x_2, y_2)$ et $C=(x_3, y_3)$.
   On a $d_X(x_1, x_3) \le d_X(x_1, x_2) + d_X(x_2, x_3)$.
   Or, $d_X(x_1, x_2) \le D(A, B)$ et $d_X(x_2, x_3) \le D(B, C)$.
   Donc, $d_X(x_1, x_3) \le D(A, B) + D(B, C)$.
   De même, $d_Y(y_1, y_3) \le D(A, B) + D(B, C)$.
   Ainsi, les deux réels $d_X(x_1, x_3)$ et $d_Y(y_1, y_3)$ sont majorés par la quantité $D(A, B) + D(B, C)$. Par conséquent, leur maximum l'est aussi :
   $$D(A, C) = \max(d_X(x_1, x_3), d_Y(y_1, y_3)) \le D(A, B) + D(B, C)$$
$D$ définit donc bien une métrique produit sur $X \times Y$.
