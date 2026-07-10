# Exercice 1 : Calcul de rayon de convergence de base

**Énoncé :**
Déterminer le rayon de convergence $R$ de la série entière $\sum_{n=1}^{+\infty} \frac{z^n}{n^2}$.

**Démonstration à blanc :**
On considère la série entière $\sum_{n=1}^{+\infty} a_n z^n$ avec $a_n = \frac{1}{n^2}$.
Pour tout $n \geq 1$, $a_n \neq 0$. Nous pouvons appliquer la règle de d'Alembert pour évaluer la limite du rapport.
Calculons le rapport $\left| \frac{a_{n+1}}{a_n} \right|$ :
$$ \left| \frac{a_{n+1}}{a_n} \right| = \frac{\frac{1}{(n+1)^2}}{\frac{1}{n^2}} = \frac{n^2}{(n+1)^2} = \left( \frac{n}{n+1} \right)^2 $$
Lorsque $n$ tend vers $+\infty$, la fraction $\frac{n}{n+1}$ tend vers 1.
Ainsi, la limite du carré est :
$$ L = \lim_{n \to +\infty} \left( \frac{n}{n+1} \right)^2 = 1^2 = 1 $$
D'après la règle de d'Alembert pour les séries entières, le rayon de convergence est donné par $R = \frac{1}{L}$.
Donc, le rayon de convergence est $R = \frac{1}{1} = 1$.
