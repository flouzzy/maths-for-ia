$\bigstar\star\star\star\star$
**Énoncé :** Unicité de la limite faible.
Soit $E$ un espace de Banach. Montrer que si une suite $(x_n)_{n \in \mathbb{N}}$ de $E$ converge faiblement vers $x \in E$ et vers $y \in E$, alors $x = y$.

**Correction Détaillée :**
Par définition de la convergence faible, pour toute forme linéaire continue $L \in E^*$, on a $\lim_{n \to \infty} L(x_n) = L(x)$ et $\lim_{n \to \infty} L(x_n) = L(y)$.
Par unicité de la limite dans le corps des scalaires (réel ou complexe), on en déduit que pour tout $L \in E^*$, $L(x) = L(y)$.
Par linéarité, $L(x - y) = 0$ pour tout $L \in E^*$.
Le théorème de Hahn-Banach (sous sa forme analytique ou via ses corollaires) garantit que si $L(z) = 0$ pour toute forme linéaire continue $L$, alors $z = 0$.
En l'appliquant à $z = x - y$, on obtient $x - y = 0$, soit $x = y$.
Ceci achève la démonstration de l'unicité de la limite faible.
