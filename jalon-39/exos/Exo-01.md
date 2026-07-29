# Convergence directe par calcul de primitive

**Difficulté :** $\star$

**Énoncé :**
Étudier la nature (convergence ou divergence) de l'intégrale généralisée suivante :
$$ I = \int_0^{+\infty} e^{-2t} dt $$

**Correction Zéro Ellipse :**
1. **Typage de l'intégrande :** Soit $f(t) = e^{-2t}$. La fonction $f$ est définie, continue et strictement positive sur l'intervalle $[0, +\infty[$. Elle est donc localement intégrable sur cet intervalle. L'unique point impropre est la borne $+\infty$.
2. **Calcul sur un segment fini :** Soit $X > 0$. On se place sur le segment $[0, X]$ où l'intégrale de Riemann classique est bien définie.
   $$ I(X) = \int_0^X e^{-2t} dt $$
3. **Recherche de primitive :** Une primitive de $e^{-at}$ est $-\frac{1}{a}e^{-at}$. Donc, pour $a=2$ :
   $$ I(X) = \left[ -\frac{1}{2} e^{-2t} \right]_0^X = -\frac{1}{2} e^{-2X} - \left(-\frac{1}{2} e^{0}\right) = -\frac{1}{2} e^{-2X} + \frac{1}{2} $$
4. **Passage à la limite :** Nous devons maintenant évaluer la limite de $I(X)$ lorsque $X \to +\infty$.
   Comme $\lim_{X \to +\infty} -2X = -\infty$, par composition avec la fonction exponentielle ($\lim_{u \to -\infty} e^u = 0$), nous obtenons :
   $$ \lim_{X \to +\infty} e^{-2X} = 0 $$
5. **Conclusion :** Par opération sur les limites :
   $$ \lim_{X \to +\infty} I(X) = -\frac{1}{2} (0) + \frac{1}{2} = \frac{1}{2} $$
   La limite existe et est une valeur réelle finie. L'intégrale est donc convergente, et sa valeur est :
   $$ \int_0^{+\infty} e^{-2t} dt = \frac{1}{2} $$
