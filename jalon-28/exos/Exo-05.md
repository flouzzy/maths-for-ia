---
title: "Exercice 5 : Calcul des itérés d'une matrice via la division euclidienne polynomiale"
difficulty: 3
---

# Exercice 5 : Calcul des itérés d'une matrice via la division euclidienne polynomiale (★★★☆☆)

## Énoncé

Soit $A = \begin{pmatrix} 0 & -1 \\ 1 & 2 \end{pmatrix} \in \mathcal{M}_2(\mathbb{R})$.
On cherche à calculer $A^n$ pour tout $n \in \mathbb{N}$.
1. Déterminer le polynôme caractéristique $\chi_A(X)$.
2. En effectuant la division euclidienne du polynôme $X^n$ par $\chi_A(X)$, exprimer le reste $R_n(X)$ en fonction de $X$, $n$ et de constantes.
3. En déduire une expression explicite de $A^n$.

## Solution Rigoureuse

### 1. Polynôme caractéristique
Calculons $\chi_A(X) = \det(X I_2 - A)$ :
$$\chi_A(X) = \begin{vmatrix} X & 1 \\ -1 & X - 2 \end{vmatrix} = X(X - 2) - (-1)(1) = X^2 - 2X + 1 = (X - 1)^2$$
On remarque que $\lambda = 1$ est la seule valeur propre, de multiplicité algébrique 2.
D'après le théorème de Cayley-Hamilton, $\chi_A(A) = 0_2$, donc $(A - I_2)^2 = 0_2$.

### 2. Division euclidienne
Effectuons la division euclidienne polynomiale de $X^n$ par $\chi_A(X)$ dans $\mathbb{R}[X]$. Il existe d'uniques polynômes $Q_n(X)$ (quotient) et $R_n(X)$ (reste) tels que :
$$X^n = Q_n(X) \chi_A(X) + R_n(X)$$
avec $\deg(R_n) < \deg(\chi_A) = 2$.
Ainsi, le reste est de degré au plus 1, on peut l'écrire sous la forme : $R_n(X) = a_n X + b_n$, avec $a_n, b_n \in \mathbb{R}$.
La relation s'écrit :
$$X^n = Q_n(X)(X - 1)^2 + a_n X + b_n$$
Pour déterminer $a_n$ et $b_n$, nous allons évaluer cette égalité formelle en des points astucieux. Le point d'annulation de la racine double $(X-1)^2$ est $X=1$.
Évaluation en $X=1$ :
$$1^n = Q_n(1) \times 0 + a_n(1) + b_n \implies a_n + b_n = 1 \quad \text{(Éq. 1)}$$
Puisque $(X-1)^2$ a une racine double, la dérivation formelle du polynôme donnera une équation indépendante. Dérivons l'égalité polynomiale par rapport à $X$ :
$$n X^{n-1} = Q'_n(X)(X-1)^2 + Q_n(X) \cdot 2(X-1) + a_n$$
Évaluons cette dérivée en $X=1$ :
$$n \times 1^{n-1} = 0 + 0 + a_n \implies a_n = n$$
Substituons $a_n = n$ dans l'Équation 1 :
$$n + b_n = 1 \implies b_n = 1 - n$$
Le reste de la division euclidienne est donc rigoureusement :
$$R_n(X) = nX + (1 - n)$$

### 3. Expression de $A^n$
Nous partons de l'égalité polynomiale :
$$X^n = Q_n(X)\chi_A(X) + nX + (1 - n)$$
En appliquant le morphisme d'évaluation en la matrice $A$ (qui préserve les opérations polynomiales), nous obtenons dans $\mathcal{M}_2(\mathbb{R})$ :
$$A^n = Q_n(A)\chi_A(A) + nA + (1 - n)I_2$$
D'après le théorème de Cayley-Hamilton, $\chi_A(A) = 0_2$. Donc le premier terme s'annule totalement :
$$A^n = nA + (1 - n)I_2$$

Remplaçons $A$ et $I_2$ par leurs matrices pour le calcul explicite :
$$A^n = n \begin{pmatrix} 0 & -1 \\ 1 & 2 \end{pmatrix} + (1 - n) \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$$
$$A^n = \begin{pmatrix} 0 & -n \\ n & 2n \end{pmatrix} + \begin{pmatrix} 1 - n & 0 \\ 0 & 1 - n \end{pmatrix}$$
$$A^n = \begin{pmatrix} 1 - n & -n \\ n & n + 1 \end{pmatrix}$$
*(Vérification : Pour n=1, on retrouve bien A. Pour n=0, on retrouve bien I_2).*
