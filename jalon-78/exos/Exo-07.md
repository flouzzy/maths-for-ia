# Exo 07 : Série de Fourier du signal triangle

**Difficulté :** \bigstar\bigstar\bigstar\bigstar\star


Soit $g(t)$ la fonction $2\pi$-périodique paire définie par $g(t) = |t|$ sur $[-\pi, \pi]$.
1. Sans utiliser les calculs de l'exercice précédent, calculer directement la série de Fourier de $g$.
2. Comparer avec le résultat obtenu si on avait intégré la série de Fourier du signal créneau impair $f(t) = \text{signe}(t)$ sur $[-\pi, \pi]$ développé à l'exercice 1.

## Correction

**1. Calcul direct :**
$g(t)$ est paire, donc $b_n = 0$ pour tout $n \ge 1$.
Calculons le terme constant :
$$ a_0 = \frac{1}{\pi} \int_{-\pi}^\pi |t| dt = \frac{2}{\pi} \int_0^\pi t dt = \frac{2}{\pi} \left[ \frac{t^2}{2} \right]_0^\pi = \pi $$
Calcul de $a_n$ pour $n \ge 1$ par intégration par parties :
$$ a_n = \frac{2}{\pi} \int_0^\pi t \cos(nt) dt $$
On pose $u=t, v'=\cos(nt) \implies u'=1, v=\frac{\sin(nt)}{n}$.
$$ a_n = \frac{2}{\pi} \left( \left[ t \frac{\sin(nt)}{n} \right]_0^\pi - \int_0^\pi \frac{\sin(nt)}{n} dt \right) $$
Le terme tout intégré est nul en $\pi$ (car $\sin(n\pi)=0$) et en $0$.
$$ a_n = \frac{-2}{n\pi} \int_0^\pi \sin(nt) dt = \frac{-2}{n\pi} \left[ \frac{-\cos(nt)}{n} \right]_0^\pi $$
$$ a_n = \frac{2}{n^2\pi} (\cos(n\pi) - 1) = \frac{2}{n^2\pi} ((-1)^n - 1) $$
Ainsi :
- Si $n$ est pair ($n=2p$), $(-1)^{2p}-1 = 0 \implies a_{2p} = 0$.
- Si $n$ est impair ($n=2p+1$), $(-1)^{2p+1}-1 = -2 \implies a_{2p+1} = \frac{-4}{(2p+1)^2 \pi}$.

La série de Fourier est :
$$ S(g)(t) = \frac{\pi}{2} - \frac{4}{\pi} \sum_{p=0}^\infty \frac{\cos((2p+1)t)}{(2p+1)^2} $$

**2. Lien par intégration :**
Le signal créneau impair $f$ de l'exercice 1 a pour série :
$$ S(f)(t) = \frac{4}{\pi} \sum_{p=0}^\infty \frac{\sin((2p+1)t)}{2p+1} $$
Notons que $g(t) = |t|$ est, à une constante d'intégration près, la primitive du signal en "dents de scie/créneau" $f(t) = \text{signe}(t)$ sur $]-\pi, \pi[$.
Plus précisément, $g(t) = \int_0^t f(u) du$.
En intégrant terme à terme la série de $f$ (ce qui est justifié par la convergence uniforme des séries pour des fonctions continues) :
$$ \int_0^t S(f)(u) du = \frac{4}{\pi} \sum_{p=0}^\infty \int_0^t \frac{\sin((2p+1)u)}{2p+1} du $$
$$ \int_0^t \frac{\sin((2p+1)u)}{2p+1} du = \left[ \frac{-\cos((2p+1)u)}{(2p+1)^2} \right]_0^t = \frac{1}{(2p+1)^2} - \frac{\cos((2p+1)t)}{(2p+1)^2} $$
Donc :
$$ \int_0^t S(f)(u) du = \frac{4}{\pi} \sum_{p=0}^\infty \frac{1}{(2p+1)^2} - \frac{4}{\pi} \sum_{p=0}^\infty \frac{\cos((2p+1)t)}{(2p+1)^2} $$
On sait (par Dirichlet sur $g$ en $t=0$ où $g(0)=0$) que $\frac{\pi}{2} = \frac{4}{\pi} \sum_{p=0}^\infty \frac{1}{(2p+1)^2}$.
Le premier terme correspond donc exactement à $\frac{\pi}{2}$. On retrouve ainsi la série $S(g)(t)$ calculée directement.
