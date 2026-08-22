# L'intégrale d'une série géométrique de fonctions

**Difficulté :** $\star\star\star\star\star$

## Énoncé

On pose $X=[0,1]$ muni de $\lambda$. Soit $f(x) = \sum_{n=1}^\infty x^n$. On admet provisoirement le théorème d'interversion de Beppo-Levi : $\int \sum u_n = \sum \int u_n$ pour $u_n \geq 0$. Calculez $\int_0^1 f(x) d\lambda(x)$ en le justifiant.

---

## Correction détaillée

Sur $[0,1[$, on reconnaît la série géométrique de raison $x$. Donc $f(x) = \frac{x}{1-x}$ pour $x < 1$. En $x=1$, la série diverge vers $+\infty$.
En utilisant le théorème de Beppo-Levi admis (ou théorème de convergence monotone) :
$$ \int_{[0,1]} \left(\sum_{n=1}^\infty x^n\right) d\lambda = \sum_{n=1}^\infty \int_{[0,1]} x^n \, d\lambda $$
Or, $x \mapsto x^n$ est continue, et sur $[0,1]$, l'intégrale de Lebesgue coïncide avec celle de Riemann. Donc $\int_{[0,1]} x^n \, d\lambda = \frac{1}{n+1}$.
L'intégrale cherchée est la série $\sum_{n=1}^\infty \frac{1}{n+1} = \frac{1}{2} + \frac{1}{3} + \dots$
C'est le reste de la série harmonique, qui diverge vers $+\infty$. L'intégrale de $f$ vaut donc $+\infty$.
