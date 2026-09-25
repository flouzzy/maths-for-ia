# Exercice 4 : Densité des polynômes (Weierstrass-style dans Lp)

**Niveau :** \bigstar\bigstar\bigstar\star\star

**Énoncé :**
Montrer que l'ensemble des polynômes (restreints à $[0,1]$) est dense dans $L^2([0,1])$.

**Correction Détaillée :**
1. **Densité des fonctions continues :**
   Nous savons par le cours (Jalon 77) que les fonctions continues $\mathcal{C}([0,1])$ sont denses dans $L^2([0,1])$.
   Soit $f \in L^2([0,1])$ et $\varepsilon > 0$. Il existe $g \in \mathcal{C}([0,1])$ telle que $\|f - g\|_2 \le \frac{\varepsilon}{2}$.

2. **Théorème d'approximation de Weierstrass :**
   Pour la fonction continue $g$, le théorème de Stone-Weierstrass garantit l'existence d'un polynôme $P$ tel que $\|g - P\|_\infty = \sup_{x \in [0,1]} |g(x) - P(x)| \le \frac{\varepsilon}{2}$.

3. **Comparaison des normes :**
   Sur l'intervalle $[0,1]$ (de mesure $1$), on a pour toute fonction $h$ :
   $\|h\|_2 = \left( \int_0^1 |h(x)|^2 dx \right)^{1/2} \le \left( \int_0^1 \|h\|_\infty^2 dx \right)^{1/2} = \|h\|_\infty$.
   Donc $\|g - P\|_2 \le \|g - P\|_\infty \le \frac{\varepsilon}{2}$.

4. **Inégalité triangulaire dans $L^2$ :**
   Par l'inégalité de Minkowski, la distance totale est :
   $\|f - P\|_2 = \|(f - g) + (g - P)\|_2 \le \|f - g\|_2 + \|g - P\|_2 \le \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon$.
   Les polynômes sont donc denses dans $L^2([0,1])$.
