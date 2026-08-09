---
title: "Exo-05 : Distances équivalentes et normes"
difficulty: "$\bigstar\bigstar\bigstar\star\star$"
---

# Exo-05 : Distances équivalentes et normes


## 1. Énoncé

Dans $\mathbb{R}^2$, on considère les trois distances usuelles induites par les normes correspondantes :
- $d_1(x, y) = |x_1 - y_1| + |x_2 - y_2|$
- $d_2(x, y) = \sqrt{(x_1 - y_1)^2 + (x_2 - y_2)^2}$
- $d_\infty(x, y) = \max(|x_1 - y_1|, |x_2 - y_2|)$

Démontrer, en revenant aux définitions et sans utiliser le théorème d'équivalence des normes en dimension finie, que $d_1$ et $d_\infty$ sont topologiquement équivalentes à $d_2$.

## 2. Correction détaillée

Nous devons trouver des constantes d'encadrement pour montrer l'équivalence forte des distances.
Posons $a = |x_1 - y_1|$ et $b = |x_2 - y_2|$.

**Comparaison $d_\infty$ et $d_1$ :**
$d_\infty = \max(a, b)$ et $d_1 = a + b$.
D'une part, $a \le \max(a, b)$ et $b \le \max(a, b)$, donc $a + b \le 2 \max(a, b)$. Soit $d_1 \le 2 d_\infty$.
D'autre part, $a \le a + b$ et $b \le a + b$ (puisque $a, b \ge 0$), donc $\max(a, b) \le a + b$. Soit $d_\infty \le d_1$.
Ainsi, $d_\infty \le d_1 \le 2 d_\infty$.

**Comparaison $d_2$ et $d_\infty$ :**
$d_2^2 = a^2 + b^2$.
D'une part, $a^2 \le (\max(a,b))^2$ et $b^2 \le (\max(a,b))^2$, donc $a^2 + b^2 \le 2(\max(a,b))^2$. En prenant la racine, $d_2 \le \sqrt{2} d_\infty$.
D'autre part, $\max(a^2, b^2) \le a^2 + b^2$, et la fonction racine est croissante, donc $\max(a, b) = \sqrt{\max(a^2, b^2)} \le \sqrt{a^2 + b^2}$. Soit $d_\infty \le d_2$.
Ainsi, $d_\infty \le d_2 \le \sqrt{2} d_\infty$.

**Conclusion :**
Les distances vérifient des inégalités du type $C_1 d_A(x,y) \le d_B(x,y) \le C_2 d_A(x,y)$. Elles induisent donc les mêmes ouverts, c'est-à-dire la même topologie sur $\mathbb{R}^2$.
