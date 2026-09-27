# Exo 08 : Identité de Parseval approchée sur l'exponentielle complexe

**Difficulté :** \bigstar\bigstar\bigstar\bigstar\star


Soit $f$ la fonction $2\pi$-périodique définie sur $]-\pi, \pi]$ par $f(t) = e^{at}$ avec $a \in \mathbb{R}^*$.
Calculer ses coefficients de Fourier complexes $c_n(f)$.

## Correction

La fonction est $2\pi$-périodique. Les coefficients sont donnés par :
$$ c_n(f) = \frac{1}{2\pi} \int_{-\pi}^\pi f(t) e^{-int} dt = \frac{1}{2\pi} \int_{-\pi}^\pi e^{at} e^{-int} dt $$
$$ c_n(f) = \frac{1}{2\pi} \int_{-\pi}^\pi e^{(a - in)t} dt $$

La fonction à intégrer est l'exponentielle complexe, sa primitive immédiate est $\frac{e^{(a-in)t}}{a-in}$ :
$$ c_n(f) = \frac{1}{2\pi} \left[ \frac{e^{(a-in)t}}{a-in} \right]_{-\pi}^\pi $$
$$ c_n(f) = \frac{1}{2\pi (a-in)} \left( e^{(a-in)\pi} - e^{-(a-in)\pi} \right) $$

Simplifions le terme $e^{\pm in\pi}$ :
$e^{in\pi} = \cos(n\pi) + i\sin(n\pi) = (-1)^n$.
De même $e^{-in\pi} = (-1)^n$.
Donc :
$$ e^{(a-in)\pi} = e^{a\pi} e^{-in\pi} = e^{a\pi} (-1)^n $$
$$ e^{-(a-in)\pi} = e^{-a\pi} e^{in\pi} = e^{-a\pi} (-1)^n $$

En remplaçant :
$$ c_n(f) = \frac{(-1)^n}{2\pi (a-in)} (e^{a\pi} - e^{-a\pi}) $$
Sachant que $\sinh(x) = \frac{e^x - e^{-x}}{2}$, on a $e^{a\pi} - e^{-a\pi} = 2\sinh(a\pi)$.
$$ c_n(f) = \frac{(-1)^n \sinh(a\pi)}{\pi(a-in)} $$

Pour mettre sous la forme $x+iy$, on multiplie par le conjugué $a+in$ au numérateur et au dénominateur :
$$ c_n(f) = \frac{(-1)^n \sinh(a\pi) (a+in)}{\pi(a^2+n^2)} $$

Cette expression analytique compacte permet de développer n'importe quelle exponentielle en série de Fourier.
