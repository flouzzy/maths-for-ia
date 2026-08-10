---
uuid: "jalon-53-exo-1"
title: "Unicité de la limite dans un espace de Hausdorff"
---

## Exercice 1 : Unicité de la limite dans un espace de Hausdorff \quad $\bigstar\star\star\star\star$


**Énoncé :**
Soit $(X, \mathcal{T})$ un espace topologique. Montrer que $X$ est un espace de Hausdorff ($T_2$) si et seulement si, pour toute suite $(x_n)_{n \in \mathbb{N}}$ convergente dans $X$, sa limite est unique.

**Correction Détaillée :**
1. **Sens direct ($\implies$) :** Supposons $X$ Hausdorff. Soit $(x_n)$ une suite convergeant vers $L_1$ et $L_2$. Si $L_1 \neq L_2$, par séparation $T_2$, il existe des ouverts $U$ et $V$ disjoints tels que $L_1 \in U$ et $L_2 \in V$. La convergence implique qu'il existe $N_1$ tel que $\forall n \ge N_1, x_n \in U$ et $N_2$ tel que $\forall n \ge N_2, x_n \in V$. Pour $n \ge \max(N_1, N_2)$, $x_n \in U \cap V$, ce qui contredit $U \cap V = \emptyset$. Donc $L_1 = L_2$.
2. **Sens réciproque ($\impliedby$) (Remarque) :** En toute rigueur, l'implication réciproque est vraie pour les espaces à bases dénombrables de voisinages (espaces métriques par exemple). Dans un espace topologique général, l'unicité de la limite des suites ne suffit pas toujours à garantir la séparation $T_2$ (il faut utiliser des filtres ou des suites généralisées). Néanmoins, le fait que $T_2$ implique l'unicité de la limite des suites est le théorème fondamental à retenir.
