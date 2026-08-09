---
title: "Exercice 2 : Une fonction non-métrique"
---

### Exercice 2 : Une fonction non-métrique \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
On considère l'application $d : \mathbb{R} \times \mathbb{R} \to \mathbb{R}_+$ définie par $d(x, y) = (x - y)^2$. Démontrer que $d$ ne définit pas une distance sur $\mathbb{R}$.

**Correction Détaillée :**
Pour que $d$ soit une distance, elle doit vérifier l'inégalité triangulaire pour tout triplet de réels $(x, y, z)$ :
$$d(x, z) \le d(x, y) + d(y, z)$$
Ce qui équivaut ici à :
$$(x - z)^2 \le (x - y)^2 + (y - z)^2$$
Cherchons un contre-exemple. Prenons $x = 0$, $y = 1$ et $z = 2$.
Évaluons le membre de gauche :
$$d(0, 2) = (0 - 2)^2 = 4$$
Évaluons le membre de droite :
$$d(0, 1) + d(1, 2) = (0 - 1)^2 + (1 - 2)^2 = 1 + 1 = 2$$
On constate que $4$ n'est pas inférieur ou égal à $2$. L'inégalité triangulaire est donc mise en défaut. Par conséquent, l'application $d$ n'est pas une distance sur $\mathbb{R}$. L'élévation au carré pénalise de manière disproportionnée les grands écarts par rapport à la somme de petits écarts, rompant ainsi l'analogie géométrique du plus court chemin.
