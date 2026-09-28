# Exercice 10 : Phénomène de Gibbs

**Difficulté :** \bigstar\bigstar\bigstar\bigstar\bigstar

**Énoncé :**
Le signal carré impair est donné par $f(t) = 1$ sur $]0, \pi[$ et $f(t) = -1$ sur $]-\pi, 0[$. La série de Fourier de $f$ est $S(f)(t) = \frac{4}{\pi} \sum_{k=0}^{+\infty} \frac{\sin((2k+1)t)}{2k+1}$.
Considérons la somme partielle $S_N(f)(t) = \frac{4}{\pi} \sum_{k=0}^N \frac{\sin((2k+1)t)}{2k+1}$.
Montrer que $S_N(f)'(t) = \frac{2}{\pi} \frac{\sin(2(N+1)t)}{\sin(t)}$ et en déduire l'abscisse du premier maximum local de $S_N$ sur $]0, \pi[$.

**Correction :**
1. Dérivons la somme partielle :
   $$S_N(f)'(t) = \frac{4}{\pi} \sum_{k=0}^N \cos((2k+1)t)$$
2. Pour calculer cette somme, multiplions par $\sin(t)$ et utilisons la formule trigonométrique $2 \cos(A) \sin(B) = \sin(A+B) - \sin(A-B)$ :
   $$\sin(t) S_N(f)'(t) = \frac{2}{\pi} \sum_{k=0}^N 2 \cos((2k+1)t) \sin(t) = \frac{2}{\pi} \sum_{k=0}^N \left( \sin((2k+2)t) - \sin(2kt) \right)$$
   C'est une somme télescopique :
   $$\sin(t) S_N(f)'(t) = \frac{2}{\pi} \left( \sin(2(N+1)t) - \sin(0) \right) = \frac{2}{\pi} \sin(2(N+1)t)$$
   D'où $S_N(f)'(t) = \frac{2}{\pi} \frac{\sin(2(N+1)t)}{\sin(t)}$.
3. Le premier maximum local sur $]0, \pi[$ correspond à la première racine positive de la dérivée.
   La dérivée s'annule quand $\sin(2(N+1)t) = 0$, donc pour $2(N+1)t = \pi, 2\pi, \dots$
   La première racine strictement positive est obtenue pour :
   $$t_N = \frac{\pi}{2(N+1)}$$
   À ce point, la valeur du signal approche $\frac{2}{\pi} \int_0^\pi \frac{\sin(x)}{x} dx \approx 1.1789$, soit un dépassement brutal d'environ 18% au-dessus du plafond $1$. C'est le célèbre phénomène de Gibbs.
