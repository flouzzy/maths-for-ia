\subsection*{Exercice 9 : Point extrémal et Hahn-Banach \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$}

Soit $C$ un convexe compact dans $E$. On admet le théorème de Krein-Milman. Montrer en utilisant Hahn-Banach que si $f \in E^*$, alors $f$ atteint son maximum sur $C$ en un point extrémal.

**Correction :**

1. Puisque $C$ est compact et $f$ est continue (pour la topologie faible ou forte), $f$ atteint son maximum $M$ sur $C$.
2. L'ensemble $K = \{ x \in C \mid f(x) = M \}$ est une "face" de $C$. Il est convexe, compact (fermé dans un compact), et non vide.
3. D'après le théorème de Krein-Milman, $K$ possède au moins un point extrémal $e$.
4. Montrons que $e$ est un point extrémal de $C$.
5. Supposons que $e = \lambda x + (1-\lambda) y$ avec $x, y \in C$ et $0 < \lambda < 1$.
6. On a $f(e) = \lambda f(x) + (1-\lambda) f(y)$.
7. Comme $f(x) \le M$ et $f(y) \le M$, et $f(e) = M$, il faut nécessairement que $f(x) = M$ et $f(y) = M$.
8. Ainsi $x \in K$ et $y \in K$.
9. Mais $e$ est un point extrémal de $K$, donc $x = y = e$.
10. Par conséquent, $e$ est un point extrémal de $C$.