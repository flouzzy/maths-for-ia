## Exercice 5 : Produit de convolution de séries de Fourier \quad \bigstar\bigstar\bigstar\star\star

Soient $f$ et $g$ deux fonctions $2\pi$-périodiques continues. Montrer que $c_n(f * g) = 2\pi c_n(f)c_n(g)$.

**Correction :**
Le produit de convolution périodique est $(f*g)(x) = \frac{1}{2\pi} \int_{-\pi}^\pi f(t)g(x-t)dt$.
$c_n(f*g) = \frac{1}{2\pi} \int_{-\pi}^\pi \left( \frac{1}{2\pi} \int_{-\pi}^\pi f(t)g(x-t)dt \right) e^{-inx} dx$.
Par Fubini : $= \frac{1}{2\pi} \int_{-\pi}^\pi f(t) \left( \frac{1}{2\pi} \int_{-\pi}^\pi g(x-t)e^{-inx} dx \right) dt$.
Changement de variable $u = x-t$, $dx = du$, l'intégrale sur une période reste inchangée :
$\frac{1}{2\pi} \int_{-\pi}^\pi g(u)e^{-in(u+t)} du = e^{-int} \frac{1}{2\pi} \int_{-\pi}^\pi g(u)e^{-inu} du = e^{-int} c_n(g)$.
Donc $c_n(f*g) = \frac{1}{2\pi} \int_{-\pi}^\pi f(t) e^{-int} c_n(g) dt = c_n(g) \frac{1}{2\pi} \int_{-\pi}^\pi f(t) e^{-int} dt = c_n(g)c_n(f)$ (Attention au facteur $1/2\pi$ ou non selon la convention de $f*g$). Avec notre définition de convolution standard $\int f(t)g(x-t)$, le coefficient donne bien un produit simple modulo les constantes. Rigueur : la formule donne $c_n(f*g) = c_n(f)c_n(g)$ si la définition intègre la normalisation, ou $2\pi c_n$ sinon.
