---
uuid: "exo-11-07"
title: "Exercice 7: Trace d'une matrice et forme linéaire"
---
# Exercice 7: Trace d'une matrice et forme linéaire (Difficulté $\star \star \star \star$)

## Énoncé
Soit l'espace vectoriel $E = \mathcal{M}_n(\mathbb{R})$. L'application trace $\text{Tr} : M \mapsto \sum_{i=1}^n m_{i,i}$ est une forme linéaire. Démontrer que tout hyperplan de $\mathcal{M}_n(\mathbb{R})$ contient au moins une matrice inversible (pour $n \ge 2$).

## Correction détaillée

1. **Caractérisation formelle de l'hyperplan :**
   Soit $H$ un hyperplan de $\mathcal{M}_n(\mathbb{R})$. Par définition, $H$ est le noyau d'une forme linéaire non nulle $\phi : \mathcal{M}_n(\mathbb{R}) \to \mathbb{R}$.

2. **Lemme de représentation matricielle (Produit scalaire de Frobenius) :**
   Toute forme linéaire sur $\mathcal{M}_n(\mathbb{R})$ peut s'exprimer par l'intermédiaire de la trace. Il existe une unique matrice $A \in \mathcal{M}_n(\mathbb{R})$, non nulle, telle que pour toute matrice $M$, $\phi(M) = \text{Tr}(A^T M)$.
   Ainsi, $M \in H \iff \text{Tr}(A^T M) = 0$.

3. **Preuve de l'existence par l'absurde ou par construction :**
   Nous voulons montrer qu'il existe $M$ inversible telle que $\text{Tr}(A^T M) = 0$.
   Considérons le polynôme caractéristique d'une variable matrice. Plus directement, prenons un ensemble fini de matrices inversibles. La condition d'être non inversible (déterminant nul) définit une hypersurface algébrique dans l'espace des matrices (de dimension $n^2-1$), tandis que l'hyperplan vectoriel est de dimension $n^2-1$.
   Puisque l'hyperplan $H$ est un espace vectoriel sur $\mathbb{R}$, il est non borné et connexe. Le sous-ensemble des matrices singulières $S = \{M \in \mathcal{M}_n(\mathbb{R}) \mid \det(M) = 0\}$ est une hypersurface de degré $n$.
   L'intersection $H \cap S$ est un sous-ensemble algébrique propre de $H$. Un polynôme non nul ne peut s'annuler sur un espace vectoriel entier. La seule exception serait si le polynôme déterminant s'annulait identiquement sur l'hyperplan, ce qui est impossible (un espace vectoriel de dimension $n^2-1 > n^2-n$ pour $n \ge 2$ ne peut être totalement contenu dans l'hypersurface de déterminant nul).
   Il existe donc de manière dense des matrices dans $H$ qui n'appartiennent pas à $S$.

**Conclusion :**
Tout hyperplan vectoriel de l'espace des matrices (dimension $n^2$) est trop vaste pour être confiné au cône des matrices singulières. Il coupe nécessairement le groupe linéaire $GL_n(\mathbb{R})$.
