# Exercice 07

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Convergence et transformée fonctionnelle continue

Soit $(X_n)$ convergeant en probabilité vers $X$. Soit $g : \mathbb{R} \to \mathbb{R}$ une fonction uniformément continue.
Démontrez que $g(X_n)$ converge en probabilité vers $g(X)$. (Ce résultat s'étend aux fonctions continues par le théorème d'approximation sur les compacts).

**Correction exhaustive :**
Puisque $g$ est uniformément continue, par définition, pour tout $\epsilon > 0$, il existe un $\delta > 0$ tel que pour tous $x, y \in \mathbb{R}$,
$$ |x - y| < \delta \implies |g(x) - g(y)| < \epsilon $$
Par contraposée de cette implication purement déterministe (logique propositionnelle), on obtient :
$$ |g(x) - g(y)| \ge \epsilon \implies |x - y| \ge \delta $$
En remplaçant $x$ par la variable aléatoire $X_n(\omega)$ et $y$ par $X(\omega)$, on obtient l'inclusion d'événements aléatoires suivante :
$$ \{\omega \in \Omega \mid |g(X_n(\omega)) - g(X(\omega))| \ge \epsilon\} \subseteq \{\omega \in \Omega \mid |X_n(\omega) - X(\omega)| \ge \delta\} $$
Puisque le premier événement est inclus dans le second, la croissance de la mesure de probabilité nous indique que :
$$ \mathbb{P}(|g(X_n) - g(X)| \ge \epsilon) \le \mathbb{P}(|X_n - X| \ge \delta) $$
Par hypothèse, $X_n$ converge en probabilité vers $X$. Donc, pour le réel fixé $\delta > 0$, nous avons :
$$ \lim_{n \to \infty} \mathbb{P}(|X_n - X| \ge \delta) = 0 $$
Le terme majorant tendant vers zéro, et les probabilités étant minorées par zéro, le théorème d'encadrement conclut formellement :
$$ \lim_{n \to \infty} \mathbb{P}(|g(X_n) - g(X)| \ge \epsilon) = 0 $$
Ceci constitue l'exacte définition de la convergence en probabilité de la suite $(g(X_n))$ vers la variable $g(X)$.
