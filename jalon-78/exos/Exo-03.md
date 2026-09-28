# Exercice 3 : Fonction exponentielle sur un intervalle $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $h$ la fonction $2\pi$-périodique, telle que $h(t) = e^{at}$ pour $t \in ]-\pi, \pi]$ (avec $a \in \mathbb{R}^*$).
Calculer les coefficients de Fourier complexes $c_n(h)$ et écrire la série associée.

**Correction Détaillée :**
Calculons $c_n(h)$ :
$$ c_n = \frac{1}{2\pi} \int_{-\pi}^{\pi} e^{at} e^{-int} dt = \frac{1}{2\pi} \int_{-\pi}^{\pi} e^{(a-in)t} dt $$
La primitive est évidente car $a - in \neq 0$ :
$$ c_n = \frac{1}{2\pi (a-in)} \left[ e^{(a-in)t} \right]_{-\pi}^\pi $$
Or, $e^{-in\pi} = e^{in\pi} = (-1)^n$. Ainsi :
$$ e^{(a-in)\pi} - e^{-(a-in)\pi} = (-1)^n e^{a\pi} - (-1)^n e^{-a\pi} = (-1)^n (e^{a\pi} - e^{-a\pi}) = 2(-1)^n \sinh(a\pi) $$
D'où :
$$ c_n = \frac{(-1)^n \sinh(a\pi)}{\pi (a-in)} = \frac{(-1)^n \sinh(a\pi) (a+in)}{\pi (a^2+n^2)} $$
La série de Fourier (complexe) est donc :
$$ S(h)(t) = \sum_{n=-\infty}^{+\infty} \frac{(-1)^n \sinh(a\pi) (a+in)}{\pi (a^2+n^2)} e^{int} $$
