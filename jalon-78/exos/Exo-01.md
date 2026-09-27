## Exercice 1 : Calcul basique des coefficients \quad \bigstar\star\star\star\star

Soit $f$ la fonction $2\pi$-périodique définie par $f(x) = \sin^2(x)$.
1. Calculer les coefficients de Fourier réels $a_n(f)$ et $b_n(f)$.
2. En déduire les coefficients complexes $c_n(f)$.

**Correction :**
1. On linéarise : $f(x) = \frac{1 - \cos(2x)}{2} = \frac{1}{2} - \frac{1}{2}\cos(2x)$.
$f$ est paire, donc $b_n(f) = 0$ pour tout $n$.
Par identification avec le développement en série de Fourier $a_0/2 + \sum a_n\cos(nx)$, on trouve directement :
$a_0 = 1$
$a_2 = -1/2$
$a_n = 0$ pour $n \neq 0, 2$.

2. $c_0 = a_0/2 = 1/2$.
$c_2 = (a_2 - ib_2)/2 = -1/4$.
$c_{-2} = (a_2 + ib_2)/2 = -1/4$.
$c_n = 0$ sinon.
