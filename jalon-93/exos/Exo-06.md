# Exercice 06 : Loi Gamma et Somme
Difficulté : $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
La loi Gamma de paramètres $r > 0$ et $\lambda > 0$, notée $\Gamma(r, \lambda)$, a pour densité :
$f(x) = \frac{\lambda^r}{\Gamma(r)} x^{r-1} e^{-\lambda x} \mathbf{1}_{[0, +\infty[}(x)$
où $\Gamma(r) = \int_0^{+\infty} t^{r-1} e^{-t} dt$.
1. Montrer que sa fonction caractéristique est $\phi_X(t) = \left(1 - \frac{it}{\lambda}\right)^{-r}$.
2. En déduire la loi de la somme de $n$ variables exponentielles indépendantes de même paramètre $\lambda$.

**Correction pas à pas :**
1. $\phi_X(t) = \int_0^{+\infty} e^{itx} \frac{\lambda^r}{\Gamma(r)} x^{r-1} e^{-\lambda x} dx = \frac{\lambda^r}{\Gamma(r)} \int_0^{+\infty} x^{r-1} e^{-(\lambda - it)x} dx$.
   Effectuons le changement de variable complexe $u = (\lambda - it)x$. Alors $x = \frac{u}{\lambda - it}$ et $dx = \frac{du}{\lambda - it}$.
   Rigoureusement, cela nécessite le théorème de Cauchy sur un contour dans le plan complexe, mais le résultat analytique se prolonge.
   L'intégrale devient :
   $\int_0^{+\infty} \left(\frac{u}{\lambda - it}\right)^{r-1} e^{-u} \frac{du}{\lambda - it} = \frac{1}{(\lambda - it)^r} \int_0^{+\infty} u^{r-1} e^{-u} du = \frac{\Gamma(r)}{(\lambda - it)^r}$.
   En multipliant par le facteur constant $\frac{\lambda^r}{\Gamma(r)}$, on obtient :
   $\phi_X(t) = \frac{\lambda^r}{\Gamma(r)} \frac{\Gamma(r)}{(\lambda - it)^r} = \left(\frac{\lambda}{\lambda - it}\right)^r = \left(1 - \frac{it}{\lambda}\right)^{-r}$.
2. Soient $X_1, \dots, X_n$ des V.A. indépendantes de loi exponentielle de paramètre $\lambda$.
   Une loi exponentielle $\mathcal{E}(\lambda)$ est exactement une loi $\Gamma(1, \lambda)$.
   Ainsi, $\phi_{X_k}(t) = \left(1 - \frac{it}{\lambda}\right)^{-1}$.
   Posons $S_n = \sum_{k=1}^n X_k$. Par indépendance,
   $\phi_{S_n}(t) = \prod_{k=1}^n \phi_{X_k}(t) = \left(1 - \frac{it}{\lambda}\right)^{-n}$.
3. On reconnaît l'expression de la fonction caractéristique de la loi $\Gamma(n, \lambda)$.
   Par injectivité de la transformée de Fourier, on conclut que la somme de $n$ variables exponentielles i.i.d. de paramètre $\lambda$ suit une loi Gamma (loi d'Erlang) de paramètres $(n, \lambda)$.
