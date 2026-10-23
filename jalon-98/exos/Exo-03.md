# Exercice 3 : Séparation d'un point et d'un convexe
$\bigstar\bigstar\bigstar\star\star$

## Énoncé
Soit $E$ un espace normé, et $C$ un sous-ensemble convexe, fermé et d'intérieur non vide. Soit $x_0 \notin C$.
Montrer, en utilisant la jauge de Minkowski $p_C$ translatée, qu'il existe une forme linéaire continue $f$ et un réel $\alpha$ tels que $f(x) \le \alpha$ pour tout $x \in C$ et $f(x_0) > \alpha$.

## Correction Détaillée
1. Quitte à faire une translation, on peut supposer que l'origine $0$ est dans l'intérieur de $C$.
2. La jauge de $C$, notée $p(x) = \inf\{ \lambda > 0 \mid x \in \lambda C \}$, est bien définie et sous-linéaire car $0 \in \text{Int}(C)$.
3. Puisque $C$ est fermé et $x_0 \notin C$, on a $p(x_0) > 1$.
4. Sur le sous-espace $M = \mathbb{R}x_0$, on définit la forme linéaire $f(t x_0) = t p(x_0)$.
5. Vérifions la domination sur $M$ : pour $t > 0$, $f(tx_0) = t p(x_0) = p(t x_0)$. Pour $t \le 0$, $f(t x_0) \le 0 \le p(tx_0)$. Donc $f \le p$ sur $M$.
6. Par le théorème de Hahn-Banach analytique, il existe un prolongement $F$ à $E$ tel que $F(x) \le p(x)$ pour tout $x \in E$.
7. Pour $x \in C$, on a $p(x) \le 1$, donc $F(x) \le 1$. Posons $\alpha = 1$.
8. On a $F(x_0) = f(x_0) = p(x_0) > 1 = \alpha$.
La forme $F$ sépare donc strictement le point $x_0$ du convexe fermé $C$. $\blacksquare$
