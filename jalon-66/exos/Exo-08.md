# Exercice 8 : Absolue continuité de l'intégrale

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $f : X \to [0, +\infty]$ intégrable ($\int f < \infty$). Démontrer que pour tout $\epsilon > 0$, il existe $\delta > 0$ tel que pour tout ensemble mesurable $A$, $\mu(A) < \delta \implies \int_A f \, d\mu < \epsilon$.

**Démonstration :**
Nous allons procéder par l'absurde, en utilisant la méthode de troncature.
Supposons que la propriété soit fausse. Il existerait un $\epsilon_0 > 0$ tel que pour tout $n \geq 1$ (en prenant $\delta = \frac{1}{2^n}$), il existe un ensemble mesurable $A_n$ vérifiant :
$$\mu(A_n) < \frac{1}{2^n} \quad \text{et} \quad \int_{A_n} f \, d\mu \geq \epsilon_0$$
Considérons la limite supérieure de ces ensembles : $A = \limsup_{n \to \infty} A_n = \bigcap_{k=1}^\infty \bigcup_{n=k}^\infty A_n$.
D'après le lemme de Borel-Cantelli (car la série des mesures converge : $\sum \mu(A_n) \leq \sum \frac{1}{2^n} < \infty$), l'ensemble $A$ est de mesure nulle : $\mu(A) = 0$.
Puisque $f$ est intégrable, $\int_A f \, d\mu = 0$.
Décomposons l'intégrale sur $A_n$ en utilisant la troncature de $f$ par une constante $M > 0$ :
$$\int_{A_n} f \, d\mu = \int_{A_n \cap \{f \leq M\}} f \, d\mu + \int_{A_n \cap \{f > M\}} f \, d\mu$$
Majorons le premier terme :
$$\int_{A_n \cap \{f \leq M\}} f \, d\mu \leq \int_{A_n} M \, d\mu = M \cdot \mu(A_n) < \frac{M}{2^n}$$
Pour le second terme, la fonction $f \mathbf{1}_{\{f > M\}}$ est dominée par $f$ qui est intégrable. Par le théorème de convergence dominée, lorsque $M \to \infty$, l'intégrale de cette queue tend vers zéro.
Fixons un $M$ suffisamment grand pour que l'intégrale de la queue sur tout l'espace soit petite :
$$\int_{\{f > M\}} f \, d\mu < \frac{\epsilon_0}{2}$$
Cette majoration est indépendante de $A_n$, donc elle reste valide en restreignant à $A_n$ :
$$\int_{A_n \cap \{f > M\}} f \, d\mu \leq \int_{\{f > M\}} f \, d\mu < \frac{\epsilon_0}{2}$$
Revenons à l'évaluation sur $A_n$ :
$$\epsilon_0 \leq \int_{A_n} f \, d\mu < \frac{M}{2^n} + \frac{\epsilon_0}{2}$$
En prenant $n$ suffisamment grand (de sorte que $\frac{M}{2^n} < \frac{\epsilon_0}{2}$), nous obtenons :
$$\epsilon_0 < \frac{\epsilon_0}{2} + \frac{\epsilon_0}{2} = \epsilon_0$$
Ce qui est une contradiction stricte. L'absolue continuité est donc vérifiée.
