# Exercice 9 : Intégration et dérivation des séries de Fourier \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit $f$ de classe $C^1$ et $2\pi$-périodique. Prouver rigoureusement la relation entre les coefficients complexes $c_n(f')$ et $c_n(f)$.

**Correction Détaillée :**

1. \textbf{Définition de $c_n(f')$ :}
   Par définition :
   $$ c_n(f') = \frac{1}{2\pi} \int_0^{2\pi} f'(t) e^{-int} dt $$

2. \textbf{Intégration par parties :}
   Puisque $f$ est de classe $C^1$, on peut effectuer une intégration par parties avec $u(t) = e^{-int} \implies u'(t) = -in e^{-int}$ et $v'(t) = f'(t) \implies v(t) = f(t)$.
   $$ c_n(f') = \frac{1}{2\pi} \left( \left[ f(t) e^{-int} \right]_0^{2\pi} - \int_0^{2\pi} f(t) (-in) e^{-int} dt \right) $$

3. \textbf{Annulation du terme de bord :}
   Évaluons le terme entre crochets :
   $$ \left[ f(t) e^{-int} \right]_0^{2\pi} = f(2\pi) e^{-in2\pi} - f(0) e^0 $$
   Puisque $n$ est entier, $e^{-i2\pi n} = 1$. Et par périodicité de $f$, on a $f(2\pi) = f(0)$.
   Donc ce terme vaut $f(0) - f(0) = 0$.

4. \textbf{Conclusion :}
   L'expression restante est :
   $$ c_n(f') = \frac{1}{2\pi} \int_0^{2\pi} in f(t) e^{-int} dt = in \left( \frac{1}{2\pi} \int_0^{2\pi} f(t) e^{-int} dt \right) $$
   D'où la relation fondamentale :
   $$ c_n(f') = in \, c_n(f) $$
   Cela signifie que la dérivation temporelle correspond à une multiplication par $in$ dans l'espace des fréquences.
