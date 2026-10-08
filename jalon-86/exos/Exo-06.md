## La méthode de la fonction muette \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $X$ une variable aléatoire de densité $f_X(x)$. On pose $Y = e^X$.
Déterminer la densité de probabilité de $Y$, notée $f_Y$, en utilisant la méthode de la fonction test (ou fonction muette).

**Correction Explicative :**
1. La méthode de la fonction muette (ou fonction test) consiste à caractériser la loi d'une variable aléatoire $Y$ en calculant l'espérance d'une fonction arbitraire bornée et mesurable $h(Y)$, puis à identifier la densité dans l'intégrale résultante.
2. Écrivons l'espérance de $h(Y)$ de deux manières différentes :
   - D'une part, par définition de la densité de $Y$ (que l'on cherche à déterminer) :
     $$\mathbb{E}[h(Y)] = \int_{-\infty}^{+\infty} h(y) f_Y(y) dy$$
   - D'autre part, en utilisant le théorème de transfert (puisque $Y = e^X$) avec la densité connue de $X$ :
     $$\mathbb{E}[h(Y)] = \mathbb{E}[h(e^X)] = \int_{-\infty}^{+\infty} h(e^x) f_X(x) dx$$
3. Notre objectif est de transformer la seconde intégrale pour qu'elle prenne la forme de la première. Pour cela, nous effectuons le changement de variable $y = e^x$.
   - Bijection : L'application $x \mapsto e^x$ est un difféomorphisme strictement croissant de $\mathbb{R}$ vers $]0, +\infty[$. Le changement de variable est donc parfaitement justifié.
   - Inverse : $x = \ln(y)$.
   - Différentielle : $dy = e^x dx = y dx$, ce qui implique que $dx = \frac{dy}{y}$.
   - Bornes d'intégration : Lorsque $x \to -\infty$, $y \to 0$. Lorsque $x \to +\infty$, $y \to +\infty$.
4. Appliquons ce changement de variable à l'intégrale issue du théorème de transfert :
   $$\mathbb{E}[h(Y)] = \int_{0}^{+\infty} h(y) f_X(\ln(y)) \frac{dy}{y}$$
5. Afin de pouvoir identifier la densité $f_Y(y)$ sur tout $\mathbb{R}$, nous prolongeons l'intégrale sur $\mathbb{R}$ en utilisant la fonction indicatrice $\mathbf{1}_{]0, +\infty[}(y)$ :
   $$\mathbb{E}[h(Y)] = \int_{-\infty}^{+\infty} h(y) \left( f_X(\ln(y)) \frac{1}{y} \mathbf{1}_{]0, +\infty[}(y) \right) dy$$
6. Identifions maintenant les deux expressions de $\mathbb{E}[h(Y)]$. L'égalité doit être vraie pour toute fonction test $h$ mesurable bornée :
   $$\int_{-\infty}^{+\infty} h(y) f_Y(y) dy = \int_{-\infty}^{+\infty} h(y) \left( \frac{1}{y} f_X(\ln(y)) \mathbf{1}_{]0, +\infty[}(y) \right) dy$$
   Cela implique que les fonctions intégrées contre $h(y)$ sont presque partout égales.
7. Conclusion : La densité de probabilité de la variable aléatoire $Y = e^X$ est :
   $$f_Y(y) = \frac{1}{y} f_X(\ln y) \mathbf{1}_{]0, +\infty[}(y)$$
   Cette méthode, fondée sur la théorie de la mesure, est extrêmement puissante et évite de passer par le calcul de la fonction de répartition, ce qui est particulièrement avantageux en dimension supérieure.
