## Exercice 8 : Inégalité de Tchebychev \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $f \in \mathcal{L}^1(\mu)$ une fonction à valeurs réelles et $\alpha > 0$.
Posons $A_\alpha = \{x \in X : |f(x)| \ge \alpha\}$.
Montrer l'inégalité de Tchebychev (aussi appelée de Markov) :
$\mu(A_\alpha) \le \frac{1}{\alpha} \int_X |f| d\mu$.

**Correction :**
1. On peut minorer $|f|$ en utilisant l'indicatrice de $A_\alpha$ :
   Pour tout $x \in X$, $|f(x)| \ge |f(x)| \mathbf{1}_{A_\alpha}(x)$.
2. Si $x \in A_\alpha$, alors $|f(x)| \ge \alpha$, donc $|f(x)| \mathbf{1}_{A_\alpha}(x) \ge \alpha \mathbf{1}_{A_\alpha}(x)$.
   Si $x \notin A_\alpha$, $\mathbf{1}_{A_\alpha}(x) = 0$, donc les deux côtés valent 0.
   Ainsi, pour tout $x \in X$, on a $|f(x)| \ge \alpha \mathbf{1}_{A_\alpha}(x)$.
3. On intègre cette inégalité entre fonctions positives :
   $\int_X |f| d\mu \ge \int_X \alpha \mathbf{1}_{A_\alpha} d\mu = \alpha \int_X \mathbf{1}_{A_\alpha} d\mu = \alpha \mu(A_\alpha)$.
4. Comme $\alpha > 0$, on peut diviser par $\alpha$ pour obtenir :
   $\mu(A_\alpha) \le \frac{1}{\alpha} \int_X |f| d\mu$.
