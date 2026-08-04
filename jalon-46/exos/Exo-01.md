# Exercice 1 : Calcul de Jacobienne basique
## Énoncé
Soit la fonction $f : \mathbb{R}^2 \to \mathbb{R}^3$ définie par :
$$ f(x,y) = \begin{pmatrix} x^2 y \\ e^{x+y} \\ \cos(xy) \end{pmatrix} $$
Calculer la matrice jacobienne $J_f(x,y)$ en tout point $(x,y) \in \mathbb{R}^2$.
## Correction Détaillée
Soient les composantes $f_1(x,y) = x^2 y$, $f_2(x,y) = e^{x+y}$ et $f_3(x,y) = \cos(xy)$.
Les dérivées partielles par rapport à $x$ (première colonne) :
- $\frac{\partial f_1}{\partial x} = 2xy$
- $\frac{\partial f_2}{\partial x} = e^{x+y}$
- $\frac{\partial f_3}{\partial x} = -y\sin(xy)$

Les dérivées partielles par rapport à $y$ (deuxième colonne) :
- $\frac{\partial f_1}{\partial y} = x^2$
- $\frac{\partial f_2}{\partial y} = e^{x+y}$
- $\frac{\partial f_3}{\partial y} = -x\sin(xy)$

La matrice jacobienne est donc de dimension $3 \times 2$ :
$$ J_f(x,y) = \begin{pmatrix} 2xy & x^2 \\ e^{x+y} & e^{x+y} \\ -y\sin(xy) & -x\sin(xy) \end{pmatrix} $$
$\blacksquare$
