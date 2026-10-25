# Exercice 10 : Optimisation KKT via séparation $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé
Montrez que les conditions de Karush-Kuhn-Tucker (KKT) en optimisation convexe dérivent directement d'un argument de séparation d'ensembles par un hyperplan.

## Correction Complète
Considérons le problème d'optimisation convexe standard :
Minimiser $f_0(x)$ sous contraintes $f_i(x) \leq 0$ ($i=1..m$), avec $f_j$ convexes.
Supposons l'existence d'un point optimal $x^*$. On peut poser sans perte de généralité $f_0(x^*) = 0$.
Le système $f_0(x) < 0$ et $f_i(x) < 0$ n'a pas de solution.
Considérons l'image géométrique des contraintes :
$A = \{ (u_0, u_1, ..., u_m) \in \mathbb{R}^{m+1} \mid \exists x \in D, f_i(x) \leq u_i, i=0..m \}$.
$A$ est un ensemble convexe par convexité des $f_i$.
Définissons l'orthant strictement négatif $B = \{ (v_0, ..., v_m) \mid v_i < 0, i=0..m \}$.
$B$ est un ensemble ouvert et convexe.
Puisqu'il n'y a pas de point réalisable améliorant la valeur optimale, $A \cap B = \emptyset$.
Par le théorème géométrique de Hahn-Banach (première forme), il existe un hyperplan séparateur défini par un vecteur normal $\lambda = (\lambda_0, \lambda_1, ..., \lambda_m) \neq 0$ et un réel $\alpha$.
Soit $\langle \lambda, u \rangle \geq \alpha$ pour $u \in A$, et $\langle \lambda, v \rangle \leq \alpha$ pour $v \in B$.
Puisque le point nul $0$ est dans l'adhérence de $B$, en passant à la limite, $\alpha \geq 0$.
De plus, si un $\lambda_i$ était strictement négatif, on pourrait prendre $v_i \to -\infty$ dans $B$, violant $\langle \lambda, v \rangle \leq \alpha$. Donc $\lambda_i \geq 0$ pour tout $i$.
Le point $(0, f_1(x^*), ..., f_m(x^*)) \in A$.
Ainsi $\lambda_0 \cdot 0 + \sum_{i=1}^m \lambda_i f_i(x^*) \geq 0$.
Mais comme $f_i(x^*) \leq 0$ et $\lambda_i \geq 0$, la somme est $\leq 0$.
Par conséquent, $\sum_{i=1}^m \lambda_i f_i(x^*) = 0$. (Ceci est la condition de dualité forte / slackness complémentaire des KKT).
Enfin, le fait que le Lagrangien $L(x, \lambda) = \lambda_0 f_0(x) + \sum \lambda_i f_i(x)$ soit minoré globalement sur $A$ donne la condition de stationnarité $\nabla L = 0$ aux points de dérivabilité.
Le théorème de Hahn-Banach constitue donc la fondation abstraite des conditions d'optimalité. $\blacksquare$
