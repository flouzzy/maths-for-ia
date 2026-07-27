---
title: "Exercice 6 : Espace des polynômes et produit scalaire avec dérivation"
difficulty: 3
---

### Exercice 6 : Forme bilinéaire associée à une trace matricielle
**Niveau : \star \star \star**

**Énoncé :**
Sur l'espace vectoriel $E = M_n(\mathbb{R})$, on pose $\phi(A, B) = \text{Tr}(A^T B)$. Démontrer que $\phi$ est un produit scalaire.

**Correction (Zéro Ellipse) :**
1. **Symétrie :**
   $\phi(B, A) = \text{Tr}(B^T A)$. Sachant que la trace d'une matrice est égale à la trace de sa transposée :
   $\text{Tr}(B^T A) = \text{Tr}((B^T A)^T) = \text{Tr}(A^T B) = \phi(A, B)$.
2. **Bilinéarité :**
   $\phi(\lambda A + B, C) = \text{Tr}((\lambda A + B)^T C) = \text{Tr}(\lambda A^T C + B^T C) = \lambda \text{Tr}(A^T C) + \text{Tr}(B^T C) = \lambda \phi(A, C) + \phi(B, C)$.
3. **Positivité :**
   $(A^T A)_{i,i} = \sum_{k=1}^n (A^T)_{i,k} A_{k,i} = \sum_{k=1}^n a_{k,i}^2$.
   $\phi(A, A) = \text{Tr}(A^T A) = \sum_{i=1}^n \sum_{k=1}^n a_{k,i}^2 \ge 0$.
4. **Définie :**
   Si $\phi(A, A) = 0$, la somme des carrés est nulle, donc chaque terme est nul : $\forall i, k \in \{1,\ldots,n\}, a_{k,i}^2 = 0 \implies a_{k,i} = 0$. Donc la matrice $A$ est la matrice nulle $0_{M_n(\mathbb{R})}$.
