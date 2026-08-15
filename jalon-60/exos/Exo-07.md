# Exercice 7 : Approximation d'une gaussienne $\bigstar\bigstar\bigstar\bigstar\star$
Approcher $f(x) = \exp(-x^2)$ sur $[-1, 1]$ par une combinaison de ReLU $\max(0, x)$.

\textbf{Correction détaillée}
$f$ est dérivable et convexe par morceaux (inflexion en $\pm 1/\sqrt{2}$).
On utilise une subdivision de $[-1, 1]$ avec pas $h = 2/N$, $x_i = -1 + ih$.
L'interpolée linéaire par morceaux est $G(x)$. La dérivée seconde de $f$ est bornée par 2, donc l'erreur d'interpolation spline linéaire est encadrée par $M_2 h^2 / 8 \le 2 / (8 N^2) = 1/(4N^2)$.
Pour avoir une erreur $\epsilon$, il suffit que $1/(4N^2) < \epsilon$, soit $N > \frac{1}{2\sqrt{\epsilon}}$.
La fonction spline $G(x)$ s'écrit formelently $G(x) = f(-1) + c_{-1}(x+1) + \sum_{i=1}^{N-1} a_i \max(0, x-x_i)$.
Où les coefficients $a_i$ représentent les sauts de dérivée aux noeuds $x_i$ : $a_i = f'(x_i+) - f'(x_i-)$.
Ainsi, l'approximation est bien une somme pondérée de ReLUs.
