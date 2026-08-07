# Exercice 10 - Niveau $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé
Caractériser topologiquement l'adhérence d'une boule ouverte dans un espace euclidien $\mathbb{R}^n$ par rapport à la boule fermée de même rayon.

## Démonstration
Soit $B(a, r)$ la boule ouverte de centre $a$ et de rayon $r > 0$ dans $\mathbb{R}^n$, définie par $\left\lbrace x \in \mathbb{R}^n \mid \|x - a\| < r \right\rbrace$.
Soit $F = \left\lbrace x \in \mathbb{R}^n \mid \|x - a\| \le r \right\rbrace$ la boule fermée.
Puisque la norme est une application continue, $F$ est un ensemble fermé contenant $B(a, r)$.
Donc, $\overline{B(a, r)} \subset F$.
Montrons que $F \subset \overline{B(a, r)}$.
Soit $x \in F$. Si $\|x - a\| < r$, alors $x \in B(a, r) \subset \overline{B(a, r)}$.
Si $\|x - a\| = r$, considérons la suite $(x_k)$ définie par $x_k = a + (1 - \frac{1}{k})(x - a)$ pour $k \ge 1$.
Alors $\|x_k - a\| = (1 - \frac{1}{k})r < r$, donc $x_k \in B(a, r)$.
De plus, la suite $(x_k)$ converge vers $x$ lorsque $k \to \infty$.
Ainsi, tout voisinage de $x$ contient des éléments $x_k$, donc rencontre $B(a, r)$.
Par conséquent, $x \in \overline{B(a, r)}$.
Ceci démontre que $\overline{B(a, r)} = F$, c'est-à-dire que l'adhérence de la boule ouverte est exactement la boule fermée dans $\mathbb{R}^n$.
