\subsection*{Exercice 4 : Stabilité par composition continue \quad $\bigstar\bigstar\star\star\star$}

Soit $X_n$ une suite de variables aléatoires et $X$ une variable aléatoire telles que $X_n \xrightarrow{\mathbb{P}} X$.
Soit $g : \mathbb{R} \to \mathbb{R}$ une fonction uniformément continue. Montrer que $g(X_n) \xrightarrow{\mathbb{P}} g(X)$.

**Correction :**
Soit $\varepsilon > 0$. Puisque $g$ est uniformément continue sur $\mathbb{R}$, il existe $\delta > 0$ tel que pour tout $x, y \in \mathbb{R}$,
$|x - y| < \delta \implies |g(x) - g(y)| < \varepsilon$.
Par contraposée, $|g(x) - g(y)| \ge \varepsilon \implies |x - y| \ge \delta$.
Si on applique cela aux variables aléatoires, l'événement $\{|g(X_n) - g(X)| \ge \varepsilon\}$ est inclus dans l'événement $\{|X_n - X| \ge \delta\}$.
Par conséquent, en termes de probabilités :
$\mathbb{P}(|g(X_n) - g(X)| \ge \varepsilon) \le \mathbb{P}(|X_n - X| \ge \delta)$.
Par hypothèse, $X_n \xrightarrow{\mathbb{P}} X$, donc pour tout $\delta > 0$, on a $\lim_{n \to \infty} \mathbb{P}(|X_n - X| \ge \delta) = 0$.
Il en découle immédiatement par le théorème des gendarmes que $\lim_{n \to \infty} \mathbb{P}(|g(X_n) - g(X)| \ge \varepsilon) = 0$.
La suite $g(X_n)$ converge donc en probabilité vers $g(X)$.
