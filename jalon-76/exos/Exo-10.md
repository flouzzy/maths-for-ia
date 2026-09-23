# Exercice 10 : Espace $L^2$ (★★★★★)

**Énoncé :**
Montrer que l'espace $C([0, 1])$ des fonctions continues n'est pas complet pour la norme $L^2$. (C'est la raison pour laquelle on a dû introduire la complétion hilbertienne $L^2$).

**Correction Détaillée :**
*Analyse de l'énoncé :* Il faut exhiber une suite de Cauchy de fonctions continues $(f_n)$ (pour la norme $L^2$) qui ne converge vers aucune fonction *continue*.

*Résolution pas-à-pas :*
1. **Construction de la suite :**
   Considérons la suite de fonctions $f_n \in C([0, 1])$ définie pour $n \ge 2$ par :
   - $f_n(x) = 0$ si $0 \le x \le 1/2$
   - $f_n(x) = n(x - 1/2)$ si $1/2 < x \le 1/2 + 1/n$
   - $f_n(x) = 1$ si $1/2 + 1/n < x \le 1$
   Ce sont des approximations continues de la fonction indicatrice $f = \mathbf{1}_{[1/2, 1]}$.

2. **C'est une suite de Cauchy dans $L^2$ :**
   Pour $m > n$, évaluons $\|f_m - f_n\|_{L^2}^2$.
   Les fonctions coïncident sur $[0, 1/2]$ (valent 0) et sur $[1/2 + 1/n, 1]$ (valent 1).
   Elles ne diffèrent que sur $[1/2, 1/2 + 1/n]$.
   La différence $f_m - f_n$ est majorée par $1$.
   $$ \|f_m - f_n\|_{L^2}^2 = \int_{1/2}^{1/2 + 1/n} |f_m(x) - f_n(x)|^2 dx \le \int_{1/2}^{1/2 + 1/n} 1^2 dx = \frac{1}{n} $$
   Comme $\lim_{n \to \infty} 1/n = 0$, la distance $\|f_m - f_n\|$ tend vers $0$ lorsque $m, n \to \infty$. La suite est donc de Cauchy.

3. **Absence de limite continue :**
   Supposons qu'il existe $g \in C([0, 1])$ telle que $\|f_n - g\|_{L^2} \to 0$.
   On a $\int_0^{1/2} |g(x)|^2 dx = \lim \int_0^{1/2} |f_n(x) - g(x)|^2 dx \le \lim \|f_n - g\|^2 = 0$.
   Comme $g$ est continue, $\int_0^{1/2} |g|^2 = 0 \implies g(x) = 0$ sur $[0, 1/2]$.
   De même, pour tout $\delta > 0$, pour $n$ assez grand, $f_n(x) = 1$ sur $[1/2 + \delta, 1]$.
   Donc $\int_{1/2+\delta}^1 |1 - g(x)|^2 dx \le \lim \|f_n - g\|^2 = 0 \implies g(x) = 1$ sur $[1/2+\delta, 1]$.
   Par continuité de $g$, $g(1/2^+) = 1$.
   Or $g(1/2^-) = 0$. $g$ ne peut donc pas être continue en $1/2$.
   Contradiction. L'espace n'est pas complet.
