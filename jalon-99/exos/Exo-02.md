\subsection*{Exercice 2 : Projection sur un convexe \quad $\bigstar\star\star\star\star$}

Soit $H$ un espace de Hilbert, $C$ un sous-ensemble convexe fermé non vide de $H$, et $x \notin C$. Soit $p$ la projection de $x$ sur $C$. Montrer que l'hyperplan orthogonal au segment $[x, p]$ passant par $p$ sépare $x$ et $C$.

**Correction :**

1. Par définition de la projection sur un convexe fermé dans un Hilbert, on a pour tout $y \in C$, $\langle x - p, y - p \rangle \le 0$.
2. Considérons la forme linéaire $L(z) = \langle x - p, z \rangle$.
3. Pour $y \in C$, on a $L(y) - L(p) = \langle x - p, y - p \rangle \le 0$, donc $L(y) \le L(p)$.
4. Pour $x$, on a $L(x) - L(p) = \langle x - p, x - p \rangle = \|x - p\|^2 > 0$ car $x \notin C$.
5. Ainsi $L(y) \le L(p) < L(x)$.
6. L'hyperplan défini par $H = \{ z \in H \mid L(z) = L(p) \}$ est exactement l'hyperplan affine passant par $p$ et de vecteur normal $x - p$. Il sépare strictement $x$ et $C$, ce qui illustre le théorème de Hahn-Banach géométrique pour un point et un fermé.