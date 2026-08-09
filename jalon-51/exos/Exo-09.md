---
title: "Exo-09 : Topologie d'un espace ultramétrique"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\bigstar$"
---

# Exo-09 : Topologie d'un espace ultramétrique


## 1. Énoncé

Soit $(X, d)$ un espace métrique vérifiant l'inégalité ultramétrique :
$$\forall x, y, z \in X, \quad d(x, z) \le \max(d(x, y), d(y, z))$$

1. Soit $B(a, r)$ une boule ouverte. Montrer que pour tout $b \in B(a, r)$, on a $B(b, r) = B(a, r)$. (Tout point de la boule en est un centre).
2. Montrer que toute boule ouverte est également un ensemble fermé.
3. Deux boules d'un tel espace sont soit disjointes, soit l'une est incluse dans l'autre. Démontrer cette propriété.

## 2. Correction détaillée

**Question 1 :**
Soit $b \in B(a, r)$, c'est-à-dire $d(a, b) < r$.
- Si $x \in B(b, r)$, alors $d(b, x) < r$.
  Par l'inégalité ultramétrique : $d(a, x) \le \max(d(a, b), d(b, x)) < r$. Donc $x \in B(a, r)$. D'où $B(b, r) \subset B(a, r)$.
- Inversement, si $x \in B(a, r)$, alors $d(a, x) < r$.
  $d(b, x) \le \max(d(b, a), d(a, x))$. Or $d(b, a) = d(a, b) < r$, donc $d(b, x) < r$. D'où $x \in B(b, r)$. Ainsi $B(a, r) \subset B(b, r)$.
Conclusion : $B(a, r) = B(b, r)$.

**Question 2 :**
Montrons que le complémentaire de $B(a, r)$ est un ouvert.
Soit $y \notin B(a, r)$, c'est-à-dire $d(a, y) \ge r$.
Montrons que la boule $B(y, r)$ ne coupe pas $B(a, r)$.
Supposons par l'absurde qu'il existe $z \in B(y, r) \cap B(a, r)$.
Alors $d(y, z) < r$ et $d(a, z) < r$.
Par l'inégalité ultramétrique : $d(a, y) \le \max(d(a, z), d(z, y)) < r$.
Cela contredit $d(a, y) \ge r$.
Ainsi $B(y, r) \subset X \setminus B(a, r)$. Le complémentaire est ouvert, donc la boule ouverte est fermée. (L'espace est dit totalement discontinu).

**Question 3 :**
Soient $B_1 = B(x_1, r_1)$ et $B_2 = B(x_2, r_2)$. Supposons $r_1 \le r_2$.
Si $B_1 \cap B_2 \neq \emptyset$, il existe $z$ dans l'intersection.
D'après la Q1, on peut recentrer les boules en $z$ :
$B_1 = B(z, r_1)$ et $B_2 = B(z, r_2)$.
Puisque $r_1 \le r_2$, la définition implique immédiatement que $B(z, r_1) \subset B(z, r_2)$.
Donc $B_1 \subset B_2$. Si elles s'intersectent, l'une est incluse dans l'autre.
