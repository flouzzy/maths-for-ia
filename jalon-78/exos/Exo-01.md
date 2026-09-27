# Exo 01 : Calcul de coefficients fondamentaux (Signal Carré)

**Difficulté :** \bigstar\star\star\star\star


Soit $f$ la fonction $2\pi$-périodique définie sur $]-\pi, \pi]$ par :
$$ f(t) = \begin{cases} 1 & \text{si } t \in [0, \pi[ \\ -1 & \text{si } t \in ]-\pi, 0[ \end{cases} $$
et $f(-\pi) = f(0) = 0$.

**1. Parité et conséquences :**
Déterminer la parité de $f$. Qu'en déduit-on pour ses coefficients de Fourier réels $a_n$ et $b_n$ ?

**2. Calcul des coefficients :**
Calculer explicitement les coefficients de Fourier de $f$.

**3. Écriture de la série :**
Écrire la série de Fourier de $f$ et déterminer vers quoi elle converge en tout point $t \in \mathbb{R}$.

## Correction

**1. Parité et conséquences :**
La fonction $f$ est impaire. En effet, pour tout $t \in ]0, \pi[$, $f(-t) = -1 = -f(t)$. De plus $f(0) = 0 = -f(0)$ et $f(-\pi) = 0 = -f(-\pi)$.
Puisque $f$ est impaire :
- Le coefficient moyen est nul : $a_0 = \frac{1}{\pi}\int_{-\pi}^{\pi} f(t) dt = 0$.
- Les coefficients $a_n$ liés au cosinus (pair) sont nuls pour tout $n \ge 1$ : $a_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f(t)\cos(nt) dt = 0$.
Il ne reste qu'à calculer les coefficients $b_n$.

**2. Calcul des coefficients :**
Pour $n \ge 1$ :
$$ b_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(t) \sin(nt) dt $$
Comme $f(t)$ et $\sin(nt)$ sont impaires, leur produit est pair. Donc :
$$ b_n = \frac{2}{\pi} \int_{0}^{\pi} f(t) \sin(nt) dt $$
Sur $]0, \pi[$, $f(t) = 1$. L'intégrale devient :
$$ b_n = \frac{2}{\pi} \int_{0}^{\pi} \sin(nt) dt = \frac{2}{\pi} \left[ \frac{-\cos(nt)}{n} \right]_0^\pi $$
$$ b_n = \frac{-2}{n\pi} (\cos(n\pi) - \cos(0)) = \frac{-2}{n\pi} ((-1)^n - 1) $$
Ainsi :
- Si $n$ est pair ($n=2p$), $(-1)^{2p} - 1 = 0$, donc $b_{2p} = 0$.
- Si $n$ est impair ($n=2p+1$), $(-1)^{2p+1} - 1 = -2$, donc $b_{2p+1} = \frac{4}{(2p+1)\pi}$.

**3. Écriture de la série :**
La série de Fourier de $f$ s'écrit :
$$ S(f)(t) = \sum_{p=0}^{+\infty} \frac{4}{(2p+1)\pi} \sin((2p+1)t) = \frac{4}{\pi} \left( \sin(t) + \frac{\sin(3t)}{3} + \frac{\sin(5t)}{5} + \dots \right) $$

D'après le théorème de Dirichlet, comme $f$ est de classe $C^1$ par morceaux, la série de Fourier converge en tout $t$ vers la demi-somme des limites à gauche et à droite.
- Pour $t \in ]0, \pi[$ (modulo $2\pi$), $f$ est continue, la série converge vers $f(t) = 1$.
- Pour $t \in ]-\pi, 0[$ (modulo $2\pi$), $f$ est continue, la série converge vers $f(t) = -1$.
- En $t=0$ (modulo $\pi$), les limites à gauche et à droite sont $-1$ et $1$. La série converge vers $\frac{1 + (-1)}{2} = 0$. Or on avait défini $f(0)=0$ et $f(\pi)=0$, donc la série converge vers $f(t)$ partout.
