# Exercice 2 : Densité et limite uniforme

**Niveau :** \bigstar\bigstar\star\star\star

**Énoncé :**
Montrer que si $(f_n)$ est une suite de $L^p([0,1])$ ($1 \le p < +\infty$) qui converge uniformément vers $f$ sur $[0,1]$, alors $f \in L^p([0,1])$ et $f_n$ converge vers $f$ dans $L^p([0,1])$.

**Correction Détaillée :**
1. **Appartenance à $L^p$ :**
   La suite $(f_n)$ converge uniformément vers $f$.
   Par définition, il existe $N \in \mathbb{N}$ tel que pour tout $n \ge N$, $\sup_{x \in [0,1]} |f_n(x) - f(x)| \le 1$.
   En particulier, pour $n=N$, on a $|f(x)| \le |f_N(x)| + 1$.
   Puisque $[0,1]$ est de mesure finie (valant 1), la fonction constante 1 est dans $L^p$.
   Comme $f_N \in L^p$, par l'inégalité de Minkowski, $f_N + 1 \in L^p$.
   Donc $f \in L^p([0,1])$.

2. **Convergence dans $L^p$ :**
   Calculons la distance en norme $L^p$ :
   $\|f_n - f\|_p^p = \int_0^1 |f_n(x) - f(x)|^p dx$.
   Par convergence uniforme, soit $\varepsilon > 0$. Il existe $N$ tel que pour $n \ge N$, pour tout $x \in [0,1]$, $|f_n(x) - f(x)| \le \varepsilon$.
   Ainsi, pour $n \ge N$ :
   $\int_0^1 |f_n(x) - f(x)|^p dx \le \int_0^1 \varepsilon^p dx = \varepsilon^p$.
   Donc $\|f_n - f\|_p \le \varepsilon$.
   Ceci prouve que $\|f_n - f\|_p \to 0$ lorsque $n \to +\infty$.

*Note géométrique :* Sur un espace de mesure finie, la topologie de la convergence uniforme est strictement plus forte que la topologie $L^p$.
