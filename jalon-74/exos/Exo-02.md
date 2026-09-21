---
title: "Exercice 2 : Inégalité de Hölder matricielle"
difficulty: "$\bigstar\bigstar\star\star\star$"
---

# Exercice 2 : Inégalité de Hölder matricielle

## Énoncé
Soit l'espace $\mathbb{R}^3$ avec la mesure de comptage. Considérons les vecteurs $x = (1, -2, 3)$ et $y = (4, 0, -1)$.
Appliquer l'inégalité de Hölder avec $p=2, q=2$ et avec $p=1, q=\infty$.

## Corrigé
**Cas $p=2, q=2$ (Cauchy-Schwarz) :**
$| \sum x_i y_i | \le \|x\|_2 \|y\|_2$.
$\sum x_i y_i = 1(4) + (-2)(0) + 3(-1) = 4 - 3 = 1$. Donc $| \sum x_i y_i | = 1$.
$\|x\|_2 = \sqrt{1^2 + (-2)^2 + 3^2} = \sqrt{1+4+9} = \sqrt{14} \approx 3.74$.
$\|y\|_2 = \sqrt{4^2 + 0^2 + (-1)^2} = \sqrt{16+0+1} = \sqrt{17} \approx 4.12$.
$\|x\|_2 \|y\|_2 = \sqrt{14 \times 17} = \sqrt{238} \approx 15.42$. On a bien $1 \le 15.42$.

**Cas $p=1, q=\infty$ :**
$| \sum x_i y_i | \le \|x\|_1 \|y\|_\infty$.
$\|x\|_1 = |1| + |-2| + |3| = 1 + 2 + 3 = 6$.
$\|y\|_\infty = \max(|4|, |0|, |-1|) = 4$.
$\|x\|_1 \|y\|_\infty = 6 \times 4 = 24$.
On a bien $1 \le 24$.
