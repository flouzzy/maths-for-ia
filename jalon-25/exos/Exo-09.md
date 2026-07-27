---
title: "Exercice 9 : Optimisation sur l'hypercube via Cauchy-Schwarz"
difficulty: 5
---

### Exercice 9 : Distance à un sous-espace vectoriel
**Niveau : \star \star \star \star**

**Énoncé :**
Soit $E = \mathbb{R}^3$ muni du produit scalaire canonique. On note $F$ le plan d'équation $x + y + z = 0$.
Déterminer par projection orthogonale la distance du point $A(1, 2, 3)$ au plan $F$.

**Correction (Zéro Ellipse) :**
La distance d'un point à un hyperplan $H$ d'équation $\langle n, X \rangle = 0$ (où $n$ est un vecteur normal) est donnée par $d = \frac{|\langle n, A \rangle|}{\|n\|}$.
Ici, l'équation du plan est $\langle n, M \rangle = 0$ avec $n = (1, 1, 1)$ et $M = (x, y, z)$.
Le vecteur $n$ est bien un vecteur normal à $F$.
Calculons le produit scalaire : $\langle n, A \rangle = 1\times1 + 1\times2 + 1\times3 = 6$.
Calculons la norme : $\|n\| = \sqrt{1^2 + 1^2 + 1^2} = \sqrt{3}$.
La distance est donc $d = \frac{6}{\sqrt{3}} = 2\sqrt{3}$.
