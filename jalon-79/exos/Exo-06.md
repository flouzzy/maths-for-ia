# Exercice 6 : Lemme de Riemann-Lebesgue via Parseval $\bigstar\bigstar\bigstar\star\star$
**Énoncé :** Soit $f \in L^2([0, 2\pi])$. Montrer, en utilisant uniquement l'identité de Parseval, que ses coefficients de Fourier complexes vérifient : $\lim_{|n| \to \infty} c_n(f) = 0$.

**Correction Détaillée :**
*Étape 1 : Rappel de l'Identité de Parseval.*
Pour $f \in L^2$, l'identité de Parseval stipule que :
$$\sum_{n=-\infty}^{+\infty} |c_n(f)|^2 = \frac{1}{2\pi} \int_0^{2\pi} |f(t)|^2 dt$$

*Étape 2 : Finitude de l'énergie.*
Puisque $f \in L^2$, l'intégrale $\int_0^{2\pi} |f(t)|^2 dt$ est un nombre réel fini, que l'on note $M$.
Ainsi, la série infinie $\sum_{n=-\infty}^{+\infty} |c_n(f)|^2$ est convergente, et sa somme vaut $M$.

*Étape 3 : Terme général d'une série convergente.*
Dans toute série numérique convergente $\sum u_n$, une condition nécessaire stricte est que le terme général tende vers $0$ lorsque l'indice tend vers l'infini.
Ici, $u_n = |c_n(f)|^2$.
Puisque la série converge bilatéralement, on a nécessairement :
$$\lim_{|n| \to \infty} |c_n(f)|^2 = 0$$

*Étape 4 : Conclusion.*
La limite du carré du module étant nulle, le module lui-même tend vers $0$ :
$$\lim_{|n| \to \infty} |c_n(f)| = 0$$
Ce qui équivaut à $\lim_{|n| \to \infty} c_n(f) = 0$.
C'est le lemme de Riemann-Lebesgue pour les fonctions $L^2$, démontré de manière presque immédiate grâce à la structure hilbertienne.
