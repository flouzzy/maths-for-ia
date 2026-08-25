# Exercice 3 : Intégrale de Lebesgue nulle et propriété presque partout

**Difficulté :** $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré et $f : X \to [0, +\infty]$ une fonction mesurable positive. Démontrer que si $\int_X f \, d\mu = 0$, alors $\mu(\{x \in X \mid f(x) > 0\}) = 0$.

**Démonstration :**
Pour démontrer ce résultat, nous allons utiliser une technique classique de théorie de la mesure : le découpage dyadique en ensembles de niveau.
Définissons pour tout entier $n \geq 1$, l'ensemble $A_n = \{x \in X \mid f(x) \geq \frac{1}{n}\}$.
Puisque $f$ est une fonction mesurable, $A_n$ est l'image réciproque de l'intervalle borélien $[\frac{1}{n}, +\infty]$, donc $A_n \in \mathcal{A}$.
Sur l'ensemble $A_n$, nous avons l'inégalité évidente : $f(x) \geq \frac{1}{n} \mathbf{1}_{A_n}(x)$.
Puisque les fonctions sont positives, la croissance de l'intégrale de Lebesgue nous permet d'intégrer cette inégalité :
$$\int_X f \, d\mu \geq \int_X \frac{1}{n} \mathbf{1}_{A_n} \, d\mu$$
L'intégrale d'une fonction indicatrice étant définie par la mesure de son support, nous obtenons :
$$0 = \int_X f \, d\mu \geq \frac{1}{n} \mu(A_n) \geq 0$$
Puisque $n \geq 1$ est strictement positif, la seule possibilité pour satisfaire cette chaîne d'inégalités est que $\mu(A_n) = 0$.
Ceci est vrai pour tout entier $n \geq 1$.
Considérons maintenant l'ensemble des points où $f$ est strictement positive : $A = \{x \in X \mid f(x) > 0\}$.
Nous pouvons écrire $A$ comme une union dénombrable croissante : $A = \bigcup_{n=1}^\infty A_n$.
Par sous-additivité de la mesure $\mu$, nous avons :
$$\mu(A) = \mu\left(\bigcup_{n=1}^\infty A_n\right) \leq \sum_{n=1}^\infty \mu(A_n)$$
Puisque chaque terme de la série est nul ($\mu(A_n) = 0$), nous concluons que $\mu(A) \leq 0$.
La mesure étant une application à valeurs positives, il s'ensuit rigoureusement que $\mu(A) = 0$. La fonction $f$ est donc nulle presque partout.
