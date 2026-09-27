# Exo 03 : Dérivation et coefficients de Fourier

**Difficulté :** \bigstar\bigstar\bigstar\star\star


Soit $f : \mathbb{R} \to \mathbb{R}$ une fonction $2\pi$-périodique de classe $C^1$.

Démontrer la relation entre les coefficients de Fourier de la dérivée $f'$ et ceux de $f$ :
$$ c_n(f') = i n c_n(f) \quad \forall n \in \mathbb{Z} $$

## Correction

On écrit la définition des coefficients de Fourier complexes pour $f'$ :
$$ c_n(f') = \frac{1}{2\pi} \int_0^{2\pi} f'(t) e^{-int} dt $$

Nous allons procéder par intégration par parties.
Posons :
$u(t) = e^{-int} \implies u'(t) = -in e^{-int}$
$v'(t) = f'(t) \implies v(t) = f(t)$

Les fonctions $u$ et $v$ sont de classe $C^1$ sur $[0, 2\pi]$, on peut appliquer la formule :
$$ \int_a^b u(t) v'(t) dt = [u(t)v(t)]_a^b - \int_a^b u'(t) v(t) dt $$

Appliquons-la à notre calcul :
$$ c_n(f') = \frac{1}{2\pi} \left( \left[ e^{-int} f(t) \right]_0^{2\pi} - \int_0^{2\pi} (-in e^{-int}) f(t) dt \right) $$

Évaluons le terme tout intégré :
$$ \left[ e^{-int} f(t) \right]_0^{2\pi} = e^{-2in\pi} f(2\pi) - e^0 f(0) $$
Puisque $n$ est un entier, $e^{-2in\pi} = 1$. De plus, $f$ est $2\pi$-périodique, donc $f(2\pi) = f(0)$.
Le terme tout intégré s'annule : $f(0) - f(0) = 0$.

Il reste l'intégrale :
$$ c_n(f') = \frac{1}{2\pi} \int_0^{2\pi} i n f(t) e^{-int} dt = i n \left( \frac{1}{2\pi} \int_0^{2\pi} f(t) e^{-int} dt \right) $$

On reconnaît exactement l'expression de $c_n(f)$. Donc :
$$ c_n(f') = i n c_n(f) $$

La dérivation dans le domaine temporel correspond donc à une simple multiplication par $in$ dans le domaine spectral.
