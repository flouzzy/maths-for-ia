# Exercice 8 : Produit de convolution de séries de Fourier

**Difficulté :** \bigstar\bigstar\bigstar\bigstar\star

**Énoncé :**
Soient $f$ et $g$ deux fonctions $2\pi$-périodiques continues. On définit leur produit de convolution $h = f * g$ par :
$$h(x) = \frac{1}{2\pi} \int_0^{2\pi} f(t) g(x-t) dt$$
Montrer que $c_n(h) = c_n(f) c_n(g)$ pour tout $n \in \mathbb{Z}$.

**Correction :**
Calculons le coefficient de Fourier de $h$ :
$$c_n(h) = \frac{1}{2\pi} \int_0^{2\pi} h(x) e^{-inx} dx = \frac{1}{2\pi} \int_0^{2\pi} \left( \frac{1}{2\pi} \int_0^{2\pi} f(t) g(x-t) dt \right) e^{-inx} dx$$
En invoquant le théorème de Fubini (les fonctions étant continues, l'intégrale double est absolument convergente), on intervertit les intégrales :
$$c_n(h) = \frac{1}{(2\pi)^2} \int_0^{2\pi} f(t) \left( \int_0^{2\pi} g(x-t) e^{-inx} dx \right) dt$$
Faisons le changement de variable $u = x - t$ dans l'intégrale interne (donc $dx = du$). Puisque les fonctions à intégrer sont $2\pi$-périodiques, l'intégrale sur $[ -t, 2\pi-t ]$ est égale à l'intégrale sur $[ 0, 2\pi ]$.
$$\int_0^{2\pi} g(x-t) e^{-inx} dx = \int_0^{2\pi} g(u) e^{-in(u+t)} du = e^{-int} \int_0^{2\pi} g(u) e^{-inu} du = 2\pi e^{-int} c_n(g)$$
On réinjecte cette expression dans l'intégrale externe :
$$c_n(h) = \frac{1}{(2\pi)^2} \int_0^{2\pi} f(t) \left( 2\pi e^{-int} c_n(g) \right) dt = c_n(g) \frac{1}{2\pi} \int_0^{2\pi} f(t) e^{-int} dt = c_n(g) c_n(f)$$
Ainsi, $c_n(h) = c_n(f) c_n(g)$. Ce résultat fondamental justifie l'utilisation des séries de Fourier dans l'étude des filtres linéaires.
