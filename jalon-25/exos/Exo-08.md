---
title: "Exercice 8 : Produit scalaire sur l'espace des matrices M_n(R)"
difficulty: 4
---

### Exercice 8 : Produit scalaire sur les polynômes
**Niveau : \star \star \star \star**

**Énoncé :**
Sur $\mathbb{R}_2[X]$, on définit $\phi(P, Q) = P(-1)Q(-1) + P(0)Q(0) + P(1)Q(1)$.
1. Prouver que $\phi$ est un produit scalaire.
2. Trouver une base orthonormale de $\mathbb{R}_2[X]$ par Gram-Schmidt à partir de $(1, X, X^2)$.

**Correction (Zéro Ellipse) :**
1. Symétrie et bilinéarité évidentes. Positivité : $\phi(P, P) = P(-1)^2 + P(0)^2 + P(1)^2 \ge 0$.
Définie : Si $\phi(P, P) = 0$, alors $P(-1)=0$, $P(0)=0$ et $P(1)=0$. Un polynôme de degré $\le 2$ admettant 3 racines distinctes est nul. Donc $P = 0$. $\phi$ est un produit scalaire.
2. Procédé de Gram-Schmidt :
   *   $e_1 = \frac{1}{\|1\|}$. On a $\|1\|^2 = 3$, donc $e_1 = \frac{1}{\sqrt{3}}$.
   *   $u_2 = X - \langle X, e_1 \rangle e_1$. $\langle X, e_1 \rangle = (-1)\frac{1}{\sqrt{3}} + (0)\frac{1}{\sqrt{3}} + (1)\frac{1}{\sqrt{3}} = 0$. Donc $u_2 = X$. $\|X\|^2 = 2 \implies e_2 = \frac{X}{\sqrt{2}}$.
   *   $u_3 = X^2 - \langle X^2, e_1 \rangle e_1 - \langle X^2, e_2 \rangle e_2$.
       $\langle X^2, e_1 \rangle = \frac{2}{\sqrt{3}}$.
       $\langle X^2, e_2 \rangle = 0$.
       Donc $u_3 = X^2 - \frac{2}{3}$.
       $\|u_3\|^2 = \frac{1}{9} + \frac{4}{9} + \frac{1}{9} = \frac{2}{3}$.
       Alors $e_3 = \sqrt{\frac{3}{2}} (X^2 - \frac{2}{3})$.
La base orthonormale est $( \frac{1}{\sqrt{3}}, \frac{X}{\sqrt{2}}, \sqrt{\frac{3}{2}}(X^2 - \frac{2}{3}) )$.
