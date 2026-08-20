## Fonction monotone et mesurabilité \quad $\bigstar\bigstar\bigstar\star\star$

Démontrez que toute fonction croissante $f : \mathbb{R} \to \mathbb{R}$ est borélienne.

### Correction Détaillée

Soit $f : \mathbb{R} \to \mathbb{R}$ une fonction croissante (c'est-à-dire $x \leq y \implies f(x) \leq f(y)$).
Il suffit de démontrer que pour tout réel $a$, l'ensemble $A_a = f^{-1}(]a, +\infty[) = \{x \in \mathbb{R} \mid f(x) > a\}$ est un borélien.

Soit $a \in \mathbb{R}$. Considérons l'ensemble $A_a$.
Deux cas peuvent se présenter :
1. $A_a$ est vide (si $f(x) \leq a$ pour tout $x$). Dans ce cas, $A_a = \emptyset \in \mathcal{B}(\mathbb{R})$.
2. $A_a$ n'est pas vide. Il existe donc au moins un point $x_0$ tel que $f(x_0) > a$.
   Puisque $f$ est croissante, pour tout $x \geq x_0$, on a $f(x) \geq f(x_0) > a$.
   Par conséquent, si un point appartient à $A_a$, tous les points à sa droite appartiennent également à $A_a$.
   Géométriquement, cela implique que l'ensemble $A_a$ est nécessairement soit un intervalle semi-ouvert $]c, +\infty[$, soit un intervalle fermé $[c, +\infty[$ (où $c = \inf A_a$, pouvant valoir $-\infty$).

Dans tous les cas possibles, $A_a$ est un intervalle.
Tout intervalle de $\mathbb{R}$ appartient à la tribu de Borel $\mathcal{B}(\mathbb{R})$.
Donc, l'image réciproque par $f$ de tout intervalle du type $]a, +\infty[$ est un borélien.
Puisque ces demi-droites engendrent la tribu borélienne, on en déduit que $f$ est borélienne.
