---
title: "Homéomorphisme entre ℝ et l'intervalle ouvert ]-1, 1["
difficulty: $\bigstar\bigstar\bigstar\star\star$
---

# Exercice 04 : Homéomorphisme entre ℝ et l'intervalle ouvert ]-1, 1[
**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
On considère la fonction $f : \mathbb{R} \to ]-1, 1[$ définie par $f(x) = \frac{x}{1+|x|}$.
Montrer que $f$ établit un homéomorphisme de $\mathbb{R}$ vers $]-1, 1[$.

**Correction Détaillée :**
1. **Bijectivité :** Soit $y \in ]-1, 1[$. Nous cherchons $x \in \mathbb{R}$ tel que $y = \frac{x}{1+|x|}$.
- Si $y \ge 0$, alors $x \ge 0$. L'équation devient $y = \frac{x}{1+x}$, d'où $y(1+x) = x \implies x(1-y) = y \implies x = \frac{y}{1-y}$.
- Si $y < 0$, alors $x < 0$. L'équation devient $y = \frac{x}{1-x}$, d'où $y(1-x) = x \implies x(1+y) = y \implies x = \frac{y}{1+y}$.
Ces deux expressions peuvent être unifiées sous la forme $f^{-1}(y) = \frac{y}{1-|y|}$. La solution est unique pour tout $y$, $f$ est bijective.
2. **Continuité de $f$ :** La fonction $x \mapsto 1+|x|$ est continue et ne s'annule jamais sur $\mathbb{R}$ (elle est toujours $\ge 1$). La fonction $f$ est donc le quotient d'une fonction continue et d'une fonction continue non nulle. Elle est continue.
3. **Continuité de $f^{-1}$ :** De même, l'expression $f^{-1}(y) = \frac{y}{1-|y|}$ ne présente aucune annulation au dénominateur sur $]-1, 1[$ puisque $|y| < 1 \implies 1-|y| > 0$. $f^{-1}$ est donc continue.
Par conséquent, $\mathbb{R}$ et $]-1, 1[$ sont homéomorphes, prouvant que la "taille infinie" n'est pas un invariant topologique.
