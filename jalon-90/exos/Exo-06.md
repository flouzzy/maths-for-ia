# Exercice 06

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Montrez rigoureusement que si une suite $(X_n)$ converge en probabilité vers une variable $X$, et qu'une fonction $g : \mathbb{R} \to \mathbb{R}$ est uniformément continue, alors la suite des variables transformées $g(X_n)$ converge en probabilité vers $g(X)$.

**Correction :**

Nous devons démontrer que pour tout $\varepsilon > 0$, la limite lorsque $n \to \infty$ de $\mathbb{P}(|g(X_n) - g(X)| \ge \varepsilon)$ est nulle.
Exploitons la continuité uniforme de $g$.
Par définition de l'uniforme continuité sur $\mathbb{R}$ : pour tout $\varepsilon > 0$, il existe un $\delta > 0$ tel que pour tout $(x, y) \in \mathbb{R}^2$, la condition $|x - y| < \delta$ implique l'inégalité stricte $|g(x) - g(y)| < \varepsilon$.

Prenons la contraposée logique de cette implication fondamentale.
Si l'écart sur les images est supérieur ou égal au seuil, c'est que l'écart sur les antécédents l'était initialement. Formellement :
$$ |g(x) - g(y)| \ge \varepsilon \implies |x - y| \ge \delta $$

Substituons nos variables aléatoires dans cette relation déterministe.
Pour chaque issue $\omega \in \Omega$, l'implication reste vraie ponctuellement :
$$ |g(X_n(\omega)) - g(X(\omega))| \ge \varepsilon \implies |X_n(\omega) - X(\omega)| \ge \delta $$
En termes de théorie des ensembles, cette implication logique se traduit par une inclusion d'événements probabilistes :
$$ \left\{ \omega \in \Omega \mid |g(X_n(\omega)) - g(X(\omega))| \ge \varepsilon \right\} \subseteq \left\{ \omega \in \Omega \mid |X_n(\omega) - X(\omega)| \ge \delta \right\} $$

Par la propriété de monotonie (croissance) des mesures de probabilité, l'inclusion des événements implique l'inégalité des probabilités associées :
$$ \mathbb{P}\left( |g(X_n) - g(X)| \ge \varepsilon \right) \le \mathbb{P}\left( |X_n - X| \ge \delta \right) $$

Puisque $\mathbb{P}$ est une mesure positive, nous encadrons :
$$ 0 \le \mathbb{P}\left( |g(X_n) - g(X)| \ge \varepsilon \right) \le \mathbb{P}\left( |X_n - X| \ge \delta \right) $$

Maintenant, appliquons l'hypothèse de convergence en probabilité de la suite $(X_n)$.
Par définition, pour notre $\delta > 0$ fraîchement construit (qui est une constante strictement positive), nous savons que :
$$ \lim_{n \to \infty} \mathbb{P}\left( |X_n - X| \ge \delta \right) = 0 $$

Le majorant de notre inégalité tendant vers zéro, le théorème d'encadrement force la limite du minorant à s'annuler également :
$$ \lim_{n \to \infty} \mathbb{P}\left( |g(X_n) - g(X)| \ge \varepsilon \right) = 0 $$

Ceci prouve formellement la convergence en probabilité :
$$ g(X_n) \xrightarrow{\mathbb{P}} g(X) $$
Ce résultat (Théorème de l'application continue, cas uniformément continu) est d'une grande puissance calculatoire en statistique asymptotique.
