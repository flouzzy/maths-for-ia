\subsection*{Exercice 3 : Séparation de cônes \quad $\bigstar\bigstar\star\star\star$}

Soit $C$ un cône convexe de sommet $0$ dans un espace normé $E$, tel que l'adhérence de $C$ ne soit pas l'espace entier. Montrer qu'il existe une forme linéaire continue non nulle $f$ sur $E$ telle que $\forall x \in C, f(x) \ge 0$.

**Correction :**

1. Soit $\overline{C}$ l'adhérence de $C$. C'est un cône convexe fermé.
2. Par hypothèse, il existe un point $x_0 \notin \overline{C}$.
3. Par le théorème de Hahn-Banach (forme géométrique de séparation stricte entre le fermé $\overline{C}$ et le compact $\{x_0\}$), il existe une forme linéaire $f \in E^*$ et un réel $\alpha$ tels que pour tout $y \in \overline{C}$, $f(y) < \alpha < f(x_0)$.
4. Puisque $0 \in \overline{C}$, on a $f(0) = 0 < \alpha$. Donc $\alpha > 0$.
5. Si pour un certain $y \in C$, on avait $f(y) > 0$, alors comme $C$ est un cône, pour tout $\lambda > 0$, $\lambda y \in C \subset \overline{C}$.
   On aurait $f(\lambda y) = \lambda f(y) < \alpha$ pour tout $\lambda > 0$, ce qui est impossible en faisant tendre $\lambda \to +\infty$.
6. Ainsi, pour tout $y \in C$, on a nécessairement $f(y) \le 0$.
7. En prenant $g = -f$, on a $g(x) \ge 0$ pour tout $x \in C$. $g$ est continue et non nulle.