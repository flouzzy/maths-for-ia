\subsection*{Exercice 3 : Complétude d'une suite de fonctions géométriques \quad $\bigstar\bigstar$}
**Énoncé :**
Sur l'espace $\mathbb{R}$ muni de la mesure de Lebesgue, on considère la suite de fonctions $f_n(x) = e^{-n|x|}$.
1. Calculer $\|f_n\|_1$.
2. Montrer que la série $\sum_{n=1}^\infty f_n(x)$ converge presque partout vers une fonction limite $F(x)$.
3. Montrer que la somme de la série converge dans $L^1(\mathbb{R})$.

**Correction détaillée :**
1. On calcule la norme $L^1$ de $f_n$ :
   $\|f_n\|_1 = \int_{-\infty}^{\infty} e^{-n|x|} \, dx = 2 \int_0^\infty e^{-nx} \, dx = 2 \left[ \frac{-e^{-nx}}{n} \right]_0^\infty = \frac{2}{n}$.
2. D'après le théorème de convergence de Riesz-Fischer (via convergence absolue), si $\sum \|f_n\|_1 < \infty$, alors on a convergence presque partout. Ici, $\sum \|f_n\|_1 = 2 \sum \frac{1}{n} = +\infty$. On ne peut donc pas utiliser Riesz-Fischer directement !
   Cependant, on peut calculer directement. Pour $x \neq 0$, $|e^{-|x|}| < 1$. C'est une suite géométrique de raison $q = e^{-|x|} < 1$.
   La série $\sum_{n=1}^\infty (e^{-|x|})^n$ converge pour tout $x \neq 0$, c'est-à-dire presque partout (en dehors de l'ensemble de mesure nulle $\{0\}$).
   La limite vaut $F(x) = \frac{e^{-|x|}}{1 - e^{-|x|}} = \frac{1}{e^{|x|} - 1}$.
3. Montrons que $F \in L^1(\mathbb{R})$.
   Au voisinage de $0$, $e^{|x|} - 1 \sim |x|$, donc $F(x) \sim \frac{1}{|x|}$, qui N'EST PAS intégrable en 0.
   L'intégrale $\int_0^1 \frac{dx}{x} = \infty$.
   Donc $F \notin L^1(\mathbb{R})$. La série des normes divergeait, ce n'est donc pas une contradiction. La somme dans $L^1$ ne converge pas. Cet exercice illustre la nécessité de l'hypothèse $\sum \|f_n\| < \infty$ pour obtenir la complétude dans l'espace. \qed
