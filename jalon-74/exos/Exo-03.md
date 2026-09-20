# Exercice 3 : Hölder en dimension finie

**Difficulté :** ★★☆☆☆


## Énoncé
Dans $\mathbb{R}^2$, soient $u = (2, 4)$ et $v = (3, 1)$. Posons $p=1$ et $q=\infty$.
1. Calculer $\|u\|_1$ et $\|v\|_\infty$.
2. Calculer le produit ponctuel $u \cdot v$ (terme à terme) et sa norme $\|\cdot\|_1$.
3. Vérifier l'inégalité de Hölder pour ces valeurs.

## Correction Détaillée
1. Calcul des normes :
- Norme $L^1$ de $u$ : $\|u\|_1 = |2| + |4| = 6$.
- Norme $L^\infty$ de $v$ : $\|v\|_\infty = \max(|3|, |1|) = 3$.

2. Produit ponctuel et sa norme :
- Produit scalaire terme à terme : $u \cdot v = (2 \times 3, 4 \times 1) = (6, 4)$.
- Norme $L^1$ du produit : $\|u \cdot v\|_1 = |6| + |4| = 10$.

3. Vérification de Hölder :
Le théorème affirme que $\|u \cdot v\|_1 \le \|u\|_1 \times \|v\|_\infty$.
Ici, $\|u \cdot v\|_1 = 10$.
Et $\|u\|_1 \times \|v\|_\infty = 6 \times 3 = 18$.
L'inégalité $10 \le 18$ est donc strictement vérifiée.
