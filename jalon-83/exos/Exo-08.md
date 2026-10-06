---
uuid: jalon-83-exo-08
title: "Exercice 08 - Dérivation des distributions"
---

# Exercice 08 $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit la fonction "partie fractionnaire" définie par $f(x) = x - \lfloor x \rfloor$, où $\lfloor x \rfloor$ est la partie entière.
1. Tracer le graphe de $f$ sur $[-2, 2]$.
2. Trouver l'expression de la dérivée usuelle $\{f'\}$.
3. Localiser les discontinuités de $f$ et calculer les sauts associés.
4. En déduire la dérivée de $f$ au sens des distributions et faire apparaître le Peigne de Dirac $\text{Ш} = \sum_{k \in \mathbb{Z}} \delta_k$.

**Correction pas à pas :**
1. La fonction $f(x) = x - \lfloor x \rfloor$ correspond à la "dents de scie". Sur l'intervalle $[k, k+1[$ (pour $k \in \mathbb{Z}$), $f(x) = x - k$. Le graphe est une succession de segments de pente 1, qui montent de 0 à 1, puis retombent brutalement à 0 pour chaque entier.

2. Sur chaque intervalle ouvert $]k, k+1[$, la fonction est affine de pente 1. Donc la dérivée usuelle (là où elle existe) est constante : $\{f'\}(x) = 1$. Soit la fonction constante égale à 1.

3. La fonction est discontinue à chaque entier $k \in \mathbb{Z}$.
Calculons la limite à gauche et à droite en $x = k$ :
- À droite : $f(k^+) = k - \lfloor k \rfloor = k - k = 0$.
- À gauche : $f(k^-) = \lim_{x \to k^-} (x - (k-1)) = k - k + 1 = 1$.
Le saut en chaque entier $k$ est donc :
$$ \sigma_k = f(k^+) - f(k^-) = 0 - 1 = -1 $$

4. Appliquons la formule des sauts généralisée à une infinité dénombrable de points de discontinuité. La somme des sauts est une somme infinie (série de distributions), dont la convergence est assurée car sur tout compact, le nombre de sauts est fini.
$$ f' = \{f'\} + \sum_{k \in \mathbb{Z}} \sigma_k \delta_k $$
$$ f' = 1 + \sum_{k \in \mathbb{Z}} (-1) \delta_k $$
$$ f' = 1 - \sum_{k \in \mathbb{Z}} \delta_k = 1 - \text{Ш} $$
La dérivée distributionnelle de la dent de scie est donc la constante 1, moins un train d'impulsions (Peigne de Dirac) aux entiers. $\blacksquare$
