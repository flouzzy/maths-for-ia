# Exercice 2: Noyau d'une forme linéaire (Hyperplan)
## Énoncé
Soit $\varphi : \mathbb{R}^3 \to \mathbb{R}$ définie par $\varphi(x, y, z) = x + 2y - z$.
1. Déterminer la dimension du noyau de $\varphi$, noté $H = \ker(\varphi)$.
2. Donner une base de cet hyperplan $H$.


## Correction détaillée
1. **Dimension du noyau :**
   L'application $\varphi$ est une forme linéaire sur $\mathbb{R}^3$. Comme $\varphi(1, 0, 0) = 1 \neq 0$, $\varphi$ n'est pas la forme linéaire nulle.
   Son image $\text{Im}(\varphi)$ est un sous-espace vectoriel de $\mathbb{R}$. Comme $\varphi \neq 0$, $\text{Im}(\varphi)$ n'est pas réduit à $\{0\}$, et puisque $\dim(\mathbb{R}) = 1$, on a nécessairement $\text{Im}(\varphi) = \mathbb{R}$, donc le rang de $\varphi$ est $1$.
   D'après le théorème du rang appliqué à $\varphi$ :
   $\dim(\mathbb{R}^3) = \dim(\ker(\varphi)) + \text{rg}(\varphi)$
   $3 = \dim(H) + 1$
   D'où $\dim(H) = 2$. Le sous-espace $H$ est bien un hyperplan.

2. **Base de l'hyperplan :**
   Un vecteur $u = (x, y, z)$ appartient à $H$ si et seulement si $\varphi(x, y, z) = 0$, c'est-à-dire :
   $x + 2y - z = 0 \iff z = x + 2y$
   Le vecteur $u$ s'écrit alors :
   $u = (x, y, x + 2y) = x(1, 0, 1) + y(0, 1, 2)$
   Posons $v_1 = (1, 0, 1)$ et $v_2 = (0, 1, 2)$.
   La famille $(v_1, v_2)$ engendre $H$.
   Montrons que cette famille est libre. Soient $\lambda_1, \lambda_2 \in \mathbb{R}$ tels que $\lambda_1 v_1 + \lambda_2 v_2 = (0, 0, 0)$.
   $\lambda_1(1, 0, 1) + \lambda_2(0, 1, 2) = (\lambda_1, \lambda_2, \lambda_1 + 2\lambda_2) = (0, 0, 0)$
   Cela donne immédiatement le système :
   $\lambda_1 = 0$ et $\lambda_2 = 0$.
   La famille est libre et génératrice de $H$. Puisque $\dim(H) = 2$, c'est une base de $H$.
