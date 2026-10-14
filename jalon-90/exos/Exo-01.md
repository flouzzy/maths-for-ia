# Exercice 01

**Difficulté :** $\bigstar\star\star\star\star$

**Énoncé :**
Soit une suite de variables aléatoires $X_n$ telles que $\mathbb{P}(X_n = 1) = \frac{1}{n}$ et $\mathbb{P}(X_n = 0) = 1 - \frac{1}{n}$.
Montrez que $X_n$ converge en probabilité vers la variable certaine $X = 0$.

**Correction :**
Nous devons montrer que pour tout $\epsilon > 0$, $\lim_{n \to \infty} \mathbb{P}(|X_n - 0| > \epsilon) = 0$.
Soit $\epsilon \in ]0, 1[$. Puisque $X_n$ ne prend que les valeurs $0$ et $1$, on a :
$$ \mathbb{P}(|X_n| > \epsilon) = \mathbb{P}(X_n = 1) = \frac{1}{n} $$
En passant à la limite lorsque $n \to \infty$ :
$$ \lim_{n \to \infty} \mathbb{P}(|X_n| > \epsilon) = \lim_{n \to \infty} \frac{1}{n} = 0 $$
Ainsi, $X_n \xrightarrow{\mathbb{P}} 0$.
