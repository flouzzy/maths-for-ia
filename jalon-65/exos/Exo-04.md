---
uuid: "jalon-65-exo-04"
title: "Exercice 4 : Mesurabilité et limites"
difficulty: "$\bigstar\bigstar\bigstar\star\star$"
---

# Exercice 4 : Mesurabilité et limites

## Énoncé

Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables de $E$ vers $\overline{\mathbb{R}}$. Montrer en détail que l'ensemble $C = \{ x \in E \mid (f_n(x))_{n} \text{ converge dans } \overline{\mathbb{R}} \}$ est mesurable.

## Solution Détaillée

Une suite dans $\overline{\mathbb{R}}$ converge si et seulement si sa limite supérieure est égale à sa limite inférieure. Ainsi, $C = \{ x \in E \mid \limsup_{n \to \infty} f_n(x) = \liminf_{n \to \infty} f_n(x) \}$. Posons $g = \limsup_{n} f_n$ et $h = \liminf_{n} f_n$. Par les propriétés de stabilité des suites de fonctions mesurables, $g$ et $h$ sont mesurables. Considérons la fonction $\Delta(x) = g(x) - h(x)$ (bien définie car $h \le g$ sauf formes indéterminées traitées à part). $C$ correspond à l'ensemble où $g = h$. Ainsi, $C = (g-h)^{-1}(\{0\})$. Puisque $g$ et $h$ sont mesurables, la soustraction (quand elle est définie) l'est, et donc $C \in \mathcal{A}$. $\blacksquare$
