# Exercice 8 : Convergence du maximum empirique \quad $\bigstar\bigstar\bigstar\bigstar\star$

Soit $(X_n)_{n \geq 1}$ une suite de variables I.I.D. de loi uniforme sur $[0, \theta]$ avec $\theta > 0$. Soit $M_n = \max(X_1, \dots, X_n)$.
1. Déterminer la fonction de répartition de $M_n$.
2. Montrer que $M_n \xrightarrow{p.s.} \theta$.
3. Est-ce que la loi forte des grands nombres a été utilisée dans la question précédente ?

**Correction :**
1. Pour tout $t \in [0, \theta]$, on a :
$$F_{M_n}(t) = \mathbb{P}(M_n \leq t) = \mathbb{P}(X_1 \leq t, \dots, X_n \leq t)$$
Par indépendance des $X_i$, cela donne :
$$F_{M_n}(t) = \prod_{i=1}^n \mathbb{P}(X_i \leq t) = \left( \frac{t}{\theta} \right)^n$$
Pour $t < 0$, $F_{M_n}(t) = 0$ et pour $t > \theta$, $F_{M_n}(t) = 1$.
2. Soit $\epsilon > 0$. On s'intéresse à l'événement $\{|M_n - \theta| \geq \epsilon\}$. Puisque $M_n \leq \theta$ p.s., cela équivaut à $\{M_n \leq \theta - \epsilon\}$.
La probabilité est $P(M_n \leq \theta - \epsilon) = \left(\frac{\theta-\epsilon}{\theta}\right)^n = \left(1 - \frac{\epsilon}{\theta}\right)^n$.
Comme $1 - \frac{\epsilon}{\theta} \in ]0, 1[$, cette probabilité est le terme général d'une série géométrique convergente.
$$\sum_{n=1}^\infty \mathbb{P}(|M_n - \theta| \geq \epsilon) = \sum_{n=1}^\infty \left(1 - \frac{\epsilon}{\theta}\right)^n < +\infty$$
D'après le lemme de Borel-Cantelli, l'événement $\{|M_n - \theta| \geq \epsilon\}$ ne se réalise qu'un nombre fini de fois presque sûrement. Donc $M_n \xrightarrow{p.s.} \theta$.
3. Non, nous n'avons pas utilisé la loi forte des grands nombres (Théorème de Kolmogorov). La LFGN concerne les sommes (ou moyennes empiriques) de variables aléatoires. Ici, nous avons étudié un maximum empirique et utilisé directement le lemme de Borel-Cantelli pour établir la convergence presque sûre.
