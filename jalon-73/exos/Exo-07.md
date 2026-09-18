# Exercice 7 : Densité des fonctions continues à support compact

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé

On admet que l'espace des fonctions étagées intégrables est dense dans $L^p(\mathbb{R})$ pour $1 \le p < +\infty$.
Prouver que l'espace $C_c(\mathbb{R})$ (fonctions continues à support compact) est dense dans $L^p(\mathbb{R})$.
*Indication : Montrer d'abord qu'on peut approcher la fonction indicatrice d'un segment $[a, b]$ par une fonction continue.*

---

## Correction détaillée

Soit $f \in L^p(\mathbb{R})$. Soit $\epsilon > 0$.
Puisque les fonctions étagées sont denses, il existe une fonction étagée $\phi = \sum_{i=1}^k c_i \mathbf{1}_{A_i}$ telle que $\|f - \phi\|_p < \epsilon/2$.
Les ensembles $A_i$ sont de mesure finie. Par régularité de la mesure de Lebesgue, tout ensemble mesurable de mesure finie peut être approché par une union finie d'intervalles disjoints. On peut donc se ramener à approcher des indicatrices de segments $[a, b]$.
Considérons $g = \mathbf{1}_{[a, b]}$.
Construisons une approximation continue $g_\delta$ en "adoucissant" les bords sur une largeur $\delta > 0$.
$$ g_\delta(x) = 1 \text{ si } x \in [a, b] $$
$$ g_\delta(x) = 0 \text{ si } x \le a-\delta \text{ ou } x \ge b+\delta $$
$$ g_\delta \text{ affine continue sur } [a-\delta, a] \text{ et } [b, b+\delta] $$
$g_\delta$ est bien continue à support compact $[a-\delta, b+\delta]$.
Évaluons la distance dans $L^p$ :
$$ \|g - g_\delta\|_p^p = \int_\mathbb{R} |g(x) - g_\delta(x)|^p \, dx = \int_{a-\delta}^a |g_\delta(x)|^p \, dx + \int_b^{b+\delta} |g_\delta(x)|^p \, dx $$
Puisque $0 \le g_\delta(x) \le 1$, l'intégrale est majorée par $1^p \times \delta + 1^p \times \delta = 2\delta$.
Donc $\|g - g_\delta\|_p \le (2\delta)^{1/p}$.
En choisissant $\delta$ suffisamment petit, cette distance peut être rendue arbitrairement petite (par exemple $<\epsilon/(2k|c_i|)$).
Par inégalité triangulaire, on reconstitue une fonction $\psi \in C_c(\mathbb{R})$ (combinaison linéaire des $g_{i,\delta}$) telle que $\|\phi - \psi\|_p < \epsilon/2$.
Finalement, $\|f - \psi\|_p \le \|f - \phi\|_p + \|\phi - \psi\|_p < \epsilon/2 + \epsilon/2 = \epsilon$.
L'espace $C_c(\mathbb{R})$ est donc dense dans $L^p(\mathbb{R})$ pour $1 \le p < +\infty$.
