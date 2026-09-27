## Exercice 9 : Noyau de Fejér \quad \bigstar\bigstar\bigstar\bigstar\bigstar

On pose $F_N(x) = \frac{1}{N} \sum_{n=0}^{N-1} D_n(x)$ où $D_n(x) = \sum_{k=-n}^n e^{ikx}$ est le noyau de Dirichlet.
1. Montrer que $F_N(x) = \frac{1}{N} \left( \frac{\sin(Nx/2)}{\sin(x/2)} \right)^2$.
2. En déduire que $F_N(x) \ge 0$.

**Correction :**
1. $D_n(x) = \frac{\sin((n+1/2)x)}{\sin(x/2)}$.
$NF_N(x) = \sum_{n=0}^{N-1} \frac{\sin((n+1/2)x)}{\sin(x/2)} = \frac{1}{\sin(x/2)} \text{Im} \sum_{n=0}^{N-1} e^{i(n+1/2)x}$.
La somme géométrique : $\sum_{n=0}^{N-1} e^{i(n+1/2)x} = e^{ix/2} \frac{1-e^{iNx}}{1-e^{ix}} = e^{ix/2} \frac{e^{iNx/2}(e^{-iNx/2}-e^{iNx/2})}{e^{ix/2}(e^{-ix/2}-e^{ix/2})} = e^{iNx/2} \frac{-2i\sin(Nx/2)}{-2i\sin(x/2)} = \frac{e^{iNx/2}\sin(Nx/2)}{\sin(x/2)}$.
La partie imaginaire est $\frac{\sin^2(Nx/2)}{\sin(x/2)}$.
Donc $NF_N(x) = \frac{\sin^2(Nx/2)}{\sin^2(x/2)}$.
2. C'est le carré d'un nombre réel divisé par $N>0$, donc $F_N(x) \ge 0$ pour tout $x$. Cette positivité fait de la somme de Fejér une approximation de l'identité qui évite le phénomène de Gibbs (Théorème de Fejér).
