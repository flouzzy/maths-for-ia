# Exercice 6 : Comparaison Tchebychev vs Hoeffding

$\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $n = 100$ variables de Bernoulli indépendantes $X_i \sim \mathcal{B}(1/2)$. On étudie l'écart de la moyenne $\overline{X}_n$ par rapport à $1/2$ d'au moins $0.1$.
1. Calculer la borne donnée par Tchebychev.
2. Calculer la borne donnée par Hoeffding.
3. Conclure.

**Correction :**
Ici, $X_i \in [0, 1]$ avec $\mathbb{E}[X_i] = p = 1/2$ et $\text{Var}(X_i) = p(1-p) = 1/4$.
La moyenne empirique a pour variance $\text{Var}(\overline{X}_n) = \frac{1/4}{100} = \frac{1}{400}$.
On cherche à borner $\mathbb{P}(|\overline{X}_n - 1/2| \ge 0.1)$.

**1. Borne de Tchebychev :**
$$ \mathbb{P}(|\overline{X}_n - 1/2| \ge 0.1) \le \frac{\text{Var}(\overline{X}_n)}{(0.1)^2} = \frac{1/400}{0.01} = \frac{1/400}{1/100} = \frac{100}{400} = \frac{1}{4} = 0.25 $$
Tchebychev garantit une probabilité inférieure ou égale à $25\%$.

**2. Borne de Hoeffding :**
Les variables sont dans $[0, 1]$ donc $b_i - a_i = 1$. L'inégalité s'écrit :
$$ \mathbb{P}(|\overline{X}_n - 1/2| \ge 0.1) \le 2 \exp(-2 n \epsilon^2) $$
Avec $n = 100$ et $\epsilon = 0.1$ :
$$ 2 n \epsilon^2 = 2 \times 100 \times 0.01 = 2 $$
La borne de Hoeffding est :
$$ 2 e^{-2} \approx 2 \times 0.1353 = 0.2706 $$
Ici, Hoeffding donne une borne de $27.06\%$.

**3. Conclusion :**
Étonnamment, pour de petites déviations ou un $n$ modéré, Tchebychev peut être légèrement plus serré ($0.25$ vs $0.27$). L'avantage de Hoeffding réside dans sa décroissance exponentielle, qui devient massivement supérieure pour un $n$ grand (ex: $n=1000$, Hoeffding donne $2e^{-20} \approx 4 \times 10^{-9}$ alors que Tchebychev donne $1/40 = 2.5\%$).
