# Exercice 9 : Continuité de la translation dans $L^p(\mathbb{R})$ \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Pour $f \in L^p(\mathbb{R})$ ($1 \le p < +\infty$) et $h \in \mathbb{R}$, on définit la translatée $\tau_h f(x) = f(x - h)$.
Il est admis que si $g$ est une fonction continue à support compact, alors $\lim_{h \to 0} \|\tau_h g - g\|_p = 0$.
En utilisant la densité des fonctions continues à support compact dans $L^p(\mathbb{R})$, démontrer que pour toute fonction $f \in L^p(\mathbb{R})$, $\lim_{h \to 0} \|\tau_h f - f\|_p = 0$.

**Correction :**
Soit $f \in L^p(\mathbb{R})$ et $\varepsilon > 0$.
Puisque l'espace des fonctions continues à support compact $C_c(\mathbb{R})$ est dense dans $L^p(\mathbb{R})$, il existe une fonction $g \in C_c(\mathbb{R})$ telle que $\|f - g\|_p < \varepsilon / 3$.

Par invariance par translation de la mesure de Lebesgue, $\|\tau_h(f - g)\|_p = \|f - g\|_p < \varepsilon / 3$.

On peut écrire :
$\tau_h f - f = (\tau_h f - \tau_h g) + (\tau_h g - g) + (g - f)$.
En appliquant l'inégalité triangulaire (Minkowski) de la norme $L^p$ :
$\|\tau_h f - f\|_p \le \|\tau_h(f - g)\|_p + \|\tau_h g - g\|_p + \|g - f\|_p$.

On majore les premier et troisième termes :
$\|\tau_h f - f\|_p < \varepsilon/3 + \|\tau_h g - g\|_p + \varepsilon/3 = \frac{2\varepsilon}{3} + \|\tau_h g - g\|_p$.

Par hypothèse (car $g \in C_c(\mathbb{R})$), il existe $\delta > 0$ tel que pour tout $|h| < \delta$, $\|\tau_h g - g\|_p < \varepsilon / 3$.

Donc, pour tout $|h| < \delta$, $\|\tau_h f - f\|_p < \frac{2\varepsilon}{3} + \frac{\varepsilon}{3} = \varepsilon$.
Cela prouve que $\lim_{h \to 0} \|\tau_h f - f\|_p = 0$. L'opérateur de translation est fortement continu sur $L^p(\mathbb{R})$.
