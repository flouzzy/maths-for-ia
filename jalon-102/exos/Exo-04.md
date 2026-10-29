$\bigstar\bigstar\bigstar\star\star$
**Énoncé :** Semi-continuité inférieure faible de la norme.
Soit $E$ un espace de Banach et $(x_n)$ une suite convergeant faiblement vers $x \in E$.
Démontrer rigoureusement que $\|x\| \le \liminf_{n \to \infty} \|x_n\|$.

**Correction Détaillée :**
Si $x = 0$, l'inégalité est immédiate car $\|x_n\| \ge 0$, d'où $\liminf \|x_n\| \ge 0 = \|0\|$.
Supposons $x \neq 0$. D'après un corollaire du théorème de Hahn-Banach, il existe $f \in E^*$ telle que $\|f\|_{E^*} = 1$ et $f(x) = \|x\|$.
Par définition de la convergence faible, la suite de scalaires $(f(x_n))$ converge vers $f(x) = \|x\|$.
Ainsi, $\|x\| = \lim_{n \to \infty} |f(x_n)|$.
D'autre part, pour tout $n$, l'inégalité fondamentale de la norme subordonnée donne :
$|f(x_n)| \le \|f\|_{E^*} \|x_n\| = 1 \cdot \|x_n\| = \|x_n\|$.
En passant à la limite inférieure des deux côtés, on obtient :
$\liminf_{n \to \infty} |f(x_n)| \le \liminf_{n \to \infty} \|x_n\|$.
Puisque la suite $(|f(x_n)|)$ est convergente, sa limite inférieure coïncide avec sa limite. D'où :
$\|x\| \le \liminf_{n \to \infty} \|x_n\|$.
Ce résultat fondamental montre que la norme ne peut "qu'augmenter" ou rester constante à la limite faible, mais jamais diminuer strictement de manière abrupte.
