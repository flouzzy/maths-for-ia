# Exercice 8 : Théorème de convergence dominée pour la LFGN

$\bigstar\bigstar\bigstar\bigstar\star$


Lors de la preuve de la convergence de la perte empirique, nous avons supposé $\mathbb{E}_{X \sim P}[|\ln q_\theta(X)|] < \infty$.
Supposons un espace compact $\mathcal{X}$, et que les densités $p(x)$ et $q_\theta(x)$ soient continues, strictement positives sur $\mathcal{X}$.

**1.** Montrer que l'hypothèse d'intégrabilité est automatiquement satisfaite sous ces conditions.
**2.** Comment cela assure-t-il la validité de la Loi Forte des Grands Nombres pour l'entropie croisée ?

**Correction :**

**1.** Puisque $q_\theta(x)$ est une fonction continue et strictement positive sur un espace compact $\mathcal{X}$, d'après le théorème des bornes atteintes de Weierstrass, elle atteint son minimum $m > 0$ et son maximum $M < \infty$ sur $\mathcal{X}$.
On a donc pour tout $x \in \mathcal{X}$, $0 < m \le q_\theta(x) \le M$.
Par croissance stricte et continuité du logarithme :
$$ \ln(m) \le \ln q_\theta(x) \le \ln(M) $$
Ainsi, la fonction $|\ln q_\theta(x)|$ est bornée par une constante $K = \max(|\ln(m)|, |\ln(M)|)$.
Par conséquent, l'espérance est majorée :
$$\mathbb{E}_{X \sim P}[|\ln q_\theta(X)|] = \int_{\mathcal{X}} p(x) |\ln q_\theta(x)| d\lambda(x) \le K \int_{\mathcal{X}} p(x) d\lambda(x) = K < \infty$$
L'hypothèse d'intégrabilité absolue est donc satisfaite.

**2.** La condition $L^1$ (espérance de la valeur absolue finie) est la condition nécessaire et suffisante du théorème fondamental de Kolmogorov (Loi Forte des Grands Nombres) pour une suite de variables i.i.d. $Y_i = - \ln q_\theta(X_i)$. Elle assure que la moyenne empirique converge presque sûrement vers son espérance théorique, validant ainsi la minimisation asymptotique.
