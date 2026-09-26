# Théorème de Féjèr et moyenne de Cesàro

$\bigstar\bigstar\bigstar\bigstar\bigstar$

Soit $f$ une fonction continue et $2\pi$-périodique. On note $S_k(f)$ la somme partielle de sa série de Fourier.
On définit les sommes de Cesàro $\sigma_N(f)(x) = \frac{1}{N} \sum_{k=0}^{N-1} S_k(f)(x)$.
Montrer que $\sigma_N(f)$ converge uniformément vers $f$ sur $\mathbb{R}$.

**Correction détaillée :**
1. Noyau de Féjèr. On sait que $S_k(f)(x) = \frac{1}{2\pi} \int_{-\pi}^\pi f(x-t) D_k(t) dt$ où $D_k(t) = \frac{\sin((k+1/2)t)}{\sin(t/2)}$.
   Par linéarité, $\sigma_N(f)(x) = \frac{1}{2\pi} \int_{-\pi}^\pi f(x-t) K_N(t) dt$ où $K_N(t) = \frac{1}{N} \sum_{k=0}^{N-1} D_k(t)$ est le noyau de Féjèr.
2. Calcul de $K_N(t)$.
   $$ K_N(t) = \frac{1}{N \sin(t/2)} \sum_{k=0}^{N-1} \sin((k+1/2)t) $$
   C'est la partie imaginaire de $\sum e^{i(k+1/2)t} = e^{it/2} \frac{1 - e^{iNt}}{1 - e^{it}} = e^{it/2} \frac{e^{iNt/2}(-2i\sin(Nt/2))}{-2i\sin(t/2) e^{it/2}} = \frac{e^{iNt/2} \sin(Nt/2)}{\sin(t/2)}$.
   Sa partie imaginaire est $\frac{\sin^2(Nt/2)}{\sin(t/2)}$.
   Donc $K_N(t) = \frac{1}{N} \left( \frac{\sin(Nt/2)}{\sin(t/2)} \right)^2$.
3. Propriétés cruciales de $K_N$ :
   - $K_N(t) \ge 0$ pour tout $t$. C'est fondamental car cela évite le phénomène de Gibbs causé par l'oscillation du noyau de Dirichlet.
   - $\frac{1}{2\pi} \int_{-\pi}^\pi K_N(t) dt = \frac{1}{N} \sum \frac{1}{2\pi} \int D_k = \frac{1}{N} \sum_{k=0}^{N-1} 1 = 1$.
   - Pour tout $\delta \in ]0, \pi[$, $\lim_{N \to \infty} \sup_{t \in [\delta, \pi]} K_N(t) = 0$ car le numérateur est majoré par 1, et le dénominateur est minoré par $\sin^2(\delta/2) > 0$, avec le facteur $1/N$ qui fait tendre vers 0.
4. Convergence.
   $$ |\sigma_N(f)(x) - f(x)| = \left| \frac{1}{2\pi} \int_{-\pi}^\pi (f(x-t) - f(x)) K_N(t) dt \right| \le \frac{1}{2\pi} \int_{-\pi}^\pi |f(x-t) - f(x)| K_N(t) dt $$
   Soit $\epsilon > 0$. $f$ est continue sur le compact $[-\pi, \pi]$, donc uniformément continue (théorème de Heine). Il existe $\delta > 0$ tel que $|t| \le \delta \implies |f(x-t) - f(x)| \le \epsilon/2$.
   On coupe l'intégrale en deux : $|t| \le \delta$ et $\delta \le |t| \le \pi$.
   - Sur $[-\delta, \delta]$ : $\frac{1}{2\pi} \int |f-f| K_N \le \frac{\epsilon}{2} \frac{1}{2\pi} \int K_N \le \frac{\epsilon}{2}$.
   - Sur $[\delta, \pi] \cup [-\pi, -\delta]$ : $f$ est bornée par $M$. $|f(x-t) - f(x)| \le 2M$.
     L'intégrale est majorée par $2M \times (\sup_{|t| \ge \delta} K_N(t))$. Puisque ce sup tend vers 0, il existe $N_0$ tel que pour $N \ge N_0$, $2M \sup K_N < \epsilon/2$.
   Finalement, pour $N \ge N_0$, $|\sigma_N(f)(x) - f(x)| \le \epsilon$, indépendamment de $x$. La convergence est bien uniforme.