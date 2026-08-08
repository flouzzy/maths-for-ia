## Exercice 10 : Isométries et Théorème de Mazur-Ulam \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :** Une application $f : E \to F$ entre deux espaces normés est une isométrie si $||f(x) - f(y)|| = ||x - y||$. Montrer que toute isométrie surjective (avec $f(0)=0$) préserve l'alignement, étape clé prouvant qu'elle est linéaire.

**Correction :** Le cœur du théorème de Mazur-Ulam réside dans la caractérisation métrique du milieu d'un segment.
Soient $x, y \in E$. Le point milieu $m = \frac{x+y}{2}$ est l'unique point de $E$ satisfaisant :
$||x - m|| = ||y - m|| = \frac{1}{2}||x - y||$.
Puisque $f$ est une isométrie :
$||f(x) - f(m)|| = ||x - m|| = \frac{1}{2}||x - y|| = \frac{1}{2}||f(x) - f(y)||$
$||f(y) - f(m)|| = ||y - m|| = \frac{1}{2}||x - y|| = \frac{1}{2}||f(x) - f(y)||$
Dans un espace strictement convexe (pour simplifier), il existe un unique point satisfaisant ces équations métriques, qui est le milieu du segment $[f(x), f(y)]$.
Ainsi $f(m) = \frac{f(x) + f(y)}{2}$. L'isométrie préserve les milieux.
Par une récurrence dyadique standard et l'utilisation de la densité et de la continuité (une isométrie étant 1-lipschitzienne donc continue), on montre que $f(tx + (1-t)y) = tf(x) + (1-t)f(y)$ pour tout réel $t$, ce qui prouve la linéarité absolue.
