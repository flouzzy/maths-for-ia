\subsection*{Exercice 4 : Séparation de deux convexes compacts \quad $\bigstar\bigstar\star\star\star$}

Soient $K_1$ et $K_2$ deux parties convexes compactes non vides et disjointes d'un espace vectoriel normé $E$. Montrer qu'il existe une forme linéaire continue $L \in E^*$ telle que $\sup_{x \in K_1} L(x) < \inf_{y \in K_2} L(y)$.

**Correction :**

1. Les ensembles $K_1$ et $K_2$ sont convexes, non vides et disjoints.
2. $K_1$ est fermé (car compact dans un espace séparé) et $K_2$ est compact.
3. D'après le théorème de séparation stricte, il existe $L \in E^*$ et des réels $\alpha, \epsilon > 0$ tels que :
   $\forall x \in K_1, \forall y \in K_2, \quad L(x) \le \alpha - \epsilon < \alpha + \epsilon \le L(y)$.
4. L'application $L$ est continue sur les compacts $K_1$ et $K_2$. Elle y atteint donc ses bornes.
5. On a ainsi $\sup_{x \in K_1} L(x) \le \alpha - \epsilon$.
6. Et $\inf_{y \in K_2} L(y) \ge \alpha + \epsilon$.
7. Par conséquent, $\sup_{x \in K_1} L(x) \le \alpha - \epsilon < \alpha + \epsilon \le \inf_{y \in K_2} L(y)$, ce qui conclut la preuve.