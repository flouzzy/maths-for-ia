# Exercice 8 - Difficulté ★★★★★

## Énoncé
Soient $A, B \in \mathcal{M}_n(\mathbb{R})$ deux matrices diagonalisables qui commutent (i.e. $AB = BA$).
Démontrer que tout sous-espace propre de $A$ est stable par $B$. En déduire, en supposant que les valeurs propres de $A$ sont simples, qu'il existe une base de vecteurs propres communs, rendant $A$ et $B$ simultanément diagonalisables.

## Solution Complète (Zéro Ellipse)

**Étape 1 : Stabilité des sous-espaces propres**
Soit $\lambda$ une valeur propre de $A$, et $E_\lambda = \ker(A - \lambda I)$ le sous-espace propre associé.
Prenons un vecteur $x \in E_\lambda$. Par définition, $Ax = \lambda x$.
Calculons $A(Bx)$. Puisque $A$ et $B$ commutent :
$$A(Bx) = (AB)x = (BA)x = B(Ax)$$
Or $Ax = \lambda x$. Par linéarité de $B$ :
$$A(Bx) = B(\lambda x) = \lambda (Bx)$$
Cette égalité signifie que le vecteur $(Bx)$ appartient également à $\ker(A - \lambda I)$, donc $Bx \in E_\lambda$.
Par conséquent, on a bien démontré que $B(E_\lambda) \subset E_\lambda$. L'espace propre de $A$ est **stable par l'action de B**.

**Étape 2 : Conséquence avec des valeurs propres simples**
Supposons que toutes les valeurs propres de $A$ sont simples (chacune a une multiplicité algébrique de $1$).
Dans ce cas, $\dim(E_\lambda) = 1$ pour chaque valeur propre $\lambda$.
Soit $x_\lambda$ un vecteur directeur de $E_\lambda$.
D'après l'étape 1, $B x_\lambda \in E_\lambda$.
Puisque $E_\lambda$ est de dimension $1$ et engendré par $x_\lambda$, tout vecteur de cet espace est colinéaire à $x_\lambda$.
Donc, il existe un scalaire $\mu \in \mathbb{R}$ tel que :
$$B x_\lambda = \mu x_\lambda$$
Cette équation est exactement la définition d'un vecteur propre !
Le vecteur $x_\lambda$, qui était déjà vecteur propre de $A$, est **aussi** un vecteur propre de $B$.
La valeur propre associée dans la matrice $B$ est $\mu$.

**Étape 3 : Conclusion globale**
Comme les valeurs propres de $A$ sont simples, $A$ admet une base complète constituée de ses vecteurs propres $x_{\lambda_1}, \dots, x_{\lambda_n}$.
Or nous venons de montrer que chacun de ces vecteurs est également un vecteur propre de $B$.
Ainsi, la même matrice de passage $P$ composée de ces vecteurs diagonisera $A$ (donnant $P^{-1}AP = D_A$) et diagonalisera $B$ (donnant $P^{-1}BP = D_B$).
Les matrices $A$ et $B$ sont dites **simultanément diagonalisables**.
