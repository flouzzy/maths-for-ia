# Approximation par suites croissantes (Lemme fondamental)

**Difficulté :** $\star\star\star\star\star$

## Énoncé

Soit $f \geq 0$ mesurable. Démontrez la formule explicite pour construire la suite $(s_n)$ de fonctions étagées qui croît ponctuellement vers $f$.

---

## Correction détaillée

L'idée est de tronquer la fonction à la hauteur $n$, et de découper l'intervalle $[0, n[$ en $n \times 2^n$ sous-intervalles de longueur $\frac{1}{2^n}$.
Pour tout entier $n \geq 1$ et tout $x \in X$, on définit :
$$ s_n(x) = \sum_{k=0}^{n2^n-1} \frac{k}{2^n} \mathbb{1}_{\{x \mid \frac{k}{2^n} \leq f(x) < \frac{k+1}{2^n}\}} + n \mathbb{1}_{\{x \mid f(x) \geq n\}} $$
Par construction, $s_n$ est étagée (car les ensembles impliqués sont mesurables par mesurabilité de $f$) et $0 \leq s_n \leq f$.
De plus, sur l'ensemble où $f(x) < n$, on a $|f(x) - s_n(x)| < \frac{1}{2^n}$. Sur l'ensemble où $f(x) \geq n$, $s_n(x) = n$.
Pour un $x$ fixé :
- Si $f(x) = +\infty$, alors $s_n(x) = n \to +\infty = f(x)$.
- Si $f(x) < +\infty$, pour $n$ assez grand ($n > f(x)$), on a $|f(x) - s_n(x)| < \frac{1}{2^n} \to 0$, donc $s_n(x) \to f(x)$.
Il reste à vérifier $s_n \leq s_{n+1}$. En passant de $n$ à $n+1$, on divise chaque intervalle de hauteur par $2$ (hauteur $\frac{1}{2^n}$ devient $\frac{1}{2^{n+1}}$). La valeur prise sur le sous-intervalle inférieur reste inchangée, celle sur le supérieur augmente de $\frac{1}{2^{n+1}}$. La suite est donc bien croissante.
