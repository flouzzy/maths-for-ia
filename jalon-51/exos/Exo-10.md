# Exercice 10 : Boules dans un espace ultramétrique
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé formel
Dans un espace ultramétrique $(X, d)$, montrer que pour toute boule ouverte $B(a, r)$, tout point $b \in B(a, r)$ peut être considéré comme le centre de la boule, c'est-à-dire que $B(b, r) = B(a, r)$.

## Résolution pas à pas
**Étape 1 : Inclusion directe $B(b, r) \subset B(a, r)$**

Soit $x \in B(b, r)$. Cela signifie que $d(b, x) < r$.
Comme $b \in B(a, r)$, nous savons par définition que $d(a, b) < r$.
Appliquons l'inégalité ultramétrique pour évaluer la distance à $a$ :
$d(a, x) \le \max(d(a, b), d(b, x))$.
Puisque $d(a, b) < r$ et $d(b, x) < r$, leur maximum est strictement inférieur à $r$.
Donc $d(a, x) < r$, ce qui prouve que $x \in B(a, r)$.

**Étape 2 : Inclusion réciproque et conclusion**

Par la parfaite symétrie du problème, on a également $d(b, a) < r$, ce qui place $a$ dans la boule de centre $b$. En répétant la logique, $B(a, r) \subset B(b, r)$.
Ainsi, $B(a,r) = B(b,r)$. Dans une géométrie ultramétrique, chaque point intérieur d'une boule en est le centre. C'est une topologie radicalement différente de celle de notre espace euclidien usuel. $\blacksquare$
