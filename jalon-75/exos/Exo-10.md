# Exercice 10 : Problème de l'X - Non-complétude de Riemann
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit $E = \{f \in C([0,1], \mathbb{R}) \}$. On munit $E$ de la norme $N_1(f) = \int_0^1 |f(x)|dx$.
Démontrer en exhibant une suite explicite que $(E, N_1)$ n'est pas complet (ce qui justifia l'invention de l'intégrale de Lebesgue et de l'espace $L^1$).

**Correction :**
Considérons la suite de fonctions rationnelles $f_n \in C([0,1])$ définie par $f_n(x) = (x^n(1-x)^n)^{1/n}$ ... Non, restons plus simple : construisons une fonction avec une "marche" limite.
Posons $f_n(x) = 0$ sur $[0, 1/2]$.
$f_n(x) = n(x - 1/2)$ sur $[1/2, 1/2 + 1/n]$.
$f_n(x) = 1$ sur $[1/2 + 1/n, 1]$.
Les $f_n$ sont continues (donc intégrables au sens de Riemann).
Vérifions que c'est une suite de Cauchy pour $N_1$. Pour $m > n$, les fonctions $f_n$ et $f_m$ ne diffèrent que sur l'intervalle $[1/2, 1/2 + 1/n]$. La différence maximale est bornée par 1.
L'intégrale de leur différence absolue est bornée par l'aire du triangle de base $1/n$ et de hauteur 1, soit $\le 1/n$.
Donc $N_1(f_n - f_m) \le 1/n$. La suite est bien de Cauchy pour $N_1$.
Supposons que $(E, N_1)$ soit complet. Il existerait $g \in C([0,1])$ telle que $N_1(f_n - g) \to 0$.
On sait que $\int_0^{1/2} |f_n - g| dx \to 0$, donc $\int_0^{1/2} |g| dx = 0$. Comme $g$ est continue et positive, $g = 0$ sur $[0, 1/2]$.
De même, $\int_{1/2+\varepsilon}^1 |f_n - g| dx \to 0$, or pour $n$ grand, $f_n = 1$ sur cet intervalle. Donc $\int_{1/2+\varepsilon}^1 |1 - g| dx = 0$, d'où $g = 1$ sur $[1/2+\varepsilon, 1]$, et par continuité $g = 1$ sur $]1/2, 1]$.
On aboutit à $g(1/2) = 0$ (limite à gauche) et $g(1/2) = 1$ (limite à droite), ce qui contredit la continuité de $g$.
Donc l'espace des fonctions continues muni de la norme $L^1$ n'est pas complet. Il faut adjoindre les limites de telles suites (les fonctions mesurables) : c'est la genèse de l'espace $L^1$.
