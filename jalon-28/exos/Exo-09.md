---
title: "Exercice 9 : Matrices de rang 1 et polynôme minimal"
difficulty: 5
---

# Exercice 9 : Matrices de rang 1 et polynôme minimal (★★★★★)

## Énoncé

Soit $A \in \mathcal{M}_n(\mathbb{R})$ une matrice non nulle de rang 1.
1. Montrer qu'il existe deux vecteurs colonnes non nuls $U, V \in \mathbb{R}^n$ tels que $A = U V^T$.
2. En déduire que $A^2 = \text{Tr}(A) A$.
3. Déterminer le polynôme minimal de $A$ en discutant selon la valeur de sa trace.
4. Montrer que $A$ est diagonalisable si et seulement si $\text{Tr}(A) \neq 0$.

## Solution Rigoureuse

### 1. Factorisation d'une matrice de rang 1
L'image de $A$ (l'espace engendré par ses colonnes) est de dimension 1. Soit $U$ un vecteur non nul engendrant $\text{Im}(A)$.
Puisque chaque colonne $C_j$ de $A$ appartient à $\text{Im}(A)$, il existe un scalaire $v_j \in \mathbb{R}$ tel que $C_j = v_j U$.
La matrice $A$ s'écrit donc en blocs colonnes : $A = \begin{pmatrix} C_1 & C_2 & \dots & C_n \end{pmatrix} = \begin{pmatrix} v_1 U & v_2 U & \dots & v_n U \end{pmatrix}$.
Ceci se factorise exactement sous la forme du produit d'une colonne par une ligne :
$$A = U \begin{pmatrix} v_1 & v_2 & \dots & v_n \end{pmatrix} = U V^T$$
où $V^T = (v_1, \dots, v_n)$. $V$ n'est pas nul car $A$ est non nulle.

### 2. Carré et Trace
Calculons $A^2$ en utilisant la factorisation :
$$A^2 = (U V^T)(U V^T) = U (V^T U) V^T$$
Le terme central $(V^T U)$ est le produit matriciel d'une ligne $1 \times n$ par une colonne $n \times 1$. C'est un scalaire de taille $1 \times 1$. Comme c'est un scalaire, il commute avec tout.
$$A^2 = (V^T U) (U V^T) = (V^T U) A$$
Il reste à identifier le scalaire $V^T U$.
Par définition, la trace est linéaire et vérifie la propriété cyclique $\text{Tr}(AB) = \text{Tr}(BA)$.
Ici, $A = U V^T$, donc $\text{Tr}(A) = \text{Tr}(U V^T) = \text{Tr}(V^T U)$.
Or $V^T U$ est un scalaire, donc sa trace est lui-même. $\text{Tr}(A) = V^T U$.
En substituant, on obtient rigoureusement :
$$A^2 = \text{Tr}(A) A$$

### 3. Polynôme minimal
L'égalité précédente se réécrit $A^2 - \text{Tr}(A) A = 0_n$.
Le polynôme $P(X) = X^2 - \text{Tr}(A) X = X(X - \text{Tr}(A))$ est donc un polynôme annulateur de $A$.
Le polynôme minimal $\pi_A$ doit diviser ce polynôme $P(X)$.
$A$ étant non nulle, son polynôme minimal ne peut pas être de degré 0 ni être $X$ (car si $\pi_A(X) = X$, alors $\pi_A(A) = A = 0_n$, absurde).
Les diviseurs de $X(X - \text{Tr}(A))$ sont $X, X - \text{Tr}(A), X(X - \text{Tr}(A))$.
Discutons selon la trace :
- **Cas 1 : $\text{Tr}(A) \neq 0$**
Les facteurs $X$ et $X - \text{Tr}(A)$ sont distincts.
Si $\pi_A(X) = X - \text{Tr}(A)$, alors $A - \text{Tr}(A) I_n = 0_n \implies A = \text{Tr}(A) I_n$. Dans ce cas, le rang de $A$ serait $n$, or l'énoncé fixe un rang de 1. Pour $n \ge 2$, c'est absurde.
Donc $\pi_A(X)$ ne peut être un diviseur de degré 1. Il doit être de degré 2 :
$$\pi_A(X) = X(X - \text{Tr}(A))$$
- **Cas 2 : $\text{Tr}(A) = 0$**
L'équation $A^2 = \text{Tr}(A) A$ devient $A^2 = 0_n$. $A$ est nilpotente d'indice 2.
Le polynôme annulateur se réduit à $P(X) = X^2$.
Le polynôme minimal divise $X^2$. Ce ne peut être $X$ car $A \neq 0_n$. Donc :
$$\pi_A(X) = X^2$$

### 4. Diagonalisabilité
Un endomorphisme est diagonalisable si et seulement si son polynôme minimal est scindé à racines simples (théorème de diagonalisation).
- Si $\text{Tr}(A) \neq 0$, le polynôme minimal $\pi_A(X) = X(X - \text{Tr}(A))$ a deux racines distinctes réelles : $0$ et $\text{Tr}(A)$. Il est scindé à racines simples. La matrice $A$ est diagonalisable.
- Si $\text{Tr}(A) = 0$, le polynôme minimal $\pi_A(X) = X^2$ admet 0 comme racine double. Il n'est pas à racines simples. La matrice $A$ n'est pas diagonalisable.
Ceci achève la démonstration complète de l'équivalence. $\blacksquare$
