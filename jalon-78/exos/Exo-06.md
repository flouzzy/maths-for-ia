# Produit de convolution et Fourier

$\bigstar\bigstar\bigstar\star\star$

Soient $f, g$ deux fonctions $2\pi$-périodiques et intégrables sur $[-\pi, \pi]$.
On définit le produit de convolution de $f$ et $g$, noté $f \ast g$, par :
$$ (f \ast g)(x) = \frac{1}{2\pi} \int_{-\pi}^\pi f(t) g(x-t) dt $$
Montrer que pour tout entier $n$, $c_n(f \ast g) = c_n(f) \cdot c_n(g)$.

**Correction détaillée :**
Par définition :
$$ c_n(f \ast g) = \frac{1}{2\pi} \int_{-\pi}^\pi (f \ast g)(x) e^{-inx} dx = \frac{1}{(2\pi)^2} \int_{-\pi}^\pi \left( \int_{-\pi}^\pi f(t) g(x-t) dt \right) e^{-inx} dx $$
On utilise le théorème de Fubini pour intervertir les intégrales (les fonctions sont dans $L^1$ sur le compact $[-\pi, \pi]$) :
$$ c_n(f \ast g) = \frac{1}{2\pi} \int_{-\pi}^\pi f(t) \left( \frac{1}{2\pi} \int_{-\pi}^\pi g(x-t) e^{-inx} dx \right) dt $$
Dans l'intégrale intérieure, on effectue le changement de variable $u = x - t \implies dx = du$. Pour un $t$ fixé, lorsque $x$ décrit $[-\pi, \pi]$, $u$ décrit $[-\pi-t, \pi-t]$. Comme la fonction $u \mapsto g(u) e^{-in(u+t)}$ est $2\pi$-périodique, l'intégrale sur tout intervalle de longueur $2\pi$ est identique à l'intégrale sur $[-\pi, \pi]$.
$$ \int_{-\pi}^\pi g(x-t) e^{-inx} dx = \int_{-\pi}^\pi g(u) e^{-in(u+t)} du = e^{-int} \int_{-\pi}^\pi g(u) e^{-inu} du = 2\pi e^{-int} c_n(g) $$
On remplace cela dans l'expression double :
$$ c_n(f \ast g) = \frac{1}{2\pi} \int_{-\pi}^\pi f(t) \left( e^{-int} c_n(g) \right) dt = c_n(g) \left( \frac{1}{2\pi} \int_{-\pi}^\pi f(t) e^{-int} dt \right) = c_n(g) c_n(f) $$
Le produit de convolution dans l'espace "temporel" correspond donc à une simple multiplication dans l'espace "fréquentiel". C'est un principe fondamental du filtrage.