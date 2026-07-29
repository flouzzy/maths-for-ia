# Convergence en un point fini

**Difficulté :** $\star\star$

**Énoncé :**
Étudier la nature de l'intégrale généralisée :
$$ J = \int_0^1 \frac{1}{\sqrt{1-t}} dt $$

**Correction Zéro Ellipse :**
1. **Typage de l'intégrande :** Soit $f(t) = \frac{1}{\sqrt{1-t}}$. La fonction $f$ est continue sur l'intervalle $[0, 1[$. En $t=1$, le dénominateur s'annule et la fonction tend vers $+\infty$. L'intégrale est donc impropre en $t=1$.
2. **Calcul sur un segment fini :** Soit $X \in [0, 1[$. Nous considérons l'intégrale partielle sur $[0, X]$ :
   $$ J(X) = \int_0^X (1-t)^{-1/2} dt $$
3. **Recherche de primitive :** La fonction est de la forme $u'(t) \cdot (u(t))^n$ avec $u(t) = 1-t$ (donc $u'(t) = -1$) et $n = -1/2$.
   Réécrivons l'intégrande : $(1-t)^{-1/2} = - (-1)(1-t)^{-1/2} = - u'(t)(u(t))^{-1/2}$.
   La primitive de $u' u^n$ est $\frac{u^{n+1}}{n+1}$. Ici, $n+1 = -1/2 + 1 = 1/2$.
   La primitive est donc $- \frac{(1-t)^{1/2}}{1/2} = -2\sqrt{1-t}$.
4. **Évaluation de l'intégrale partielle :**
   $$ J(X) = \left[ -2\sqrt{1-t} \right]_0^X = -2\sqrt{1-X} - (-2\sqrt{1-0}) = -2\sqrt{1-X} + 2 $$
5. **Passage à la limite :** Nous devons évaluer la limite lorsque $X$ tend vers $1$ par valeurs inférieures ($X \to 1^-$).
   $$ \lim_{X \to 1^-} \sqrt{1-X} = \sqrt{0} = 0 $$
6. **Conclusion :**
   $$ \lim_{X \to 1^-} J(X) = -2(0) + 2 = 2 $$
   La limite étant finie, l'intégrale $J$ converge et $\int_0^1 \frac{1}{\sqrt{1-t}} dt = 2$.
