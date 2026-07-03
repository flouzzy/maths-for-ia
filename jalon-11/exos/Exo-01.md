# Exercice 1: Espace dual en dimension 2
## Énoncé
Soit $E = \mathbb{R}^2$ muni de sa base canonique $\mathcal{B} = (e_1, e_2)$. Soit $\varphi : E \to \mathbb{R}$ l'application définie par $\varphi(x, y) = 3x - 2y$.
1. Montrer que $\varphi$ est une forme linéaire, c'est-à-dire que $\varphi \in E^*$.
2. Déterminer les coordonnées de $\varphi$ dans la base duale $\mathcal{B}^* = (e_1^*, e_2^*)$.


## Correction détaillée
1. **Démonstration de la linéarité :**
   Soient $u = (x_1, y_1)$ et $v = (x_2, y_2)$ deux vecteurs de $E$, et $\lambda \in \mathbb{R}$ un scalaire.
   Calculons $\varphi(\lambda u + v)$ :
   Le vecteur $\lambda u + v$ a pour coordonnées $(\lambda x_1 + x_2, \lambda y_1 + y_2)$.
   Par définition de $\varphi$, on a :
   $\varphi(\lambda u + v) = 3(\lambda x_1 + x_2) - 2(\lambda y_1 + y_2)$
   En développant et en regroupant les termes :
   $\varphi(\lambda u + v) = 3\lambda x_1 + 3x_2 - 2\lambda y_1 - 2y_2 = \lambda(3x_1 - 2y_1) + (3x_2 - 2y_2)$
   On reconnaît $\varphi(u)$ et $\varphi(v)$ :
   $\varphi(\lambda u + v) = \lambda \varphi(u) + \varphi(v)$
   L'application $\varphi$ est donc bien une forme linéaire, $\varphi \in E^*$.

2. **Coordonnées dans la base duale :**
   La base duale $\mathcal{B}^* = (e_1^*, e_2^*)$ est caractérisée par $e_i^*(e_j) = \delta_{i,j}$.
   Toute forme linéaire $\varphi \in E^*$ se décompose de manière unique sur $\mathcal{B}^*$ :
   $\varphi = \varphi(e_1)e_1^* + \varphi(e_2)e_2^*$
   Calculons les évaluations sur les vecteurs de base :
   $\varphi(e_1) = \varphi(1, 0) = 3(1) - 2(0) = 3$
   $\varphi(e_2) = \varphi(0, 1) = 3(0) - 2(1) = -2$
   On en déduit l'expression de $\varphi$ :
   $\varphi = 3e_1^* - 2e_2^*$
   Les coordonnées de $\varphi$ dans la base $\mathcal{B}^*$ sont donc $(3, -2)$.
