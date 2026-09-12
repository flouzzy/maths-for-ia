---
title: "Exercice 5 : Sous-additivité dénombrable de la mesure extérieure"
difficulty: "$\bigstar\bigstar\bigstar\star\star$"
---

## Énoncé

Démontrer que la mesure extérieure de Lebesgue est sous-additive dénombrable. C'est-à-dire que pour toute suite d'ensembles $(A_k)_{k \in \mathbb{N}^*}$ de $\mathcal{P}(\mathbb{R})$ :
$$\lambda^*\left( \bigcup_{k=1}^{+\infty} A_k \right) \le \sum_{k=1}^{+\infty} \lambda^*(A_k)$$

## Correction Détaillée

Si la série du membre de droite diverge vers $+\infty$, l'inégalité est trivialement satisfaite puisque $\lambda^* \le +\infty$. Supposons donc que la somme de la série soit finie, ce qui implique que pour chaque entier $k$, $\lambda^*(A_k) < +\infty$.

Soit $\epsilon > 0$ un réel strictement positif fixé arbitrairement.
Pour chaque sous-ensemble $A_k$, appliquons la définition de la mesure extérieure par recouvrement d'intervalles ouverts. Par caractérisation de la borne inférieure, il existe un recouvrement de $A_k$ par une suite dénombrable d'intervalles ouverts $(I_{k,j})_{j \in \mathbb{N}^*}$ tel que :
$$A_k \subset \bigcup_{j=1}^{+\infty} I_{k,j}$$
et dont la somme des longueurs majore la mesure extérieure d'une marge contrôlée. Pour s'assurer que la somme globale des marges d'erreur ne diverge pas, nous allons allouer à chaque $A_k$ une marge d'erreur géométriquement décroissante $\frac{\epsilon}{2^k}$ :
$$\sum_{j=1}^{+\infty} \ell(I_{k,j}) \le \lambda^*(A_k) + \frac{\epsilon}{2^k}$$

Posons $E = \bigcup_{k=1}^{+\infty} A_k$.
La famille de tous les intervalles $(I_{k,j})_{(k,j) \in (\mathbb{N}^*)^2}$ forme un ensemble dénombrable (produit de deux ensembles dénombrables). De plus, pour tout point $x \in E$, il existe un indice $k$ tel que $x \in A_k$, donc il existe un indice $j$ tel que $x \in I_{k,j}$.
Par conséquent, l'union dénombrable de tous ces intervalles forme bien un recouvrement ouvert global pour l'ensemble $E$ :
$$E \subset \bigcup_{k=1}^{+\infty} \bigcup_{j=1}^{+\infty} I_{k,j}$$

La mesure extérieure de $E$ étant l'infimum sur l'ensemble de tous les recouvrements possibles, elle est majorée par la somme des longueurs de ce recouvrement particulier. Les sommes étant à termes positifs, le théorème de Fubini pour les séries à termes positifs autorise l'interversion de sommation :
$$\lambda^*(E) \le \sum_{k=1}^{+\infty} \sum_{j=1}^{+\infty} \ell(I_{k,j})$$

Substituons la majoration de la somme interne par la mesure de chaque composante :
$$\lambda^*(E) \le \sum_{k=1}^{+\infty} \left( \lambda^*(A_k) + \frac{\epsilon}{2^k} \right)$$
Séparons la somme (les deux séries convergent) :
$$\lambda^*(E) \le \sum_{k=1}^{+\infty} \lambda^*(A_k) + \epsilon \sum_{k=1}^{+\infty} \frac{1}{2^k}$$

Nous reconnaissons la série géométrique $\sum_{k=1}^{+\infty} \frac{1}{2^k} = 1$. L'inégalité devient :
$$\lambda^*(E) \le \sum_{k=1}^{+\infty} \lambda^*(A_k) + \epsilon$$

L'inégalité algébrique obtenue lie des grandeurs indépendantes de $\epsilon$. Puisqu'elle est vraie pour tout $\epsilon > 0$ aussi petit que l'on veut, un passage rigoureux à la limite lorsque $\epsilon \to 0$ impose inéluctablement :
$$\lambda^*(E) \le \sum_{k=1}^{+\infty} \lambda^*(A_k)$$
Ce qui achève la démonstration complète de la sous-additivité dénombrable de la mesure extérieure sur $\mathcal{P}(\mathbb{R})$.
