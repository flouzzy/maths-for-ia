# Exercice 7 : Série de Fourier du cosinus hyperbolique et déduction de série \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Déduire de l'Exercice 6 la série de Fourier de la fonction paire $g(t) = \cosh(\lambda t)$ sur $[-\pi, \pi]$. En déduire la somme $\sum_{n=1}^\infty \frac{1}{\lambda^2 + n^2}$.

**Correction Détaillée :**

1. \textbf{Calcul de la série par parité :}
   $g(t) = \frac{1}{2}(e^{\lambda t} + e^{-\lambda t})$. On peut sommer les séries de Fourier par linéarité.
   Mais plus directement, $g$ est paire donc $b_n = 0$.
   $$ a_n = c_n + c_{-n} = \frac{(-1)^n \sinh(\lambda\pi)}{\pi(\lambda^2 + n^2)} (\lambda + in + \lambda - in) = \frac{2\lambda (-1)^n \sinh(\lambda\pi)}{\pi(\lambda^2 + n^2)} $$
   Et pour $n=0$ : $a_0 = \frac{\sinh(\lambda\pi)}{\lambda\pi}$.
   La série trigonométrique est donc :
   $$ \cosh(\lambda t) = \frac{\sinh(\lambda\pi)}{\lambda\pi} + \frac{2\lambda\sinh(\lambda\pi)}{\pi} \sum_{n=1}^\infty \frac{(-1)^n}{\lambda^2 + n^2} \cos(nt) $$
   (Égalité stricte car $\cosh$ est continue et $C^1$ par morceaux).

2. \textbf{Évaluation en $t=\pi$ :}
   Pour retrouver la somme demandée, on évalue en $t=\pi$. On a $\cos(n\pi) = (-1)^n$, donc $(-1)^n \cos(n\pi) = 1$.
   $$ \cosh(\lambda\pi) = \frac{\sinh(\lambda\pi)}{\lambda\pi} + \frac{2\lambda\sinh(\lambda\pi)}{\pi} \sum_{n=1}^\infty \frac{1}{\lambda^2 + n^2} $$

3. \textbf{Isolement de la série :}
   On divise tout par $\frac{\sinh(\lambda\pi)}{\pi}$ :
   $$ \frac{\pi \cosh(\lambda\pi)}{\sinh(\lambda\pi)} = \frac{1}{\lambda} + 2\lambda \sum_{n=1}^\infty \frac{1}{\lambda^2 + n^2} $$
   $$ \pi \coth(\lambda\pi) = \frac{1}{\lambda} + 2\lambda \sum_{n=1}^\infty \frac{1}{\lambda^2 + n^2} $$
   Donc :
   $$ \sum_{n=1}^\infty \frac{1}{\lambda^2 + n^2} = \frac{\pi \coth(\lambda\pi) - 1/\lambda}{2\lambda} $$
