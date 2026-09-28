# Exercice 1 : Calcul élémentaire pour un signal pair

**Difficulté :** \bigstar\star\star\star\star

**Énoncé :**
Soit $f$ la fonction $2\pi$-périodique, paire, définie sur $[0, \pi]$ par $f(t) = 1 - \frac{t}{\pi}$.
1. Représenter graphiquement $f$ sur $[-2\pi, 2\pi]$.
2. Déterminer les coefficients de Fourier réels de $f$.
3. Écrire la série de Fourier associée.

**Correction :**
1. La fonction est périodique de période $2\pi$. Sur $[-\pi, \pi]$, par parité, $f(t) = 1 - \frac{|t|}{\pi}$. Le graphe forme des "dents de scie" continues (triangles de hauteur 1 aux multiples pairs de $\pi$ et 0 aux multiples impairs de $\pi$).
2. La fonction étant paire, les coefficients $b_n$ sont nuls pour tout $n \ge 1$.
   Calcul de $a_0$ :
   $$a_0 = \frac{1}{\pi} \int_{-\pi}^\pi f(t) dt = \frac{2}{\pi} \int_0^\pi \left(1 - \frac{t}{\pi}\right) dt = \frac{2}{\pi} \left[ t - \frac{t^2}{2\pi} \right]_0^\pi = \frac{2}{\pi} \left( \pi - \frac{\pi}{2} \right) = 1$$
   Calcul de $a_n$ pour $n \ge 1$ :
   $$a_n = \frac{1}{\pi} \int_{-\pi}^\pi f(t) \cos(nt) dt = \frac{2}{\pi} \int_0^\pi \left(1 - \frac{t}{\pi}\right) \cos(nt) dt$$
   On procède par intégration par parties. Posons $u(t) = 1 - \frac{t}{\pi}$ et $v'(t) = \cos(nt)$, de sorte que $u'(t) = -\frac{1}{\pi}$ et $v(t) = \frac{\sin(nt)}{n}$.
   $$a_n = \frac{2}{\pi} \left( \left[ \left(1 - \frac{t}{\pi}\right) \frac{\sin(nt)}{n} \right]_0^\pi - \int_0^\pi \left(-\frac{1}{\pi}\right) \frac{\sin(nt)}{n} dt \right)$$
   Le terme de bord s'annule car $\sin(n\pi) = 0$ et $\sin(0) = 0$.
   $$a_n = \frac{2}{\pi^2 n} \int_0^\pi \sin(nt) dt = \frac{2}{\pi^2 n} \left[ -\frac{\cos(nt)}{n} \right]_0^\pi = \frac{2}{\pi^2 n^2} (1 - (-1)^n)$$
   Si $n$ est pair ($n = 2p$), $a_{2p} = 0$.
   Si $n$ est impair ($n = 2p+1$), $a_{2p+1} = \frac{4}{\pi^2 (2p+1)^2}$.
3. La série de Fourier de $f$ est :
   $$S(f)(t) = \frac{1}{2} + \frac{4}{\pi^2} \sum_{p=0}^{+\infty} \frac{\cos((2p+1)t)}{(2p+1)^2}$$
