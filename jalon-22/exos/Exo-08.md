# Exercice 8 : Convergence uniforme sans convergence normale

**Difficulté :** $\star\star\star\star$

**Énoncé :**
Soit $f_n(x) = \frac{x}{(1+x^2)^n}$ sur $[0, +\infty[$. Montrer que la série $\sum_{n \ge 0} f_n$ converge uniformément sur $[\delta, +\infty[$ avec $\delta > 0$, mais ne converge pas uniformément sur $[0, +\infty[$.

**Démonstration :**
1. **Convergence simple sur $[0, +\infty[$ :**
   - Si $x=0$, $f_n(0)=0$, la somme est $0$.
   - Si $x > 0$, $1+x^2 > 1$. La série est géométrique de raison $q = \frac{1}{1+x^2} < 1$.
     La somme vaut $S(x) = \sum_{n=0}^\infty x \left( \frac{1}{1+x^2} \right)^n = x \frac{1}{1 - \frac{1}{1+x^2}} = x \frac{1+x^2}{x^2} = \frac{1+x^2}{x} = x + \frac{1}{x}$.
   La fonction somme est donc $S(x) = x + \frac{1}{x}$ pour $x>0$, et $S(0) = 0$.

2. **Défaut de convergence uniforme sur $[0, +\infty[$ :**
   La limite $S$ n'est pas continue en 0 (elle tend vers $+\infty$ en $0^+$).
   Or chaque fonction $f_n$ est continue sur $[0, +\infty[$.
   Par contraposée du théorème de continuité, la convergence ne peut pas être uniforme sur $[0, +\infty[$.

3. **Convergence uniforme sur $[\delta, +\infty[$ ($\delta > 0$) :**
   Pour $x \ge \delta > 0$, $1+x^2 \ge 1+\delta^2$.
   $$ f_n(x) = \frac{x}{(1+x^2)^n} $$
   Étudions $f_n(x)$ : la dérivée est $f_n'(x) = \frac{1 - (2n-1)x^2}{(1+x^2)^{n+1}}$.
   Le maximum est atteint en $x_n = \frac{1}{\sqrt{2n-1}}$.
   Pour $n$ assez grand, $x_n < \delta$. Donc sur $[\delta, +\infty[$, $f_n$ est décroissante, son max est $f_n(\delta) = \frac{\delta}{(1+\delta^2)^n}$.
   Ceci est le terme général d'une série géométrique convergente. Donc la série converge normalement, et donc uniformément, sur $[\delta, +\infty[$.
$\blacksquare$
