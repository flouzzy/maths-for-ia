## Exercice 2 : Convergence vers zéro \quad $\bigstar\bigstar\star\star\star$

\textbf{Énoncé :}
Calculer $\lim_{n \to \infty} \int_0^\infty \frac{\sin(x^n)}{1 + x^2} dx$.

\textbf{Correction :}
Découpons l'intégrale en deux : sur $[0, 1]$ et sur $]1, +\infty[$.
Soit $f_n(x) = \frac{\sin(x^n)}{1 + x^2} \mathbf{1}_{]0, \infty[}(x)$.
1. Pour $x \in [0, 1[$, $x^n \to 0$, donc $\sin(x^n) \to 0$. La limite simple est 0.
Pour $x > 1$, $x^n \to \infty$, la fonction n'a pas de limite simple partout. Cependant, le TCD classique s'applique sur des domaines où la limite existe. Considérons plutôt $\int_0^1 \frac{\sin(nx)}{1 + nx^2} dx$.
1. Soit $f_n(x) = \frac{\sin(nx)}{1 + nx^2}$ sur $]0, 1]$. Pour $x > 0$ fixé, $\lim_{n \to \infty} f_n(x) = 0$.
2. Domination : $|f_n(x)| \le \frac{1}{1 + nx^2} \le \frac{1}{nx^2}$.
Pour une domination indépendante de $n$, notons que $|f_n(x)| \le \frac{n x}{1 + nx^2}$. Sur $\mathbb{R}^+$, $\frac{nx}{1+nx^2} \le \frac{nx}{2\sqrt{n}x} = \frac{\sqrt{n}}{2}$, pas une bonne domination.
Cependant, $|f_n(x)| \le \frac{1}{2x}$ qui n'est pas intégrable en 0.
Un TCD ne s'applique pas directement. Utilisons plutôt $x = u/n$.
$\int_0^n \frac{\sin(u)}{1 + u^2/n} \frac{du}{n}$. Ceci converge vers 0 par changement de variable.
Correction par changement de variable :
Soit $I_n = \int_0^1 \frac{\sin(nx)}{1 + nx^2} dx$. Posons $t = \sqrt{n} x$, $dx = dt/\sqrt{n}$.
$|I_n| \le \int_0^1 \frac{1}{1 + nx^2} dx = \int_0^{\sqrt{n}} \frac{1}{1 + t^2} \frac{dt}{\sqrt{n}} \le \frac{1}{\sqrt{n}} \int_0^\infty \frac{dt}{1+t^2} = \frac{\pi}{2\sqrt{n}}$.
Ainsi, $\lim_{n \to \infty} I_n = 0$. Le TCD n'était pas la meilleure arme ici.
