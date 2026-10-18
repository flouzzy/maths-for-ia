# Exercice 1 : Convergence presque sûre d'une suite de Bernoulli \quad $\bigstar\star\star\star\star$

Soit $(X_n)_{n \in \mathbb{N}^*}$ une suite de variables aléatoires indépendantes et identiquement distribuées suivant une loi de Bernoulli de paramètre $p \in ]0,1[$. On note $S_n = \sum_{i=1}^n X_i$.
1. Rappeler l'espérance et la variance de $X_1$.
2. Énoncer la loi forte des grands nombres pour cette suite.
3. Déterminer la limite presque sûre de la suite de variables aléatoires $Y_n = \frac{1}{n} S_n (1 - \frac{1}{n} S_n)$.

**Correction :**
1. Comme $X_1 \sim \mathcal{B}(p)$, par définition, $\mathbb{E}[X_1] = p \times 1 + (1-p) \times 0 = p$. La variance est $\text{Var}(X_1) = \mathbb{E}[X_1^2] - (\mathbb{E}[X_1])^2$. Or $X_1^2 = X_1$ car $X_1 \in \{0,1\}$, donc $\mathbb{E}[X_1^2] = p$. Ainsi, $\text{Var}(X_1) = p - p^2 = p(1-p)$.
2. La suite $(X_n)$ est constituée de variables I.I.D. admettant une espérance finie $\mathbb{E}[X_1] = p$. D'après la loi forte des grands nombres (Théorème de Kolmogorov), la moyenne empirique $\frac{S_n}{n} = \frac{1}{n} \sum_{i=1}^n X_i$ converge presque sûrement vers $\mathbb{E}[X_1] = p$. C'est-à-dire : $\mathbb{P}(\lim_{n \to \infty} \frac{S_n}{n} = p) = 1$.
3. Posons $g(x) = x(1-x)$. La fonction $g$ est continue sur $\mathbb{R}$. Par composition de limites presque sûres (la continuité préservant la convergence presque sûre), puisque $\frac{S_n}{n} \xrightarrow{p.s.} p$, on a $g(\frac{S_n}{n}) \xrightarrow{p.s.} g(p)$. Ainsi, la suite $Y_n = \frac{S_n}{n} (1 - \frac{S_n}{n})$ converge presque sûrement vers $p(1-p)$, qui est la variance de la loi de Bernoulli.
