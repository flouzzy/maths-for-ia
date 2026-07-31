# Exercice 5 - Difficulté \quad $\bigstar$$\bigstar$$\bigstar$$\star$$\star$

## Énoncé
Soit la matrice de rotation d'angle $\pi/2$ :
$$R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$$
Montrer que $R$ n'est pas diagonalisable sur $\mathbb{R}$, mais qu'elle l'est sur $\mathbb{C}$. Déterminer ses éléments propres dans $\mathbb{C}$.

## Solution Complète

**Étape 1 : Polynôme caractéristique**
$\chi_R(X) = \det\begin{pmatrix} X & 1 \\ -1 & X \end{pmatrix} = X^2 - (-1)(1) = X^2 + 1$.

**Étape 2 : Étude sur le corps $\mathbb{R}$**
Le polynôme $X^2 + 1$ n'admet aucune racine réelle.
$\forall X \in \mathbb{R}, X^2 + 1 > 0$.
Ainsi, $\text{Sp}_{\mathbb{R}}(R) = \emptyset$.
Comme le polynôme caractéristique n'est pas scindé sur $\mathbb{R}$, la matrice $R$ **n'est pas diagonalisable sur $\mathbb{R}$**.

**Étape 3 : Étude sur le corps $\mathbb{C}$**
Dans $\mathbb{C}$, le polynôme se factorise : $X^2 + 1 = (X - i)(X + i)$.
Le polynôme caractéristique est scindé à racines simples. Les valeurs propres sont $i$ et $-i$.
Donc $R$ est **diagonalisable sur $\mathbb{C}$**.

**Étape 4 : Calcul des vecteurs propres complexes**
- Pour $\lambda_1 = i$ : $\ker(R - iI_2)$.
$\begin{pmatrix} -i & -1 \\ 1 & -i \end{pmatrix} \begin{pmatrix} z_1 \\ z_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \implies -i z_1 - z_2 = 0 \implies z_2 = -i z_1$.
Un vecteur propre est $v_1 = \begin{pmatrix} 1 \\ -i \end{pmatrix}$.

- Pour $\lambda_2 = -i$ : $\ker(R + iI_2)$.
$\begin{pmatrix} i & -1 \\ 1 & i \end{pmatrix} \begin{pmatrix} z_1 \\ z_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \implies i z_1 - z_2 = 0 \implies z_2 = i z_1$.
Un vecteur propre est $v_2 = \begin{pmatrix} 1 \\ i \end{pmatrix}$.

**Étape 5 : Matrice de passage complexe**
On a $P = \begin{pmatrix} 1 & 1 \\ -i & i \end{pmatrix}$ telle que $P^{-1} R P = \begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix}$.
