## Exercice 7 : Fonction $f(x)=e^{ax}$ sur $[-\pi, \pi[$ \quad \bigstar\bigstar\bigstar\bigstar\star

Soit $a \neq 0$ réel. On pose $f(x)=e^{ax}$ sur $[-\pi, \pi[$ prolongée par $2\pi$-périodicité. Calculer sa série de Fourier et en déduire la valeur de $\sum_{n=1}^\infty \frac{1}{a^2+n^2}$.

**Correction :**
Calculons $c_n(f) = \frac{1}{2\pi} \int_{-\pi}^\pi e^{ax}e^{-inx}dx = \frac{1}{2\pi} \left[ \frac{e^{(a-in)x}}{a-in} \right]_{-\pi}^\pi$.
$e^{(a-in)\pi} = e^{a\pi}(-1)^n$ et $e^{-(a-in)\pi} = e^{-a\pi}(-1)^n$.
$c_n(f) = \frac{(-1)^n}{2\pi(a-in)} (e^{a\pi} - e^{-a\pi}) = \frac{(-1)^n \sinh(a\pi)}{\pi(a-in)} = \frac{(-1)^n \sinh(a\pi)(a+in)}{\pi(a^2+n^2)}$.
En $x=0$, continue : $f(0) = 1 = \sum_{n \in \mathbb{Z}} c_n$.
$1 = c_0 + \sum_{n=1}^\infty (c_n + c_{-n}) = \frac{\sinh(a\pi)}{\pi a} + \sum_{n=1}^\infty \frac{2(-1)^n \sinh(a\pi) a}{\pi(a^2+n^2)}$.
En $x=\pi$, la somme est $\frac{e^{a\pi} + e^{-a\pi}}{2} = \cosh(a\pi)$.
$\cosh(a\pi) = \sum c_n e^{in\pi} = \sum c_n (-1)^n$.
$\cosh(a\pi) = \frac{\sinh(a\pi)}{\pi a} + \sum_{n=1}^\infty \frac{2\sinh(a\pi)a}{\pi(a^2+n^2)}$.
Donc $\sum_{n=1}^\infty \frac{1}{a^2+n^2} = \frac{\pi}{2a \tanh(a\pi)} - \frac{1}{2a^2}$.
