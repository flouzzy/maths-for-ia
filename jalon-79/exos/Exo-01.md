# Exercice 1 : Calcul de somme (Série de Fourier de la fonction créneau) $\bigstar\star\star\star\star$
**Énoncé :** Soit la fonction $f$ impaire, $2\pi$-périodique, telle que $f(t) = 1$ pour $t \in ]0, \pi[$. En appliquant l'identité de Parseval, calculer la somme $S = \sum_{p=0}^\infty \frac{1}{(2p+1)^2}$.

**Correction Détaillée :**
*Étape 1 : Calcul des coefficients de Fourier.*
La fonction est impaire, donc $a_n = 0$ pour tout $n \ge 0$.
Pour $n \ge 1$ :
$$b_n = \frac{2}{\pi} \int_0^\pi 1 \cdot \sin(nt) dt = \frac{2}{\pi} \left[ \frac{-\cos(nt)}{n} \right]_0^\pi = \frac{2}{\pi n} (1 - (-1)^n)$$
Si $n$ est pair ($n=2p$), $b_{2p} = 0$.
Si $n$ est impair ($n=2p+1$), $b_{2p+1} = \frac{4}{\pi(2p+1)}$.

*Étape 2 : Calcul de l'énergie temporelle.*
L'intégrale du carré de la fonction sur une période est :
$$\frac{1}{2\pi} \int_{-\pi}^\pi |f(t)|^2 dt = \frac{1}{2\pi} \int_{-\pi}^\pi 1 dt = 1$$

*Étape 3 : Application de l'identité de Parseval.*
Parseval (version réelle) donne :
$$\frac{1}{2\pi} \int_{-\pi}^\pi |f(t)|^2 dt = \frac{a_0^2}{4} + \frac{1}{2} \sum_{n=1}^\infty (a_n^2 + b_n^2)$$
$$1 = \frac{1}{2} \sum_{p=0}^\infty b_{2p+1}^2 = \frac{1}{2} \sum_{p=0}^\infty \frac{16}{\pi^2(2p+1)^2} = \frac{8}{\pi^2} \sum_{p=0}^\infty \frac{1}{(2p+1)^2}$$
On en déduit immédiatement :
$$\sum_{p=0}^\infty \frac{1}{(2p+1)^2} = \frac{\pi^2}{8}$$
