# Exercice 10 : Inégalité de Tchebychev \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit $f \in \mathcal{M}_+$ et $\alpha > 0$. Démontrer l'inégalité de Tchebychev-Markov : $\mu(\{x \in X \mid f(x) \ge \alpha\}) \le \frac{1}{\alpha} \int_X f \, d\mu$.

**Correction :**
Soit $A_\alpha = \{x \in X \mid f(x) \ge \alpha\}$.

Sur l'ensemble $X$, nous avons l'inégalité ponctuelle :
$f(x) \ge f(x) \mathbf{1}_{A_\alpha}(x)$. (car $f$ est positive et $\mathbf{1}_{A_\alpha}$ vaut 0 ou 1).

De plus, par définition de $A_\alpha$, si $x \in A_\alpha$, alors $f(x) \ge \alpha$. Donc :
$f(x) \mathbf{1}_{A_\alpha}(x) \ge \alpha \mathbf{1}_{A_\alpha}(x)$.

En combinant les deux, pour tout $x \in X$ :
$f(x) \ge \alpha \mathbf{1}_{A_\alpha}(x)$.

L'intégrale préserve l'ordre (croissance) :
$\int_X f \, d\mu \ge \int_X \alpha \mathbf{1}_{A_\alpha} \, d\mu$.

Par homogénéité de l'intégrale d'une fonction simple :
$\int_X \alpha \mathbf{1}_{A_\alpha} \, d\mu = \alpha \mu(A_\alpha)$.

Ainsi :
$\int_X f \, d\mu \ge \alpha \mu(A_\alpha)$.

Comme $\alpha > 0$, on peut diviser par $\alpha$ pour obtenir :
$\mu(A_\alpha) \le \frac{1}{\alpha} \int_X f \, d\mu$.

C'est l'inégalité de Tchebychev (ou Markov).
