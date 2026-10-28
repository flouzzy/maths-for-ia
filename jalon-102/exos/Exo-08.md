$\bigstar\bigstar\bigstar\bigstar\bigstar$
**Énoncé :** Compacité de la boule unité : le lemme de Riesz vs la topologie faible.
Montrer que si la boule unité fermée $B_E$ d'un espace de Banach $E$ est faiblement compacte, alors la topologie faible coïncide avec la topologie forte sur $B_E$ si et seulement si $\dim(E) < \infty$.

**Correction Détaillée :**
Sens réciproque : Si $\dim(E) < \infty$, la topologie forte et la topologie faible coïncident sur l'espace tout entier (cf. Exo 2). La boule unité fermée est fortement compacte par le théorème de Borel-Lebesgue, et donc faiblement compacte.
Sens direct : Supposons que $\dim(E) = \infty$. Le lemme de Riesz stipule que l'on peut construire une suite $(x_n)$ d'éléments de la sphère unité (donc $\|x_n\| = 1$) telle que pour tout $n \neq m$, $\|x_n - x_m\| \ge 1/2$.
Cette suite ne possède aucune sous-suite fortement de Cauchy, donc aucune sous-suite fortement convergente.
Cependant, si la boule unité $B_E$ est faiblement compacte, il existe une sous-suite $(x_{\phi(n)})$ qui converge faiblement vers un point $x \in B_E$.
Si la topologie faible coïncidait avec la topologie forte sur $B_E$, cette sous-suite convergerait également fortement. Mais nous venons de voir que c'est impossible car les éléments sont uniformément éloignés.
Ainsi, en dimension infinie, la topologie faible et la topologie forte ne peuvent jamais coïncider sur la boule unité, ce qui met en exergue l'affaiblissement strict apporté par la topologie $\sigma(E, E^*)$.
