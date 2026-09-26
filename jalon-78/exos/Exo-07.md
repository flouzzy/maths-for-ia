# Exercice 7 : Action de l'opérateur de dérivation

**Difficulté :** \bigstar\bigstar\bigstar\bigstar\star

**Énoncé :**
Soit $f : \mathbb{R} \to \mathbb{C}$ une fonction $2\pi$-périodique, de classe $C^1$.
1. Montrer que $c_n(f') = in c_n(f)$ pour tout $n \in \mathbb{Z}$.
2. En déduire que les coefficients de Fourier de $f$ vérifient $c_n(f) = o(1/n)$ lorsque $|n| \to +\infty$.

**Correction :**
1. Par définition, les coefficients de Fourier de la dérivée $f'$ sont :
   $$c_n(f') = \frac{1}{2\pi} \int_0^{2\pi} f'(t) e^{-int} dt$$
   Puisque $f$ est de classe $C^1$, nous effectuons une intégration par parties avec $u = e^{-int}$ et $v' = f'$, de sorte que $u' = -in e^{-int}$ et $v = f$.
   $$c_n(f') = \frac{1}{2\pi} \left( \left[ f(t) e^{-int} \right]_0^{2\pi} - \int_0^{2\pi} f(t) (-in) e^{-int} dt \right)$$
   Le terme tout intégré s'écrit $\frac{1}{2\pi} (f(2\pi) e^{-in 2\pi} - f(0) e^0)$. Puisque $f$ est $2\pi$-périodique, $f(2\pi) = f(0)$ et $e^{-2in\pi} = 1$, le terme s'annule strictement.
   $$c_n(f') = \frac{in}{2\pi} \int_0^{2\pi} f(t) e^{-int} dt = in c_n(f)$$
2. La fonction $f'$ est continue, donc de carré intégrable. Par le Lemme de Riemann-Lebesgue (ou l'inégalité de Bessel appliquée à $f'$), on sait que les coefficients de Fourier $c_n(f')$ tendent vers $0$ quand $|n| \to \infty$.
   Or, $c_n(f') = in c_n(f) \implies c_n(f) = \frac{c_n(f')}{in}$.
   Comme $c_n(f') \to 0$, nous avons $n c_n(f) \to 0$, ce qui signifie exactement que $c_n(f) = o(1/n)$.
