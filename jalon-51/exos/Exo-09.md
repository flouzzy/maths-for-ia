# Exercice 9 : Produit d'espaces métriques
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé formel
Soient $(X_1, d_1)$ et $(X_2, d_2)$ deux espaces métriques. On équipe $X = X_1 \times X_2$ de la distance produit : $D(x, y) = \sqrt{d_1(x_1, y_1)^2 + d_2(x_2, y_2)^2}$. Vérifier l'inégalité triangulaire de $D$.

## Résolution pas à pas
**Étape 1 : Passage à l'espace euclidien bidimensionnel**

Pour trois points $x, y, z$ dans l'espace produit $X_1 \times X_2$, on a des composantes $(x_1, x_2)$, $(y_1, y_2)$ et $(z_1, z_2)$.
Posons les réels $a = d_1(x_1, y_1)$, $b = d_2(x_2, y_2)$, $u = d_1(y_1, z_1)$ et $v = d_2(y_2, z_2)$.
Les inégalités triangulaires sur les espaces de base donnent : $d_1(x_1, z_1) \le a + u$ et $d_2(x_2, z_2) \le b + v$.

**Étape 2 : Évaluation du membre de gauche**

Le carré de la distance cible est :
$D(x,z)^2 = d_1(x_1, z_1)^2 + d_2(x_2, z_2)^2 \le (a+u)^2 + (b+v)^2$.

**Étape 3 : Utilisation de Minkowski (Cauchy-Schwarz)**

Nous voulons montrer que $\sqrt{(a+u)^2 + (b+v)^2} \le \sqrt{a^2+b^2} + \sqrt{u^2+v^2}$.
Cette inégalité est exactement l'inégalité triangulaire pour la norme euclidienne usuelle sur $\mathbb{R}^2$ appliquée aux vecteurs $V_1 = (a,b)$ et $V_2 = (u,v)$.
Ainsi, $D(x,z) \le D(x,y) + D(y,z)$. La distance produit est parfaitement valide. $\blacksquare$
