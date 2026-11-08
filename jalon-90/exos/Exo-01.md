# Exercice 01

**Difficulté :** $\bigstar\star\star\star\star$

**Énoncé :**
Soit une suite de variables aléatoires réelles $(X_n)_{n \ge 1}$ définies sur un espace probabilisé $(\Omega, \mathcal{F}, \mathbb{P})$. On suppose que $X_n$ suit une loi de Bernoulli modifiée telle que $\mathbb{P}(X_n = 1) = \frac{1}{n}$ et $\mathbb{P}(X_n = 0) = 1 - \frac{1}{n}$.
1. Montrez par une preuve $\varepsilon$-$\delta$ directe que la suite $(X_n)$ converge en probabilité vers la variable certaine $X = 0$.
2. Étudiez la convergence de $X_n$ dans l'espace $L^1(\Omega)$.
3. Étudiez la convergence de $X_n$ dans l'espace $L^2(\Omega)$.

**Correction :**

**1. Convergence en probabilité :**
Rappelons la définition de la convergence en probabilité : $X_n \xrightarrow{\mathbb{P}} 0$ si et seulement si pour tout $\varepsilon > 0$, $\lim_{n \to \infty} \mathbb{P}(|X_n - 0| > \varepsilon) = 0$.
Soit $\varepsilon > 0$ un réel strictement positif fixé arbitrairement.
Puisque la variable aléatoire $X_n$ ne prend que les valeurs $0$ et $1$, nous devons distinguer deux cas selon la position de $\varepsilon$ par rapport à $1$.
- Cas $0 < \varepsilon < 1$ : L'événement $\{|X_n| > \varepsilon\}$ est strictement identique à l'événement $\{X_n = 1\}$. Par conséquent,
$$ \mathbb{P}(|X_n| > \varepsilon) = \mathbb{P}(X_n = 1) = \frac{1}{n} $$
En passant à la limite lorsque $n \to \infty$, on obtient de manière immédiate :
$$ \lim_{n \to \infty} \mathbb{P}(|X_n| > \varepsilon) = \lim_{n \to \infty} \frac{1}{n} = 0 $$
- Cas $\varepsilon \ge 1$ : L'événement $\{|X_n| > \varepsilon\}$ est vide (puisque la valeur maximale de $X_n$ est $1$). Ainsi, $\mathbb{P}(|X_n| > \varepsilon) = 0$, dont la limite est bien $0$.

Dans tous les cas, la limite est nulle, ce qui prouve rigoureusement que $X_n \xrightarrow{\mathbb{P}} 0$.

**2. Convergence dans $L^1$ :**
La convergence dans $L^1$ requiert que $\lim_{n \to \infty} \mathbb{E}[|X_n - 0|] = 0$.
Calculons explicitement l'espérance de la valeur absolue (qui est ici identique à la variable elle-même car elle est positive) :
$$ \mathbb{E}[|X_n|] = \mathbb{E}[X_n] = 1 \cdot \mathbb{P}(X_n = 1) + 0 \cdot \mathbb{P}(X_n = 0) = 1 \cdot \frac{1}{n} + 0 = \frac{1}{n} $$
En passant à la limite, $\lim_{n \to \infty} \mathbb{E}[|X_n|] = \lim_{n \to \infty} \frac{1}{n} = 0$.
La suite $(X_n)$ converge donc vers $0$ dans l'espace $L^1$.

**3. Convergence dans $L^2$ :**
La convergence dans $L^2$ requiert que $\lim_{n \to \infty} \mathbb{E}[|X_n - 0|^2] = 0$.
Puisque $X_n$ est à valeurs dans $\{0, 1\}$, on a la particularité algébrique $X_n^2 = X_n$.
Ainsi, le calcul de l'espérance du carré se réduit au calcul précédent :
$$ \mathbb{E}[|X_n|^2] = \mathbb{E}[X_n] = \frac{1}{n} $$
La limite lorsque $n \to \infty$ est à nouveau $0$.
La suite $(X_n)$ converge également vers $0$ dans l'espace $L^2$. Ce résultat illustre que pour des variables bornées (ici par 1), la convergence en probabilité garantit la convergence dans tous les espaces $L^p$.
