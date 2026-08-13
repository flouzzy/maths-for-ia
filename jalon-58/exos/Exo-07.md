---
uuid: "jalon-58-exo-07"
title: "Exercice 07 : Convergence des polynômes"
---

## Convergence des polynômes \quad $\bigstar\bigstar\bigstar\bigstar\star$

Soit $(P_n)$ une suite de polynômes qui converge simplement sur $\mathbb{R}$ vers une fonction $f$. Montrer qu'il existe un intervalle ouvert non vide sur lequel la suite des degrés des $P_n$ est bornée.

## Correction Détaillée (Zéro Ellipse)


1. Par hypothèse, pour tout $x \in \mathbb{R}$, la suite $(P_n(x))$ converge. Donc, en particulier, elle est bornée.
2. Posons $F_m = \{x \in \mathbb{R} \mid \sup_n |P_n(x)| \leq m\}$. Les $F_m$ sont des fermés et $\bigcup_{m} F_m = \mathbb{R}$.
3. Par Baire, il existe $M$ tel que $F_M$ contient un intervalle ouvert non vide $I = ]a, b[$.
4. Donc, pour tout $n$, et tout $x \in I$, $|P_n(x)| \leq M$.
5. Un polynôme borné sur un intervalle non vide ne peut pas avoir un degré arbitrairement grand sans que ses coefficients (et donc la borne) n'explosent, à l'exception du polynôme nul.
6. (Variante plus directe du problème souvent posé): Si $(P_n)$ converge ponctuellement vers 0, on peut montrer par Baire que, ponctuellement à partir d'un certain rang les $P_n$ sont identiques, etc.
