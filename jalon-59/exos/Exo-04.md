### Exercice 4 : Propriétés de l'équicontinuité \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $\mathcal{F}$ une famille de fonctions de $[0, 1]$ dans $\mathbb{R}$ dérivables telles que pour tout $f \in \mathcal{F}$ et tout $x \in [0, 1]$, $|f'(x)| \le M$, où $M$ est une constante universelle pour la famille.
Montrer que $\mathcal{F}$ est uniformément équicontinue.

**Correction :**
Soit $f \in \mathcal{F}$ arbitraire. La fonction $f$ est dérivable sur $[0, 1]$ et sa dérivée est bornée par $M$.
D'après l'Inégalité des Accroissements Finis, pour tous $x, y \in [0, 1]$,
$$ |f(x) - f(y)| \le M |x - y| $$
Soit $\epsilon > 0$. Posons $\delta = \frac{\epsilon}{M}$ (si $M>0$, sinon les fonctions sont constantes et $\delta=1$ convient).
Si $|x - y| \le \delta$, alors pour toute $f \in \mathcal{F}$,
$$ |f(x) - f(y)| \le M \frac{\epsilon}{M} = \epsilon $$
Le choix de $\delta$ ne dépend ni de $f$, ni de $x$, ni de $y$. La famille est donc uniformément équicontinue.
