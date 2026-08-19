# Exercice 2 : Sous-additivité stricte

**Difficulté :** $\displaystyle \\bigstar\\bigstar\\star$

## Énoncé

Trouver un exemple de suite d'ensembles $(A_n)$ où $\lambda^*(\bigcup A_n) < \sum \lambda^*(A_n)$ (inégalité stricte).

## Correction Détaillée

Pour avoir une inégalité stricte, il faut que les ensembles ne soient pas disjoints et aient une intersection de mesure non nulle.
Prenons $A_1 = [0, 2]$ et $A_2 = [1, 3]$.
On a $\lambda^*(A_1) = 2$ et $\lambda^*(A_2) = 2$. La somme est $\lambda^*(A_1) + \lambda^*(A_2) = 4$.
L'union est $A_1 \cup A_2 = [0, 3]$, dont la mesure extérieure est $\lambda^*([0, 3]) = 3$.
On a bien $3 < 4$. Cela montre que la mesure (extérieure) n'est additive que pour des ensembles disjoints.
