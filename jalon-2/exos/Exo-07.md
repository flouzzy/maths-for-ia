# Exercice 7 - Difficulté: Niveau 4

## 1. Énoncé
Soient $a, b \in \mathbb{R}^n$. Démontrer l'inégalité de Cauchy-Schwarz par étude d'un trinôme.

## 2. Démonstration (Zéro Ellipse)
Soient $a = (a_1, \dots, a_n) \in \mathbb{R}^n$ et $b = (b_1, \dots, b_n) \in \mathbb{R}^n$. On considère le polynôme $P(t) = \sum_{i=1}^n (a_i + tb_i)^2$.

Pour tout $t \in \mathbb{R}$, $P(t) \ge 0$ car il s'agit d'une somme de carrés de nombres réels.

Développons l'expression de $P(t)$ :
$P(t) = \sum_{i=1}^n (a_i^2 + 2ta_ib_i + t^2b_i^2) = \left(\sum_{i=1}^n b_i^2\right)t^2 + 2\left(\sum_{i=1}^n a_ib_i\right)t + \left(\sum_{i=1}^n a_i^2\right)$.

Posons les coefficients suivants :
- $A = \sum_{i=1}^n b_i^2$
- $B = 2\sum_{i=1}^n a_ib_i$
- $C = \sum_{i=1}^n a_i^2$

On a ainsi $P(t) = At^2 + Bt + C \ge 0$ pour tout $t \in \mathbb{R}$.

Distinguons deux cas selon la valeur de $A$ :

**Cas 1 : $A = 0$.**
Puisque $A = \sum_{i=1}^n b_i^2 = 0$ et qu'il s'agit d'une somme de termes positifs ou nuls ($b_i^2 \ge 0$), chaque terme doit être nul. Ainsi, pour tout $i \in \{1, \dots, n\}$, $b_i = 0$.
Par conséquent, $B = 2\sum_{i=1}^n a_ib_i = 2\sum_{i=1}^n a_i(0) = 0$.
L'inégalité que l'on cherche à démontrer est $B^2 \le 4AC$. Dans ce cas, nous avons $0^2 \le 4(0)C$, c'est-à-dire $0 \le 0$, ce qui est rigoureusement vrai. L'inégalité de Cauchy-Schwarz est donc vérifiée dans ce cas.

**Cas 2 : $A \neq 0$.**
Comme $A$ est une somme de carrés, $A \ge 0$. Puisque $A \neq 0$, nous avons strictement $A > 0$.
Le polynôme $P(t) = At^2 + Bt + C$ est un trinôme du second degré. Puisque ce trinôme est positif ou nul pour tout $t \in \mathbb{R}$ et que $A > 0$, cela implique nécessairement que son discriminant $\Delta$ est inférieur ou égal à zéro (sinon le trinôme admettrait deux racines réelles distinctes et changerait de signe).
Le discriminant s'écrit $\Delta = B^2 - 4AC$.
Nous obtenons donc l'inégalité : $\Delta \le 0 \iff B^2 - 4AC \le 0 \iff B^2 \le 4AC$.

En remplaçant $A, B$ et $C$ par leurs expressions respectives, on obtient :
$\left(2\sum_{i=1}^n a_ib_i\right)^2 \le 4\left(\sum_{i=1}^n b_i^2\right)\left(\sum_{i=1}^n a_i^2\right)$.

Ce qui se simplifie en divisant par 4 des deux côtés :
$\left(\sum_{i=1}^n a_ib_i\right)^2 \le \left(\sum_{i=1}^n b_i^2\right)\left(\sum_{i=1}^n a_i^2\right)$.

C'est exactement l'inégalité de Cauchy-Schwarz.
