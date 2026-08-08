## Exercice 1 : Distance ultramétrique \quad $\bigstar$

**Énoncé :** Soit $(X, d)$ un espace métrique tel que pour tout $(x, y, z) \in X^3$, $d(x, z) \le \max(d(x, y), d(y, z))$. Montrer que dans cet espace, tout triangle est isocèle.

**Correction :** Soient $x, y, z \in X$ distincts. Supposons sans perte de généralité que $d(x, y) \neq d(y, z)$. Par exemple, $d(x, y) < d(y, z)$.
Par l'inégalité ultramétrique, $d(x, z) \le \max(d(x, y), d(y, z)) = d(y, z)$.
D'autre part, en appliquant l'inégalité ultramétrique au triangle $y, x, z$, on obtient :
$d(y, z) \le \max(d(y, x), d(x, z)) = \max(d(x, y), d(x, z))$.
Puisque $d(x, y) < d(y, z)$, la seule possibilité pour que $\max(d(x, y), d(x, z))$ soit supérieur ou égal à $d(y, z)$ est que $\max(d(x, y), d(x, z)) = d(x, z)$.
Donc $d(y, z) \le d(x, z)$.
En combinant les deux inégalités, on obtient $d(x, z) = d(y, z)$. Ainsi, le triangle a au moins deux côtés égaux (isocèle).
