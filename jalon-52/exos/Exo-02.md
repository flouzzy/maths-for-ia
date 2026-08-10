---
title: "Homéomorphisme entre intervalles ouverts"
difficulty: $\bigstar\bigstar\star\star\star$
---

# Exercice 02 : Homéomorphisme entre intervalles ouverts
**Difficulté :** $\bigstar\bigstar\star\star\star$

**Énoncé :**
Montrer que les espaces topologiques $X = ]0, 1[$ et $Y = ]a, b[$ (avec $a < b$ des réels), munis de la topologie usuelle induite par $\mathbb{R}$, sont homéomorphes.
En déduire une fonction explicite qui réalise cet homéomorphisme.

**Correction Détaillée :**
L'objectif est de trouver une fonction affine $f : ]0, 1[ \to ]a, b[$ telle que $f(0)=a$ et $f(1)=b$ en passant aux limites.
Posons $f(x) = a + x(b-a)$.
1. **Bijectivité :** Pour tout $y \in ]a, b[$, résolvons $y = a + x(b-a)$.
$$ x = \frac{y-a}{b-a} $$
Puisque $a < y < b$, on a $0 < y-a < b-a$, donc $0 < \frac{y-a}{b-a} < 1$, donc $x \in ]0, 1[$. La solution est unique, $f$ est bijective.
2. **Continuité de $f$ :** $f$ est une fonction polynomiale (affine) de domaine $\mathbb{R}$, restreinte à $]0, 1[$. Elle est continue.
3. **Continuité de l'inverse :** La fonction $f^{-1}(y) = \frac{y-a}{b-a}$ est également affine sur $\mathbb{R}$, donc continue.
Conclusion : $f$ définit un homéomorphisme explicite, et les intervalles ouverts $]0, 1[$ et $]a, b[$ sont homéomorphes.
