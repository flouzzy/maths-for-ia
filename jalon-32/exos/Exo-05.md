# Exercice 5 : Théorème Spectral et Matrices Symétriques \quad $\$bigstar$\bigstar$\bigstar\star\star$

## Énoncé
Soit un espace euclidien $E$ et un opérateur symétrique plus complexe.
Démontrer que le spectre de cet opérateur possède des propriétés particulières en utilisant le théorème spectral.
Soit $A = \begin{pmatrix} 10 & 5 \\ 5 & 10 \end{pmatrix}$.
Calculer ses valeurs propres, et trouver une base orthonormée de vecteurs propres.

## Solution

**1 - Polynôme caractéristique**
Soit $A = \begin{pmatrix} 10 & 5 \\ 5 & 10 \end{pmatrix}$.
Le polynôme caractéristique de $A$ est :
$\chi_A(X) = \det(X I - A) = \begin{vmatrix} X - 10 & -5 \\ -5 & X - 10 \end{vmatrix}$
$\chi_A(X) = (X - 10)^2 - (-5)^2$
$\chi_A(X) = (X - 10 - 5)(X - 10 + 5)$
$\chi_A(X) = (X - 15)(X - 5)$

**2 - Racines (Valeurs propres)**
Les racines du polynôme caractéristique sont évidentes. La matrice admet deux valeurs propres réelles distinctes :
$\lambda_1 = 15$ et $\lambda_2 = 5$.
Le fait que les valeurs propres soient réelles est garanti par le théorème spectral, car $A$ est symétrique réelle.

**3 - Vecteurs propres**
Pour $\lambda_1 = 15$ : on résout $AX = \lambda_1 X$.
Soit $X = \begin{pmatrix} x \\ y \end{pmatrix}$.
$\begin{pmatrix} 10 & 5 \\ 5 & 10 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 15x \\ 15y \end{pmatrix}$
Cela donne le système :
$10x + 5y = 15x \implies 5y = 5x \implies y = x$ (car $n \neq 0$)
Un vecteur propre est $V_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$.
Calculons sa norme euclidienne : $\|V_1\| = \sqrt{1^2 + 1^2} = \sqrt{2}$.
Le vecteur propre unitaire associé est $U_1 = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \end{pmatrix}$.

Pour $\lambda_2 = 5$ : on résout $AX = \lambda_2 X$.
$\begin{pmatrix} 10 & 5 \\ 5 & 10 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 5x \\ 5y \end{pmatrix}$
Cela donne :
$10x + 5y = 5x \implies 5x + 5y = 0 \implies y = -x$.
Un vecteur propre est $V_2 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$.
Calculons sa norme euclidienne : $\|V_2\| = \sqrt{1^2 + (-1)^2} = \sqrt{2}$.
Le vecteur propre unitaire associé est $U_2 = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ -1 \end{pmatrix}$.

**4 - Vérification de l'orthogonalité**
Vérifions que $U_1$ et $U_2$ sont orthogonaux (propriété fondamentale du théorème spectral pour des valeurs propres distinctes) :
$\langle U_1, U_2 \rangle = \frac{1}{2} (1 \times 1 + 1 \times (-1)) = 0$.
Ainsi, $\mathcal{B}' = (U_1, U_2)$ est une base orthonormée de $\mathbb{R}^2$ constituée de vecteurs propres de $A$.
