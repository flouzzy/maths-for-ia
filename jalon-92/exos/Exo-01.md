# Exercice 01

**Difficulté :** $\bigstar\star\star\star\star$

**Énoncé :**
Soit $(X_n)_{n \in \mathbb{N}^*}$ une suite de variables aléatoires indépendantes suivant une loi de Bernoulli de paramètre $p = 0.4$. On note $S_n = \sum_{i=1}^n X_i$.
1. Quelle est la signification de $S_n$ dans une expérience de tirage à pile ou face biaisée ?
2. Vers quelle limite la variable aléatoire $\frac{S_n}{n}$ converge-t-elle presque sûrement ? Justifier.

**Correction :**
1. La variable $S_n$ compte le nombre de succès (par exemple "Pile", si $X_i=1$ pour Pile et 0 pour Face) lors de $n$ expériences indépendantes. Elle suit une loi binomiale $\mathcal{B}(n, 0.4)$.
2. Les variables $(X_n)$ sont indépendantes et identiquement distribuées.
Leur espérance est $\mathbb{E}[X_1] = 0.4 \times 1 + 0.6 \times 0 = 0.4$.
Comme $\mathbb{E}[|X_1|] = 0.4 < +\infty$, on peut appliquer la Loi Forte des Grands Nombres.
On en déduit que $\frac{S_n}{n} = \frac{1}{n} \sum_{i=1}^n X_i$ converge presque sûrement vers $\mathbb{E}[X_1] = 0.4$.
Ainsi, $\lim_{n \to \infty} \frac{S_n}{n} = 0.4$ presque sûrement.
