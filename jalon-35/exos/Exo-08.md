# Exercice 8 : ★★★★

**Énoncé :**
Caractérisation d'un compact.

**Correction (Zéro Ellipse) :**
Dans un espace vectoriel normé de dimension finie, un ensemble $K$ est compact si et seulement si de toute suite de $K$, on peut extraire une sous-suite convergeant dans $K$.
Démontrer que si $K$ vérifie la propriété de Bolzano-Weierstrass, alors il est fermé et borné.

- **Fermé :** Soit $(x_n)_{n \in \mathbb{N}}$ une suite de $K$ convergeant vers $x \in E$. Montrons $x \in K$.
Puisque $K$ est compact, on peut extraire de $(x_n)$ une sous-suite $(x_{\phi(n)})$ qui converge vers une limite $y \in K$.
Or, la suite globale converge vers $x$, donc toute sous-suite converge également vers $x$.
Par unicité de la limite dans un espace normé, $x = y \in K$. $K$ contient ses limites, il est fermé.

- **Borné :** Raisonnons par l'absurde. Supposons $K$ non borné.
Pour tout $n \in \mathbb{N}$, on peut trouver un point $x_n \in K$ tel que $\|x_n\| \ge n$.
Ceci définit une suite $(x_n)$ dans $K$.
Puisque $K$ est compact, il existe une sous-suite $(x_{\phi(n)})$ convergeant vers $L \in K$.
Une suite convergente étant bornée, il existe une constante $M > 0$ telle que pour tout $n$, $\|x_{\phi(n)}\| \le M$.
Mais par définition de la suite originelle, $\|x_{\phi(n)}\| \ge \phi(n) \ge n$.
On aurait donc pour tout $n \in \mathbb{N}$, $n \le M$, ce qui est absurde. Donc $K$ est borné. $\blacksquare$
