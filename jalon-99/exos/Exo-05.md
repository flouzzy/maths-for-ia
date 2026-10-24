\subsection*{Exercice 5 : Cône polaire \quad $\bigstar\bigstar\bigstar\star\star$}

Soit $C$ un cône convexe fermé non vide de $E$ et $C^* = \{ f \in E^* \mid \forall x \in C, f(x) \ge 0 \}$. Montrer que si $x_0 \in E$ vérifie $f(x_0) \ge 0$ pour tout $f \in C^*$, alors $x_0 \in C$.

**Correction :**

1. Raisonnons par l'absurde. Supposons que $x_0 \notin C$.
2. Puisque $C$ est fermé, on peut appliquer le théorème de Hahn-Banach géométrique (séparation stricte) à $C$ et au compact $\{x_0\}$.
3. Il existe $L \in E^*$ et $\alpha \in \mathbb{R}$ tels que $\forall x \in C, L(x) < \alpha < L(x_0)$.
4. Puisque $0 \in C$, on a $L(0) = 0 < \alpha$, donc $\alpha > 0$.
5. Comme $C$ est un cône, si $L(x) > 0$ pour un $x \in C$, alors $L(\lambda x) = \lambda L(x) < \alpha$ pour tout $\lambda > 0$, ce qui est absurde.
6. Donc, $\forall x \in C, L(x) \le 0$.
7. Considérons la forme $f = -L$. On a $f(x) \ge 0$ pour tout $x \in C$, donc $f \in C^*$.
8. D'après l'inégalité de séparation, $L(x_0) > \alpha > 0$, donc $f(x_0) = -L(x_0) < 0$.
9. Ceci contredit l'hypothèse selon laquelle $\forall f \in C^*, f(x_0) \ge 0$.
10. Ainsi, $x_0 \in C$.