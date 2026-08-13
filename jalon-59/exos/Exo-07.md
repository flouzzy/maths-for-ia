# Exercice 7 : Opérateurs à noyau et compacité

## Énoncé
Soit $K \in \mathcal{C}([0, 1] \times [0, 1], \mathbb{R})$.
On définit l'opérateur $T : \mathcal{C}([0, 1], \mathbb{R}) \to \mathcal{C}([0, 1], \mathbb{R})$ par :
$$(Tf)(x) = \int_0^1 K(x, y) f(y) dy$$
Montrer que si $B$ est la boule unité fermée de $\mathcal{C}([0, 1], \mathbb{R})$, alors $T(B)$ est relativement compact.

## Correction Détaillée

On pose $\mathcal{F} = T(B) = \{Tf \mid \|f\|_\infty \le 1\}$. On veut appliquer Arzelà-Ascoli.
Puisque $K$ est continue sur le compact $[0, 1] \times [0, 1]$, $K$ est bornée. Posons $M = \sup |K(x, y)|$.
$K$ est aussi uniformément continue sur ce compact (théorème de Heine).

1. **Bornitude ponctuelle :**
Soit $g \in \mathcal{F}$, il existe $f \in B$ tel que $g = Tf$.
$|g(x)| = \left|\int_0^1 K(x, y) f(y) dy\right| \le \int_0^1 |K(x, y)| \cdot |f(y)| dy \le \int_0^1 M \cdot 1 dy = M$.
Donc pour tout $x$, $\{g(x) \mid g \in \mathcal{F}\} \subset [-M, M]$, qui est relativement compact dans $\mathbb{R}$.

2. **Équicontinuité :**
$|g(x_1) - g(x_2)| = \left|\int_0^1 (K(x_1, y) - K(x_2, y))f(y) dy\right| \le \int_0^1 |K(x_1, y) - K(x_2, y)| dy$.
Par uniforme continuité de $K$, pour tout $\epsilon > 0$, il existe $\delta > 0$ tel que $\|(x_1, y) - (x_2, y)\| = |x_1 - x_2| < \delta \implies |K(x_1, y) - K(x_2, y)| < \epsilon$.
Donc $|x_1 - x_2| < \delta \implies |g(x_1) - g(x_2)| \le \int_0^1 \epsilon dy = \epsilon$.
Ceci est vrai indépendamment de $f \in B$, donc $\mathcal{F}$ est équicontinue.

3. **Conclusion :**
Par Arzelà-Ascoli, $\mathcal{F}$ est relativement compacte. $T$ est un opérateur compact.
