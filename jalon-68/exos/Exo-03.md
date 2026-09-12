# Exercice 3 : Intégrabilité et séries de fonctions
$\bigstar\bigstar\star\star\star$

## Énoncé
Soit la fonction $f(x) = \sum_{n=1}^{\infty} \frac{\sin(nx)}{n^3}$ définie sur $[0, \pi]$.
Montrer rigoureusement que $f$ est intégrable au sens de Lebesgue sur $[0, \pi]$ en justifiant l'utilisation des théorèmes de théorie de la mesure.

## Correction
On considère la suite de sommes partielles $S_N(x) = \sum_{n=1}^N \frac{\sin(nx)}{n^3}$.
Chaque terme $u_n(x) = \frac{\sin(nx)}{n^3}$ est continu, donc borélien (mesurable).
Cependant, la suite des $S_N$ n'est pas de signe constant. Nous allons démontrer l'intégrabilité de $f$ (c'est-à-dire que $\int_0^\pi |f| d\lambda < \infty$) en majorant.

Pour tout $x \in [0, \pi]$, par inégalité triangulaire :
$$|f(x)| = \left| \sum_{n=1}^\infty \frac{\sin(nx)}{n^3} \right| \leq \sum_{n=1}^\infty \left| \frac{\sin(nx)}{n^3} \right|$$
Puisque $|\sin(nx)| \leq 1$, on a :
$$|f(x)| \leq \sum_{n=1}^\infty \frac{1}{n^3}$$

La série numérique $\sum \frac{1}{n^3}$ est une série de Riemann convergente (car $3 > 1$). Notons $C$ sa somme.
Ainsi, la fonction $|f(x)|$ est majorée presque partout (ici partout) par la constante $C$.

Par croissance de l'intégrale de Lebesgue :
$$\int_{[0, \pi]} |f(x)| d\lambda(x) \leq \int_{[0, \pi]} C d\lambda(x) = C \times \pi < +\infty$$

Puisque l'intégrale de la valeur absolue est finie, $f^+$ et $f^-$ ont nécessairement des intégrales finies (car $0 \leq f^+ \leq |f|$ et $0 \leq f^- \leq |f|$).
Par conséquent, $f$ est bien Lebesgue-intégrable sur $[0, \pi]$.
