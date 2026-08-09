---
title: "Exo-03 : L'ultramétrique p-adique"
difficulty: "$\bigstar\bigstar\star\star\star$"
---

# Exo-03 : L'ultramétrique p-adique


## 1. Énoncé

Soit $p$ un nombre premier. Pour tout $n \in \mathbb{Z}^*$, on définit la valuation $p$-adique $v_p(n)$ comme le plus grand entier $k$ tel que $p^k$ divise $n$. On pose $v_p(0) = +\infty$.
On définit sur $\mathbb{Z}$ la distance $d_p(x, y) = p^{-v_p(x - y)}$ si $x \neq y$, et $0$ sinon.

1. Calculer $d_3(10, 1)$ et $d_3(28, 1)$.
2. Démontrer l'inégalité ultramétrique : $d_p(x, z) \le \max(d_p(x, y), d_p(y, z))$.
3. En déduire que $d_p$ vérifie l'inégalité triangulaire classique.

## 2. Correction détaillée

**Question 1 :**
- Pour $x=10, y=1$ : $x-y = 9$. On cherche la plus grande puissance de $3$ divisant $9$. C'est $3^2$. Donc $v_3(9) = 2$.
  Ainsi, $d_3(10, 1) = 3^{-2} = \frac{1}{9}$.
- Pour $x=28, y=1$ : $x-y = 27 = 3^3$. Donc $v_3(27) = 3$.
  Ainsi, $d_3(28, 1) = 3^{-3} = \frac{1}{27}$.

**Question 2 :**
Soient $x, y, z \in \mathbb{Z}$. Si l'un des écarts est nul, l'inégalité est triviale. Supposons-les distincts.
On pose $a = x - y$ et $b = y - z$. Alors $x - z = a + b$.
Montrons d'abord que $v_p(a + b) \ge \min(v_p(a), v_p(b))$.
Soit $k_1 = v_p(a)$ et $k_2 = v_p(b)$. On a $a = p^{k_1} q_1$ et $b = p^{k_2} q_2$.
Soit $m = \min(k_1, k_2)$. On peut factoriser par $p^m$ :
$a + b = p^m (p^{k_1-m} q_1 + p^{k_2-m} q_2)$. Le terme entre parenthèses est un entier.
Donc $p^m$ divise $a+b$, d'où $v_p(a+b) \ge m = \min(v_p(a), v_p(b))$.
Ainsi, $v_p(x - z) \ge \min(v_p(x - y), v_p(y - z))$.
En passant à l'opposé et à l'exponentielle de base $p$ (fonction décroissante pour les exposants négatifs) :
$p^{-v_p(x - z)} \le p^{-\min(v_p(x - y), v_p(y - z))} = \max(p^{-v_p(x - y)}, p^{-v_p(y - z)})$.
Soit $d_p(x, z) \le \max(d_p(x, y), d_p(y, z))$.

**Question 3 :**
Pour tout couple de réels positifs $A, B$, on a trivialement $\max(A, B) \le A + B$.
Ainsi, $d_p(x, z) \le \max(d_p(x, y), d_p(y, z)) \le d_p(x, y) + d_p(y, z)$.
L'inégalité triangulaire est donc satisfaite, et $d_p$ est une distance.
