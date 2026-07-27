---
title: "Exercice 1 : Produit scalaire canonique et inégalité triangulaire dans $\mathbb{R}^n$"
difficulty: 1
---

### Exercice 1 : Produit scalaire canonique et propriétés fondamentales
**Niveau : \star**

**Énoncé :**
Soit $E = \mathbb{R}^3$. On considère les vecteurs $u = (1, -2, 3)$ et $v = (2, 1, -1)$.
1. Calculer le produit scalaire canonique $\langle u, v \rangle$.
2. Calculer les normes $\|u\|$ et $\|v\|$.
3. Vérifier explicitement l'inégalité de Cauchy-Schwarz sur ces vecteurs.

**Correction (Zéro Ellipse) :**
1. Le produit scalaire canonique sur $\mathbb{R}^3$ est donné par $\langle x, y \rangle = x_1 y_1 + x_2 y_2 + x_3 y_3$.
Ainsi :
\[ \langle u, v \rangle = (1)(2) + (-2)(1) + (3)(-1) = 2 - 2 - 3 = -3 \]
2. La norme est induite par le produit scalaire : $\|x\| = \sqrt{\langle x, x \rangle}$.
Pour $u$ :
\[ \|u\|^2 = 1^2 + (-2)^2 + 3^2 = 1 + 4 + 9 = 14 \implies \|u\| = \sqrt{14} \]
Pour $v$ :
\[ \|v\|^2 = 2^2 + 1^2 + (-1)^2 = 4 + 1 + 1 = 6 \implies \|v\| = \sqrt{6} \]
3. Évaluons les termes de l'inégalité de Cauchy-Schwarz $| \langle u, v \rangle | \le \|u\| \|v\|$.
D'une part, la valeur absolue du produit scalaire est $| -3 | = 3$.
D'autre part, le produit des normes est $\sqrt{14} \sqrt{6} = \sqrt{84}$.
Puisque $84 > 9$, la fonction racine carrée étant croissante, $\sqrt{84} > \sqrt{9} = 3$.
On a bien $3 \le \sqrt{84}$, l'inégalité de Cauchy-Schwarz est numériquement confirmée de manière rigoureuse.
