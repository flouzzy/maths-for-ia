# Exercice 5 : Densité des fonctions continues à support compact
**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
On admet que l'espace des fonctions en escalier à support borné est dense dans $L^p(\mathbb{R})$ ($1 \le p < +\infty$).
En déduire, en utilisant la complétude de $L^p$, que l'espace $C_c(\mathbb{R})$ (fonctions continues à support compact) est dense dans $L^p(\mathbb{R})$.

**Correction :**
Soit $f \in L^p(\mathbb{R})$ et $\varepsilon > 0$. Par densité des fonctions en escalier, il existe une fonction en escalier $g = \sum_{i=1}^n c_i \mathbf{1}_{[a_i, b_i]}$ telle que $\|f - g\|_p < \varepsilon/2$.
Il suffit donc d'approcher la fonction indicatrice $\mathbf{1}_{[a,b]}$ par une fonction continue à support compact.
On définit $h_\delta(x)$ affine continue valant 1 sur $[a,b]$, 0 hors de $[a-\delta, b+\delta]$, et reliant ces valeurs linéairement sur $[a-\delta, a]$ et $[b, b+\delta]$.
La fonction $h_\delta \in C_c(\mathbb{R})$.
On a $\|h_\delta - \mathbf{1}_{[a,b]}\|_p^p = \int_{a-\delta}^a |h_\delta(x)|^p dx + \int_b^{b+\delta} |h_\delta(x)|^p dx \le 1 \times \delta + 1 \times \delta = 2\delta$.
En choisissant $\delta$ suffisamment petit, disons $(2\delta)^{1/p} < \frac{\varepsilon}{2n \max|c_i|}$, on construit $h \in C_c(\mathbb{R})$ telle que $\|g - h\|_p < \varepsilon/2$.
Par l'inégalité triangulaire, $\|f - h\|_p \le \|f - g\|_p + \|g - h\|_p < \varepsilon/2 + \varepsilon/2 = \varepsilon$.
L'espace $C_c(\mathbb{R})$ est donc dense dans $L^p(\mathbb{R})$. (La complétude intervient conceptuellement en ce sens que $L^p$ est la complétion de $C_c(\mathbb{R})$ pour la norme $\|\cdot\|_p$).
