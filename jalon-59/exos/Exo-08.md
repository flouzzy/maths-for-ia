### Exercice 8 : Limite des équations intégrales (Type Picard-Lindelöf) \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $K(x,y)$ une fonction continue sur $[0,1] \times [0,1]$. On pose $T(f)(x) = \int_0^1 K(x,y) f(y) dy$ pour $f \in \mathcal{C}([0,1])$.
Soit $B$ la boule unité fermée de $\mathcal{C}([0,1])$ pour la norme infinie. Montrer que l'image $T(B)$ est relativement compacte.

**Correction :**
Soit $g = T(f)$ pour $f \in B$. Puisque $\|f\|_\infty \le 1$,
$|g(x)| \le \int_0^1 |K(x,y)| |f(y)| dy \le \max_{x,y} |K(x,y)| = M$.
Donc $T(B)$ est bornée en norme infinie, et donc ponctuellement bornée.
Montrons l'équicontinuité. $K$ étant continue sur le compact $[0,1]^2$, elle est uniformément continue. Pour $\epsilon > 0$, il existe $\delta > 0$ tel que $|x - x'| \le \delta \implies |K(x,y) - K(x',y)| \le \epsilon$ pour tout $y$.
Ainsi, pour $g \in T(B)$ :
$$ |g(x) - g(x')| = \left| \int_0^1 (K(x,y) - K(x',y)) f(y) dy \right| \le \int_0^1 \epsilon \cdot 1 dy = \epsilon $$
Ceci est vrai pour toute $g \in T(B)$. La famille $T(B)$ est équicontinue et bornée ponctuellement. Par Arzelà-Ascoli, $T(B)$ est relativement compacte. L'opérateur $T$ est donc compact.
