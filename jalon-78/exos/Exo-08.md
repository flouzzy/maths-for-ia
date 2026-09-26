# Phénomène de Gibbs pour un signal créneau

$\bigstar\bigstar\bigstar\bigstar\star$

Soit $f$ impaire, $2\pi$-périodique, valant $1$ sur $]0, \pi[$.
On note $S_N(t) = \frac{4}{\pi} \sum_{k=0}^N \frac{\sin((2k+1)t)}{2k+1}$.
Montrer que $S_N' (t) = \frac{2}{\pi} \frac{\sin(2(N+1)t)}{\sin(t)}$ et en déduire que le maximum local de $S_N$ sur $]0, \pi[$ se trouve en $t_N = \frac{\pi}{2(N+1)}$, et tend vers une valeur strictement supérieure à 1.

**Correction détaillée :**
1. Dérivation de la somme partielle :
   $$ S_N'(t) = \frac{4}{\pi} \sum_{k=0}^N \cos((2k+1)t) $$
   C'est la partie réelle de $\frac{4}{\pi} \sum_{k=0}^N e^{i(2k+1)t}$.
   $$ \sum_{k=0}^N e^{i(2k+1)t} = e^{it} \sum_{k=0}^N e^{2ikt} = e^{it} \frac{1 - e^{i2(N+1)t}}{1 - e^{2it}} = e^{it} \frac{e^{i(N+1)t}(e^{-i(N+1)t} - e^{i(N+1)t})}{e^{it}(e^{-it} - e^{it})} $$
   $$ = \frac{-2i\sin((N+1)t) e^{i(N+1)t}}{-2i\sin(t)} = e^{i(N+1)t} \frac{\sin((N+1)t)}{\sin(t)} $$
   En prenant la partie réelle : $\cos((N+1)t) \frac{\sin((N+1)t)}{\sin(t)} = \frac{1}{2} \frac{\sin(2(N+1)t)}{\sin(t)}$.
   Donc $S_N'(t) = \frac{4}{\pi} \times \frac{1}{2} \frac{\sin(2(N+1)t)}{\sin(t)} = \frac{2}{\pi} \frac{\sin(2(N+1)t)}{\sin(t)}$.
2. Recherche du maximum. $S_N'$ s'annule en changeant de signe (de + à -) pour la première fois sur $]0, \pi[$ lorsque $2(N+1)t = \pi$, soit $t_N = \frac{\pi}{2(N+1)}$.
3. Valeur du maximum en $t_N$ :
   $$ S_N(t_N) = \frac{4}{\pi} \sum_{k=0}^N \frac{\sin((2k+1)\frac{\pi}{2(N+1)})}{2k+1} = \frac{2}{\pi} \sum_{k=0}^N \frac{\sin(\frac{2k+1}{2N+2}\pi)}{\frac{2k+1}{2N+2}} \frac{2}{2N+2} $$
   Ceci est une somme de Riemann pour l'intégrale $\frac{2}{\pi} \int_0^1 \frac{\sin(\pi x)}{x} dx = \frac{2}{\pi} \int_0^\pi \frac{\sin(u)}{u} du$.
   Numériquement, $\int_0^\pi \frac{\sin(u)}{u} du \approx 1.85$. Ainsi, le pic tend vers $\frac{2}{\pi} \times 1.85 \approx 1.18$. Le "dépassement" (overshoot) aux abords de la discontinuité est donc d'environ $9\%$. C'est le phénomène de Gibbs.