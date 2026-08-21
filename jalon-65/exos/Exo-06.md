---
uuid: "jalon-65-exo-06"
title: "Exercice 6 : Fonction étagée et partition"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

# Exercice 6 : Fonction étagée et partition

## Énoncé

Montrer que toute fonction étagée mesurable $s : E \to \mathbb{R}$ admet une unique représentation sous la forme $s = \sum_{i=1}^n \alpha_i \mathbb{1}_{A_i}$, où les $\alpha_i$ sont deux à deux distincts et les $A_i$ forment une partition mesurable de $E$.

## Solution Détaillée

Soit $s$ une fonction étagée mesurable. Soit $V = s(E) = \{\alpha_1, \alpha_2, \dots, \alpha_n\}$ l'ensemble fini des valeurs prises par $s$, que l'on ordonne $\alpha_1 < \alpha_2 < \dots < \alpha_n$. Posons $A_i = s^{-1}(\{\alpha_i\})$. Puisque $s$ est mesurable et que les singletons $\{\alpha_i\}$ sont des boréliens, les ensembles $A_i$ sont mesurables. De plus, comme tout $x \in E$ a une unique image $s(x) \in V$, les ensembles $A_i$ sont disjoints et leur réunion est $E$. Donc $(A_i)$ forme une partition mesurable de $E$. Pour tout $x \in E$, $x$ appartient à un unique $A_i$, donc $\sum_{j=1}^n \alpha_j \mathbb{1}_{A_j}(x) = \alpha_i = s(x)$. L'unicité découle de la stricte définition de la partition et des valeurs distinctes. $\blacksquare$
