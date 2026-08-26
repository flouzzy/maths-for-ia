### L'inégalité de Markov \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $f \in \mathcal{M}_+$. Démontrer l'inégalité de Markov :
Pour tout $\alpha > 0$,
$$\mu(\{x \in X \mid f(x) \ge \alpha\}) \le \frac{1}{\alpha} \int_X f d\mu$$

**Correction Détaillée :**
**Étape 1 : Cadre géométrique.**
Soit $\alpha > 0$. Posons l'ensemble $A_\alpha = \{x \in X \mid f(x) \ge \alpha\}$.
Puisque $f$ est une fonction mesurable, $A_\alpha$ est un ensemble mesurable ($A_\alpha \in \mathcal{F}$).

**Étape 2 : Minoration de la fonction $f$.**
Sur l'ensemble $A_\alpha$, nous savons par définition que $f(x) \ge \alpha$.
Sur le complémentaire $A_\alpha^c$, nous savons que $f(x) \ge 0$ (car $f \in \mathcal{M}_+$).
Nous pouvons synthétiser cela par une unique inégalité valable sur tout l'espace $X$ en utilisant la fonction indicatrice de l'ensemble $A_\alpha$ :
Pour tout $x \in X$, $f(x) \ge \alpha \mathbf{1}_{A_\alpha}(x)$.

**Étape 3 : Croissance de l'intégrale.**
La fonction $g = \alpha \mathbf{1}_{A_\alpha}$ est une fonction simple positive.
Nous appliquons la propriété de croissance de l'intégrale. Si $g \le f$, alors :
$$\int_X g d\mu \le \int_X f d\mu$$
Soit :
$$\int_X (\alpha \mathbf{1}_{A_\alpha}) d\mu \le \int_X f d\mu$$

**Étape 4 : Calcul de l'intégrale de la fonction simple.**
Par définition de l'intégrale d'une fonction simple :
$$\int_X (\alpha \mathbf{1}_{A_\alpha}) d\mu = \alpha \mu(A_\alpha)$$

**Étape 5 : Conclusion.**
En substituant ce résultat dans l'inégalité, nous obtenons :
$$\alpha \mu(A_\alpha) \le \int_X f d\mu$$
Comme $\alpha > 0$, on peut diviser par $\alpha$ (même si l'intégrale est infinie, l'inégalité reste vraie avec la convention adéquate) :
$$\mu(A_\alpha) \le \frac{1}{\alpha} \int_X f d\mu$$
Ce résultat fondamental est à la base de nombreuses inégalités de concentration en probabilités (notamment l'inégalité de Bienaymé-Tchebychev).
