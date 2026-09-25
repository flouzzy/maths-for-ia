# Exercice 4 : Densité de l'espace des polynômes $\star\star\star\mathstrut\mathstrut$

**Énoncé :**
Montrer que l'espace vectoriel des fonctions polynomiales est dense dans l'espace $L^p([a, b])$, où $[a,b]$ est un intervalle compact de $\mathbb{R}$ et $1 \le p < \infty$.

**Correction détaillée :**
Cette preuve procède par un argument de composition de densités.
1. D'après le théorème de densité dans les espaces mesurés, l'espace des fonctions continues $C([a, b])$ est dense dans $L^p([a, b])$.
Formellement, pour tout $f \in L^p([a, b])$ et tout $\varepsilon > 0$, il existe $g \in C([a, b])$ telle que :
$$ \|f - g\|_{L^p} < \frac{\varepsilon}{2} $$
2. Le théorème d'approximation de Weierstrass stipule que toute fonction continue sur un segment $[a, b]$ peut être approchée uniformément par une suite de polynômes.
Ainsi, pour notre $g$ continue et pour $\eta > 0$, il existe un polynôme $P$ tel que $\sup_{x \in [a, b]} |g(x) - P(x)| < \eta$.
3. Évaluons la norme $L^p$ de la différence entre $g$ et $P$ :
$$ \|g - P\|_{L^p} = \left( \int_a^b |g(x) - P(x)|^p \, dx \right)^{1/p} \le \left( \int_a^b \eta^p \, dx \right)^{1/p} = \eta (b - a)^{1/p} $$
4. En choisissant $\eta = \frac{\varepsilon}{2(b-a)^{1/p}}$, on garantit que $\|g - P\|_{L^p} \le \frac{\varepsilon}{2}$.
5. Par l'inégalité de Minkowski, on conclut :
$$ \|f - P\|_{L^p} \le \|f - g\|_{L^p} + \|g - P\|_{L^p} < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon $$
L'espace des polynômes est donc dense dans $L^p([a, b])$. $\blacksquare$
