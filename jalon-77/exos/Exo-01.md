# Exercice 1 : Approximation d'une indicatrice par une fonction continue $\star\mathstrut\mathstrut\mathstrut\mathstrut$

**Énoncé :**
Soit $f = \mathbf{1}_{[0, 2]}$ définie sur $\mathbb{R}$. Trouver, de manière explicite, une fonction $g \in C_c(\mathbb{R})$ telle que $\|f - g\|_{L^1(\mathbb{R})} < \frac{1}{10}$.

**Correction détaillée :**
Nous allons construire une fonction affine par morceaux ("trapèze") qui interpole $f$.
Pour tout $\delta > 0$, posons $g_\delta(x)$ ainsi définie :
- $g_\delta(x) = 1$ pour $x \in [0, 2]$.
- $g_\delta(x) = 0$ pour $x \le -\delta$ et $x \ge 2+\delta$.
- $g_\delta(x) = \frac{x+\delta}{\delta}$ pour $x \in [-\delta, 0)$.
- $g_\delta(x) = \frac{2+\delta-x}{\delta}$ pour $x \in (2, 2+\delta]$.

La fonction $g_\delta$ est continue sur $\mathbb{R}$ et son support est le compact $[-\delta, 2+\delta]$, donc $g_\delta \in C_c(\mathbb{R})$.
Calculons la norme $L^1$ de la différence $f - g_\delta$. Remarquons que $f(x) - g_\delta(x) = 0$ sur $[0, 2]$ et en dehors de $[-\delta, 2+\delta]$.
$$ \|f - g_\delta\|_1 = \int_{\mathbb{R}} |f(x) - g_\delta(x)| \, dx = \int_{-\delta}^0 |-g_\delta(x)| \, dx + \int_2^{2+\delta} |-g_\delta(x)| \, dx $$
Comme $g_\delta \ge 0$ :
$$ \int_{-\delta}^0 \frac{x+\delta}{\delta} \, dx = \left[ \frac{(x+\delta)^2}{2\delta} \right]_{-\delta}^0 = \frac{\delta^2}{2\delta} - 0 = \frac{\delta}{2} $$
Par symétrie, l'intégrale sur $(2, 2+\delta]$ vaut également $\frac{\delta}{2}$.
Ainsi, $\|f - g_\delta\|_1 = \frac{\delta}{2} + \frac{\delta}{2} = \delta$.
Pour obtenir $\|f - g_\delta\|_1 < \frac{1}{10}$, il suffit de choisir n'importe quel $\delta \in (0, \frac{1}{10})$, par exemple $\delta = \frac{1}{20} = 0.05$.
Avec ce choix, la fonction $g_{0.05} \in C_c(\mathbb{R})$ répond à la contrainte demandée. $\blacksquare$
