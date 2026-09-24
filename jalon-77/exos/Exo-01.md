## Exercice 1 : Approximation d'une indicatrice par une fonction continue \quad $\bigstar\star\star\star\star$

**Énoncé :**
Soit $f = \mathbf{1}_{[0, 1]} \in L^1(\mathbb{R})$.
Proposer une fonction $g \in C_c(\mathbb{R})$ (continue à support compact) telle que $\| f - g \|_1 \le \epsilon$, pour un $\epsilon > 0$ donné. Calculer explicitement l'intégrale pour prouver la majoration.

**Correction :**
Nous cherchons à construire une fonction $g$ continue qui interpole $f$. Définissons $g_\delta$ pour $\delta > 0$ :
$g_\delta(x) = 1$ pour $x \in [0, 1]$
$g_\delta(x) = 1 + \frac{x}{\delta}$ pour $x \in [-\delta, 0]$
$g_\delta(x) = 1 - \frac{x-1}{\delta}$ pour $x \in [1, 1+\delta]$
$g_\delta(x) = 0$ ailleurs.

La fonction $g_\delta$ est continue sur $\mathbb{R}$ et son support est $[-\delta, 1+\delta]$, qui est compact.
L'écart est $f(x) - g_\delta(x) = -g_\delta(x)$ sur $[-\delta, 0[ \cup ]1, 1+\delta]$.
La norme $L^1$ de la différence est l'aire sous les deux "triangles" latéraux :
$\| f - g_\delta \|_1 = \int_{-\delta}^0 \left(1 + \frac{x}{\delta}\right) dx + \int_1^{1+\delta} \left(1 - \frac{x-1}{\delta}\right) dx$
L'aire d'un tel triangle de base $\delta$ et de hauteur $1$ est $\frac{1 \times \delta}{2} = \frac{\delta}{2}$.
Ainsi, $\| f - g_\delta \|_1 = \frac{\delta}{2} + \frac{\delta}{2} = \delta$.
Pour obtenir $\| f - g_\delta \|_1 \le \epsilon$, il suffit de choisir $\delta = \epsilon$.
La fonction correspondante est bien un élément de $C_c(\mathbb{R})$.
