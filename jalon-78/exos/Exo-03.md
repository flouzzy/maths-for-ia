# Exercice 3 : Fonction parabolique \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $f$ la fonction $2\pi$-périodique définie par $f(t) = t^2$ sur $[-\pi, \pi]$. Calculer sa série de Fourier.

**Correction Détaillée :**

1. \textbf{Parité et valeur moyenne :}
   La fonction est paire, donc $b_n = 0$ pour tout $n \ge 1$.
   Calculons la valeur moyenne :
   $$ a_0 = \frac{1}{2\pi} \int_{-\pi}^\pi t^2 dt = \frac{1}{\pi} \int_0^\pi t^2 dt = \frac{1}{\pi} \left[ \frac{t^3}{3} \right]_0^\pi = \frac{\pi^2}{3} $$

2. \textbf{Calcul des coefficients $a_n$ :}
   Pour $n \ge 1$, on a :
   $$ a_n = \frac{2}{\pi} \int_0^\pi t^2 \cos(nt) dt $$
   On réalise une double intégration par parties.
   Première IPP ($u=t^2, v'=\cos(nt)$) :
   $$ a_n = \frac{2}{\pi} \left( \left[ t^2 \frac{\sin(nt)}{n} \right]_0^\pi - \int_0^\pi 2t \frac{\sin(nt)}{n} dt \right) $$
   Le terme aux bornes est nul (car $\sin(n\pi)=0$).
   $$ a_n = -\frac{4}{n\pi} \int_0^\pi t \sin(nt) dt $$
   Deuxième IPP ($u=t, v'=\sin(nt)$) :
   $$ a_n = -\frac{4}{n\pi} \left( \left[ -t \frac{\cos(nt)}{n} \right]_0^\pi - \int_0^\pi -\frac{\cos(nt)}{n} dt \right) $$
   L'intégrale restante donne $[\frac{\sin(nt)}{n^2}]_0^\pi = 0$. Le terme aux bornes est :
   $$ a_n = -\frac{4}{n\pi} \left( -\frac{\pi \cos(n\pi)}{n} - 0 \right) = \frac{4}{n^2} (-1)^n $$

3. \textbf{Synthèse de la série :}
   La fonction $f$ étant continue et $C^1$ par morceaux, Dirichlet donne :
   $$ t^2 = \frac{\pi^2}{3} + 4 \sum_{n=1}^{+\infty} \frac{(-1)^n}{n^2} \cos(nt) \quad \text{pour } t \in [-\pi, \pi] $$
