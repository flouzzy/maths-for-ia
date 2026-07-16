---
title: "Exercice 1 : Calcul du polynôme annulateur d'une matrice nilpotente"
difficulty: 1
---

# Exercice 1 : Calcul du polynôme annulateur d'une matrice nilpotente (★☆☆☆☆)

## Énoncé

Soit la matrice $A = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix} \in \mathcal{M}_3(\mathbb{R})$.
1. Calculer $A^2$ et $A^3$.
2. En déduire le polynôme minimal $\pi_A(X)$ de $A$.
3. Le théorème de Cayley-Hamilton est-il vérifié pour cette matrice ?

## Solution Rigoureuse

### 1. Calcul des puissances de A
Effectuons le produit matriciel $A^2 = A \times A$ :
$$A^2 = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 \times 0 + 1 \times 0 + 0 \times 0 & 0 \times 1 + 1 \times 0 + 0 \times 0 & 0 \times 0 + 1 \times 1 + 0 \times 0 \\ 0 \times 0 + 0 \times 0 + 1 \times 0 & 0 \times 1 + 0 \times 0 + 1 \times 0 & 0 \times 0 + 0 \times 1 + 1 \times 0 \\ 0 \times 0 + 0 \times 0 + 0 \times 0 & 0 \times 1 + 0 \times 0 + 0 \times 0 & 0 \times 0 + 0 \times 1 + 0 \times 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$$

Calculons ensuite $A^3 = A^2 \times A$ :
$$A^3 = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 \times 0 + 0 \times 0 + 1 \times 0 & 0 \times 1 + 0 \times 0 + 1 \times 0 & 0 \times 0 + 0 \times 1 + 1 \times 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} = 0_3$$

### 2. Déduction du polynôme minimal
D'après ce qui précède, le polynôme $P(X) = X^3$ est un polynôme annulateur de $A$, car $P(A) = A^3 = 0_3$. Le polynôme minimal $\pi_A$ divise tout polynôme annulateur, donc $\pi_A$ divise $X^3$.
Les diviseurs unitaires de $X^3$ sont $1, X, X^2, X^3$.
- Si $\pi_A(X) = 1$, alors $\pi_A(A) = I_3 \neq 0_3$.
- Si $\pi_A(X) = X$, alors $\pi_A(A) = A \neq 0_3$.
- Si $\pi_A(X) = X^2$, alors $\pi_A(A) = A^2 = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} \neq 0_3$.
- Si $\pi_A(X) = X^3$, alors $\pi_A(A) = A^3 = 0_3$.

Donc le polynôme minimal de $A$ est rigoureusement $\pi_A(X) = X^3$.

### 3. Vérification de Cayley-Hamilton
Le polynôme caractéristique de $A$ est :
$$\chi_A(X) = \det(X I_3 - A) = \begin{vmatrix} X & -1 & 0 \\ 0 & X & -1 \\ 0 & 0 & X \end{vmatrix}$$
Le déterminant d'une matrice triangulaire supérieure est le produit de ses éléments diagonaux.
Donc $\chi_A(X) = X \times X \times X = X^3$.
On remarque que $\chi_A(A) = A^3 = 0_3$.
Le théorème de Cayley-Hamilton est bien vérifié.
