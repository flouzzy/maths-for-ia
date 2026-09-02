# Exo 07 : Transformation de Laplace et continuité ($\bigstar$\bigstar$\bigstar$\bigstar\star$)

## Énoncé
Soit $f : \mathbb{R}^+ \to \mathbb{R}^+$ une fonction mesurable. On définit sa transformée de Laplace :
$F(p) = \int_0^{+\infty} f(t) e^{-pt} \, dt$, pour $p > 0$.
Soit une suite $p_n$ décroissante convergeant vers $p_0 > 0$.
À l'aide du TCM, démontrer que $F(p_n)$ converge vers $F(p_0)$.

## Correction Détaillée
**Étape 1 : Construction de la suite de fonctions**
Définissons $g_n(t) = f(t) e^{-p_n t}$.
Comme $f$ est positive et que l'exponentielle est strictement positive, $g_n$ est positive sur $\mathbb{R}^+$.
Puisque la suite $(p_n)$ est décroissante ($p_{n+1} \le p_n$), pour tout $t \ge 0$, on a $-p_{n+1} t \ge -p_n t$.
L'exponentielle étant croissante, il s'ensuit que $e^{-p_{n+1} t} \ge e^{-p_n t}$.
Donc $f(t) e^{-p_{n+1} t} \ge f(t) e^{-p_n t}$, soit $g_{n+1}(t) \ge g_n(t)$.
La suite de fonctions $(g_n)$ est donc une suite croissante de fonctions mesurables positives.

**Étape 2 : Limite de la suite de fonctions**
Par continuité de la fonction exponentielle, pour tout $t \ge 0$, $\lim_{n \to \infty} e^{-p_n t} = e^{-p_0 t}$.
Ainsi, la limite ponctuelle de $g_n(t)$ est $g(t) = f(t) e^{-p_0 t}$.

**Étape 3 : Application du Théorème de Convergence Monotone**
D'après Beppo Levi, nous pouvons intervertir la limite et l'intégrale :
$$ \lim_{n \to \infty} \int_0^{+\infty} g_n(t) \, dt = \int_0^{+\infty} \lim_{n \to \infty} g_n(t) \, dt $$
Ce qui donne précisément :
$$ \lim_{n \to \infty} F(p_n) = \int_0^{+\infty} f(t) e^{-p_0 t} \, dt = F(p_0) $$
Nous avons ainsi démontré la continuité à droite de la transformée de Laplace en utilisant la monotonie de Beppo Levi, sans exiger de propriétés de domination sophistiquées.
