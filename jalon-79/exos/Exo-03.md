# Exercice 3 : Énergie d'un signal exponentiel $\bigstar\bigstar\star\star\star$
**Énoncé :** Soit $\alpha > 0$. On définit $f(t) = e^{\alpha t}$ sur $[-\pi, \pi[$, que l'on prolonge par $2\pi$-périodicité.
1. Calculer les coefficients de Fourier complexes $c_n(f)$.
2. En utilisant l'identité de Parseval, démontrer la relation :
   $$\sum_{n=-\infty}^\infty \frac{1}{\alpha^2 + n^2} = \frac{\pi}{\alpha \tanh(\alpha \pi)}$$

**Correction Détaillée :**
*Étape 1 : Calcul des coefficients $c_n(f)$.*
$$c_n(f) = \frac{1}{2\pi} \int_{-\pi}^\pi e^{\alpha t} e^{-int} dt = \frac{1}{2\pi} \int_{-\pi}^\pi e^{(\alpha - in)t} dt$$
$$c_n(f) = \frac{1}{2\pi (\alpha - in)} \left[ e^{(\alpha - in)t} \right]_{-\pi}^\pi = \frac{1}{2\pi (\alpha - in)} (e^{\alpha \pi} e^{-in\pi} - e^{-\alpha \pi} e^{in\pi})$$
Puisque $e^{in\pi} = e^{-in\pi} = (-1)^n$, on a :
$$c_n(f) = \frac{(-1)^n}{2\pi (\alpha - in)} (e^{\alpha \pi} - e^{-\alpha \pi}) = \frac{(-1)^n \sinh(\alpha \pi)}{\pi (\alpha - in)}$$

*Étape 2 : Énergie fréquentielle.*
Le module au carré du coefficient est :
$$|c_n(f)|^2 = \frac{\sinh^2(\alpha \pi)}{\pi^2 (\alpha^2 + n^2)}$$
La somme de la série est donc $\sum_{n=-\infty}^\infty \frac{\sinh^2(\alpha \pi)}{\pi^2 (\alpha^2 + n^2)}$.

*Étape 3 : Énergie temporelle.*
$$\frac{1}{2\pi} \int_{-\pi}^\pi |e^{\alpha t}|^2 dt = \frac{1}{2\pi} \int_{-\pi}^\pi e^{2\alpha t} dt = \frac{1}{2\pi} \left[ \frac{e^{2\alpha t}}{2\alpha} \right]_{-\pi}^\pi = \frac{e^{2\alpha \pi} - e^{-2\alpha \pi}}{4\pi \alpha} = \frac{\sinh(2\alpha \pi)}{2\pi \alpha}$$

*Étape 4 : Conclusion par Parseval.*
$$\frac{\sinh(2\alpha \pi)}{2\pi \alpha} = \frac{\sinh^2(\alpha \pi)}{\pi^2} \sum_{n=-\infty}^\infty \frac{1}{\alpha^2 + n^2}$$
Or $\sinh(2\alpha \pi) = 2 \sinh(\alpha \pi) \cosh(\alpha \pi)$.
$$\frac{2 \sinh(\alpha \pi) \cosh(\alpha \pi)}{2\pi \alpha} = \frac{\sinh^2(\alpha \pi)}{\pi^2} \sum_{n=-\infty}^\infty \frac{1}{\alpha^2 + n^2}$$
$$\frac{\cosh(\alpha \pi)}{\pi \alpha} = \frac{\sinh(\alpha \pi)}{\pi^2} \sum_{n=-\infty}^\infty \frac{1}{\alpha^2 + n^2}$$
$$\sum_{n=-\infty}^\infty \frac{1}{\alpha^2 + n^2} = \frac{\pi \cosh(\alpha \pi)}{\alpha \sinh(\alpha \pi)} = \frac{\pi}{\alpha \tanh(\alpha \pi)}$$
