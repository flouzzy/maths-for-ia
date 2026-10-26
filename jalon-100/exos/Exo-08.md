# Exercice 8 : Divergence des séries de Fourier (Construction)
$\bigstar\bigstar\bigstar\bigstar\star$
**Énoncé :**
Soit $E = \mathcal{C}_{2\pi}$ muni de la norme $\|f\|_{\infty}$.
Considérons l'opérateur de somme partielle de Fourier en $0$ : $S_n(f)(0) = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(t) D_n(t) dt$ où $D_n(t) = \frac{\sin((n+1/2)t)}{\sin(t/2)}$.
On sait que $\|S_n\|_{\mathcal{L}(E, \mathbb{C})} = \frac{1}{2\pi} \int_{-\pi}^{\pi} |D_n(t)| dt$.
Montrer que si on sait que $\int_{-\pi}^{\pi} |D_n(t)| dt \to \infty$, il existe $f \in E$ dont la série de Fourier diverge en $0$.

**Correction :**
1. Posons $T_n : E \to \mathbb{C}$ défini par $T_n(f) = S_n(f)(0)$.
   $T_n$ est une forme linéaire continue, et sa norme $\|T_n\|$ est précisément égale à $\frac{1}{2\pi} \|D_n\|_1$.
2. L'hypothèse indique que $\lim_{n \to \infty} \|T_n\| = +\infty$.
   La suite des normes n'est donc pas bornée : $\sup_n \|T_n\| = +\infty$.
3. L'espace $E$ muni de la norme uniforme est un espace de Banach.
   Si, par l'absurde, la série de Fourier de toute fonction continue convergeait en $0$, alors pour tout $f \in E$, la suite numérique $(S_n(f)(0))_{n}$ serait convergente, et donc bornée.
4. Par le théorème de Banach-Steinhaus, si on avait $\sup_n |T_n(f)| < \infty$ pour tout $f$, alors on aurait $\sup_n \|T_n\| < \infty$.
5. Contradiction avec le point 2.
   Donc il existe nécessairement une fonction $f \in E$ telle que la suite $(T_n(f))_{n}$ n'est pas bornée.
   En particulier, cette suite diverge. La série de Fourier de $f$ diverge en $0$.