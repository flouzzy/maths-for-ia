$\bigstar\bigstar\bigstar\bigstar\star$
**Énoncé :** Convergence faible et produit scalaire.
Dans un espace de Hilbert $H$, soit $(x_n)$ une suite convergeant faiblement vers $x$, et $(y_n)$ une suite convergeant fortement vers $y$.
Montrer que $\langle x_n, y_n \rangle \to \langle x, y \rangle$.

**Correction Détaillée :**
On écrit la décomposition suivante de la différence :
$\langle x_n, y_n \rangle - \langle x, y \rangle = \langle x_n, y_n - y \rangle + \langle x_n, y \rangle - \langle x, y \rangle = \langle x_n, y_n - y \rangle + \langle x_n - x, y \rangle$.
Évaluons la limite de chacun des deux termes.
Pour le second terme : par le théorème de Riesz, l'application $z \mapsto \langle z, y \rangle$ est une forme linéaire continue sur $H$. Par définition de la convergence faible de $(x_n)$ vers $x$, ce terme tend vers $0$.
Pour le premier terme : par l'inégalité de Cauchy-Schwarz,
$|\langle x_n, y_n - y \rangle| \le \|x_n\| \|y_n - y\|$.
Puisque $(x_n)$ converge faiblement, elle est bornée (cf. exercice précédent) : il existe $M > 0$ tel que $\|x_n\| \le M$ pour tout $n$.
Ainsi, $|\langle x_n, y_n - y \rangle| \le M \|y_n - y\|$.
Comme $(y_n)$ converge fortement vers $y$, $\|y_n - y\| \to 0$, d'où ce terme tend également vers $0$.
La somme de deux suites tendant vers zéro tend vers zéro, on a donc bien $\lim_{n \to \infty} \langle x_n, y_n \rangle = \langle x, y \rangle$.
