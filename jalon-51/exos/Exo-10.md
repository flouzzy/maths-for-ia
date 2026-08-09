---
title: "Exo-10 : Isométrie et plongement"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\bigstar$"
---

# Exo-10 : Isométrie et plongement


## 1. Énoncé

Soit $(X, d)$ un espace métrique. On note $\mathcal{B}(X)$ l'espace des fonctions bornées de $X$ dans $\mathbb{R}$, muni de la norme $\|f\|_\infty = \sup_{x \in X} |f(x)|$ et de la distance associée $d_\infty(f, g) = \|f - g\|_\infty$.
On fixe un point $a \in X$. Pour tout $x \in X$, on définit l'application $f_x : X \to \mathbb{R}$ par :
$$f_x(y) = d(x, y) - d(a, y)$$

1. Montrer que pour tout $x \in X$, $f_x \in \mathcal{B}(X)$.
2. Montrer que l'application $\Phi : X \to \mathcal{B}(X)$ définie par $\Phi(x) = f_x$ est une **isométrie**, c'est-à-dire que pour tous $x, z \in X$, $d_\infty(\Phi(x), \Phi(z)) = d(x, z)$.
3. Quel est l'intérêt topologique de ce théorème (dû à Kuratowski) ?

## 2. Correction détaillée

**Question 1 :**
Fixons $x \in X$. Pour tout $y \in X$, évaluons $|f_x(y)|$.
$|f_x(y)| = |d(x, y) - d(a, y)|$.
Par l'inégalité triangulaire inversée (démontrée dans le cours), on a :
$|d(x, y) - d(a, y)| \le d(x, a)$.
Cette majoration est indépendante de $y$.
Ainsi, $\sup_{y \in X} |f_x(y)| \le d(x, a) < +\infty$.
La fonction $f_x$ est donc bien bornée, elle appartient à $\mathcal{B}(X)$.

**Question 2 :**
Soient $x, z \in X$.
$d_\infty(\Phi(x), \Phi(z)) = \|f_x - f_z\|_\infty = \sup_{y \in X} |f_x(y) - f_z(y)|$.
Évaluons $f_x(y) - f_z(y)$ :
$f_x(y) - f_z(y) = (d(x, y) - d(a, y)) - (d(z, y) - d(a, y)) = d(x, y) - d(z, y)$.
Ainsi, on cherche $\sup_{y \in X} |d(x, y) - d(z, y)|$.
Par l'inégalité triangulaire inversée :
$|d(x, y) - d(z, y)| \le d(x, z)$.
Donc le supremum est majoré par $d(x, z)$. On a $d_\infty(\Phi(x), \Phi(z)) \le d(x, z)$.
Pour prouver l'égalité, montrons que la valeur $d(x, z)$ est atteinte pour un certain $y$.
Prenons $y = z$.
$|f_x(z) - f_z(z)| = |d(x, z) - d(z, z)| = |d(x, z) - 0| = d(x, z)$.
Le supremum est donc exactement atteint.
Par conséquent, $d_\infty(\Phi(x), \Phi(z)) = d(x, z)$. $\Phi$ est bien une isométrie.

**Question 3 :**
L'intérêt de ce théorème de Kuratowski est colossal : il prouve que **tout** espace métrique $(X, d)$ (aussi abstrait soit-il) peut être plongé isométriquement dans un espace de Banach (l'espace complet normé $\mathcal{B}(X)$).
Cela permet de traiter n'importe quel espace métrique comme une simple partie d'un espace vectoriel normé complet, facilitant ainsi les extensions géométriques de théorèmes abstraits.
