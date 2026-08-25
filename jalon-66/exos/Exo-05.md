# Exercice 5 : Inégalité de Markov

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $f : X \to [0, +\infty]$ une fonction mesurable et $a > 0$ une constante réelle stricte. Établir mathématiquement l'inégalité de Markov : $\mu(\{x \in X \mid f(x) \geq a\}) \leq \frac{1}{a} \int_X f \, d\mu$.

**Démonstration :**
Définissons l'ensemble de niveau $A = \{x \in X \mid f(x) \geq a\}$.
Puisque $f$ est une fonction mesurable, l'ensemble $A$ est un élément de la tribu $\mathcal{A}$.
Nous construisons une fonction mineure. Considérons la fonction $g(x) = a \cdot \mathbf{1}_A(x)$.
Évaluons $g(x)$ par rapport à $f(x)$ pour tout point $x \in X$ :
- Si $x \in A$, par définition de $A$, on a $f(x) \geq a$. Or $g(x) = a \cdot 1 = a$. Donc $f(x) \geq g(x)$.
- Si $x \notin A$, la fonction $f$ étant positive par hypothèse, $f(x) \geq 0$. Or $g(x) = a \cdot 0 = 0$. Donc $f(x) \geq g(x)$.
Dans tous les cas, nous avons l'inégalité ponctuelle sur $X$ : $f \geq a \cdot \mathbf{1}_A \geq 0$.
La construction de l'intégrale de Lebesgue préserve l'ordre (propriété de croissance).
En intégrant chaque membre de cette inégalité sur l'espace entier $X$ par rapport à la mesure $\mu$, nous obtenons :
$$\int_X f \, d\mu \geq \int_X (a \cdot \mathbf{1}_A) \, d\mu$$
L'intégrale est homogène (linéarité par rapport aux constantes) et l'intégrale d'une indicatrice est la mesure de l'ensemble :
$$\int_X (a \cdot \mathbf{1}_A) \, d\mu = a \int_X \mathbf{1}_A \, d\mu = a \cdot \mu(A)$$
Nous avons donc : $\int_X f \, d\mu \geq a \cdot \mu(A)$.
Puisque $a > 0$, nous pouvons diviser les deux membres de l'inégalité par $a$ sans en altérer le sens :
$$\mu(A) \leq \frac{1}{a} \int_X f \, d\mu$$
L'inégalité de Markov est ainsi rigoureusement établie. Elle constitue la clé de voûte des inégalités de concentration en probabilités.
