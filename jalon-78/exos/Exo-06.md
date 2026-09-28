# Exercice 6 : L'équation de la chaleur avec condition initiale $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
On cherche une solution $u(x,t)$ à l'équation de la chaleur $\frac{\partial u}{\partial t} = \frac{\partial^2 u}{\partial x^2}$ sur $[0, \pi] \times \mathbb{R}^+$ avec :
$u(0, t) = u(\pi, t) = 0$ et condition initiale $u(x,0) = x(\pi - x)$.
Proposer une solution sous forme de série.

**Correction Détaillée :**
1. **Séparation des variables :**
On cherche des solutions fondamentales $u_n(x,t) = X(x)T(t)$.
Les conditions aux bords $X(0)=X(\pi)=0$ imposent $X_n(x) = \sin(nx)$ pour $n \in \mathbb{N}^*$.
L'équation en temps donne $T'(t) = -n^2 T(t) \implies T_n(t) = e^{-n^2 t}$.
La solution générale est $u(x,t) = \sum_{n=1}^\infty b_n \sin(nx) e^{-n^2 t}$.

2. **Identification des $b_n$ par Fourier :**
En $t=0$, $u(x,0) = \sum_{n=1}^\infty b_n \sin(nx) = x(\pi-x)$.
$b_n$ sont les coefficients de Fourier de la fonction impaire $2\pi$-périodique coïncidant avec $x(\pi-x)$ sur $[0,\pi]$.
$$ b_n = \frac{2}{\pi} \int_0^\pi (x\pi - x^2) \sin(nx) dx $$
Par double IPP :
Pour $x\pi \sin(nx)$, l'IPP donne $\frac{\pi}{n}$.
Pour $x^2 \sin(nx)$, la double IPP donne $\frac{\pi^2}{n} - \frac{2\pi}{n^3}(1 - (-1)^n)$ (calcul classique).
Finalement, $b_n = \frac{4}{\pi n^3} (1 - (-1)^n)$.
$$ b_{2k} = 0, \quad b_{2k+1} = \frac{8}{\pi (2k+1)^3} $$
La solution est :
$$ u(x,t) = \frac{8}{\pi} \sum_{k=0}^\infty \frac{\sin((2k+1)x)}{(2k+1)^3} e^{-(2k+1)^2 t} $$
