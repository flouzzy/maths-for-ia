# Exercice 4 : Linéarité de l'intégrale pour les fonctions mesurables positives

**Difficulté :** $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soient $f, g : X \to [0, +\infty]$ deux fonctions mesurables positives et $\alpha, \beta \geq 0$. Démontrer l'additivité $\int_X (f+g) \, d\mu = \int_X f \, d\mu + \int_X g \, d\mu$ en utilisant le théorème d'approximation par des fonctions étagées.

**Démonstration :**
La démonstration s'appuie sur le théorème fondamental d'approximation.
Il existe deux suites de fonctions étagées positives, $(s_n)_{n \in \mathbb{N}}$ et $(t_n)_{n \in \mathbb{N}}$, telles que :
1. $0 \leq s_n \leq s_{n+1} \leq f$ et $\lim_{n \to \infty} s_n(x) = f(x)$ pour tout $x \in X$.
2. $0 \leq t_n \leq t_{n+1} \leq g$ et $\lim_{n \to \infty} t_n(x) = g(x)$ pour tout $x \in X$.
Construisons la suite $(u_n)_{n \in \mathbb{N}}$ définie par $u_n = s_n + t_n$.
D'après nos propriétés algébriques, la somme de deux fonctions étagées positives est une fonction étagée positive.
La suite $(u_n)$ est croissante car $(s_n)$ et $(t_n)$ le sont.
Par arithmétique des limites, pour tout $x \in X$ :
$$\lim_{n \to \infty} u_n(x) = \lim_{n \to \infty} (s_n(x) + t_n(x)) = f(x) + g(x)$$
Nous pouvons appliquer le théorème de convergence monotone (Beppo-Levi) à ces trois suites.
Pour la somme $f+g$, nous avons :
$$\int_X (f+g) \, d\mu = \lim_{n \to \infty} \int_X u_n \, d\mu$$
Or, l'intégrale est linéaire sur l'espace des fonctions étagées. Donc pour chaque $n$ :
$$\int_X u_n \, d\mu = \int_X (s_n + t_n) \, d\mu = \int_X s_n \, d\mu + \int_X t_n \, d\mu$$
En passant à la limite (les deux termes étant positifs, la limite de la somme est la somme des limites dans $[0, +\infty]$) :
$$\lim_{n \to \infty} \int_X u_n \, d\mu = \lim_{n \to \infty} \int_X s_n \, d\mu + \lim_{n \to \infty} \int_X t_n \, d\mu$$
En appliquant de nouveau le théorème de convergence monotone aux suites $s_n$ et $t_n$ :
$$\lim_{n \to \infty} \int_X s_n \, d\mu = \int_X f \, d\mu \quad \text{et} \quad \lim_{n \to \infty} \int_X t_n \, d\mu = \int_X g \, d\mu$$
En substituant ces limites, nous obtenons le résultat final :
$$\int_X (f+g) \, d\mu = \int_X f \, d\mu + \int_X g \, d\mu$$
