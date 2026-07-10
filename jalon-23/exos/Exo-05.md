# Exercice 5 : Calcul de somme avec primitives

**Énoncé :**
Calculer pour $x \in ]-1, 1[$, la somme $S(x) = \sum_{n=1}^{+\infty} \frac{x^n}{n}$.

**Démonstration à blanc :**
Le rayon de convergence est 1 (par d'Alembert, $\frac{1/(n+1)}{1/n} \to 1$).
Pour $x \in ]-1, 1[$, la somme $S(x)$ définit une fonction dérivable.
Dérivons $S(x)$ terme à terme :
$$ S'(x) = \sum_{n=1}^{+\infty} \frac{d}{dx}\left(\frac{x^n}{n}\right) = \sum_{n=1}^{+\infty} \frac{n x^{n-1}}{n} = \sum_{n=1}^{+\infty} x^{n-1} $$
En posant $k = n-1$, l'indice va de 0 à $+\infty$ :
$$ S'(x) = \sum_{k=0}^{+\infty} x^k $$
C'est la série géométrique de raison $x$. Pour $|x| < 1$ :
$$ S'(x) = \frac{1}{1-x} $$
Pour obtenir $S(x)$, il faut intégrer $S'(x)$.
$$ S(x) = \int_0^x S'(t) dt + S(0) $$
On a $S(0) = \sum_{n=1}^{+\infty} \frac{0^n}{n} = 0$.
Donc :
$$ S(x) = \int_0^x \frac{1}{1-t} dt = \left[ -\ln(1-t) \right]_0^x = -\ln(1-x) - (-\ln(1)) = -\ln(1-x) $$
Ainsi, pour $x \in ]-1, 1[$, $\sum_{n=1}^{+\infty} \frac{x^n}{n} = -\ln(1-x)$.
