## Exercice 2 : Interversion série-intégrale classique \quad $\bigstar\star\star\star\star$

**Énoncé :**
Calculer l'intégrale $\int_0^1 \frac{1}{1-x} dx$ en développant l'intégrande en série entière et en justifiant soigneusement l'interversion.

**Correction Détaillée :**
1. Pour tout $x \in [0, 1[$, on a le développement en série entière : $\frac{1}{1-x} = \sum_{n=0}^\infty x^n$.
2. Posons $u_n(x) = x^n$ sur $[0, 1[$. Les fonctions $u_n$ sont mesurables et positives.
3. D'après le corollaire du théorème de convergence monotone (ou théorème de sommation terme à terme de Beppo Levi), on peut écrire :
   $$\int_0^1 \left(\sum_{n=0}^\infty x^n\right) dx = \sum_{n=0}^\infty \int_0^1 x^n dx$$
4. Calculons l'intégrale du terme général : $\int_0^1 x^n dx = \left[ \frac{x^{n+1}}{n+1} \right]_0^1 = \frac{1}{n+1}$.
5. On a donc $\int_0^1 \frac{1}{1-x} dx = \sum_{n=0}^\infty \frac{1}{n+1}$.
6. Cette série est la série harmonique, qui diverge vers $+\infty$. L'intégrale vaut donc $+\infty$.
