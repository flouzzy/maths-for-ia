# Exo 06 : Phénomène de Gibbs pour un échelon

**Difficulté :** \bigstar\bigstar\bigstar\bigstar\star


On reprend la fonction $f$ signal carré impaire de l'Exo 01 :
$f(t) = 1$ sur $]0, \pi[$, $-1$ sur $]-\pi, 0[$.
Sa série de Fourier d'ordre $N$ s'écrit :
$$ S_{2N+1}(f)(t) = \frac{4}{\pi} \sum_{k=0}^N \frac{\sin((2k+1)t)}{2k+1} $$

Montrer que la dérivée $S'_{2N+1}(f)(t)$ s'annule en $t_N = \frac{\pi}{2N+2}$. (Ce point correspond au premier dépassement de l'approximation de Fourier près de la discontinuité en $0$, illustrant le phénomène de Gibbs).

## Correction

Dérivons la somme partielle terme à terme par rapport à $t$ :
$$ S'_{2N+1}(f)(t) = \frac{4}{\pi} \sum_{k=0}^N \frac{d}{dt} \left( \frac{\sin((2k+1)t)}{2k+1} \right) $$
$$ S'_{2N+1}(f)(t) = \frac{4}{\pi} \sum_{k=0}^N \frac{(2k+1)\cos((2k+1)t)}{2k+1} = \frac{4}{\pi} \sum_{k=0}^N \cos((2k+1)t) $$

On reconnaît la partie réelle d'une somme géométrique complexe.
Soit $C = \sum_{k=0}^N \cos((2k+1)t)$ et $S = \sum_{k=0}^N \sin((2k+1)t)$.
$C + iS = \sum_{k=0}^N e^{i(2k+1)t} = e^{it} \sum_{k=0}^N (e^{2it})^k$
La raison est $q = e^{2it}$. Pour $t \notin \pi\mathbb{Z}$, $q \neq 1$.
$$ C + iS = e^{it} \frac{1 - e^{2i(N+1)t}}{1 - e^{2it}} $$
Utilisons la technique de l'angle moitié : $1 - e^{2i\alpha} = e^{i\alpha}(e^{-i\alpha} - e^{i\alpha}) = -2i \sin(\alpha) e^{i\alpha}$.
Le numérateur est $-2i \sin((N+1)t) e^{i(N+1)t}$.
Le dénominateur est $1 - e^{2it} = -2i \sin(t) e^{it}$.
$$ C + iS = e^{it} \frac{-2i \sin((N+1)t) e^{i(N+1)t}}{-2i \sin(t) e^{it}} = \frac{\sin((N+1)t)}{\sin(t)} e^{i(N+1)t} $$
En prenant la partie réelle :
$$ C = \frac{\sin((N+1)t) \cos((N+1)t)}{\sin(t)} = \frac{\sin(2(N+1)t)}{2\sin(t)} $$

Donc :
$$ S'_{2N+1}(f)(t) = \frac{4}{\pi} \frac{\sin(2(N+1)t)}{2\sin(t)} = \frac{2 \sin(2(N+1)t)}{\pi \sin(t)} $$

Nous cherchons les zéros de cette dérivée sur $]0, \pi[$. La dérivée s'annule lorsque $\sin(2(N+1)t) = 0$, c'est-à-dire $2(N+1)t = m\pi$ pour un certain entier $m > 0$.
Le premier zéro strictement positif (le point de premier dépassement maximum de l'oscillation) est obtenu pour $m=1$ :
$$ 2(N+1)t_1 = \pi \implies t_1 = \frac{\pi}{2(N+1)} $$
Ce qui démontre que $S'_{2N+1}(f)(t)$ s'annule en $t_N = \frac{\pi}{2N+2}$. Ce pic de dépassement (overshoot) ne disparaît pas quand $N \to \infty$, son amplitude converge vers environ $1.178$, ce qui dépasse la limite théorique de $1$ : c'est le phénomène de Gibbs.
