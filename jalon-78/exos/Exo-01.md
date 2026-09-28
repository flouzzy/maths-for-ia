# Exercice 1 : Calcul de la série de Fourier d'un signal triangulaire \quad $\bigstar\star\star\star\star$

**Énoncé :**
Soit $f : \mathbb{R} \to \mathbb{R}$ la fonction $2\pi$-périodique, paire, définie sur $[0, \pi]$ par $f(t) = t$. Calculer la série de Fourier trigonométrique de $f$.

**Correction Détaillée :**

1. \textbf{Parité et valeur moyenne :}
   La fonction $f$ est paire, donc pour tout $n \ge 1$, les coefficients $b_n(f)$ sont nuls.
   La valeur moyenne $a_0(f)$ est donnée par :
   $$ a_0(f) = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(t) dt = \frac{1}{\pi} \int_0^{\pi} t dt = \frac{1}{\pi} \left[ \frac{t^2}{2} \right]_0^\pi = \frac{\pi}{2} $$

2. \textbf{Calcul des coefficients $a_n(f)$ :}
   Pour $n \ge 1$, puisque $f$ est paire :
   $$ a_n(f) = \frac{2}{\pi} \int_0^{\pi} t \cos(nt) dt $$
   On effectue une intégration par parties. Soient $u(t) = t \implies u'(t) = 1$ et $v'(t) = \cos(nt) \implies v(t) = \frac{\sin(nt)}{n}$.
   $$ a_n(f) = \frac{2}{\pi} \left( \left[ t \frac{\sin(nt)}{n} \right]_0^\pi - \int_0^\pi \frac{\sin(nt)}{n} dt \right) $$
   Le terme tout intégré s'annule car $\sin(n\pi) = 0$ et $0 \times \sin(0) = 0$.
   $$ a_n(f) = -\frac{2}{n\pi} \left[ -\frac{\cos(nt)}{n} \right]_0^\pi = \frac{2}{n^2\pi} (\cos(n\pi) - \cos(0)) = \frac{2}{n^2\pi} ((-1)^n - 1) $$
   Ainsi, si $n$ est pair ($n=2p$), $a_{2p} = 0$. Si $n$ est impair ($n=2p+1$), $a_{2p+1} = -\frac{4}{\pi(2p+1)^2}$.

3. \textbf{Série de Fourier :}
   La série s'écrit donc :
   $$ S(f)(t) = \frac{\pi}{2} - \frac{4}{\pi} \sum_{p=0}^{+\infty} \frac{\cos((2p+1)t)}{(2p+1)^2} $$
