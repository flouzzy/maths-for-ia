## Exercice 10 : Mesure sans atomes $\quad \bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Si $\mu$ est une mesure de probabilité sans atomes sur $\mathbb{R}$, montrer que la fonction de répartition $F(x) = \mu((-\infty, x])$ est continue.

**Correction :**
La fonction de répartition est toujours croissante et continue à droite (par continuité décroissante des mesures).
Étudions la limite à gauche en un point $a$.
Soit $x_n \to a$ avec $x_n < a$.
Les ensembles $A_n = (-\infty, x_n]$ sont croissants. L'union des $A_n$ est $(-\infty, a)$.
Par continuité croissante de la mesure, $\lim_{n \to \infty} \mu(A_n) = \mu((-\infty, a))$.
Donc $F(a^-) = \mu((-\infty, a))$.
La différence avec $F(a)$ est $F(a) - F(a^-) = \mu((-\infty, a]) - \mu((-\infty, a)) = \mu(\{a\})$.
Dire que $\mu$ est sans atomes signifie exactement que $\mu(\{a\}) = 0$ pour tout $a$.
Donc $F(a) = F(a^-)$, la fonction est continue à gauche.
Étant continue à droite et à gauche en tout point, elle est continue.
