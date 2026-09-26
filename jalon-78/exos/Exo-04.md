# Coefficients exponentiels et fonction en e^(at)

$\bigstar\bigstar\star\star\star$

Soit $\alpha > 0$. Soit $f$ la fonction $2\pi$-périodique, telle que sur $]-\pi, \pi]$, $f(t) = e^{\alpha t}$.
1. Calculer les coefficients de Fourier exponentiels $c_n(f)$.
2. En déduire la série de Fourier de $f$ sous forme trigonométrique.
3. Évaluer la somme de la série $\sum_{n=1}^{+\infty} \frac{1}{\alpha^2 + n^2}$.

**Correction détaillée :**
1. Calcul de $c_n(f)$ :
   $$ c_n(f) = \frac{1}{2\pi} \int_{-\pi}^\pi e^{\alpha t} e^{-int} dt = \frac{1}{2\pi} \int_{-\pi}^\pi e^{(\alpha - in)t} dt $$
   $$ c_n(f) = \frac{1}{2\pi} \left[ \frac{e^{(\alpha - in)t}}{\alpha - in} \right]_{-\pi}^\pi = \frac{1}{2\pi(\alpha - in)} (e^{(\alpha - in)\pi} - e^{-(\alpha - in)\pi}) $$
   Or $e^{-in\pi} = (-1)^n$ et $e^{in\pi} = (-1)^n$.
   $$ c_n(f) = \frac{(-1)^n}{2\pi(\alpha - in)} (e^{\alpha\pi} - e^{-\alpha\pi}) = \frac{(-1)^n \sinh(\alpha\pi)}{\pi(\alpha - in)} = \frac{(-1)^n \sinh(\alpha\pi)(\alpha + in)}{\pi(\alpha^2 + n^2)} $$
2. On passe aux coefficients trigonométriques : $a_n = c_n + c_{-n}$ et $b_n = i(c_n - c_{-n})$.
   $$ a_n = \frac{(-1)^n \sinh(\alpha\pi)}{\pi(\alpha^2 + n^2)} ( \alpha + in + \alpha - in ) = \frac{2\alpha (-1)^n \sinh(\alpha\pi)}{\pi(\alpha^2 + n^2)} $$
   $$ b_n = i \frac{(-1)^n \sinh(\alpha\pi)}{\pi(\alpha^2 + n^2)} ( \alpha + in - (\alpha - in) ) = i \frac{(-1)^n \sinh(\alpha\pi)}{\pi(\alpha^2 + n^2)} (2in) = -\frac{2n (-1)^n \sinh(\alpha\pi)}{\pi(\alpha^2 + n^2)} $$
   $a_0 = \frac{2\sinh(\alpha\pi)}{\pi\alpha}$.
3. Par Dirichlet en $t=\pi$, point de discontinuité :
   $$ \frac{f(\pi^+) + f(\pi^-)}{2} = \frac{e^{-\alpha\pi} + e^{\alpha\pi}}{2} = \cosh(\alpha\pi) $$
   D'autre part, la série en $\pi$ donne :
   $$ \cosh(\alpha\pi) = \frac{\sinh(\alpha\pi)}{\pi\alpha} + \sum_{n=1}^{+\infty} \frac{2\alpha (-1)^n \sinh(\alpha\pi)}{\pi(\alpha^2 + n^2)} \cos(n\pi) $$
   Puisque $\cos(n\pi) = (-1)^n$, $(-1)^n \cos(n\pi) = 1$.
   $$ \cosh(\alpha\pi) = \frac{\sinh(\alpha\pi)}{\pi\alpha} + \frac{2\alpha\sinh(\alpha\pi)}{\pi} \sum_{n=1}^{+\infty} \frac{1}{\alpha^2 + n^2} $$
   En divisant par $\sinh(\alpha\pi) \neq 0$ :
   $$ \coth(\alpha\pi) = \frac{1}{\pi\alpha} + \frac{2\alpha}{\pi} \sum_{n=1}^{+\infty} \frac{1}{\alpha^2 + n^2} \implies \sum_{n=1}^{+\infty} \frac{1}{\alpha^2 + n^2} = \frac{\pi}{2\alpha} \coth(\alpha\pi) - \frac{1}{2\alpha^2} $$