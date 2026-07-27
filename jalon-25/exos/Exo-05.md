---
title: "Exercice 5 : Cas d'égalité dans Cauchy-Schwarz"
difficulty: 3
---

### Exercice 5 : Forme sesquilinéaire hermitienne
**Niveau : \star \star \star**

**Énoncé :**
Soit $E = \mathbb{C}^2$. On définit l'application $h(x, y) = x_1 \overline{y_1} + (1+i)x_1 \overline{y_2} + (1-i)x_2 \overline{y_1} + 3x_2 \overline{y_2}$.
Démontrer que $h$ définit un produit scalaire hermitien sur $E$.

**Correction (Zéro Ellipse) :**
1. **Linéarité à gauche et semi-linéarité à droite :**
   L'expression est une combinaison linéaire de termes de la forme $x_j \overline{y_k}$. Ces monômes sont linéaires en la variable $x$ et conjugués-linéaires en la variable $y$. La somme préserve ces propriétés, donc $h$ est une forme sesquilinéaire.
2. **Symétrie hermitienne :**
   Calculons $\overline{h(y, x)}$ :
   \[ \overline{h(y, x)} = \overline{y_1 \overline{x_1} + (1+i)y_1 \overline{x_2} + (1-i)y_2 \overline{x_1} + 3y_2 \overline{x_2}} \]
   \[ = \overline{y_1} x_1 + (1-i)\overline{y_1} x_2 + (1+i)\overline{y_2} x_1 + 3\overline{y_2} x_2 = h(x, y) \]
   $h$ est bien hermitienne.
3. **Positivité :**
   Évaluons $h(x, x)$ :
   \[ h(x, x) = |x_1|^2 + (1+i)x_1 \overline{x_2} + (1-i)x_2 \overline{x_1} + 3|x_2|^2 \]
   Une approche algébrique par complétion de carrés donne :
   \[ h(x, x) = |x_1 + (1-i)x_2|^2 - |(1-i)x_2|^2 + 3|x_2|^2 \]
   Calculons $|1-i|^2 = 1^2 + (-1)^2 = 2$.
   Donc $h(x, x) = |x_1 + (1-i)x_2|^2 - 2|x_2|^2 + 3|x_2|^2 = |x_1 + (1-i)x_2|^2 + |x_2|^2 \ge 0$.
4. **Définie :**
   Si $h(x, x) = 0$, la somme des carrés positifs est nulle :
   $|x_1 + (1-i)x_2|^2 = 0$ et $|x_2|^2 = 0$.
   La seconde équation donne $x_2 = 0$. En injectant dans la première, $|x_1|^2 = 0 \implies x_1 = 0$. Donc $x = 0_E$.
Conclusion : $h$ est un produit scalaire hermitien.
