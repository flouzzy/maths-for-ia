# Exo 02 : Coefficient complexes d'un décalage

**Difficulté :** \bigstar\bigstar\star\star\star


Soit $f \in L^1_{per}(0, 2\pi)$ de coefficients de Fourier complexes $c_n(f)$.
On définit la fonction décalée $g(t) = f(t - \tau)$ pour un certain réel $\tau$.

Calculer les coefficients de Fourier $c_n(g)$ en fonction des $c_n(f)$.

## Correction

Par définition, le $n$-ième coefficient complexe de $g$ est :
$$ c_n(g) = \frac{1}{2\pi} \int_0^{2\pi} g(t) e^{-int} dt = \frac{1}{2\pi} \int_0^{2\pi} f(t - \tau) e^{-int} dt $$

Effectuons le changement de variable $u = t - \tau$.
Les bornes d'intégration deviennent $-\tau$ et $2\pi - \tau$.
La différentielle est $dt = du$.
Le terme exponentiel devient $e^{-in(u + \tau)} = e^{-inu} e^{-in\tau}$.
L'intégrale se réécrit :
$$ c_n(g) = \frac{1}{2\pi} \int_{-\tau}^{2\pi-\tau} f(u) e^{-in(u+\tau)} du = e^{-in\tau} \left( \frac{1}{2\pi} \int_{-\tau}^{2\pi-\tau} f(u) e^{-inu} du \right) $$

Puisque la fonction $u \mapsto f(u) e^{-inu}$ est $2\pi$-périodique, son intégrale sur n'importe quel intervalle de longueur $2\pi$ est la même. En particulier, elle est égale à l'intégrale sur $[0, 2\pi]$.
$$ c_n(g) = e^{-in\tau} \left( \frac{1}{2\pi} \int_0^{2\pi} f(u) e^{-inu} du \right) $$

On reconnaît l'expression de $c_n(f)$. Par conséquent :
$$ c_n(g) = e^{-in\tau} c_n(f) $$

Un décalage temporel d'un signal correspond donc à une multiplication par une phase pure $e^{-in\tau}$ dans le domaine spectral, sans modification de l'amplitude $|c_n|$.
