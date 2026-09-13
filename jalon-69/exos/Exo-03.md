##{Exercice 3 : Limite d'une intégrale avec fonction puissance \quad $\bigstar\bigstar\bigstar\star\star$}

\textbf{Énoncé :}
Montrer que $\lim_{n \to \infty} \int_0^1 \frac{n x^{n-1}}{1 + x} dx = \frac{1}{2}$.

\textbf{Correction :}
Si on utilise le TCD directement, la fonction $f_n(x) = \frac{n x^{n-1}}{1 + x}$ converge simplement vers 0 sur $[0, 1[$. Mais $\int_0^1 f_n(x) dx$ ne tend pas vers 0 ! Il n'y a donc pas de domination possible.
Procédons autrement pour appliquer le TCD.
Par intégration par parties :
$$ \int_0^1 \frac{n x^{n-1}}{1 + x} dx = \left[ \frac{x^n}{1+x} \right]_0^1 - \int_0^1 x^n \left(-\frac{1}{(1+x)^2}\right) dx = \frac{1}{2} + \int_0^1 \frac{x^n}{(1+x)^2} dx $$
Maintenant, appliquons le TCD sur l'intégrale restante.
Soit $h_n(x) = \frac{x^n}{(1+x)^2}$.
1. Convergence simple : pour $x \in [0, 1[$, $\lim_{n \to \infty} h_n(x) = 0$.
2. Domination : $|h_n(x)| \le \frac{1}{(1+x)^2} \le 1$. La constante 1 est intégrable sur $[0, 1]$.
3. Par TCD, $\lim_{n \to \infty} \int_0^1 h_n(x) dx = \int_0^1 0 dx = 0$.
Par conséquent, la limite de l'intégrale initiale est $\frac{1}{2} + 0 = \frac{1}{2}$.
