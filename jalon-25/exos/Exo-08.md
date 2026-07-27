---
title: "Exercice 8 : Produit scalaire sur l'espace des matrices M_n(R)"
difficulty: 4
---

## Énoncé Formel et Typage Rigoureux
Soit $\mathbb{K}$ un corps commutatif (typiquement $\mathbb{R}$ ou $\mathbb{C}$) et $E$ un $\mathbb{K}$-espace vectoriel. L'enjeu est d'éprouver la consistance algébrique des formes bilinéaires.
Sur $E = M_n(\mathbb{R})$, on définit l'application $\varphi(A, B) = \text{Tr}(A^T B)$, où $\text{Tr}$ désigne la trace de la matrice et $A^T$ la transposée.
1. Montrer que $\varphi$ définit un produit scalaire sur $E$.
2. En déduire que pour toutes matrices $A, B \in M_n(\mathbb{R})$, $|\text{Tr}(A^T B)| \le \sqrt{\text{Tr}(A^T A)} \sqrt{\text{Tr}(B^T B)}$.
3. Si $S$ est une matrice symétrique et $A$ une matrice antisymétrique, montrer que $\varphi(S, A) = 0$ (les espaces des matrices symétriques et antisymétriques sont orthogonaux pour ce produit scalaire).

## Preuve Analytique Pas-à-Pas (Zéro Ellipse)
La démarche déductive exige une formalisation intégrale sans ellipse.
**1. Validation du produit scalaire :**
Soient $A, B, C \in M_n(\mathbb{R})$ et $\lambda \in \mathbb{R}$.
- **Bilinéarité :** L'application trace et la transposition sont des opérateurs linéaires.
  La linéarité à droite s'établit par :
  $\varphi(A, \lambda B + C) = \text{Tr}(A^T(\lambda B + C)) = \text{Tr}(\lambda A^TB + A^TC)$
  $= \lambda \text{Tr}(A^TB) + \text{Tr}(A^TC) = \lambda \varphi(A, B) + \varphi(A, C)$.
- **Symétrie :** Propriété de la trace : pour toute matrice carrée $M$, $\text{Tr}(M) = \text{Tr}(M^T)$.
  Donc $\varphi(B, A) = \text{Tr}(B^T A) = \text{Tr}((B^T A)^T) = \text{Tr}(A^T (B^T)^T) = \text{Tr}(A^T B) = \varphi(A, B)$.
  L'application est symétrique (ce qui valide aussi la bilinéarité totale).
- **Positivité et caractère défini :**
  Soit $A \in M_n(\mathbb{R})$ avec des coefficients $A = (a_{ij})_{1\le i,j \le n}$.
  Calculons la trace de $A^T A$. Soit $C = A^T A$. Par définition du produit matriciel :
  $c_{ii} = \sum_{k=1}^n (A^T)_{ik} A_{ki} = \sum_{k=1}^n A_{ki} A_{ki} = \sum_{k=1}^n a_{ki}^2$.
  La trace est la somme des éléments diagonaux :
  $\varphi(A, A) = \text{Tr}(A^T A) = \sum_{i=1}^n c_{ii} = \sum_{i=1}^n \sum_{k=1}^n a_{ki}^2$.
  - C'est la somme de tous les carrés des coefficients de la matrice $A$. C'est donc toujours $\ge 0$. (Positivité).
  - Si $\varphi(A, A) = 0$, alors $\sum_{i,k} a_{ki}^2 = 0$. Étant une somme de termes positifs, chaque terme doit être nul, soit $a_{ki} = 0$ pour tous $i, k$. Donc $A$ est la matrice nulle. (Caractère défini).
C'est donc bien un produit scalaire.

**2. Application de l'inégalité de Cauchy-Schwarz :**
Puisque $\varphi(A, B) = \text{Tr}(A^T B)$ est un produit scalaire, nous pouvons directement lui appliquer l'inégalité de Cauchy-Schwarz : $|\langle A, B \rangle| \le \|A\| \|B\|$.
Ici, $\|A\| = \sqrt{\varphi(A, A)} = \sqrt{\text{Tr}(A^T A)}$.
L'inégalité se réécrit donc exactement :
$$|\text{Tr}(A^T B)| \le \sqrt{\text{Tr}(A^T A)} \sqrt{\text{Tr}(B^T B)}$$

**3. Orthogonalité des symétriques et antisymétriques :**
Soit $S$ une matrice symétrique (donc $S^T = S$) et $A$ une matrice antisymétrique (donc $A^T = -A$).
Calculons leur produit scalaire $\varphi(S, A)$ :
$\varphi(S, A) = \text{Tr}(S^T A)$.
Puisque $S^T = S$, on a $\varphi(S, A) = \text{Tr}(SA)$.
Utilisons la propriété de commutativité circulaire de la trace $\text{Tr}(MN) = \text{Tr}(NM)$ :
$\text{Tr}(SA) = \text{Tr}(AS)$.
Or, appliquons la transposition globale (car $\text{Tr}(M) = \text{Tr}(M^T)$) :
$\text{Tr}(AS) = \text{Tr}((AS)^T) = \text{Tr}(S^T A^T)$.
Puisque $S^T = S$ et $A^T = -A$, on substitue :
$\text{Tr}(S^T A^T) = \text{Tr}(S(-A)) = -\text{Tr}(SA)$.
Nous avons donc prouvé que $\text{Tr}(SA) = -\text{Tr}(SA)$.
Ceci implique $2\text{Tr}(SA) = 0 \implies \text{Tr}(SA) = 0$.
Donc $\varphi(S, A) = 0$. Les deux matrices sont orthogonales pour ce produit scalaire.
