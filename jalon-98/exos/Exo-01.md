# Exercice 1 : Prolongement simple sur $\mathbb{R}^2$
$\bigstar\star\star\star\star$

## Énoncé
Soit $E = \mathbb{R}^2$ muni de la norme $\| (x, y) \| = |x| + |y|$ (norme 1).
Soit $M = \{ (x, 0) \mid x \in \mathbb{R} \}$ le sous-espace des abscisses.
On définit $f : M \to \mathbb{R}$ par $f(x, 0) = x$.
Trouver toutes les formes linéaires $F : E \to \mathbb{R}$ qui prolongent $f$ tout en vérifiant $\forall v \in E, F(v) \le \| v \|$.

## Correction Détaillée
Toute forme linéaire sur $\mathbb{R}^2$ s'écrit $F(x, y) = ax + by$.
Pour que $F$ prolonge $f$, il faut que pour tout $x \in \mathbb{R}$, $F(x, 0) = f(x, 0)$, soit $ax = x$, d'où $a = 1$.
Ainsi $F(x, y) = x + by$.
La condition de domination s'écrit : $\forall (x, y) \in \mathbb{R}^2, x + by \le |x| + |y|$.
Prenons $x = 0$. La condition devient $by \le |y|$ pour tout $y \in \mathbb{R}$.
Pour $y = 1$, on a $b \le 1$.
Pour $y = -1$, on a $-b \le 1 \implies b \ge -1$.
Donc $b \in [-1, 1]$.
Réciproquement, si $b \in [-1, 1]$, alors pour tout $(x, y) \in \mathbb{R}^2$ :
$F(x, y) = x + by \le |x| + |b||y| \le |x| + |y| = \|(x,y)\|$.
Les prolongements solutions sont donc exactement les formes $F(x, y) = x + by$ avec $b \in [-1, 1]$.
Il y a donc une infinité de prolongements (le prolongement n'est pas unique). $\blacksquare$
