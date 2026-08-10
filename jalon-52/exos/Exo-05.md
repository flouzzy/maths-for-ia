---
title: "Cercle et droite : Absence d'homéomorphisme"
difficulty: $\bigstar\bigstar\bigstar\star\star$
---

# Exercice 05 : Cercle et droite : Absence d'homéomorphisme
**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $S^1 = \{ (x,y) \in \mathbb{R}^2 \mid x^2+y^2=1 \}$ le cercle unité avec la topologie trace de $\mathbb{R}^2$, et $\mathbb{R}$ la droite réelle usuelle.
Démontrer par l'absurde que $S^1$ et $\mathbb{R}$ ne sont pas homéomorphes en utilisant les propriétés topologiques conservées par homéomorphisme.

**Correction Détaillée :**
Supposons par l'absurde qu'il existe un homéomorphisme $f : S^1 \to \mathbb{R}$.
1. La notion de compacité est un invariant topologique.
2. Le cercle $S^1 \subset \mathbb{R}^2$ est fermé et borné, il est donc compact d'après le théorème de Borel-Lebesgue (ou Heine-Borel).
3. L'image d'un compact par une application continue est un compact.
4. Donc $f(S^1)$ doit être un compact de $\mathbb{R}$. Puisque $f$ est bijective sur $\mathbb{R}$, $f(S^1) = \mathbb{R}$.
5. Or, $\mathbb{R}$ n'est pas compact (il n'est pas borné).
C'est une contradiction. Donc, $S^1$ et $\mathbb{R}$ ne sont pas homéomorphes.
*(On peut aussi utiliser la connexité : retirer un point de $\mathbb{R}$ donne deux composantes connexes, alors que retirer un point de $S^1$ préserve la connexité).*
