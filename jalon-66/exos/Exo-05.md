# Exercice 5 : Intégrale sur un ensemble infini \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Calculer l'intégrale de $f(x) = 2^{-x}$ sur $[0, +\infty[$ par rapport à la mesure de comptage restreinte aux entiers $\mu = \sum_{n=0}^\infty \delta_n$.

**Correction :**
L'intégrale de $f$ par rapport à cette mesure est par définition la somme de la série évaluée aux entiers positifs.

$\int_{[0,+\infty[} f \, d\mu = \sum_{n=0}^\infty f(n) = \sum_{n=0}^\infty 2^{-n}$.

C'est la somme d'une série géométrique de raison $q = \frac{1}{2}$.

Puisque $|q| < 1$, la série converge et sa somme est :
$S = \frac{\text{premier terme}}{1 - q} = \frac{1}{1 - 1/2} = \frac{1}{1/2} = 2$.

L'intégrale vaut donc 2.
