## Exercice 2 : Série de Fourier du signal carré et Problème de Bâle (partie 1) \quad \bigstar\bigstar\star\star\star

Soit $f$ la fonction $2\pi$-périodique, impaire, définie sur $]0, \pi[$ par $f(x) = 1$, et $f(0) = f(\pi) = 0$.
1. Calculer la série de Fourier de $f$.
2. En évaluant la série en $x=\pi/2$, en déduire la valeur de $\sum_{p=0}^\infty \frac{(-1)^p}{2p+1}$.

**Correction :**
1. $f$ est impaire, $a_n = 0$.
$b_n = \frac{2}{\pi} \int_0^\pi 1 \cdot \sin(nx)dx = \frac{2}{\pi} \left[ -\frac{\cos(nx)}{n} \right]_0^\pi = \frac{2}{n\pi}(1 - (-1)^n)$.
Pour $n=2p$, $b_{2p} = 0$. Pour $n=2p+1$, $b_{2p+1} = \frac{4}{\pi(2p+1)}$.
La série de Fourier est $\frac{4}{\pi} \sum_{p=0}^\infty \frac{\sin((2p+1)x)}{2p+1}$.
2. Par le théorème de Dirichlet, $f$ est $C^1$ par morceaux, continue en $\pi/2$, donc $S(f)(\pi/2) = f(\pi/2) = 1$.
$\frac{4}{\pi} \sum_{p=0}^\infty \frac{\sin((2p+1)\pi/2)}{2p+1} = 1$.
Or $\sin(p\pi + \pi/2) = (-1)^p$.
Donc $\sum_{p=0}^\infty \frac{(-1)^p}{2p+1} = \frac{\pi}{4}$ (Formule de Leibniz/Gregory).
