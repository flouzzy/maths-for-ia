# Exercice 4 : Dérivation de série entière

**Énoncé :**
Calculer la somme de la série entière $S(x) = \sum_{n=1}^{+\infty} n x^{n-1}$ pour $x \in ]-1, 1[$.

**Démonstration à blanc :**
On reconnaît dans l'expression $n x^{n-1}$ la dérivée de $x^n$.
Considérons la série entière géométrique $f(x) = \sum_{n=0}^{+\infty} x^n$.
Le rayon de convergence de cette série géométrique est $R = 1$, car pour $|x| < 1$ elle converge vers $\frac{1}{1-x}$, et diverge pour $|x| \geq 1$.
D'après le théorème de dérivation des séries entières, la série dérivée terme à terme a le même rayon de convergence $R=1$, et pour tout $x \in ]-1, 1[$ :
$$ f'(x) = \sum_{n=1}^{+\infty} \frac{d}{dx}(x^n) = \sum_{n=1}^{+\infty} n x^{n-1} $$
Ainsi, $S(x) = f'(x)$.
Puisque $f(x) = \frac{1}{1-x} = (1-x)^{-1}$ sur $]-1, 1[$, on dérive cette fonction :
$$ f'(x) = -1 \cdot (1-x)^{-2} \cdot (-1) = \frac{1}{(1-x)^2} $$
Par conséquent, pour tout $x \in ]-1, 1[$, $S(x) = \frac{1}{(1-x)^2}$.
