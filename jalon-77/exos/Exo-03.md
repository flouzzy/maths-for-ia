## Exercice 3 : Non-densité dans $L^\infty$ \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit l'espace $L^\infty(\mathbb{R})$ muni de la norme du supremum essentiel.
Montrer que l'espace des fonctions continues à support compact $C_c(\mathbb{R})$ **n'est pas** dense dans $L^\infty(\mathbb{R})$.
Donner un contre-exemple explicite et calculer la distance minimale à $C_c(\mathbb{R})$.

**Correction :**
La norme dans $L^\infty(\mathbb{R})$ est définie par $\| h \|_\infty = \text{ess sup}_{x \in \mathbb{R}} |h(x)|$.
Considérons la fonction constante $f(x) = 1$ pour tout $x \in \mathbb{R}$. Il est clair que $f \in L^\infty(\mathbb{R})$ car $\| f \|_\infty = 1 < \infty$.

Soit $g \in C_c(\mathbb{R})$ une fonction continue à support compact quelconque.
Puisque le support de $g$ est compact, il est borné. Il existe donc $M > 0$ tel que pour tout $|x| > M$, $g(x) = 0$.

Pour tout $x$ tel que $|x| > M$, nous avons :
$|f(x) - g(x)| = |1 - 0| = 1$.
Ainsi, le supremum essentiel de $|f - g|$ sur $\mathbb{R}$ est au moins $1$.
$$ \| f - g \|_\infty = \text{ess sup}_{x \in \mathbb{R}} |f(x) - g(x)| \ge 1 $$

Cette inégalité étant vraie pour *toute* fonction $g \in C_c(\mathbb{R})$, la distance entre $f$ et $C_c(\mathbb{R})$ est exactement $1$.
Il est donc impossible de trouver une suite de fonctions dans $C_c(\mathbb{R})$ qui converge vers $f$ en norme $L^\infty$. $C_c(\mathbb{R})$ n'est pas dense dans $L^\infty(\mathbb{R})$.
