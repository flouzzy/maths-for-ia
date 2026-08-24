# Exercice 9 : Limite et Intégration sur ensemble fini \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit $X = \{1, 2, 3\}$ avec la mesure de comptage. Soit $f_n(x) = x^n$. Étudier la convergence de $\int_X f_n \, d\mu$ lorsque $n \to \infty$. Que vaut $\int_X (\lim_{n \to \infty} f_n) \, d\mu$ ?

**Correction :**
Cet exercice prépare au théorème de convergence monotone, mais peut se traiter à la main sur un espace fini.
1. L'espace $X$ est fini. L'intégrale est une somme finie : $\int_X f_n \, d\mu = f_n(1) + f_n(2) + f_n(3) = 1^n + 2^n + 3^n$.
2. Lorsque $n \to \infty$, $1^n \to 1$, $2^n \to +\infty$ et $3^n \to +\infty$. Donc $\lim_{n\to\infty} \int_X f_n \, d\mu = +\infty$.
3. Étudions maintenant la limite ponctuelle de la suite de fonctions $f_n(x)$ : pour tout $x \in \{1,2,3\}$, $f(x) = \lim_{n\to\infty} f_n(x)$.
4. On a $f(1) = 1$, $f(2) = +\infty$, $f(3) = +\infty$.
5. Calculons l'intégrale de cette fonction limite $f$ (qui appartient bien à $\mathcal{M}_+$ car on autorise la valeur $+\infty$) : $\int_X f \, d\mu = f(1) + f(2) + f(3) = 1 + \infty + \infty = +\infty$.
6. On observe que l'interversion limite/intégrale est valide ici (ce qui est toujours le cas pour des fonctions positives par le Lemme de Fatou).
