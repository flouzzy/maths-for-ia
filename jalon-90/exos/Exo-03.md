# Exercice 3 : Composition par une fonction continue
$\bigstar\bigstar\star\star\star$


Soient une suite $(X_n)$ de variables aléatoires convergeant en probabilité vers $X$ et $g: \mathbb{R} \to \mathbb{R}$ une fonction uniformément continue.
Démontrez de façon rigoureuse, en utilisant la définition avec les $\epsilon$, que $g(X_n) \xrightarrow{\mathbb{P}} g(X)$.

**Correction :**
1. $g$ est uniformément continue, donc : $\forall \epsilon > 0, \exists \delta > 0, \forall x,y \in \mathbb{R}, |x-y| \leq \delta \implies |g(x)-g(y)| \leq \epsilon$.
2. Par contraposée, $|g(X_n) - g(X)| > \epsilon \implies |X_n - X| > \delta$.
3. En passant aux probabilités, on obtient la majoration :
$$ \mathbb{P}(|g(X_n) - g(X)| > \epsilon) \leq \mathbb{P}(|X_n - X| > \delta) $$
4. Comme $X_n \xrightarrow{\mathbb{P}} X$, nous savons par définition que $\lim_{n \to \infty} \mathbb{P}(|X_n - X| > \delta) = 0$.
5. Par le théorème d'encadrement, puisque les probabilités sont positives :
$$ 0 \leq \lim_{n \to \infty} \mathbb{P}(|g(X_n) - g(X)| > \epsilon) \leq 0 $$
Ainsi la limite est bien $0$, et on a prouvé $g(X_n) \xrightarrow{\mathbb{P}} g(X)$.
