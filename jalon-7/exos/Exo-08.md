---
uuid: "exo-7-8"
title: "Exo 8 - Jalon 7"
---

# Exercice 8 : Supplémentaires

## Énoncé
Soit $E = \mathbb{R}^3$. On considère le plan $P$ d'équation $x+y+z=0$ et la droite $D$ engendrée par le vecteur $u = (1, 1, 1)$.
Montrer que $P$ et $D$ sont supplémentaires dans $E$.

## Correction
Pour montrer que $E = P \oplus D$, on doit montrer deux choses :
1. $P \cap D = \{0_E\}$
2. $\dim(P) + \dim(D) = \dim(E)$

**Intersection :**
Soit $v \in P \cap D$.
Puisque $v \in D$, il existe $\lambda \in \mathbb{R}$ tel que $v = \lambda(1, 1, 1) = (\lambda, \lambda, \lambda)$.
Puisque $v \in P$, ses coordonnées vérifient l'équation de $P$ :
$x + y + z = 0 \implies \lambda + \lambda + \lambda = 0 \implies 3\lambda = 0 \implies \lambda = 0$.
Donc $v = (0, 0, 0)$. Ainsi $P \cap D = \{0_E\}$.

**Dimensions :**
$D$ est engendrée par un vecteur non nul, donc $\dim(D) = 1$.
L'équation $x+y+z=0$ définit le noyau de la forme linéaire non nulle $\varphi(x,y,z) = x+y+z$ sur $\mathbb{R}^3$. L'image de $\varphi$ est $\mathbb{R}$ (de dimension 1). Par le théorème du rang, $\dim(P) = \dim(\mathbb{R}^3) - \dim(\text{Im}(\varphi)) = 3 - 1 = 2$.
On a bien $\dim(P) + \dim(D) = 2 + 1 = 3 = \dim(\mathbb{R}^3)$.

**Conclusion :**
Les deux sous-espaces sont en somme directe et la somme de leurs dimensions vaut celle de l'espace total. Ils sont donc supplémentaires : $\mathbb{R}^3 = P \oplus D$.
