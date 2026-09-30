## Exercice 3 : Continuité et isométrie de l'opérateur de Fourier \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
Montrer que si l'on munit $L^1 \cap L^2$ de la norme $\|\cdot\|_{L^2}$, l'opérateur $\mathcal{F} : (L^1 \cap L^2, \|\cdot\|_2) \to (L^2, \|\cdot\|_2)$ est uniformément continu.

**Correction :**
Soit l'opérateur linéaire $\mathcal{F}$ restreint à $L^1 \cap L^2$, sous-espace de $L^2$.
Par l'identité de Plancherel pour les fonctions de l'espace de Schwartz $\mathcal{S}$ (qui est dense dans $L^1 \cap L^2$ pour la norme $\|\cdot\|_2$), nous savons que :
$$ \forall \phi \in \mathcal{S}, \quad \|\mathcal{F}(\phi)\|_2 = \sqrt{2\pi} \|\phi\|_2 $$
Soit $f \in L^1 \cap L^2$. Par densité, il existe une suite $(\phi_n)$ dans $\mathcal{S}$ telle que $\|\phi_n - f\|_2 \to 0$ et $\|\phi_n - f\|_1 \to 0$.
Par la continuité de $\mathcal{F}$ sur $L^1$ vers $L^\infty$, $\mathcal{F}(\phi_n) \to \mathcal{F}(f)$ ponctuellement (et uniformément).
Le lemme de Fatou permet de passer à la limite dans l'identité hilbertienne :
$$ \|\mathcal{F}(f)\|_2^2 \le \liminf_{n \to \infty} \|\mathcal{F}(\phi_n)\|_2^2 = \liminf_{n \to \infty} 2\pi \|\phi_n\|_2^2 = 2\pi \|f\|_2^2 $$
En fait, l'égalité stricte est maintenue (ce qui peut être prouvé en utilisant la complétude et la continuité du produit scalaire).
Dès lors, pour toute fonction $f \in L^1 \cap L^2$, l'opérateur satisfait :
$$ \|\mathcal{F}(f)\|_2 \le \sqrt{2\pi} \|f\|_2 $$
Pour la continuité uniforme, prenons $f, g \in L^1 \cap L^2$.
La linéarité de l'opérateur permet d'écrire :
$$ \|\mathcal{F}(f) - \mathcal{F}(g)\|_2 = \|\mathcal{F}(f - g)\|_2 $$
En appliquant la majoration de la norme à la fonction $h = f - g \in L^1 \cap L^2$ :
$$ \|\mathcal{F}(f) - \mathcal{F}(g)\|_2 \le \sqrt{2\pi} \|f - g\|_2 $$
Cette inégalité lipschitzienne montre que l'opérateur est globalement lipschitzien de rapport $\sqrt{2\pi}$, donc a fortiori uniformément continu. Cela garantit l'existence d'un unique prolongement continu à l'espace complet $L^2$.
