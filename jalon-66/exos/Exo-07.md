# Exercice 7 : Intégrabilité et mesure finie \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $f \in \mathcal{M}_+$. On suppose que $\int_X f \, d\mu < +\infty$. Montrer que pour tout $\epsilon > 0$, l'ensemble $A_\epsilon = \{x \in X \mid f(x) \ge \epsilon\}$ est de mesure finie.

**Correction :**
Sur l'ensemble $X$, nous avons l'inégalité :
$f(x) \ge \epsilon \cdot \mathbf{1}_{A_\epsilon}(x)$ pour tout $x \in X$.

En effet, si $x \in A_\epsilon$, $f(x) \ge \epsilon = \epsilon \cdot 1$.
Si $x \notin A_\epsilon$, $f(x) \ge 0 = \epsilon \cdot 0$.

Par croissance et homogénéité de l'intégrale de Lebesgue pour les fonctions mesurables positives :
$\int_X f \, d\mu \ge \int_X \epsilon \cdot \mathbf{1}_{A_\epsilon} \, d\mu = \epsilon \mu(A_\epsilon)$.

Puisque $\int_X f \, d\mu = I < +\infty$, on a :
$I \ge \epsilon \mu(A_\epsilon)$

Comme $\epsilon > 0$, on peut diviser :
$\mu(A_\epsilon) \le \frac{I}{\epsilon} < +\infty$.

L'ensemble $A_\epsilon$ est donc de mesure finie.
