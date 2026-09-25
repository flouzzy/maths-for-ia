# Exercice 6 : Fonction exponentielle périodisée \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $\lambda > 0$. On définit $f$ sur $[-\pi, \pi[$ par $f(t) = e^{\lambda t}$ et on la prolonge par $2\pi$-périodicité. Calculer sa série de Fourier.

**Correction Détaillée :**

1. \textbf{Choix des coefficients :}
   Pour une fonction exponentielle, les coefficients complexes $c_n$ sont beaucoup plus simples à calculer car l'exponentielle réelle et l'exponentielle complexe fusionnent.
   $$ c_n = \frac{1}{2\pi} \int_{-\pi}^\pi e^{\lambda t} e^{-int} dt = \frac{1}{2\pi} \int_{-\pi}^\pi e^{(\lambda - in)t} dt $$

2. \textbf{Intégration directe :}
   $$ c_n = \frac{1}{2\pi} \left[ \frac{e^{(\lambda - in)t}}{\lambda - in} \right]_{-\pi}^\pi = \frac{e^{(\lambda - in)\pi} - e^{-(\lambda - in)\pi}}{2\pi(\lambda - in)} $$
   Sachant que $e^{-in\pi} = (-1)^n$ et $e^{in\pi} = (-1)^n$ :
   $$ c_n = \frac{(-1)^n (e^{\lambda\pi} - e^{-\lambda\pi})}{2\pi(\lambda - in)} = \frac{(-1)^n \sinh(\lambda\pi)}{\pi} \frac{1}{\lambda - in} $$

3. \textbf{Forme algébrique propre du coefficient :}
   Pour enlever le $i$ du dénominateur, on multiplie en haut et en bas par le conjugué $\lambda + in$ :
   $$ c_n = \frac{(-1)^n \sinh(\lambda\pi)}{\pi} \frac{\lambda + in}{\lambda^2 + n^2} $$

4. \textbf{Écriture de la série :}
   La série s'écrit donc :
   $$ S(f)(t) = \frac{\sinh(\lambda\pi)}{\pi} \sum_{n=-\infty}^{+\infty} \frac{(-1)^n (\lambda + in)}{\lambda^2 + n^2} e^{int} $$
