# Exercice 2 : Théorème Spectral et Matrices Symétriques \quad $\$bigstar\star\star\star\star$

## Énoncé
Considérons une matrice $A$ symétrique réelle simple.
Démontrer que le spectre de cet opérateur possède des propriétés particulières en utilisant le théorème spectral.
Soit $A = \begin{pmatrix} 4 & 2 \\ 2 & 4 \end{pmatrix}$.
Calculer ses valeurs propres, et trouver une base orthonormée de vecteurs propres.

## Solution

**1 - Polynôme caractéristique**
Soit $A = \begin{pmatrix} 4 & 2 \\ 2 & 4 \end{pmatrix}$.
Le polynôme caractéristique de $A$ est :
$\chi_A(X) = \det(X I - A) = \begin{vmatrix} X - 4 & -2 \\ -2 & X - 4 \end{vmatrix}$
$\chi_A(X) = (X - 4)^2 - (-2)^2$
$\chi_A(X) = (X - 4 - 2)(X - 4 + 2)$
$\chi_A(X) = (X - 6)(X - 2)$

**2 - Racines (Valeurs propres)**
Les racines du polynôme caractéristique sont évidentes. La matrice admet deux valeurs propres réelles distinctes :
$\lambda_1 = 6$ et $\lambda_2 = 2$.
Le fait que les valeurs propres soient réelles est garanti par le théorème spectral, car $A$ est symétrique réelle.

**3 - Vecteurs propres**
Pour $\lambda_1 = 6$ : on résout $AX = \lambda_1 X$.
Soit $X = \begin{pmatrix} x \\ y \end{pmatrix}$.
$\begin{pmatrix} 4 & 2 \\ 2 & 4 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 6x \\ 6y \end{pmatrix}$
Cela donne le système :
$4x + 2y = 6x \implies 2y = 2x \implies y = x$ (car $n \neq 0$)
Un vecteur propre est $V_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$.
Calculons sa norme euclidienne : $\|V_1\| = \sqrt{1^2 + 1^2} = \sqrt{2}$.
Le vecteur propre unitaire associé est $U_1 = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \end{pmatrix}$.

Pour $\lambda_2 = 2$ : on résout $AX = \lambda_2 X$.
$\begin{pmatrix} 4 & 2 \\ 2 & 4 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 2x \\ 2y \end{pmatrix}$
Cela donne :
$4x + 2y = 2x \implies 2x + 2y = 0 \implies y = -x$.
Un vecteur propre est $V_2 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$.
Calculons sa norme euclidienne : $\|V_2\| = \sqrt{1^2 + (-1)^2} = \sqrt{2}$.
Le vecteur propre unitaire associé est $U_2 = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ -1 \end{pmatrix}$.

**4 - Vérification de l'orthogonalité**
Vérifions que $U_1$ et $U_2$ sont orthogonaux (propriété fondamentale du théorème spectral pour des valeurs propres distinctes) :
$\langle U_1, U_2 \rangle = \frac{1}{2} (1 \times 1 + 1 \times (-1)) = 0$.
Ainsi, $\mathcal{B}' = (U_1, U_2)$ est une base orthonormée de $\mathbb{R}^2$ constituée de vecteurs propres de $A$.
