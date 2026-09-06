---
uuid: "exo-67-06"
title: "Exercice 06 : Théorème de Tonelli pour les séries"
difficulty: "$\bigstar\bigstar\bigstar\star\star$"
---

# Exercice 06 : Théorème de Tonelli pour les séries ($\bigstar\bigstar\bigstar\star\star$)

## Énoncé

Montrer que pour une fonction $f: \mathbb{N}^2 \to \mathbb{R}^+$, $\int_{\mathbb{N}^2} f d(\mu \otimes \nu) = \sum_n \sum_m f(n,m) = \sum_m \sum_n f(n,m)$.

## Corrigé Rigoureux

1. **Fonction indicatrice :** Il s'agit du théorème de Tonelli. Pour le prouver, on commence par une fonction $f = \mathbf{1}_{A \times B}$. Alors $\int f = \mu(A)\nu(B) = \sum_n \mathbf{1}_A(n) \sum_m \mathbf{1}_B(m) = \sum_n \sum_m f(n,m)$.
2. **Généralisation par linéarité :** Le résultat s'étend aux fonctions étagées positives par linéarité (somme finie de telles indicatrices).
3. **Passage à la limite (Beppo Levi) :** Toute fonction $f : \mathbb{N}^2 \to \mathbb{R}^+$ est la limite d'une suite croissante $(f_k)$ de fonctions étagées positives. Par le TCM, on a l'égalité des intégrales pour la limite.
$$\int \lim_k f_k = \lim_k \int f_k = \lim_k \sum_n \sum_m f_k(n,m)$$
Par double application de Beppo Levi sur les sommes (qui sont des intégrales par rapport à la mesure de comptage), on prouve l'égalité complète.
