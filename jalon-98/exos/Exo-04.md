# Exercice 4 : Limite de Banach
$\bigstar\bigstar\bigstar\star\star$

## Énoncé
Soit $l^\infty$ l'espace des suites réelles bornées $x = (x_n)_{n \ge 1}$.
On définit $p(x) = \limsup_{n \to \infty} x_n$.
Montrer qu'il existe une forme linéaire $L : l^\infty \to \mathbb{R}$ telle que :
1. $\liminf x_n \le L(x) \le \limsup x_n$
2. Si $(x_n)$ converge vers $l$, alors $L(x) = l$.
Cette forme est appelée "Limite de Banach".

## Correction Détaillée
1. Montrons que $p$ est sous-linéaire.
   $\limsup(x_n + y_n) \le \limsup x_n + \limsup y_n$ est une propriété classique des limites supérieures.
   Pour $\lambda \ge 0$, $\limsup(\lambda x_n) = \lambda \limsup x_n$.
   Donc $p$ est sous-linéaire.
2. Soit $c$ le sous-espace de $l^\infty$ constitué des suites convergentes.
3. Sur $c$, on définit $f(x) = \lim x_n$.
   Clairement, $f$ est linéaire sur $c$.
4. Pour tout $x \in c$, $f(x) = \lim x_n = \limsup x_n = p(x)$, donc $f(x) \le p(x)$ est vérifié.
5. D'après le théorème de Hahn-Banach, il existe un prolongement linéaire $L$ de $f$ à $l^\infty$ tel que $L(x) \le p(x) = \limsup x_n$.
6. De plus, $L(-x) \le p(-x) = \limsup(-x_n) = -\liminf x_n$.
   Puisque $L(-x) = -L(x)$, on obtient $-L(x) \le -\liminf x_n \implies L(x) \ge \liminf x_n$.
7. Si $x \in c$, alors $L(x) = f(x) = \lim x_n$.
La Limite de Banach est ainsi construite. $\blacksquare$
