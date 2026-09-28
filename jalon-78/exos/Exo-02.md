# Exercice 2 : Calcul élémentaire pour un signal impair

**Difficulté :** \bigstar\star\star\star\star

**Énoncé :**
Soit $f$ la fonction $2\pi$-périodique, impaire, définie sur $]0, \pi[$ par $f(t) = \pi - t$. On pose $f(0) = f(\pi) = 0$.
1. Calculer les coefficients de Fourier trigonométriques de $f$.
2. Écrire la série de Fourier associée.

**Correction :**
1. La fonction étant impaire sur $[-\pi, \pi]$ à un ensemble de mesure nulle près, tous les coefficients $a_n$ ($n \ge 0$) sont nuls.
   Calculons les coefficients $b_n$ pour $n \ge 1$ :
   $$b_n = \frac{1}{\pi} \int_{-\pi}^\pi f(t) \sin(nt) dt = \frac{2}{\pi} \int_0^\pi (\pi - t) \sin(nt) dt$$
   On utilise une intégration par parties avec $u(t) = \pi - t$ et $v'(t) = \sin(nt)$, ce qui donne $u'(t) = -1$ et $v(t) = -\frac{\cos(nt)}{n}$.
   $$b_n = \frac{2}{\pi} \left( \left[ -(\pi - t) \frac{\cos(nt)}{n} \right]_0^\pi - \int_0^\pi (-1) \left(-\frac{\cos(nt)}{n}\right) dt \right)$$
   En $t=\pi$, le terme est $0$. En $t=0$, le terme est $-\pi \frac{1}{n}$. Ainsi :
   $$b_n = \frac{2}{\pi} \left( \frac{\pi}{n} - \int_0^\pi \frac{\cos(nt)}{n} dt \right)$$
   $$b_n = \frac{2}{n} - \frac{2}{\pi} \left[ \frac{\sin(nt)}{n^2} \right]_0^\pi = \frac{2}{n}$$
2. La série de Fourier est :
   $$S(f)(t) = \sum_{n=1}^{+\infty} \frac{2}{n} \sin(nt)$$
