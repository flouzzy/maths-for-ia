# Exercice 5 : Forme de la Jauge
$\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé
Dans $E = C([0, 1], \mathbb{R})$, on considère $C = \{ u \in E \mid \int_0^1 |u(t)| dt \le 1 \}$.
Déterminer la jauge de Minkowski $p_C(u)$.

## Correction Détaillée
Par définition, $p_C(u) = \inf\{ \lambda > 0 \mid u \in \lambda C \}$.
$u \in \lambda C \iff \frac{u}{\lambda} \in C \iff \int_0^1 \frac{|u(t)|}{\lambda} dt \le 1 \iff \frac{1}{\lambda} \int_0^1 |u(t)| dt \le 1 \iff \lambda \ge \int_0^1 |u(t)| dt$.
Par conséquent, le plus petit $\lambda > 0$ vérifiant cela est exactement $I(u) = \int_0^1 |u(t)| dt$.
Donc la jauge de Minkowski est $p_C(u) = \|u\|_1$. $\blacksquare$
