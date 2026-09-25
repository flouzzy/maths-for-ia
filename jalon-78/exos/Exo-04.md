# Exercice 4 : Problème de Bâle via Fourier \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
En utilisant le résultat de l'Exercice 3, démontrer la formule $\sum_{n=1}^{+\infty} \frac{1}{n^2} = \frac{\pi^2}{6}$.

**Correction Détaillée :**

1. \textbf{Choix du point d'évaluation :}
   On repart de la série de la fonction $f(t) = t^2$ sur $[-\pi, \pi]$ :
   $$ f(t) = \frac{\pi^2}{3} + 4 \sum_{n=1}^{+\infty} \frac{(-1)^n}{n^2} \cos(nt) $$
   Pour éliminer le terme alterné $(-1)^n$, le choix optimal est $t = \pi$, car $\cos(n\pi) = (-1)^n$.

2. \textbf{Calcul de la série évaluée :}
   On a $f(\pi) = \pi^2$.
   En injectant $t=\pi$ dans la série :
   $$ \pi^2 = \frac{\pi^2}{3} + 4 \sum_{n=1}^{+\infty} \frac{(-1)^n}{n^2} (-1)^n $$
   Or $(-1)^n \times (-1)^n = (-1)^{2n} = 1$.
   $$ \pi^2 - \frac{\pi^2}{3} = 4 \sum_{n=1}^{+\infty} \frac{1}{n^2} $$
   $$ \frac{2\pi^2}{3} = 4 \sum_{n=1}^{+\infty} \frac{1}{n^2} $$

3. \textbf{Conclusion :}
   En divisant par 4 :
   $$ \sum_{n=1}^{+\infty} \frac{1}{n^2} = \frac{2\pi^2}{3 \times 4} = \frac{\pi^2}{6} $$
   C'est la solution classique apportée par Euler au problème de Bâle.
