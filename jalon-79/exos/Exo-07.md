# Exercice 7 : Optimisation dans un sous-espace de dimension finie $\bigstar\bigstar\bigstar\bigstar\star$
**Énoncé :** Soit $f(t) = |t|$ sur $[-\pi, \pi]$.
On cherche les coefficients $\alpha, \beta, \gamma \in \mathbb{R}$ qui minimisent l'intégrale :
$$I(\alpha, \beta, \gamma) = \int_{-\pi}^\pi ( |t| - \alpha - \beta \cos(t) - \gamma \sin(t) )^2 dt$$
En justifiant par la géométrie hilbertienne, trouver $\alpha, \beta, \gamma$.

**Correction Détaillée :**
*Étape 1 : Interprétation géométrique.*
On se place dans l'espace de Hilbert $L^2([-\pi, \pi])$ avec le produit scalaire standard.
L'intégrale $I(\alpha, \beta, \gamma)$ représente (à un facteur de normalisation $2\pi$ près) le carré de la distance $L^2$ entre la fonction $f(t) = |t|$ et une fonction $g(t) = \alpha \cdot 1 + \beta \cos(t) + \gamma \sin(t)$.
La fonction $g$ appartient au sous-espace $H_1 = \text{Vect}(1, \cos(t), \sin(t))$.

*Étape 2 : Projection orthogonale.*
Le théorème de projection sur un sous-espace fermé (ici de dimension finie) d'un espace de Hilbert garantit que la distance est minimisée de manière unique lorsque $g$ est la projection orthogonale de $f$ sur $H_1$.
Or, on sait que la projection orthogonale d'une fonction sur les harmoniques trigonométriques est donnée précisément par la somme partielle de Fourier d'ordre 1.
Ainsi, les coefficients optimaux sont exactement les coefficients de Fourier correspondants :
- $\alpha = \frac{a_0(f)}{2}$
- $\beta = a_1(f)$
- $\gamma = b_1(f)$

*Étape 3 : Calcul des coefficients.*
$f(t) = |t|$ est paire, donc $\gamma = b_1 = 0$.
$$a_0 = \frac{1}{\pi} \int_{-\pi}^\pi |t| dt = \frac{2}{\pi} \int_0^\pi t dt = \frac{2}{\pi} \frac{\pi^2}{2} = \pi$$
Donc $\alpha = \frac{\pi}{2}$.
$$a_1 = \frac{2}{\pi} \int_0^\pi t \cos(t) dt$$
Par intégration par parties ($u=t, v'=\cos(t)$) :
$$a_1 = \frac{2}{\pi} \left( [t \sin(t)]_0^\pi - \int_0^\pi \sin(t) dt \right) = \frac{2}{\pi} ( 0 - [-\cos(t)]_0^\pi ) = \frac{2}{\pi} ( 0 - (1 - (-1)) ) = -\frac{4}{\pi}$$
Donc $\beta = -\frac{4}{\pi}$.

*Étape 4 : Conclusion.*
Le minimum de l'intégrale est atteint pour $(\alpha, \beta, \gamma) = \left(\frac{\pi}{2}, -\frac{4}{\pi}, 0\right)$.
