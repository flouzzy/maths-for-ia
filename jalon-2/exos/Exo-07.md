# Exercice 7 - Difficulté: Niveau 4

## 1. Énoncé
Soient $a, b \in \mathbb{R}^n$. Démontrer l'inégalité de Cauchy-Schwarz par étude d'un trinôme.

## 2. Démonstration (Zéro Ellipse)
Soient $a = (a_1, \dots, a_n) \in \mathbb{R}^n$ et $b = (b_1, \dots, b_n) \in \mathbb{R}^n$. On considère le polynôme $P(t) = \sum_{i=1}^n (a_i + tb_i)^2$. Pour tout $t \in \mathbb{R}$, $P(t) \ge 0$ (somme de carrés). Développons $P(t) : P(t) = \sum_{i=1}^n (a_i^2 + 2ta_ib_i + t^2b_i^2) = (\sum_{i=1}^n b_i^2)t^2 + 2(\sum_{i=1}^n a_ib_i)t + (\sum_{i=1}^n a_i^2)$. Posons $A = \sum b_i^2$, $B = 2\sum a_ib_i$, $C = \sum a_i^2$. On a $P(t) = At^2 + Bt + C$. Si $A = 0$, $b=0$, l'inégalité $0 \le 0$ est triviale. Si $A \neq 0$, le trinôme garde le même signe (positif) pour tout $t$, ce qui signifie que son discriminant est négatif ou nul : $\Delta = B^2 - 4AC \le 0$. Ainsi, $(2\sum a_ib_i)^2 - 4(\sum b_i^2)(\sum a_i^2) \le 0$, d'où $(\sum a_ib_i)^2 \le (\sum b_i^2)(\sum a_i^2)$.
