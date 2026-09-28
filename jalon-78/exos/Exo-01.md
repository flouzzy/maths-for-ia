# Exercice 1 : Calcul direct sur un signal créneau $\bigstar\star\star\star\star$

**Énoncé :**
Soit $f$ la fonction $2\pi$-périodique définie sur $]-\pi, \pi]$ par :
$$ f(t) = 1 \text{ si } t \in [0, \pi] \text{, et } f(t) = -1 \text{ si } t \in ]-\pi, 0[ $$
1. Étudier la parité de $f$.
2. Déterminer la série de Fourier de $f$.

**Correction Détaillée :**
1. **Parité :**
Pour tout $t \in ]0, \pi[$, $-t \in ]-\pi, 0[$. On a $f(-t) = -1 = -f(t)$.
Ainsi, $f$ est impaire. Par conséquent, les coefficients $a_n(f)$ sont nuls pour tout $n \ge 0$.

2. **Série de Fourier :**
Calculons les coefficients $b_n$ pour $n \ge 1$ :
$$ b_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(t) \sin(nt) dt = \frac{2}{\pi} \int_{0}^{\pi} 1 \cdot \sin(nt) dt $$
$$ b_n = \frac{2}{\pi} \left[ \frac{-\cos(nt)}{n} \right]_0^\pi = \frac{2}{n\pi} (1 - \cos(n\pi)) = \frac{2}{n\pi} (1 - (-1)^n) $$
Si $n$ est pair ($n=2k$), $b_{2k} = 0$.
Si $n$ est impair ($n=2k+1$), $b_{2k+1} = \frac{4}{(2k+1)\pi}$.
La série de Fourier est :
$$ S(f)(t) = \frac{4}{\pi} \sum_{k=0}^{+\infty} \frac{\sin((2k+1)t)}{2k+1} $$
