---
uuid: "jalon-66-exo-01"
title: "Exercice 1 - Jalon 66"
difficulty: "$\bigstar\star\star\star\star$"
---

# Exercice 1 : Calcul élémentaire pour une fonction simple

**Énoncé :**
On considère l'espace mesurable $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ muni de la mesure de Lebesgue $\lambda$.
Soit la fonction $f : \mathbb{R} \to \mathbb{R}$ définie par :
$$f(x) = 2 \cdot \mathbf{1}_{[0, 3]}(x) + 4 \cdot \mathbf{1}_{]3, 5]}(x) + 7 \cdot \mathbf{1}_{\{6\}}(x)$$
Calculer rigoureusement l'intégrale de Lebesgue $\int_{\mathbb{R}} f \, d\lambda$.

**Corrigé :**
La fonction $f$ est une fonction simple positive (étagée). Elle prend un nombre fini de valeurs (0, 2, 4, 7) et s'écrit comme une combinaison linéaire de fonctions indicatrices d'ensembles mesurables (des intervalles ou singletons de $\mathbb{R}$, qui sont bien des boréliens).

La définition de l'intégrale d'une fonction simple $s = \sum_{i=1}^n a_i \mathbf{1}_{A_i}$ est :
$$\int s \, d\lambda = \sum_{i=1}^n a_i \lambda(A_i)$$

Identifions les composantes de notre fonction $f$ :
- $a_1 = 2$, $A_1 = [0, 3]$
- $a_2 = 4$, $A_2 = ]3, 5]$
- $a_3 = 7$, $A_3 = \{6\}$

Calculons la mesure de Lebesgue de chaque ensemble :
- $\lambda(A_1) = \lambda([0, 3]) = 3 - 0 = 3$
- $\lambda(A_2) = \lambda(]3, 5]) = 5 - 3 = 2$
- $\lambda(A_3) = \lambda(\{6\}) = 0$ (la mesure de Lebesgue d'un singleton est nulle).

Nous pouvons maintenant calculer l'intégrale :
$$\int_{\mathbb{R}} f \, d\lambda = 2 \times \lambda([0, 3]) + 4 \times \lambda(]3, 5]) + 7 \times \lambda(\{6\})$$
$$\int_{\mathbb{R}} f \, d\lambda = 2 \times 3 + 4 \times 2 + 7 \times 0$$
$$\int_{\mathbb{R}} f \, d\lambda = 6 + 8 + 0 = 14$$

L'intégrale de $f$ par rapport à la mesure de Lebesgue vaut 14.
